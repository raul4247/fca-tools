# -*- coding: utf-8 -*-
from src.fcatools.dyadic.DyadicConcept import DyadicConcept


def __add_connection_on_lattice(intent_1, intent_2, concepts_reversed, concepts_lattice):
    intent_1 = frozenset(intent_1)
    intent_2 = frozenset(intent_2)

    if intent_1 in concepts_reversed and intent_2 not in concepts_reversed:
        extent = concepts_reversed[intent_1]
        if extent not in concepts_lattice:
            concepts_lattice[extent] = DyadicConcept(extent, intent_1)

    elif intent_2 in concepts_reversed and intent_1 not in concepts_reversed:
        extent = concepts_reversed[intent_2]
        if extent not in concepts_lattice:
            concepts_lattice[extent] = DyadicConcept(extent, intent_2)

    elif intent_2 in concepts_reversed and intent_1 in concepts_reversed:
        extent_1 = concepts_reversed[intent_1]
        extent_2 = concepts_reversed[intent_2]

        if extent_1 in concepts_lattice and extent_2 in concepts_lattice:
            concepts_lattice[extent_1].add_connection(concepts_lattice[extent_2])
        elif extent_1 not in concepts_lattice and extent_2 in concepts_lattice:
            c = DyadicConcept(extent_1, intent_1)
            c.add_connection(concepts_lattice[extent_2])
            concepts_lattice[extent_1] = c
        elif extent_1 in concepts_lattice and extent_2 not in concepts_lattice:
            c = DyadicConcept(extent_2, intent_2)
            c.add_connection(concepts_lattice[extent_1])
            concepts_lattice[extent_2] = c
        else:
            c1 = DyadicConcept(extent_1, intent_1)
            c2 = DyadicConcept(extent_2, intent_2)
            c1.add_connection(c2)
            concepts_lattice[extent_1] = c1
            concepts_lattice[extent_2] = c2

    return concepts_lattice


def build_lattice_iPred(concepts):
    links_count = 0
    attributes = concepts.values()
    attributes = [i for i in attributes]

    attributes.sort(key=len)

    if frozenset({'ø'}) not in attributes:
        attributes.insert(0, frozenset({'ø'}))

    empty_set = {'ø'}
    faces = {}
    links = []
    concepts_lattice = {}
    concepts_reversed = {attr: obj for obj, attr in concepts.items()}

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
                concepts_lattice = __add_connection_on_lattice(Ci, set(element), concepts_reversed, concepts_lattice)
                links_count += 1
                links.append([Ci, set(element)])
                faces[frozenset(element)] = (faces[frozenset(element)] | (Ci - set(element))) - empty_set
                border = (border - frozenset({element})) - empty_set

        border = border | {Ci}

    return links
