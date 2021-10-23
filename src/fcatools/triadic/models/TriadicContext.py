# -*- coding: utf-8 -*-

from typing import List

from src.fcatools.triadic.models.TriadicIncidence import TriadicIncidence


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
