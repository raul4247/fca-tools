# -*- coding: utf-8 -*-

class TriadicIncidence:
    def __init__(self):
        self.obj = None
        self.attr = None
        self.conditions = []

    def __repr__(self):
        return f'obj, attr, cond = ({self.obj}), ({self.attr}), ({self.conditions})'
