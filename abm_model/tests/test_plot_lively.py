import pytest
import numpy.testing as npt
from abm_model.gif_plot import Point, gif_plotter
import abm_model


def test_point_attri():

    a = Point([1, 2])
    npt.assert_equal(a.position, [1, 2])
    npt.assert_equal(a.data, None)
    npt.assert_equal(a.history, None)


def test_point_repr():

    a = Point([1, 2])
    npt.assert_string_equal('Point(position = [1, 2], data = None, history = None)', str(a))


def test_gif_plotter_attri():

    a = abm_model.Minicell(recovery_period=100)
    gif = gif_plotter(a)
    npt.assert_equal(gif.point_list, None)


def test_gif_plotter_error():

    a = abm_model.Minicell(recovery_period=100)
    gif = gif_plotter(a)
    with pytest.raises(KeyError):
        gif.gif_plotter()

    with pytest.raises(TypeError):
        gif_plotter('a')


def test_gif_plotter_points_manipulation():

    a = abm_model.Minicell(population_size=1)
    gif = gif_plotter(a)
    gif.points_manipulation()
    p = Point([0.1, 0.125])
    p.data = abm_model.Person('0', abm_model.Infected(1, 1))
    p.history = [None, 0]
    if gif.point_list[0] == p:
        pass
    else:
        raise AssertionError("Manipulation unexpected")

