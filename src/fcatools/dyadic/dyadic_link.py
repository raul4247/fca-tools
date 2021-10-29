# -*- coding: utf-8 -*-
class DyadicLink:
    def __init__(self, first: frozenset, second: frozenset):
        self.first = first
        self.second = second

    def __str__(self):
        return f'{list(self.first)} <-> {list(self.second)}'

    def __repr__(self):
        return f'DyadicLink({list(self.first)}, {list(self.second)})'
