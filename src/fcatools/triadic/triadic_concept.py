# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List
import os

class TriadicConcept:
    def __init__(self, objects, attrs, conditions):
        self.objects = objects
        self.attrs = attrs
        self.conditions = conditions
    
    @staticmethod
    def get_concepts_d_peeler(context_file, output_file) -> List[TriadicConcept]:
        os.system('d-peeler {0} --out {1}'.format(context_file, output_file))

        return TriadicConcept.read_concepts_from_file(output_file)

    @staticmethod
    def read_concepts_from_file(output_file) -> List[TriadicConcept]:
        file = open(output_file, 'r', encoding='utf-8')
        concepts: List[TriadicConcept] = []

        for line in file.readlines():
            obj, attr, conditions = line.rstrip('\n').split(' ')

            obj_set = frozenset(obj.split(','))
            attr_set = frozenset(attr.split(','))
            conditions_set = frozenset(conditions.split(','))

            concepts.append(TriadicConcept(obj_set, attr_set, conditions_set))

        return concepts

    def __repr__(self):
        return f'TriadicConcept({self.incidences}, {self.objects}, {self.attrs}, {self.conditions})'
