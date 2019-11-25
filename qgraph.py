class QGraph(object):
    _name = None
    _type = None
    _structure = []

    def __init__(self, name=None, typeof=None, structure=None):
        if typeof not in [None, 'AM', 'IM', 'AL', 'LE']:
            raise ValueError('A QGraph can only be represented as an adjacency matrix(AM), an incidence matrix(IM), an'
                             ' adjacency list(AL), and a list of edges(LE) or created manually(None)')
        else:
            self._name = name
            if typeof is not None:
                self._type = typeof
                if structure is not None:
                    self._structure = structure
                else:
                    raise ValueError('A QGraph can only be represented as an adjacency matrix(AM), an incidence '
                                     'matrix(IM), an adjacency list(AL), and a list of edges(LE) or '
                                     'created manually(None)')
            else:
                self._type = None

    # def addNode(self, start, finis):
    def getType(self):
        return self._type

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
        del self._structure
        return self

    def draw(self):
        from vizualise import vizualise_0 as vis
        vis(self)

    def __del__(self):
        del self
