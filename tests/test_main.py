from contextlib import nullcontext as does_not_raise

import pytest

from src.main import Calculator


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            (5.5, -1, 4.5, does_not_raise()),
            (5, "1", 5, pytest.raises(TypeError)),
        ],
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 1, 0, does_not_raise()),
            (1, -1, 2, does_not_raise()),
            (1, 2, -1, does_not_raise()),
            (5, "1", 4, pytest.raises(TypeError)),
        ],
    )
    def test_minus(self, x, y, res, expectation):
        with expectation:
            assert Calculator().minus(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (2, 2, 4, does_not_raise()),
            (2, 2.5, 5, does_not_raise()),
            (2.2, 2, 4.4, does_not_raise()),
            (5, "1", 5, pytest.raises(TypeError)),
            (5, 0, 0, does_not_raise()),
        ],
    )
    def test_multiplication(self, x, y, res, expectation):
        with expectation:
            assert Calculator().multiplication(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (7.5, 2.5, 3.0, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "1", 5, pytest.raises(TypeError)),
            (5, 0, 5, pytest.raises(ZeroDivisionError)),
        ],
    )
    def test_devide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (2, 2, 4, does_not_raise()),
            (5, 5, 3125, does_not_raise()),
            (5, "1", 5, pytest.raises(TypeError)),
            (5, 0, 1, does_not_raise()),
            (5, -1, 0.2, does_not_raise()),
            (-5, 1, -5, does_not_raise()),
        ],
    )
    def test_exponentiation(self, x, y, res, expectation):
        with expectation:
            assert Calculator().exponentiation(x, y) == res

    @pytest.mark.parametrize(
        "x, res, expectation",
        [
            (25, 5, does_not_raise()),
            (125, 11.180339887498949, does_not_raise()),
            ("25", 5, pytest.raises(TypeError)),
        ],
    )
    def test_square_root(self, x, res, expectation):
        with expectation:
            assert Calculator().square_root(x) == res

    @pytest.mark.parametrize(
        "x, res, expectation",
        [
            (100, 1, does_not_raise()),
            (-5, -0.05, does_not_raise()),
            ("200", 2, pytest.raises(TypeError)),
        ],
    )
    def test_percent(self, x, res, expectation):
        with expectation:
            assert Calculator().percent(x) == res
