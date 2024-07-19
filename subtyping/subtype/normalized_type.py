from typing import Final, get_origin, get_args, Any, TypeVar, Iterable
from .types import TypeT
from .builtin_subclasses import CollectionABCCompare

T_co = TypeVar("T_co", covariant=True, bound="NormalizedType")


class NTuple(tuple[T_co]):
    def __new__(self, iterable: Iterable[T_co] = ()) -> Any:
        return super().__new__(NTuple, iterable)

    def isany(self) -> bool:
        return len(self) == 1 and self[0].origin is Any


class NormalizedType:
    def __init__(self, _type: TypeT) -> None:
        origin, args = self._parse_type(_type)
        self.origin: Final = origin
        self.args: Final = args

    @staticmethod
    def _parse_type(_type: TypeT) -> tuple[TypeT, NTuple["NormalizedType"]]:
        origin = get_origin(_type) or _type
        args: NTuple[NormalizedType]

        if origin is Any:
            args = NTuple()
        else:
            args = NTuple(NormalizedType(arg) for arg in (get_args(_type) or (Any,)))

        return origin, args

    def __eq__(self, supertype: object) -> bool:
        if not isinstance(supertype, NormalizedType):
            return False

        return self.origin == supertype.origin and self.args == supertype.args

    def __le__(self, supertype: "NormalizedType") -> bool:
        if self == supertype:
            return True

        if self.origin is Any or supertype.origin is Any:
            return True

        assert isinstance(self.origin, type)
        assert isinstance(supertype.origin, type)

        if issubclass(self.origin, supertype.origin) and any(
            [self.args.isany(), supertype.args.isany()]
        ):
            return True

        if CollectionABCCompare(self, supertype):
            return True

        return False
