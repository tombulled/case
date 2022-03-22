from .models import Case, Renderer
from .protocols import Parser, Translator
from .abc import RendererABC

# from . import styles
from . import renderers, translators

import typing

# cases = registrate.Record()

snake = Case(
    name="snake",
    renderer=renderers.underscore,
    translators=[translators.lower],
)


# lower: Case = cases(styles.Lower())
# upper: Case = cases(styles.Upper())
# title: Case = cases(styles.Title())
# sentence: Case = cases(styles.Sentence())
# snake: Case = cases(styles.Snake())
# helter: Case = cases(styles.Helter())
# macro: Case = cases(styles.Macro())
# kebab: Case = cases(styles.Kebab())
# train: Case = cases(styles.Train())
# cobol: Case = cases(styles.Cobol())
# flat: Case = cases(styles.Flat())
# flush: Case = cases(styles.Flush())
# pascal: Case = cases(styles.Pascal())
# camel: Case = cases(styles.Camel())
# dot: Case = cases(styles.Dot())
# path: Case = cases(styles.Path())


# def identify(
#     string: str, case_styles: typing.Optional[typing.List[Case]] = None
# ) -> typing.List[Case]:
#     if case_styles is None:
#         case_styles = cases

#     return [case for case in case_styles if case.match(string)]
