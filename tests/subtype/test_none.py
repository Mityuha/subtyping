from subtyping import issubtype
from typing import Any


def test_none() -> None:
    assert issubtype(None, Any)
    assert issubtype(Any, None)
    assert issubtype(None, None)
    assert issubtype(list[None], list[None])
    assert not issubtype(list[str], None)
    assert not issubtype(None, list[str])
