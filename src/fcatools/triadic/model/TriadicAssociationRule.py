class TriadicAssociationRule:
    # TODO verificar nomes
    def __init__(self, left_side, right_side, condition, support, confidence):
        self.left_side = left_side
        self.right_side = right_side
        self.condition = condition
        self.support = support
        self.confidence = confidence

    # TODO verificar representação
    def __repr__(self):
        return f'({self.left_side} -> {self.right_side}) {self.condition} (sup: {self.support}, conf: {self.confidence})'
