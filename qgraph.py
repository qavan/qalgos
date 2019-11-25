class QGraph(object):
    _name = 'QGraph class object'
    _type = None
    _structure = []

    def __init__(self, name=None, typeof=None, structure=None):
        if typeof not in [None, 'AM', 'IM', 'AL', 'LE']:
            raise Exception('A QGraph can only be represented as an adjacency matrix(AM), an incidence matrix(IM), an '
                            'adjacency list(AL), and a list of edges(LE) or created manually(None)')
        else:
            if typeof is not None:
                self._name = name
                self._type = typeof
                if typeof is 'AL':
                    self._structure = structure
                elif typeof is 'AM':
                    self._structure = structure
                elif typeof is 'LE':
                    self._structure = structure
                elif typeof is 'IM':
                    self._structure = structure
                else:
                    raise Exception('A QGraph can only be represented as an adjacency matrix(AM), an incidence '
                                    'matrix(IM), an adjacency list(AL), and a list of edges(LE) or created '
                                    'manually(None)')
            else:
                self._name = name

    # def addNode(self, start, finis):

    def __del__(self):
        del self

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def draw(self):
        from vizualise import vizualise_0 as vis
        vis(self)

qg = QGraph()
qg.setName('Simple graph')
