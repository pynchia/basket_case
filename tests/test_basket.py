import pytest

from basket_case import fit_objects_into_baskets


def test_fit_objects_bigger_than_basket(oversize_objects_all_five):
    baskets = iter(fit_objects_into_baskets(oversize_objects_all_five, 4))
    try:
        next(baskets)
    except ValueError as err:
        assert err.args[0] == oversize_objects_all_five
