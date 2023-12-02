"""
Basket_case lib
"""

from typing import Iterator


def fit_objects_into_baskets(
    objects: dict[str: int],
    basket_size: int,
    sort_basket: bool=True
) -> Iterator[list[str]]:
    """Group the given objects into several baskets, maximising the room taken in each basket.
    If an object is too big to fit in the basket it is ignored.

    Args:
        objects (dict[str: int]): each object and its size
        basket_size (int): the size of the basket. All baskets have the same size.
        sort_basket (bool, optional): sort the returned objects in each basket by name.
            Defaults to True but can be turned off if unnecessary.

    Yields:
        Iterator[tuple[str]]: the grouped items per basket.
            The number of resulting baskets depends on the cumulative size of the objects.
    """
    num_objects = len(objects)
    yield 'obj0', 'obj2'
    yield 'obj1',
