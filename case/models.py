import dataclasses
import typing

from . import types
from . import parsers
from . import utils

model = dataclasses.dataclass(frozen = True, repr = False)

@model
class Case:
    render:  types.Renderer
    prepare: types.Translator     = utils.identity
    style:   typing.Optional[str] = None # TODO: Add validation. E.g. 'some name' is unacceptable, as can't be a key in the namespace

    def __repr__(self) -> str:
        return '{class_name}(style={style!r})'.format \
        (
            class_name = type(self).mro()[-2].__name__,
            style = self.style,
        )

    def __call__(self, string: str) -> str:
        return self.render(self.prepare(self.parse(string)))

    @staticmethod
    def parse(string: str) -> typing.Iterable[str]:
        return parsers.parse(string)

    def match(self, string: str) -> bool:
        return self(string) == string
