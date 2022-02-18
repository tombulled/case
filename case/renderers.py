import typing


def space(strings: typing.List[str], /) -> str:
    return " ".join(strings)


def concatenate(strings: typing.List[str], /) -> str:
    return "".join(strings)


def underscore(strings: typing.List[str], /) -> str:
    return "_".join(strings)


def hyphen(strings: typing.List[str], /) -> str:
    return "-".join(strings)


def period(strings: typing.List[str], /) -> str:
    return ".".join(strings)


def slash(strings: typing.List[str], /) -> str:
    return "/".join(strings)
