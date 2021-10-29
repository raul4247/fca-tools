# -*- coding: utf-8 -*-
class TriadicIncidence:
    def __init__(self, obj, attr, conditions):
        self.obj = obj
        self.attr = attr
        self.conditions = conditions

    def __str__(self):
        return f'obj, attr, cond = ({self.obj}), ({self.attr}), ({self.conditions})'

    def __repr__(self):
        return f'TriadicIncidence({self.obj}, {self.attr}, {self.conditions})'
