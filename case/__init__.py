from .repository import Cases
from .models     import Case
from .parsers    import parse, unflatten
from .styles     import *

identify = cases.identify
case     = cases.__call__

locals().update({case.style: case for case in cases})
