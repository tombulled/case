from . import cases
from .cases import *

from .parsers import parse
from .models  import Case
from .style  import styles, style, register

lower    = cases.Lower()
upper    = cases.Upper()
title    = cases.Title()
sentence = cases.Sentence()
snake    = cases.Snake()
helter   = cases.Helter()
macro    = cases.Macro()
kebab    = cases.Kebab()
train    = cases.Train()
cobol    = cases.Cobol()
flat     = cases.Flat()
flush    = cases.Flush()
pascal   = cases.Pascal()
camel    = cases.Camel()
dot      = cases.Dot()
path     = cases.Path()
