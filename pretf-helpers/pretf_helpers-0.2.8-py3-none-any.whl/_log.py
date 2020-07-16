# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
from typing import Any

import colorama
import pretf.log

accept = pretf.log.accept
bad = pretf.log.bad
ok = pretf.log.ok


class warn(Exception):
    @pretf.log.colorama_init
    def __init__(self, message: Any):
        """
        Displays a message prefixed with [pref] in yellow.
        Can be raised as an exception to display the message and then exit.
        """
        print(
            f"{colorama.Fore.YELLOW}[pretf] {message}{colorama.Style.RESET_ALL}",
            file=sys.stderr,
        )
