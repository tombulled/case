import typing


class Parser(typing.Protocol):
    def __call__(self, string: str, /) -> typing.Iterable[str]:
        ...

class Renderer(typing.Protocol):
    def __call__(self, strings: typing.Iterable[str], /) -> str:
        ...

class Translator(typing.Protocol):
    def __call__(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        ...
