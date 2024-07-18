from typing import Any
from collections.abc import (
    Iterable,
    Iterator,
    Reversible,
    Generator,
    Sequence,
    Set,
    Mapping,
    Collection,
    Sized,
)
import pytest
from subtyping import issubtype


class Animal: ...


class Cat(Animal): ...


@pytest.mark.parametrize(
    "t1, t2",
    [
        (Reversible, Iterable),
        (Iterator[int], Iterable[Any]),
        (Generator[Cat, None, None], Iterator[Animal]),
        (Sequence[Any], Reversible[Cat]),
        (Set[Cat], Iterable[Animal]),
        (Mapping[Cat, int], Collection[Animal]),
        (Collection[Animal], Sized),
    ],
)
def test_subclass_immutable(t1: type, t2: type) -> None:
    assert issubtype(t1, t2)
