import unittest
from gif_plot import Point, gif_plotter
import abm_model


class TestPoint(unittest.TestCase):

    def test_attributes(self):
        a = Point([1, 2])
        self.assertListEqual(a.position, [1, 2])
        self.assertIsNone(a.data)
        self.assertIsNone(a.history)

    def test_representation(self):
        a = Point([1, 2])
        self.assertEqual(str(a), 'Point(position = [1, 2], data = None, history = None)')

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            Point(['123', 2])
        with self.assertRaises(ValueError):
            Point([1])


class TestGifPlotter(unittest.TestCase):

    def test_attributes(self):
        a = abm_model.Minicell(recovery_period=100)
        gif = gif_plotter(a)
        self.assertIsNone(gif.point_list)

    def test_error_cases(self):
        a = abm_model.Minicell(recovery_period=100)
        gif = gif_plotter(a)
        with self.assertRaises(KeyError):
            gif.gif_plotter()
        with self.assertRaises(TypeError):
            gif_plotter('a')

    def test_points_manipulation(self):
        a = abm_model.Minicell(I0=1, population_size=1)
        gif = gif_plotter(a)
        gif.points_manipulation()
        p = Point([0.1, 0.125])
        p.data = a.i_list[0]

        p.history = [None, 0]
        self.assertEqual(gif.point_list[0], p)


if __name__ == "__main__":
    unittest.main()
