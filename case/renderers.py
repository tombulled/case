import dataclasses
import typing

from . import protocols

@dataclasses.dataclass
class JoinRenderer(protocols.Renderer):
    sep: str

    def __call__(self, strings: typing.Iterable[str], /) -> str:
        return self.sep.join(strings)

space: protocols.Renderer = JoinRenderer(" ")
concatenate: protocols.Renderer = JoinRenderer("")
underscore: protocols.Renderer = JoinRenderer("_")
hyphen: protocols.Renderer = JoinRenderer("-")
period: protocols.Renderer = JoinRenderer(".")
slash: protocols.Renderer = JoinRenderer("/")