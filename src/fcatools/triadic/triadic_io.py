import csv

from src.fcatools.triadic.model.TriadicContext import TriadicContext
from src.fcatools.triadic.model.TriadicIncidence import TriadicIncidence


def read_triadic_context_data(path, entries_delimiter=' ', conditions_delimiter=',') -> TriadicContext:
    input_file = open(path, 'r')
    rdr = csv.reader(input_file, delimiter=entries_delimiter)

    objects = []
    attributes = []
    conditions = []

    incidences = []
    for rec in rdr:
        assert len(rec) == 3, "Triadic contexts should contain only objects, attributes and conditions"

        incidence = TriadicIncidence()

        obj = str(rec[0].strip())
        if obj not in objects:
            objects.append(obj)

        incidence.obj = obj

        attr = str(rec[1].strip())
        if attr not in attributes:
            attributes.append(attr)

        incidence.attr = attr

        for condition in str(rec[2].strip()).split(conditions_delimiter):
            if condition not in conditions:
                conditions.append(condition)

            incidence.conditions.append(condition)

        incidences.append(incidence)

    input_file.close()

    return TriadicContext(incidences, objects, attributes, conditions)


def write_triadic_context_data(triadic_context: TriadicContext, path, entries_delimiter=' ', conditions_delimiter=','):
    with open(path, mode='pnrks_concepts.txt', newline='', encoding='utf-8') as triadic_file:
        writer = csv.writer(triadic_file, delimiter=entries_delimiter)

        for i in triadic_context.incidences:
            conditions = conditions_delimiter.join(i.conditions)
            writer.writerow([i.objects, i.attr, conditions])

    triadic_file.close()
