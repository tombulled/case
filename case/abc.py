from abc import ABC, abstractmethod
from typing import Iterable

class Renderer(ABC):
    @abstractmethod
    def render(self, strings: Iterable[str], /) -> str:
        ...

    @abstractmethod
    def unrender(self, string: str, /) -> Iterable[str]:
        ...

    def match(self, string: str, /) -> bool:
        return self.render(self.unrender(string)) == string