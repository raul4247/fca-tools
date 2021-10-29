# -*- coding: utf-8 -*-
class DyadicGenerator:
    def __init__(self, attrs: frozenset, generator: set):
        self.attrs = attrs
        self.generator = generator

    def __str__(self):
        return f'{list(self.attrs)}: {list([list(g) for g in self.generator])}'

    def __repr__(self) -> str:
        return f'DyadicGenerator({self.attrs}, {self.generator})'
        