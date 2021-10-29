# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List
import csv

from fcatools.dyadic.dyadic_context import DyadicContext
from fcatools.dyadic.dyadic_incidence import DyadicIncidence
from .triadic_incidence import TriadicIncidence

class TriadicContext:
    def __init__(self, incidences, objects, attributes, conditions):
        self.incidences: List[TriadicIncidence] = incidences
        self.objects = objects
        self.attributes = attributes
        self.conditions = conditions

    def get_density(self):
        unique_incidences = []

        for i in self.incidences:
            for attr in i.attr:
                for condition in i.conditions:
                    incidence = (i.obj, attr, condition)

                    if incidence not in unique_incidences:
                        unique_incidences.append(incidence)

        incidences_count = len(unique_incidences)
        total = len(self.objects) * len(self.attributes) * len(self.conditions)

        return incidences_count / total

    def flat_triadic_to_dyadic(self, divider='.') -> DyadicContext:
        incidences = {}
        objects = []
        attributes = []

        for incidence in self.incidences:
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
            d = DyadicIncidence(obj, attr)
            dyadic_incidences.append(d)

        return DyadicContext(dyadic_incidences, objects, attributes)

    def write_triadic_context_data(self, path, entries_delimiter=' ', conditions_delimiter=','):
        with open(path, mode='w', newline='', encoding='utf-8') as triadic_file:
            writer = csv.writer(triadic_file, delimiter=entries_delimiter)

            for i in self.incidences:
                conditions = conditions_delimiter.join(i.conditions)
                writer.writerow([i.obj, i.attr, conditions])

        triadic_file.close()

    @staticmethod
    def read_triadic_context_data(path, entries_delimiter=' ', conditions_delimiter=',') -> TriadicContext:
        input_file = open(path, 'r')
        rdr = csv.reader(input_file, delimiter=entries_delimiter)

        objects = []
        attributes = []
        conditions = []

        incidences = []
        for rec in rdr:
            assert len(rec) == 3, "Triadic contexts should contain only objects, attributes and conditions"


            obj = str(rec[0].strip())
            if obj not in objects:
                objects.append(obj)

            attr = str(rec[1].strip())
            if attr not in attributes:
                attributes.append(attr)
            
            incidence_conditions = []
            for condition in str(rec[2].strip()).split(conditions_delimiter):
                if condition not in conditions:
                    conditions.append(condition)

                incidence_conditions.append(condition)

            incidence = TriadicIncidence(obj, attr, incidence_conditions)
            incidences.append(incidence)

        input_file.close()

        return TriadicContext(incidences, objects, attributes, conditions)

    def __repr__(self):
        return f'TriadicContext({self.incidences}, {self.objects}, {self.attributes}, {self.conditions})'
        