from parse import parse

from .models import Case
from .repositories import Cases
from .styles import *

identify = cases.identify
case = cases.__call__

locals().update({case.style: case for case in cases})
