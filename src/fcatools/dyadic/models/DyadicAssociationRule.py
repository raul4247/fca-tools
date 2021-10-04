class DyadicAssociationRule:
    def __init__(self, generator, potential_cons, support, confidence):
        self.generator = generator
        self.potential_cons = potential_cons
        self.support = support
        self.confidence = confidence

    def __repr__(self):
        return f'{self.generator} -> {self.potential_cons} (sup: {self.support}, conf: {self.confidence})'
