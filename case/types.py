import typing

T = typing.TypeVar('T')

Words = typing.List[str]

WordTranslator = typing.Callable[[str], str]

Parser     = typing.Callable[[str], typing.Iterable[str]]
Renderer   = typing.Callable[[typing.Iterable[str]], str]
Translator = typing.Callable[[typing.Iterable[str]], typing.Iterable[str]]
