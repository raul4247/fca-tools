# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Dict, List, Tuple

from fcatools import EMPTY_VALUE
from .dyadic_link import DyadicLink
from .dyadic_concept import DyadicConcept
from .dyadic_generator import DyadicGenerator
from .dyadic_association_rule import DyadicAssociationRule

class DyadicLattice:
    def __init__(self):
        self.lattice: Dict[frozenset, DyadicConcept] = {}

    def add_connection(self, intent_1, intent_2, concepts):
        concepts_reversed = {i.attrs: i.objects for i in concepts}

        intent_1 = frozenset(intent_1)
        intent_2 = frozenset(intent_2)

        if intent_1 in concepts_reversed and intent_2 not in concepts_reversed:
            extent = concepts_reversed[intent_1]
            if extent not in self.lattice:
                self.lattice[extent] = DyadicConcept(extent, intent_1)

        elif intent_2 in concepts_reversed and intent_1 not in concepts_reversed:
            extent = concepts_reversed[intent_2]
            if extent not in self.lattice:
                self.lattice[extent] = DyadicConcept(extent, intent_2)

        elif intent_2 in concepts_reversed and intent_1 in concepts_reversed:
            extent_1 = concepts_reversed[intent_1]
            extent_2 = concepts_reversed[intent_2]

            if extent_1 in self.lattice and extent_2 in self.lattice:
                self.lattice[extent_1].add_connection(self.lattice[extent_2])
            elif extent_1 not in self.lattice and extent_2 in self.lattice:
                c = DyadicConcept(extent_1, intent_1)
                c.add_connection(self.lattice[extent_2])
                self.lattice[extent_1] = c
            elif extent_1 in self.lattice and extent_2 not in self.lattice:
                c = DyadicConcept(extent_2, intent_2)
                c.add_connection(self.lattice[extent_1])
                self.lattice[extent_2] = c
            else:
                c1 = DyadicConcept(extent_1, intent_1)
                c2 = DyadicConcept(extent_2, intent_2)
                c1.add_connection(c2)
                self.lattice[extent_1] = c1
                self.lattice[extent_2] = c2

    def get_objects_count(self) -> int:
        unique_objects = []
        for objects, concept in self.lattice.items():
            for o in objects:
                if o not in unique_objects:
                    unique_objects.append(o)

        if EMPTY_VALUE in unique_objects:
            unique_objects.remove(EMPTY_VALUE)

        return len(unique_objects)

    def compute_association_rules(self, generators: List[DyadicGenerator]) -> List[DyadicAssociationRule]:
        rules = []
        objects_count = self.get_objects_count()
        for extent, concept in self.lattice.items():

            for g in generators:
                if concept.attrs == g.attrs:
                    gen = g

                    ant_support = len(concept.objects) / objects_count
                    children = self.lattice[concept.objects].children

                    for attrs in gen.generator:
                        if len(children) != 0 and len(concept.attrs) != 0:
                            for child in children:

                                cons_support = len(child.objects - frozenset({EMPTY_VALUE})) / objects_count
                                potential_cons = [i for i in child.attrs if i not in concept.attrs]

                                rule_conf = cons_support / ant_support

                                if len(potential_cons) != 0:
                                    rules.append(DyadicAssociationRule(attrs, potential_cons, cons_support, rule_conf))

                        rule_support = len(concept.objects - frozenset({EMPTY_VALUE})) / objects_count
                        potential_cons = [i for i in concept.attrs if i not in attrs]

                        if len(potential_cons) != 0:
                            rules.append(DyadicAssociationRule(attrs, potential_cons, rule_support,  1.0))

        return rules

    def compute_generators(self) -> List[DyadicGenerator]:
        generators: List[DyadicGenerator] = []

        for extent, concept in self.lattice.items():
            gen = []

            if len(concept.attrs) > 0:
                parents = concept.parents
                faces = []
                for p in parents:
                    faces.append(concept.attrs - p.attrs)

                if len(faces) > 0:
                    first_face = faces.pop(0)
                    for f in first_face:
                        gen.append(frozenset({f}))

                    if len(faces) > 0:
                        for f in faces:
                            min_blockers = []
                            blockers = []

                            for g in gen:
                                if len(g & f) == 0:
                                    for element in f:
                                        union = frozenset({element}) | g
                                        if union not in blockers:
                                            blockers.append(union)
                                else:
                                    if frozenset(g) not in min_blockers:
                                        min_blockers.append(frozenset(g))

                            if len(blockers) == 0:
                                gen = min_blockers
                            elif len(min_blockers) == 0:
                                gen = blockers
                            else:
                                result = []
                                for b in blockers:
                                    for min_b in min_blockers:
                                        if min_b <= b:
                                            if b not in result:
                                                result.append(b)
                                                break
                                gen = list(frozenset(min_blockers) | (frozenset(blockers) - frozenset(result)))
                else:
                    gen = [frozenset({i}) for i in concept.attrs]

            generators.append(DyadicGenerator(concept.attrs, gen))

        return generators
    
    @staticmethod
    def build_lattice_iPred(concepts: List[DyadicConcept]) -> Tuple[DyadicLattice, List[DyadicLink]]:
        attributes = [c.attrs for c in concepts]

        attributes.sort(key=len)

        if frozenset({EMPTY_VALUE}) not in attributes:
            attributes.insert(0, frozenset({EMPTY_VALUE}))

        empty_set = {EMPTY_VALUE}
        faces = {}
        links = []
        concepts_lattice = DyadicLattice()

        for i in attributes:
            faces[i] = empty_set

        border = attributes.pop(0)

        for Ci in attributes:
            candidates = set({})

            for element in border:
                candidates = candidates | frozenset({(Ci & frozenset(element))})

            candidates = (candidates - frozenset({frozenset({})})) | empty_set

            for element in candidates:
                delta_intersection = Ci & faces[frozenset(element)]
                if len(delta_intersection) == 0 or delta_intersection == empty_set:
                    concepts_lattice.add_connection(Ci, set(element), concepts)

                    links.append(
                        DyadicLink(
                            DyadicLattice.__getObjectFromAttr(Ci, concepts),
                            DyadicLattice.__getObjectFromAttr(frozenset(element), concepts)
                        )
                    )
                    faces[frozenset(element)] = (faces[frozenset(element)] | (Ci - set(element))) - empty_set
                    border = (border - frozenset({element})) - empty_set

            border = border | {Ci}

        return concepts_lattice, links

    @staticmethod
    def __getObjectFromAttr(attrs: frozenset, concepts: List[DyadicConcept]) -> frozenset:
        for c in concepts:
            if c.attrs == attrs:
                return c.objects

        return frozenset(EMPTY_VALUE)

    def __repr__(self) -> str:
        return f'DyadicLattice({self.lattice})'
