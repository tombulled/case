import typing
from . import abc, renderers, translators


class Lower(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.lower(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.space(strings)


class Upper(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.upper(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.space(strings)


class Title(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.title(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.space(strings)


class Sentence(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.capitalize(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.space(strings)


class Snake(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.lower(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.underscore(strings)


class Helter(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.title(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.underscore(strings)


class Macro(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.upper(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.underscore(strings)


class Kebab(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.lower(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.hyphen(strings)


class Train(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.title(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.hyphen(strings)


class Cobol(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.upper(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.hyphen(strings)


class Flat(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.lower(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.concatenate(strings)


class Flush(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.upper(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.concatenate(strings)


class Pascal(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.title(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.concatenate(strings)


class Camel(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.dromedary(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.concatenate(strings)


class Dot(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.lower(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.period(strings)


class Path(abc.Case):
    @staticmethod
    def translate(strings: typing.List[str], /) -> typing.List[str]:
        return translators.lower(strings)

    @staticmethod
    def render(strings: typing.List[str], /) -> str:
        return renderers.slash(strings)
