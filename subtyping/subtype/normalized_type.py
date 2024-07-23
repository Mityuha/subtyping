from typing import Final, get_origin, get_args, Any, TypeVar, Iterable
from .types import TypeT, IsSubtype
from .handlers import handlers
from subtyping.logger import logger

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
        for handler in handlers:
            res: IsSubtype = handler(self, supertype)
            if res is None:
                continue
            logger.debug(f"[{handler.__qualname__}]: triggered with '{res}' result")
            return res

        return False
