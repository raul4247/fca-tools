from fcatools.dyadic.DyadicContext import DyadicContext
from fcatools.dyadic.DyadicIncidence import DyadicIncidence
from fcatools.triadic.TriadicContext import TriadicContext


def flat_triadic_to_dyadic(triadic_context: TriadicContext, divider='.') -> DyadicContext:
    incidences = []
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

        dyadic_incidence = DyadicIncidence()
        dyadic_incidence.obj = obj
        dyadic_incidence.attrs = dyadic_attrs

        incidences.append(dyadic_incidence)

    return DyadicContext(incidences, objects, attributes)
