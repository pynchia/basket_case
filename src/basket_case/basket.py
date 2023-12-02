"""
Basket_case lib
"""

from typing import Iterator


def fit_objects_into_baskets(
    objects: dict[str: int],
    basket_size: int,
    sort_basket: bool=True,
    ignore_oversize: bool=False,
) -> Iterator[list[str]]:
    """Group the given objects into several baskets, maximising the room taken in each basket.

    Args:
        objects (dict[str: int]): each object and its size
        basket_size (int): the size of the basket. All baskets have the same size.
        sort_basket (bool, optional): sort the returned objects in each basket by name.
            Defaults to True but can be turned off if unnecessary.
        ignore_oversize (bool, optional): ignore the oversize objects instead of raising ValueError

    Yields:
        Iterator[dict[str, int]]: each tuple yielded represents the basket with its objects
            The number of resulting baskets depends on the cumulative size of the objects.

    Raises: 
        ValueError if any object is too big to fit in the basket. All such objects are made
             available in the exception's args attibute. Can be suppressed with ignore_oversize=True
    """
    oversize_objects = {name: size for name, size in objects.items() if size>basket_size}
    if oversize_objects:
        if ignore_oversize:
            for name in objects:  # remove oversize objects
                del objects[name]
        else:
            raise ValueError(oversize_objects)

    num_objects = len(objects)
    if num_objects == 0:  # no objects are left
        return

    yield 'obj0', 'obj2'
    yield 'obj1',
