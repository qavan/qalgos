class QGraph(object):
    _name = None
    _type = None
    _structure = []

    def __init__(self, name=None, typeof=None, structure=None):
        # if typeof not in [None, 'AM', 'IM', 'AL', 'LE']:
        if typeof not in [None, 'AL']:
            raise ValueError('Now QGraph can only be represented as an adjacency list(AL)')
        else:
            if structure is None:
                ...
            elif type(structure) is list or type(structure) is dict:
                self._structure = structure
            else:
                raise ValueError('Now QGraph can only be represented as an adjacency list(AL) uses dict')
            self._name = name
            self._type = typeof

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
