import collections.abc
from typing import Final
from .types import INormalizedType
from subtyping.logger import logger


COLLECTIONS_ABC_TYPES: Final = set(collections.abc.__all__)


def CollectionABCCompare(subtype: INormalizedType, supertype: INormalizedType) -> bool:
    if not (
        (subtype.origin.__qualname__ in COLLECTIONS_ABC_TYPES)
        and (supertype.origin.__qualname__ in COLLECTIONS_ABC_TYPES)
    ):
        logger.trace(
            f"[ABCCmp]: Either {subtype.origin} or {supertype.origin} not collection.abc type"
        )
        return False

    if not issubclass(subtype.origin, supertype.origin):
        return False

    if subtype.args.isany() or supertype.args.isany():
        return True

    if len(subtype.args) >= len(supertype.args):
        return all(
            subarg <= superarg for subarg, superarg in zip(subtype.args, supertype.args)
        )

    return False
