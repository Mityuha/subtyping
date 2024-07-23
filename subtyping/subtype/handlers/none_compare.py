from ..types import INormalizedType, IsSubtype
from typing import Any


def none_comparison(
    subtype: INormalizedType, supertype: INormalizedType, **_kwargs: Any
) -> IsSubtype:
    return False if ((subtype.origin is None) != (supertype.origin is None)) else None
