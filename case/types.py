import typing

Renderer   = typing.Callable[[typing.Iterable[str]], str]
Translator = typing.Callable[[typing.Iterable[str]], typing.Iterable[str]]
