from ..types import INormalizedType, IsSubtype
from typing import Any


def any_comparison(
    subtype: INormalizedType, supertype: INormalizedType, **_kwargs: Any
) -> IsSubtype:
    return True if (subtype.origin is Any or supertype.origin is Any) else None
