import typing
import functools

from . import models
from . import utils

# TODO: Make base repository <Repository>

class Cases:
    _store: set

    def __init__(self):
        self._store = set()

    def __iter__(self):
        return iter(self._store)

    def __repr__(self) -> str:
        return '{class_name}[{cases}]'.format \
        (
            class_name = type(self).__name__,
            cases = ', '.join(map(repr, self))
        )

    def __call__ \
            (
                self,
                cls_or_fn: typing.Optional[typing.Union[typing.Type, typing.Callable]] = None,
                /,
                *,
                name: typing.Optional[str] = None,
            ):
        def wrap(cls_or_fn: typing.Union[typing.Type[models.Case], typing.Callable]):
            # NOTE: Be more lenient?
            if not (is_type := isinstance(cls_or_fn, type)) and not (is_callable := callable(cls_or_fn)):
                raise TypeError(f'Must be called with a Case type, or callable, not {type(cls_or_fn)!r}')

            if utils.is_lambda(cls_or_fn):
                raise TypeError('Provided callable is an anonymous lambda function, hence it has no usable name')

            case_name = name

            if case_name is None:
                case_name = cls_or_fn.__name__.lower()

            if is_type:
                @functools.wraps(cls_or_fn, updated = ())
                @models.model
                class Wrapper(models.model(cls_or_fn)):
                    style: typing.Optional[str] = case_name

                styled = Wrapper
                case = Wrapper()
            elif is_callable:
                styled = cls_or_fn

                case = models.Case(cls_or_fn, style = case_name)

            self.add(case)

            return styled

        if cls_or_fn is None:
            return wrap

        return wrap(cls_or_fn)

    def get(self, style: str, default: typing.Any = None) -> typing.Any:
        return self._store.get(style, default = default)

    def add(self, case: models.Case):
        return self._store.add(case)

    def clear(self) -> None:
        return self._store.clear()

    def copy(self):
        inst = self.__class__()
        inst.update(self._store)
        return inst

    def pop(self) -> models.Case:
        return self._store.pop()

    def remove(self, case: models.Case) -> None:
        return self._store.remove(case)

    def update(self, cases) -> None:
        self._store.update(cases)

    def identify(self, string: str) -> typing.List[models.Case]:
        return \
        [
            case
            for case in self
            if case.match(string)
        ]
