import unittest
from src.game import *

file_path = os.path.join(os.path.dirname(os.getcwd()), os.getcwd(), 'src/story/plot_tropes.csv')
file_path_2 = os.path.join(os.path.dirname(os.getcwd()), os.getcwd(), 'src/story/protagonist_tropes.csv')
file_path_3 = os.path.join(os.path.dirname(os.getcwd()), os.getcwd(), 'src/story/antagonist_tropes.csv')


class TropeSelectionTests(unittest.TestCase):
    def test_read_valid_csv_file(self):
        result = read_csv_file(file_path)
        self.assertEqual(type(result), list)
        for r in result:
            self.assertEqual(type(r), dict)
            self.assertEqual(r.keys(), {"id": [], "name": [], "description": [], "conflicts": []}.keys())

    def test_read_invalid_csv_file(self):
        self.assertRaises(FileNotFoundError, read_csv_file, 'invalid.csv')

    def test_create_trope_objects(self):
        file_lines = read_csv_file(file_path)
        result = create_tropes(file_lines)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), len(file_lines))
        for r in result:
            self.assertEqual(type(r), Trope)

    def test_get_random_tropes(self):
        result = get_random_tropes(create_tropes(read_csv_file(file_path)), 3)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 3)
        ids = [r.id_ for r in result]
        for r in result:
            self.assertEqual(type(r), Trope)
            if r.conflicts:
                for c in r.conflicts:
                    self.assertEqual(c in ids, False)

    def test_select_tropes(self):
        result = select_tropes(file_path, file_path_2, file_path_3, 3, 1, 1)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 5)
        ids = [r.id_ for r in result]
        for r in result:
            self.assertEqual(type(r), Trope)
            if r.conflicts:
                for c in r.conflicts:
                    self.assertEqual(c in ids, False)
