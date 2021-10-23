# -*- coding: utf-8 -*-

from src.fcatools.dyadic.models.DyadicContext import DyadicContext
from src.fcatools.dyadic.models.DyadicIncidence import DyadicIncidence
from src.fcatools.triadic.models.TriadicContext import TriadicContext


def flat_triadic_to_dyadic(triadic_context: TriadicContext, divider='.') -> DyadicContext:
    incidences = {}
    objects = []
    attributes = []

    for incidence in triadic_context.incidences:
        obj = incidence.obj
        attr = incidence.attr
        conditions = incidence.conditions

        if obj not in objects:
            objects.append(obj)

        dyadic_attrs = []
        for condition in conditions:
            dyadic_attr = attr + divider + condition
            if dyadic_attr not in attributes:
                attributes.append(dyadic_attr)

            dyadic_attrs.append(dyadic_attr)

        if obj not in incidences:
            incidences[obj] = [a for a in dyadic_attrs]
        else:
            incidences[obj] += dyadic_attrs

    dyadic_incidences = []

    for obj, attr in incidences.items():
        d = DyadicIncidence()
        d.obj = obj
        d.attrs = attr
        dyadic_incidences.append(d)

    return DyadicContext(dyadic_incidences, objects, attributes)
