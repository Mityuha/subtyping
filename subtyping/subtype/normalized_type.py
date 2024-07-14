from typing import Final, get_origin, get_args, Any
from .types import TypeT


# TODO: think about this class
class NormalizedArgs:
    def __init__(self, args: tuple["NormalizedType", ...]) -> None:
        self.args: Final = args

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NormalizedArgs):
            return False
        return self.args == other.args

    def isany(self) -> bool:
        return len(self.args) == 1 and self.args[0].origin is Any


class NormalizedType:
    def __init__(self, _type: TypeT) -> None:
        origin, args = self._parse_type(_type)
        self.origin: Final = origin
        self.args: Final = args

    @staticmethod
    def _parse_type(_type: TypeT) -> tuple[TypeT, tuple["NormalizedType", ...]]:
        origin = get_origin(_type) or _type
        args: tuple[NormalizedType, ...]

        if origin is Any:
            args = ()
        else:
            args = tuple(NormalizedType(arg) for arg in (get_args(_type) or (Any,)))

        return origin, args

    def __eq__(self, right: object) -> bool:
        if not isinstance(right, NormalizedType):
            return False

        return self.origin == right.origin and self.args == right.args

    def isargsany(self) -> bool:
        return len(self.args) == 1 and self.args[0].origin is Any

    def __ge__(self, right: "NormalizedType") -> bool:
        """Check if S (right) is a subtype of T (left).
        Made for simplicity.
        class Animal: ...
        class Cat(Animal): ...

        #     left   right
               v       v
        res: Animal = Cat()
        """
        if self == right:
            return True

        if self.origin is Any or right.origin is Any:
            return True

        # tests required
        # if issubclass(right.origin, self.origin):
        #     return any(
        #         [
        #             self.isargsany(),
        #             right.isargsany(),
        #             (
        #                 len(self.args) == len(right.args)
        #                 and all(
        #                     larg == rarg for larg, rarg in zip(self.args, right.args)
        #                 )
        #             ),
        #         ]
        #     )
        return False
