# -*- coding: utf-8 -*-

from typing import List, Tuple

from src.fcatools.dyadic.models.DyadicAssociationRule import DyadicAssociationRule
from src.fcatools.triadic.models.TriadicAssociationRule import TriadicAssociationRule


def calculate_bacars_from_dyadic_rules(
        dyadic_rules: List[DyadicAssociationRule],
        separator: str
) -> Tuple[List[TriadicAssociationRule], List[TriadicAssociationRule]]:
    implication_bacars = []
    association_bacars = []

    for dyadic_rule in dyadic_rules.copy():
        attrs = frozenset({})
        conditions = frozenset({})
        dyadic_rule.generator -= frozenset({'ø'})
        for i in dyadic_rule.generator:
            attr_cond = i.split(separator)
            attrs |= {attr_cond[0]}
            conditions |= {attr_cond[1]}

        if (len(attrs) * len(conditions)) == len(dyadic_rule.generator):
            bacars = __bacars_algorithm(
                attrs,
                conditions,
                dyadic_rule.potential_cons,
                dyadic_rule.support,
                dyadic_rule.confidence,
                separator
            )

            if len(bacars) > 0 and bacars[0].confidence == 1.0:
                implication_bacars += bacars
            else:
                association_bacars += bacars

    return implication_bacars, association_bacars


def calculate_bcaars_from_dyadic_rules(
        dyadic_rules: List[DyadicAssociationRule],
        separator: str
) -> Tuple[List[TriadicAssociationRule], List[TriadicAssociationRule]]:
    implication_bcaars = []
    association_bcaars = []

    for dyadic_rule in dyadic_rules.copy():
        attrs = frozenset({})
        conditions = frozenset({})
        dyadic_rule.generator -= frozenset({'ø'})
        for i in dyadic_rule.generator:
            attr_cond = i.split(separator)
            attrs |= {attr_cond[0]}
            conditions |= {attr_cond[1]}

        if (len(attrs) * len(conditions)) == len(dyadic_rule.generator):
            bcaars = __bcaars_algorithm(
                attrs,
                conditions,
                dyadic_rule.potential_cons,
                dyadic_rule.support,
                dyadic_rule.confidence,
                separator
            )

            if len(bcaars) > 0 and bcaars[0].confidence == 1.0:
                implication_bcaars += bcaars
            else:
                association_bcaars += bcaars

    return implication_bcaars, association_bcaars


def __bacars_algorithm(al, ml, rhs, support, confidence, separator) -> List[TriadicAssociationRule]:
    mr = frozenset({})
    c = []
    for e in rhs:
        attrs = {e.split(separator)[0]}
        attrs = attrs - (attrs - al)
        if len(attrs) > 0:
            c.append(e)

    if len(c) > 0:
        for e in c:
            modus = e.split(separator)[1]
            count = 0
            for i in c:
                if modus == i.split(separator)[1]:
                    count += 1

            if count == len(al):
                mr |= {modus}

    if len(mr) != 0:
        return [TriadicAssociationRule(ml, mr, al, support, confidence)]
    else:
        return []


def __bcaars_algorithm(al, ml, rhs, support, confidence, separator) -> List[TriadicAssociationRule]:
    ar = frozenset({})
    c = []
    for e in rhs:
        conditions = {e.split(separator)[1]}
        conditions = conditions - (conditions - ml)
        if len(conditions) > 0:
            c.append(e)

    if len(c) > 0:
        for e in c:
            attrs = e.split(separator)[0]
            count = 0
            for i in c:
                if attrs == i.split(separator)[0]:
                    count += 1

            if count == len(ml):
                ar |= {attrs}

    if len(ar) != 0:
        return [TriadicAssociationRule(al, ar, ml, support, confidence)]
    else:
        return []
