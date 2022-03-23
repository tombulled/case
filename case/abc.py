import abc
from typing import Iterable


class RendererABC(abc.ABC):
    def __call__(self, strings: Iterable[str], /) -> str:
        return "".join(self.render(strings))

    @abc.abstractmethod
    def render(self, strings: Iterable[str], /) -> Iterable[str]:
        ...

    @abc.abstractmethod
    def unrender(self, string: str, /) -> Iterable[str]:
        ...

    def match(self, string: str, /) -> bool:
        return self.render(self.unrender(string)) == string
