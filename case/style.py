import dataclasses
import types
import typing
import warnings

from . import models
from . import parsers
from . import renderers
from . import translators
from . import utils

styles = types.SimpleNamespace()

def register(case):
    if case.style is not None:
        setattr(styles, case.style, case)
    else:
        raise Exception('Case has no style, cannot be registered.')

def _style(name):
    def wrapper(entity):
        if isinstance(entity, type):
            dc = dataclasses.dataclass(frozen = True, repr = False)

            @dc
            class Wrapper(dc(entity)):
                style: typing.Optional[str] = name

            styled_entity = Wrapper
            case = Wrapper()
        elif callable(entity):
            if utils.is_lambda(entity):
                raise Exception('entity is lambda (anonymous function), so has no name')

            styled_entity = entity

            case = models.Case(entity, style = name)
        else:
            raise Exception('entity is not a class or named callable')

        try:
            register(case)
        except:
            raise warnings.warn('registration of case failed')

        return styled_entity

    return wrapper

def style(entity):
    if isinstance(entity, str):
        name = entity

        return _style(name)
    else:
        snake = utils.compose \
        (
            parsers.unflatten,
            translators.lower,
            renderers.underscore,
        )

        return _style(snake(entity.__name__))(entity)
