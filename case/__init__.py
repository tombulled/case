import typing

import roster

from . import renderers, translators
from .abc import RendererABC
from .models import Case, Renderer
from .protocols import Parser, Translator

cases: roster.Record[Case] = roster.Record()

lower: Case = cases(
    Case(
        name="lower",
        renderer=renderers.space,
        translator=translators.lower,
    )
)

upper: Case = cases(
    Case(
        name="upper",
        renderer=renderers.space,
        translator=translators.upper,
    )
)

title: Case = cases(
    Case(
        name="title",
        renderer=renderers.space,
        translator=translators.title,
    )
)

sentence: Case = cases(
    Case(
        name="sentence",
        renderer=renderers.space,
        translator=translators.capitalize,
    )
)

snake: Case = cases(
    Case(
        name="snake",
        renderer=renderers.underscore,
        translator=translators.lower,
    )
)

helter: Case = cases(
    Case(
        name="helter",
        renderer=renderers.underscore,
        translator=translators.title,
    )
)

macro: Case = cases(
    Case(
        name="macro",
        renderer=renderers.underscore,
        translator=translators.upper,
    )
)

kebab: Case = cases(
    Case(
        name="kebab",
        renderer=renderers.hyphen,
        translator=translators.lower,
    )
)

train: Case = cases(
    Case(
        name="train",
        renderer=renderers.hyphen,
        translator=translators.title,
    )
)

cobol: Case = cases(
    Case(
        name="cobol",
        renderer=renderers.hyphen,
        translator=translators.upper,
    )
)

flat: Case = cases(
    Case(
        name="flat",
        renderer=renderers.concatenate,
        translator=translators.lower,
    )
)

flush: Case = cases(
    Case(
        name="flush",
        renderer=renderers.concatenate,
        translator=translators.upper,
    )
)

pascal: Case = cases(
    Case(
        name="pascal",
        renderer=renderers.concatenate,
        translator=translators.title,
    )
)

camel: Case = cases(
    Case(
        name="camel",
        renderer=renderers.concatenate,
        translator=translators.dromedary,
    )
)

dot: Case = cases(
    Case(
        name="dot",
        renderer=renderers.period,
        translator=translators.lower,
    )
)

path: Case = cases(
    Case(
        name="path",
        renderer=renderers.slash,
        translator=translators.lower,
    )
)


def identify(
    string: str, case_styles: typing.Optional[typing.List[Case]] = None
) -> typing.List[Case]:
    if case_styles is None:
        case_styles = cases

    return [case for case in case_styles if case.match(string)]

def register(case: Case) -> None:
    cases.append(case)