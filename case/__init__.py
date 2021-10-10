'''
TODO:
    * Make sibling library `export` to auto add classes/function names to `__all__`
'''

from .db import Cases

cases = Cases()

from .parsers import parse
from .models  import Case

from .styles import *

determine = cases.determine
case = cases.__call__

lower    = cases['lower']
upper    = cases['upper']
title    = cases['title']
sentence = cases['sentence']
snake    = cases['snake']
helter   = cases['helter']
macro    = cases['macro']
kebab    = cases['kebab']
train    = cases['train']
cobol    = cases['cobol']
flat     = cases['flat']
flush    = cases['flush']
pascal   = cases['pascal']
camel    = cases['camel']
dot      = cases['dot']
path     = cases['path']
