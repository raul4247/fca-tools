# -*- coding: utf-8 -*-
class DyadicAssociationRule:
    def __init__(self, generator, potential_cons, support, confidence):
        self.generator = generator
        self.potential_cons = potential_cons
        self.support = support
        self.confidence = confidence

    def __str__(self):
        return f'{list(self.generator)} -> {self.potential_cons} (sup: {self.support}, conf: {self.confidence})'

    def __repr__(self):
        return f'DyadicAssociationRule({list(self.generator)}, {self.potential_cons}, {self.support}, {self.confidence})'
