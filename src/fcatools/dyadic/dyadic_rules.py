# -*- coding: utf-8 -*-
from typing import List

from src.fcatools.consts import EMPTY_VALUE
from src.fcatools.dyadic.models.DyadicAssociationRule import DyadicAssociationRule
from src.fcatools.dyadic.models.DyadicLattice import DyadicLattice


# TODO:
#  * make generators be a class
#  * make link be a class
def compute_association_rules(
        dyadic_lattice: DyadicLattice,
        generators  # TODO create generators class
) -> List[DyadicAssociationRule]:

    rules = []
    objects_count = dyadic_lattice.get_objects_count()

    for extent, concept in dyadic_lattice.lattice.items():
        if concept.attrs in generators:

            ant_support = len(concept.objects) / objects_count
            children = dyadic_lattice.lattice[concept.objects].children

            for g in generators[concept.attrs]:
                if len(children) != 0 and len(concept.attrs) != 0:
                    for child in children:

                        cons_support = len(child.objects - frozenset({EMPTY_VALUE})) / objects_count
                        potential_cons = [i for i in child.attrs if i not in concept.attrs]

                        rule_conf = cons_support / ant_support

                        if len(potential_cons) != 0:
                            rules.append(DyadicAssociationRule(g, potential_cons, cons_support, rule_conf))

                rule_support = len(concept.objects - frozenset({EMPTY_VALUE})) / objects_count
                potential_cons = [i for i in concept.attrs if i not in g]

                if len(potential_cons) != 0:
                    rules.append(DyadicAssociationRule(g, potential_cons, rule_support,  1.0))

    return rules
