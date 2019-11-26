import unittest
from qgraph import QGraph


class QGraphTests(unittest.TestCase):
    """Test for representation of qgraphs with error situations"""
    # def test_error_init_types(self):
    #     with self.assertRaises(ValueError):
    #         QGraph(typeof='')
    #     with self.assertRaises(ValueError):
    #         QGraph(typeof='fuck')
    """Tests for representation settings of qgraphs w/out errors"""
    def test_init_getType(self):
        self.assertEqual(QGraph(typeof='AL', structure={1: [2, 3], 2: [4]}).getType(), 'AL')
        # self.assertEqual(QGraph(typeof='AM', structure=[[0, 1], [1, 0]]).getType(), 'AM')
        # self.assertEqual(QGraph(typeof='LE', structure=[[1, 2], [1, 3], [2, 3]]).getType(), 'LE')
        # self.assertEqual(QGraph(typeof='IM', structure=[[1, 0, 1], [1, 1, 1], [0, 1, 0]]).getType(), 'IM')
        # self.assertIsNone(QGraph().getType())
        # self.assertIsNone(QGraph(typeof=None).getType())
    """Tests for getName"""
    def test_name_get(self):
        self.assertEqual(QGraph(name='TestName').getName(), 'TestName')
    """Tests for setName > getName combos"""
    def test_name_set_get(self):
        self.assertEqual(QGraph().setName('TestName').getName(), 'TestName')
    """Tests for setName > delName > getName combos"""
    def test_name_set_del_get(self):
        self.assertIsNone(QGraph().setName('TestName').delName().getName())
    """Tests for getStructure"""
    def test_structure_get(self):
        self.assertEqual(QGraph().getStructure(), {})
        self.assertEqual(QGraph(name='TestName').getStructure(), {})
        self.assertEqual(QGraph(typeof='AL', structure={1: [2, 3], 2: [3]}).getStructure(), {1: [2, 3], 2: [3]})
        # self.assertEqual(QGraph(typeof='AM', structure=[[0, 0], [1, 0]]).getStructure(), [[0, 0], [1, 0]])
        # self.assertEqual(QGraph(typeof='LE', structure=[[1, 3], [1, 2]]).getStructure(), [[1, 3], [1, 2]])
        # self.assertEqual(QGraph(typeof='IM', structure=[[1, 1], [1, 1]]).getStructure(), [[1, 1], [1, 1]])
    """Tests for updateStructure > getStructure combos"""
    def test_structure_update_get(self):
        self.assertEqual(QGraph().updateStructure({1: [2, 3], 2: [3]}).getStructure(), {1: [2, 3], 2: [3]})
    """Tests for clearStructure > getStructure combos"""
    def test_structure_clear_get(self):
        self.assertEqual(QGraph().clearStructure().getStructure(), {})
    """Tests for updateStructure > clearStructure > getStructure combos"""
    def test_structure_update_clear_get(self):
        self.assertEqual(QGraph().updateStructure({1: [2, 3], 2: [3]}).clearStructure().getStructure(), {})
    """Tests for addEdge > getStructure combos"""
    def test_edge_add_getStructure(self):
        self.assertEqual(QGraph().addEdge(1, 2).getStructure(), {1: [2], 2: []})
        self.assertEqual(QGraph().addEdge(2, 1).getStructure(), {1: [], 2: [1]})
        self.assertEqual(QGraph().addEdge(1, 2).addEdge(2, 1).getStructure(), {1: [2], 2: [1]})
        self.assertEqual(QGraph().addEdge(1, 2).addEdge(2, 1).addEdge(2, 3).getStructure(), {1: [2], 2: [1, 3], 3: []})
    """Tests for addEdge > delEdge > getStructure"""
    def test_edge_del_getStructure(self):
        self.assertEqual(QGraph().addEdge(1, 2).addEdge(2, 1).delEdge(1, 2).getStructure(), {1: [], 2: [1]})
        g = QGraph().addEdge(1, 2).addEdge(1, 3).addEdge(3, 2)
        with self.assertRaises(ValueError):
            g.delEdge(4, 5)
    """Tests for delNode"""
    def test_node_del(self):
        self.assertEqual(QGraph(structure={1: [2, 3], 2: [3, 4], 3: [], 4: [1]}).delNode(3).getStructure(),
                         {1: [2], 2: [4], 4: [1]})
        self.assertEqual(QGraph(structure={1: [2], 2: [1]}).delNode(2).getStructure(), {1: []})
        self.assertEqual(QGraph(structure={1: [2], 2: [1]}).delNode(2).delNode(1).getStructure(), {})
    """Tests for weight_of_nodes"""
    def test_weight_of_nodes(self):
        self.assertEqual(QGraph(structure={1: [2, 3], 2: [3, 4], 3: [], 4: [1]}).weight_of_nodes(), {1: 1, 2: 1, 3: 2,
                                                                                                     4: 1})
    """Tests for isolated_nodes"""
    def test_isolated_nodes(self):
        self.assertEqual(QGraph(structure={1: [2, 3], 2: [3, 4], 3: [], 4: [1]}).isolated_nodes(), [])
        self.assertEqual(QGraph(structure={1: [2, 3], 2: [3], 3: [], 4: []}).isolated_nodes(), [4])


if __name__ == '__main__':
    unittest.main()
