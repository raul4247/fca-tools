from typing import Dict

from src.fcatools.consts import EMPTY_VALUE
from src.fcatools.dyadic.models.DyadicConcept import DyadicConcept


class DyadicLattice:
    def __init__(self):
        self.lattice: Dict[frozenset, DyadicConcept] = {}

    def add_connection(self, intent_1, intent_2, concepts):
        concepts_reversed = {attr: obj for obj, attr in concepts.items()}

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
