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

    def delEdge(self, start, finish):
        if start in self._structure.keys():
            ssStart = self._structure[start]
            if finish in ssStart:
                ssStart.pop(ssStart.index(finish))
                self._structure.update({start: ssStart})
            else:
                raise ValueError('Node <' + str(finish) + '> doesnt exist in graph as end of edge from <' + str(start)
                                 + '> node.')
        else:
            raise ValueError('Node <' + str(finish) + '> doesnt exist in graph as end of edge from <' + str(start)
                             + '> node.')
        return self

    def delNode(self, node):
        if node in list(self._structure.keys()):
            del self._structure[node]
        ssV = list(self._structure.values())
        for x in range(len(ssV)):
            if node in ssV[x]:
                ssV[x].pop(ssV[x].index(node))
        return self

    def getType(self):
        return self._typeof

    def setName(self, name):
        self._name = name
        return self

    def getName(self):
        return self._name

    def delName(self):
        self._name = None
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

    def weight_of_nodes(self):
        m = {key: 0 for key in self._structure.keys()}
        for key, value in self._structure.items():
            for elem in value:
                m.update({elem: m[elem]+1})
        return m

    def isolated_nodes(self):
        xm = {key: 0 for key in self._structure.keys()}
        for key, value in self._structure.items():
            if value == []:
                for _key, _value in self._structure.items():
                    for elem in _value:
                        if elem == key:
                            xm.update({key: xm[key]+1})
                            break
            else:
                xm.update({key: xm[key]+1})
        return [key for key in xm.keys() if xm[key] == 0]
