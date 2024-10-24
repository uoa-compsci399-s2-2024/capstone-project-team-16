import unittest
import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')))
from utils.narrative_elements import *

THEMES_FILE = os.path.join(os.path.dirname(os.getcwd()), 'src/story/themes.txt')
PLOT_TROPE_FILE = os.path.join(os.path.dirname(os.getcwd()), 'src/story/plot_tropes.csv')
PROTAGONIST_TROPE_FILE = os.path.join(os.path.dirname(os.getcwd()), 'src/story/protagonist_tropes.csv')
ANTAGONIST_TROPE_FILE = os.path.join(os.path.dirname(os.getcwd()), 'src/story/antagonist_tropes.csv')


class TropeSelectionTests(unittest.TestCase):
    def test_read_valid_csv_file(self):
        result = read_csv_file(PLOT_TROPE_FILE)
        self.assertEqual(type(result), list)
        for r in result:
            self.assertEqual(type(r), dict)
            self.assertEqual(r.keys(), {"id": [], "name": [], "description": [], "conflicts": []}.keys())

    def test_read_invalid_csv_file(self):
        self.assertRaises(FileNotFoundError, read_csv_file, 'invalid.csv')

    def test_create_trope_objects(self):
        file_lines = read_csv_file(PLOT_TROPE_FILE)
        result = create_tropes(file_lines)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), len(file_lines))
        for r in result:
            self.assertEqual(type(r), Trope)

    def test_get_random_tropes(self):
        result = get_random_tropes(create_tropes(read_csv_file(PLOT_TROPE_FILE)), 3)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 3)
        ids = [r.id_ for r in result]
        for r in result:
            self.assertEqual(type(r), Trope)
            if r.conflicts:
                for c in r.conflicts:
                    self.assertEqual(c in ids, False)

    def test_get_random_theme(self):
        result = get_random_theme(THEMES_FILE)
        self.assertEqual(type(result), str)

    def test_get_random_theme_invalid_file(self):
        self.assertRaises(FileNotFoundError, get_random_theme, 'invalid.csv')

    def test_select_narrative_elements(self):
        result = select_narrative_elements(THEMES_FILE, PLOT_TROPE_FILE, PROTAGONIST_TROPE_FILE, ANTAGONIST_TROPE_FILE,
                                           3, 1, 1)
        self.assertEqual(type(result[0]), str)
        self.assertEqual(type(result[1]), list)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[1]), 5)
        ids = [r.id_ for r in result[1]]
        for r in result[1]:
            self.assertEqual(type(r), Trope)
            if r.conflicts:
                for c in r.conflicts:
                    self.assertEqual(c in ids, False)
