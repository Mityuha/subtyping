import collections.abc
from typing import Final, Any
from ..types import INormalizedType, IsSubtype
from subtyping.logger import logger


COLLECTIONS_ABC_TYPES: Final = set(collections.abc.__all__)


def immutable_collection_comparison(
    subtype: INormalizedType,
    supertype: INormalizedType,
    **_kwargs: Any,
) -> IsSubtype:
    if not getattr(subtype.origin, "__qualname__") or not getattr(
        supertype.origin, "__qualname__"
    ):
        return None

    if not (
        (subtype.origin.__qualname__ in COLLECTIONS_ABC_TYPES)  # type: ignore[attr-defined]
        and (supertype.origin.__qualname__ in COLLECTIONS_ABC_TYPES)  # type: ignore[attr-defined]
    ):
        logger.trace(
            f"[immutable_collections]: Either {subtype.origin} or {supertype.origin} not collection.abc type"
        )
        return None

    if not issubclass(subtype.origin, supertype.origin):  # type: ignore[arg-type]
        return None

    if subtype.args.isany() or supertype.args.isany():
        return True

    if len(subtype.args) >= len(supertype.args):
        return all(
            subarg <= superarg for subarg, superarg in zip(subtype.args, supertype.args)
        )

    return None
