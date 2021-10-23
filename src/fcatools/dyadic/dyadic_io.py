# -*- coding: utf-8 -*-

import csv
import xmltodict

from src.fcatools.dyadic.models.DyadicContext import DyadicContext
from src.fcatools.dyadic.models.DyadicIncidence import DyadicIncidence


def read_dyadic_context_data(path, entries_delimiter=' ', attrs_delimiter=',') -> DyadicContext:
    input_file = open(path, 'r')
    rdr = csv.reader(input_file, delimiter=entries_delimiter)

    objects = []
    attributes = []

    incidences = []
    for rec in rdr:
        assert len(rec) == 2, "Dyadic contexts should contain only objects and attributes"

        incidence = DyadicIncidence()

        obj = str(rec[0].strip())
        if obj not in objects:
            objects.append(obj)

        incidence.obj = obj

        for attr in str(rec[1].strip()).split(attrs_delimiter):
            if attr not in attributes:
                attributes.append(attr)

            incidence.attrs.append(attr)

        incidences.append(incidence)

    input_file.close()

    return DyadicContext(incidences, objects, attributes)


def write_dyadic_context_data(dyadic_context: DyadicContext, path, entries_delimiter=' ', attributes_delimiter=','):
    with open(path, mode='w', newline='', encoding='utf-8') as dyadic_file:
        writer = csv.writer(dyadic_file, delimiter=entries_delimiter)

        for i in dyadic_context.incidences:
            attrs = attributes_delimiter.join(i.attrs)
            writer.writerow([i.obj, attrs])

    dyadic_file.close()


def read_dyadic_context_cex(path) -> DyadicContext:
    with open(path) as cex_file:
        content = xmltodict.parse(cex_file.read())

        cex_conceptual_system = content['ConceptualSystem']

        objects = []
        attributes = []
        incidences = []

        if cex_conceptual_system.get('Contexts'):
            cex_context = cex_conceptual_system['Contexts']['Context']

            for obj in cex_context['Objects']['Object']:
                new_obj = obj['Name']

                if new_obj not in objects:
                    objects.append(new_obj)

                new_attr = None
                for attrs_ids in obj['Intent']['HasAttribute']:
                    attr_id = attrs_ids['@AttributeIdentifier']
                    for attr in cex_context['Attributes']['Attribute']:
                        if attr_id == attr['@Identifier']:
                            new_attr = attr['Name']
                            break

                    assert new_attr is not None, "Invalid .cex file!"

                    if new_attr not in attributes:
                        attributes.append(new_attr)

                    dyadic_incidence = DyadicIncidence()
                    dyadic_incidence.objects = new_obj
                    dyadic_incidence.attrs = [new_attr]

                    incidences.append(dyadic_incidence)

            return DyadicContext(incidences, objects, attributes)
