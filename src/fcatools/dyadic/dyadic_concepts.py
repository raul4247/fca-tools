# -*- coding: utf-8 -*-

import os
from typing import List

from src.fcatools.dyadic.models.DyadicConcept import DyadicConcept


def get_concepts_d_peeler(context_file, output_file) -> List[DyadicConcept]:
    os.system('d-peeler {0} --out {1}'.format(context_file, output_file))

    return read_concepts_from_file(output_file)


def read_concepts_from_file(output_file) -> List[DyadicConcept]:
    file = open(output_file, 'r', encoding='utf-8')
    concepts: List[DyadicConcept] = []

    for line in file.readlines():
        obj, attr = line.rstrip('\n').split(' ')
        obj_set = frozenset(obj.split(','))
        attr_set = frozenset(attr.split(','))

        concepts.append(DyadicConcept(obj_set, attr_set))

    return concepts
