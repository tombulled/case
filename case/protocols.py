import typing


class Parser(typing.Protocol):
    def __call__(self, string: str, /) -> typing.List[str]:
        ...


class Renderer(typing.Protocol):
    def __call__(self, strings: typing.List[str], /) -> str:
        ...


class Translator(typing.Protocol):
    def __call__(self, strings: typing.List[str], /) -> typing.List[str]:
        ...
