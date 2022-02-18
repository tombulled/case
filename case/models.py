import dataclasses
import typing

@dataclasses.dataclass
class Character:
    value: str
    index: int = 0
    offset: int = 0

@dataclasses.dataclass
class Word:
    value: str
    index: int = 0
    offset: int = 0
    
    def __iter__(self) -> typing.Iterable[Character]:
        index: int
        character: str
        for index, character in enumerate(self.value):
            yield Character(
                value=character,
                index=index,
                offset=self.offset+index,
            )