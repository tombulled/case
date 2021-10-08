import abc
import typing

from . import parsers

class Case(abc.ABC):
    def __repr__(self) -> str:
        return f'Case<{self.__class__.__name__}>'

    def __call__(self, string: str) -> str:
        return self.render(self.prepare(self.parse(string)))

    # @classmethod
    # def convert(self, string: str) -> str:
    #     return self.render(self.prepare(self.parse(string)))

    @staticmethod
    @abc.abstractmethod
    def render(segments: typing.Iterable[str]) -> str:
        raise NotImplementedError

    @staticmethod
    def parse(string: str) -> typing.Iterable[str]:
        return parsers.parse(string)

    def match(self, string: str) -> bool:
        return self(string) == string

    @staticmethod
    def prepare(segments: typing.Iterable[str]) -> typing.Iterable[str]:
        return segments
