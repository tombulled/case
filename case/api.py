import typing
from . import models

def tokenize(strings: typing.Iterable[str], /) -> typing.Iterable[models.Word]:
    offset: int = 0

    string_index: int
    string: str
    for string_index, string in enumerate(strings):
        yield models.Word(
            value=string,
            index=string_index,
            offset=offset,
        )

        offset += len(string)