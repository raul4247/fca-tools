class TriadicIncidence:
    def __init__(self):
        self.obj = None
        self.attr = None
        self.conditions = []

    def __repr__(self):
        return f'Obj: {self.obj} Attr: {self.attr} Cond: {self.conditions}'
