# -*- coding: utf-8 -*-
class DyadicIncidence:
    def __init__(self, obj, attrs):
        self.obj = obj
        self.attrs = attrs

    def __str__(self):
        return f'obj, attr = ({self.obj}), ({self.attrs})'

    def __repr__(self):
        return f'DyadicIncidence({self.obj}, {self.attrs})'
