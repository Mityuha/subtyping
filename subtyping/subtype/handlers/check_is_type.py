from ..types import INormalizedType, IsSubtype
from typing import Any
from subtyping.logger import logger


def check_is_type(
    subtype: INormalizedType, supertype: INormalizedType, **_kwargs: Any
) -> IsSubtype:
    if not all([isinstance(subtype.origin, type), isinstance(supertype.origin, type)]):
        logger.error(
            f"Either '{subtype.origin}' is not type or '{supertype.origin}' is not type"
        )
        return False

    return None
