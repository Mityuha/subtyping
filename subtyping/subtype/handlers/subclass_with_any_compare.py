from ..types import INormalizedType, IsSubtype
from typing import Any


def subclass_with_any_comparison(
    subtype: INormalizedType, supertype: INormalizedType, **_kwargs: Any
) -> IsSubtype:
    return (
        True
        if (
            issubclass(subtype.origin, supertype.origin)  # type: ignore[arg-type]
            and any([subtype.args.isany(), supertype.args.isany()])
        )
        else None
    )
