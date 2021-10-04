# -*- coding: utf-8 -*-

from src.fcatools.dyadic.models.DyadicLattice import DyadicLattice


def compute_generators(dyadic_lattice: DyadicLattice):
    generators = {}

    for extent, concept in dyadic_lattice.lattice.items():
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

        generators[concept.attrs] = gen

    return generators
