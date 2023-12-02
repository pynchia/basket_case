import pytest

from basket_case import fit_objects_into_baskets

from .fixtures import OK_OBJECTS, OVERSIZE_OBJECTS_2, OVERSIZE_OBJECTS_ALL


def test_fit_no_objects():
    baskets = iter(fit_objects_into_baskets({}, 4))
    with pytest.raises(StopIteration):
        next(baskets)


@pytest.mark.parametrize(
    "objects,expected_oversize_objs",
    [
        (OVERSIZE_OBJECTS_ALL, OVERSIZE_OBJECTS_ALL),
        (OK_OBJECTS|OVERSIZE_OBJECTS_2, OVERSIZE_OBJECTS_2),
    ],
    ids=[
        "all objects are oversize",
        "a few objects are oversize",
    ],
)
def test_fit_objects_bigger_than_basket_raises(objects, expected_oversize_objs):
    baskets = iter(fit_objects_into_baskets(objects, 4))
    try:
        next(baskets)
    except ValueError as err:
        assert err.args[0] == expected_oversize_objs
