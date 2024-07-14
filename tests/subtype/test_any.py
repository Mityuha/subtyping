from subtyping import issubtype
from typing import Any


def test_any() -> None:
    assert issubtype(int, Any)
    assert issubtype(list[str], Any)
    assert issubtype(Any, tuple[str])
    assert issubtype(Any, tuple[tuple[tuple[str]]])
    assert issubtype(Any, Any)
