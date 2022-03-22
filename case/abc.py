import abc
from typing import Iterable


class RendererABC(abc.ABC):
    @abc.abstractmethod
    def render(self, strings: Iterable[str], /) -> str:
        ...

    @abc.abstractmethod
    def unrender(self, string: str, /) -> Iterable[str]:
        ...

    def match(self, string: str, /) -> bool:
        return self.render(self.unrender(string)) == string
