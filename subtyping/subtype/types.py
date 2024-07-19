from __future__ import annotations

from typing import Protocol, Collection, TypeVar, Any


TypeT = None | type | TypeVar | object


T_co = TypeVar("T_co", covariant=True, bound="INormalizedType")


class ICollection(Protocol[T_co], Collection[T_co]):
    def isany(self) -> bool: ...


class INormalizedType(Protocol):
    @property
    def origin(self) -> TypeT: ...

    @property
    def args(self) -> ICollection["INormalizedType"]: ...

    def __le__(self, supertype: Any) -> bool: ...

    def __eq__(self, supertype: object) -> bool: ...
