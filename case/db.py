import typing
import functools

from . import models
from . import utils
from . import errors
from . import parsers
from . import translators
from . import renderers

class Cases(dict):
    def __iter__(self):
        return iter(self.values())

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
                snake = utils.compose \
                (
                    parsers.unflatten,
                    translators.lower,
                    renderers.underscore,
                )

                case_name = snake(cls_or_fn.__name__)

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

    def __setitem__(self, style: str, case: models.Case):
        assert style == case.style, 'Case styles do not match'

        # Note: Instead use - if isinstance(style, str) and style and ...
        if style is None:
            raise errors.RegistrationError('Anyonymous cases cannot be registered')

        # Note: Should anonymous cases be allowed if provided a `style` name?
        super().__setitem__(style, case)

    def add(self, case: models.Case):
        self[case.style] = case

    def determine(self, string: str) -> typing.List[models.Case]:
        return \
        [
            case
            for case in self
            if case.match(string)
        ]
