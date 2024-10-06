import unittest
from src.utils.story_beats import *


class TestStoryBeats(unittest.TestCase):

    def test_change_beat(self):
        random.seed(200)
        result = change_beat(0)
        self.assertEqual(type(result), tuple)
        self.assertEqual(type(result[0]), tuple)
        self.assertEqual(result[0], list(BEATS.items())[1])
        self.assertEqual(result[1], False)

    def test_change_beat_end(self):
        random.seed(200)
        result = change_beat(8)
        self.assertEqual(type(result), tuple)
        self.assertEqual(type(result[0]), tuple)
        self.assertEqual(result[0], list(BEATS.items())[9])
        self.assertEqual(result[1], True)

    def test_change_beat_no_change(self):
        random.seed(100)
        result = change_beat(0)
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], None)
        self.assertEqual(result[1], False)

    def test_get_first_beat(self):
        result = get_initial_beat()
        self.assertEqual(type(result), tuple)
        self.assertEqual(result, list(BEATS.items())[0])
