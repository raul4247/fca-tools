# -*- coding: utf-8 -*-

class TriadicAssociationRule:
    def __init__(self, left_side, right_side, condition, support, confidence):
        self.left_side = left_side
        self.right_side = right_side
        self.condition = condition
        self.support = support
        self.confidence = confidence

    def __repr__(self):
        return f'({list(self.left_side)} -> {list(self.right_side)}) {list(self.condition)} (sup: {self.support}, conf: {self.confidence})'
