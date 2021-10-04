from typing import List

from src.fcatools.consts import EMPTY_VALUE


class DyadicConcept:
    def __init__(self, objects, attrs):
        self.objects = objects
        self.attrs = attrs
        self.parents: List[DyadicConcept] = []
        self.children: List[DyadicConcept] = []

    def add_connection(self, other_concept):
        self_length = len(self.objects)
        other_length = len(other_concept.objects)

        if self.objects == frozenset({EMPTY_VALUE}):
            self_length -= 1

        if other_concept.objects == frozenset({EMPTY_VALUE}):
            other_length -= 1

        if self_length > other_length:
            self.children.append(other_concept)
            other_concept.parents.append(self)
        elif other_length > self_length:
            other_concept.children.append(self)
            self.parents.append(other_concept)
