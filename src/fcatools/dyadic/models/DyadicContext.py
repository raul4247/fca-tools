# -*- coding: utf-8 -*-

from typing import List

from src.fcatools.dyadic.models.DyadicIncidence import DyadicIncidence


class DyadicContext:
    def __init__(self, incidences, objects, attributes):
        self.incidences: List[DyadicIncidence] = incidences
        self.objects = objects
        self.attributes = attributes

    def get_density(self):
        unique_incidences = []

        for i in self.incidences:
            for attr in i.attrs:
                incidence = (i.obj, attr)

                if incidence not in unique_incidences:
                    unique_incidences.append(incidence)

        incidences_count = len(unique_incidences)
        total = len(self.objects) * len(self.attributes)

        return incidences_count / total
