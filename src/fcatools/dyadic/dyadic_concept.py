import os
from typing import Dict


def get_concepts_d_peeler(context_file, output_file) -> Dict[frozenset, frozenset]:
    os.system('d-peeler {0} --out {1}'.format(context_file, output_file))

    return read_concepts_from_file(output_file)


def read_concepts_from_file(output_file) -> Dict[frozenset, frozenset]:
    file = open(output_file, 'r', encoding='utf-8')
    concepts = {}

    for line in file.readlines():
        obj = frozenset(line.split(' ')[0].split(','))
        attr = frozenset([a.rstrip('\n') for a in line.split(' ')[1].split(',')])

        concepts.update({obj: attr})

    return concepts
