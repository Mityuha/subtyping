from __future__ import annotations

from typing import Any
from .types import TypeT
from .normalized_type import NormalizedType


def issubtype(
    subtype: TypeT, supertype: TypeT, *, forward_refs: dict[str, Any] | None = None
) -> bool:
    return NormalizedType(supertype) >= NormalizedType(subtype)
