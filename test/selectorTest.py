import unittest

from selector import DOWN
from selector import LEFT
from selector import RIGHT
from selector import UP
from selector import calc_selection_direction


class SelectorTest(unittest.TestCase):
    def test_directions(self):

        self.assertEqual(UP, calc_selection_direction((0, 1), (0, 0)))
        self.assertEqual(DOWN, calc_selection_direction((0, 0), (0, 1)))
        self.assertEqual(RIGHT, calc_selection_direction((0, 0), (1, 0)))
        self.assertEqual(LEFT, calc_selection_direction((1, 0), (0, 0)))


if __name__ == '__main__':
    unittest.main()
