from .delpy import *
"""
* Copyright (C) 200?-200? DelpyWidget
* based on code by gwangyi CopyrightHolder copyright (C) 200?-200? Delpy
* License: gnu.org/licenses/gpl.html GPL version 2 or higher
"""

def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        src="static",
        dest="delpy",
        require="delpy/index")]
