from subtyping import issubtype
from typing import Any, TypeVar, Generic

T = TypeVar("T")


class Foo(Generic[T]):
    def __init__(self, val: T) -> None: ...


def test_any() -> None:
    assert issubtype(Foo, Foo[int])
    assert issubtype(Foo[int], Foo)
    assert issubtype(Foo[Any], Foo)
    assert issubtype(set, set[Any])
