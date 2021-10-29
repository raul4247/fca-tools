# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List
import os

from fcatools import EMPTY_VALUE

class DyadicConcept:
    def __init__(self, objects, attrs):
        self.objects: frozenset = objects
        self.attrs: frozenset = attrs
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

    @staticmethod
    def get_concepts_d_peeler(context_file, output_file) -> List[DyadicConcept]:
        os.system('d-peeler {0} --out {1}'.format(context_file, output_file))

        return DyadicConcept.read_concepts_from_file(output_file)

    @staticmethod
    def read_concepts_from_file(output_file) -> List[DyadicConcept]:
        file = open(output_file, 'r', encoding='utf-8')
        concepts: List[DyadicConcept] = []

        for line in file.readlines():
            obj, attr = line.rstrip('\n').split(' ')
            obj_set = frozenset(obj.split(','))
            attr_set = frozenset(attr.split(','))

            concepts.append(DyadicConcept(obj_set, attr_set))

        return concepts

    def __str__(self) -> str:
        return f'{self.objects} - {self.attrs}'

    def __repr__(self) -> str:
        return f'DyadicConcept({self.objects}, {self.attrs})'
        