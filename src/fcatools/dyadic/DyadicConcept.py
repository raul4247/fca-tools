class DyadicConcept:
    def __init__(self, obj, attrs):
        self.obj = attrs
        self.attrs = attrs
        self.parents = []
        self.children = []

    def add_connection(self, other_concept):
        self_length = len(self.obj)
        other_length = len(other_concept.obj)

        if self.obj == frozenset({'ø'}):
            self_length -= 1

        if other_concept.obj == frozenset({'ø'}):
            other_length -= 1

        if self_length > other_length:
            self.children.append(other_concept)
            other_concept.parents.append(self)
        elif other_length > self_length:
            other_concept.children.append(self)
            self.parents.append(other_concept)
