import typing

__all__ = ['Renderer', 'Translator']

Renderer   = typing.Callable[[typing.Iterable[str]], str]
Translator = typing.Callable[[typing.Iterable[str]], typing.Iterable[str]]
