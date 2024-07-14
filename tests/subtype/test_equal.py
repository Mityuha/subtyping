from subtyping import issubtype
from collections.abc import Sequence, Iterable, Callable


class Foo: ...


def test_equal() -> None:
    assert issubtype(list[Foo], list[Foo])
    assert issubtype(
        Callable[[int, float, str], tuple[Foo]], Callable[[int, float, str], tuple[Foo]]
    )
    assert issubtype(Sequence[Foo], Sequence[Foo])
    assert issubtype(Iterable[float], Iterable[float])
