# -*- coding: utf-8 -*-
from src.fcatools.consts import EMPTY_VALUE
from src.fcatools.dyadic.models.DyadicLattice import DyadicLattice


def build_lattice_iPred(concepts) -> DyadicLattice:
    links_count = 0
    attributes = concepts.values()
    attributes = [i for i in attributes]

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
                links_count += 1
                links.append([Ci, set(element)])
                faces[frozenset(element)] = (faces[frozenset(element)] | (Ci - set(element))) - empty_set
                border = (border - frozenset({element})) - empty_set

        border = border | {Ci}

    return concepts_lattice
