from .parsers import parse
from .cases   import *
from .enums   import Case

lower    = lambda string: Lower.render(parse(string))
upper    = lambda string: Upper.render(parse(string))
title    = lambda string: Title.render(parse(string))
sentence = lambda string: Sentence.render(parse(string))
snake    = lambda string: Snake.render(parse(string))
