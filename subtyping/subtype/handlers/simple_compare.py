from ..types import INormalizedType, IsSubtype
from typing import Any


def simple_comparison(
    subtype: INormalizedType,
    supertype: INormalizedType,
    **_kwargs: Any,
) -> IsSubtype:
    return True if subtype == supertype else None
