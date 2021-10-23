# -*- coding: utf-8 -*-

from typing import List, Tuple

from src.fcatools.consts import EMPTY_VALUE
from src.fcatools.dyadic.models.DyadicConcept import DyadicConcept
from src.fcatools.dyadic.models.DyadicLattice import DyadicLattice
from src.fcatools.dyadic.models.DyadicLink import DyadicLink


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
                        __getObjectFromAttr(Ci, concepts),
                        __getObjectFromAttr(frozenset(element), concepts)
                    )
                )
                faces[frozenset(element)] = (faces[frozenset(element)] | (Ci - set(element))) - empty_set
                border = (border - frozenset({element})) - empty_set

        border = border | {Ci}

    return concepts_lattice, links


def __getObjectFromAttr(attrs: frozenset, concepts: List[DyadicConcept]) -> frozenset:
    for c in concepts:
        if c.attrs == attrs:
            return c.objects

    return frozenset(EMPTY_VALUE)
