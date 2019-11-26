class QGraph(object):
    def __init__(self, name=None, typeof='AL', structure=None):
        self._name = name
        self._typeof = typeof
        if structure is None:
            self._structure = {}
        elif type(structure) is dict:
            self._structure = structure
        else:
            raise ValueError('Now QGraph can only be represented as an adjacency list(AL)')
        # [None, 'AM', 'IM', 'AL', 'LE']

    def addEdge(self, start, finish):
        ssk = self._structure.keys()
        if self._structure is {} or (start not in ssk and finish not in ssk):
            self._structure.update({start: [finish], finish: list()})
        elif start in ssk and finish in ssk:
            self._structure.update({start: self._structure[start] + [finish]})
        elif start in ssk:
            self._structure.update({start: self._structure[start] + [finish], finish: list()})
        elif finish in ssk:
            self._structure.update({start: [finish]})
        else:
            raise ValueError('Test')
        return self

    def getType(self):
        return self._typeof

    def setName(self, name):
        self._name = name
        return self

    def getName(self):
        return self._name

    def delName(self):
        del self._name
        return self

    def getStructure(self):
        return self._structure

    def updateStructure(self, structure):
        self._structure = structure
        return self

    def clearStructure(self):
        self._structure = {}
        return self

    def draw(self):
        from vizualise import vizualise_0 as vis
        vis(self)
