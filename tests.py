import unittest
from qgraph import QGraph


class InitTests(unittest.TestCase):
    """Test for representation of qgraphs with error situations"""
    def test_error_init_types(self):
        with self.assertRaises(ValueError):
            QGraph(typeof='')
        with self.assertRaises(ValueError):
            QGraph(typeof='fuck')


class TypeTests(unittest.TestCase):
    """Tests for representation settings of qgraphs w/out errors"""
    def test_normal_get_type(self):
        self.assertEqual(QGraph(typeof='AL', structure={1: [2, 3], 2: [4]}).getType(), 'AL')
        # self.assertEqual(QGraph(typeof='AM', structure=[[0, 1], [1, 0]]).getType(), 'AM')
        # self.assertEqual(QGraph(typeof='LE', structure=[[1, 2], [1, 3], [2, 3]]).getType(), 'LE')
        # self.assertEqual(QGraph(typeof='IM', structure=[[1, 0, 1], [1, 1, 1], [0, 1, 0]]).getType(), 'IM')
        self.assertIsNone(QGraph().getType())
        self.assertIsNone(QGraph(typeof=None).getType())


class NameTests(unittest.TestCase):
    """Tests for getName"""
    def test_name_get(self):
        self.assertEqual(QGraph(name='TestName').getName(), 'TestName')
    """Tests for setName > getName combos"""
    def test_name_set_get(self):
        self.assertEqual(QGraph().setName('TestName').getName(), 'TestName')
    """Tests for setName > delName > getName combos"""
    def test_name_set_del_get(self):
        self.assertEqual(QGraph().setName('TestName').delName().getName(), None)


class StructureTests(unittest.TestCase):
    """Tests for getStructure"""
    def test_structure_get(self):
        self.assertEqual(QGraph().getStructure(), [])
        self.assertEqual(QGraph(name='TestName').getStructure(), [])
        self.assertEqual(QGraph(typeof='AL', structure={1: [2, 3], 2: [3]}).getStructure(), {1: [2, 3], 2: [3]})
        # self.assertEqual(QGraph(typeof='AM', structure=[[0, 0], [1, 0]]).getStructure(), [[0, 0], [1, 0]])
        # self.assertEqual(QGraph(typeof='LE', structure=[[1, 3], [1, 2]]).getStructure(), [[1, 3], [1, 2]])
        # self.assertEqual(QGraph(typeof='IM', structure=[[1, 1], [1, 1]]).getStructure(), [[1, 1], [1, 1]])
    """Tests for updateStructure > getStructure combos"""
    def test_structure_update_get(self):
        self.assertEqual(QGraph().updateStructure({1: [2, 3], 2: [3]}).getStructure(), {1: [2, 3], 2: [3]})
    """Tests for clearStructure > getStructure combos"""
    def test_structure_clear_get(self):
        self.assertEqual(QGraph().clearStructure().getStructure(), [])
    """Tests for updateStructure > clearStructure > getStructure combos"""
    def test_structure_update_clear_get(self):
        self.assertEqual(QGraph().updateStructure({1: [2, 3], 2: [3]}).clearStructure().getStructure(), {1: [2, 3],
                                                                                                         2: [3]})


if __name__ == '__main__':
    unittest.main()


