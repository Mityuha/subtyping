from .immutable_collection_compare import immutable_collection_comparison
from .simple_compare import simple_comparison
from .any_compare import any_comparison
from .none_compare import none_comparison
from .subclass_with_any_compare import subclass_with_any_comparison
from .check_is_type import check_is_type

from typing import Any, Protocol, Final
from collections.abc import Iterable
from ..types import IsSubtype, INormalizedType


class IHandler(Protocol):
    __qualname__: str

    def __call__(
        self,
        subtype: INormalizedType,
        supertype: INormalizedType,
        **kwargs: Any,
    ) -> IsSubtype: ...


handlers: Final[Iterable[IHandler]] = (
    simple_comparison,
    any_comparison,
    none_comparison,
    check_is_type,
    subclass_with_any_comparison,
    immutable_collection_comparison,
)
