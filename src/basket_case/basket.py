"""
Basket_case lib
"""

from collections import deque
import itertools as it
from typing import Iterator


def fit_objects_into_baskets(
    objects: dict[str: int],
    basket_size: int,
    ignore_oversize: bool=False,
) -> Iterator[dict[str, int]]:
    """Group the given objects into several baskets, maximising the room taken in each basket.

    Args:
        objects (dict[str: int]): each object expressed as name: size.
            Note: the size of an object can be zero (useful for files of zero length)
        basket_size (int): the size of the basket. All baskets have the same size.
        ignore_oversize (bool, optional): ignore the oversize objects instead of raising ValueError

    Yields:
        Iterator[dict[str, int]]: each dict yielded represents a basket with its objects
            The number of resulting baskets depends on the cumulative size of the objects.

    Raises: 
        ValueError if any object is too big to fit in the basket. All such objects are made
             available in the exception's args attibute, as a dict.
             Can be suppressed with ignore_oversize=True
    """
    if not objects:
        return

    oversize_objects = {name: size for name, size in objects.items() if size>basket_size}
    if oversize_objects:
        if ignore_oversize:
            # build objects without the oversize ones, without altering the input dict
            objects = {name: size for name, size in objects.items() if size<=basket_size}
        else:
            raise ValueError(oversize_objects)

    consume = deque(maxlen=0).extend
    while objects:
        max_comb_size = 0
        for k in range(1, len(objects)+1):
            for comb in it.combinations(objects, k):
                comb_size = sum(objects[name] for name in comb)
                if max_comb_size <= comb_size <= basket_size:
                    max_comb_size = comb_size  # update max size found
                    best_comb = comb  # save combination
        yield {name: objects[name] for name in best_comb}  # yield a basket
        consume(objects.pop(name, None) for name in best_comb)  # remove the objs in the comb
