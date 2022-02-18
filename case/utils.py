import io
import typing


def chunk(string: str, sizes: typing.Iterable[int]) -> typing.List[str]:
    buffer: io.StringIO = io.StringIO(string)

    return [buffer.read(size) for size in sizes]
