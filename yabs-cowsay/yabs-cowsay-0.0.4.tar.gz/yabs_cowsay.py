# -*- coding: utf-8 -*-
# (c) 2020 Martin Wendt and contributors; see https://github.com/mar10/yabs
# Licensed under the MIT license: https://www.opensource.org/licenses/mit-license.php
"""
"""
import logging
from textwrap import wrap

__version__ = "0.0.4"

logger = logging.getLogger("yabs")


def register(task_base, **kwargs):

    logger.info("RUNNING yabs_cowsay.register()")

    class CowsayTask(task_base):
        DEFAULT_OPTS = {
            "message": "moo",
            "width": 40,
        }

        def __init__(self, opts):
            super().__init__(opts)

        @classmethod
        def register_cli_command(cls, subparsers, parents, run_parser):
            """"""
            # Additional arguments for the 'run' command
            run_parser.add_argument(
                "--no-cowsay",
                action="store_true",
                help="skip cowsay tasks",
            )

        @classmethod
        def check_task_def(cls, task_def, parser, args, yaml):
            return True

        def run(self, context):
            opts = self.opts
            if context.args.no_cowsay:
                logger.debug("`--no-cowsay` was passed: skipping task.")
                return True

            width = int(opts["width"])
            # Replace `{name}` macros in the message if any:
            message = opts["message"].format(**vars(context))

            res = cowsay(message, width)
            logger.info(res)
            return True

    # Return the implementstin class
    return CowsayTask

# ------------------------------------------------------------------------------
# cowsay implementation
# ------------------------------------------------------------------------------

COW = """\
    \   ^__^
     \  (oo)\_______
        (__)\       )\/\\
            ||----w |
            ||     ||
"""

def cowsay(msg, width=40):
    # Wrap text to max. width, but keep existing linebreaks:
    msg_lines = []
    for msg in msg.split("\n"):
        msg_lines.extend(wrap(msg, width))
    # Shrink to the minimal required width
    width = max(len(s) for s in msg_lines)
    # Print bubble:
    lines = []
    lines.append(" " + "_" * (width + 2))
    if len(msg_lines) == 1:
        lines.append("< {} >".format(msg_lines[0]))
    else:
        lines.append("/ {:<{w}} \\".format(msg_lines[0], w=width))
        for line in msg_lines[1:-1]:
            lines.append("| {:<{w}} |".format(line, w=width))
        lines.append("\\ {:<{w}} /".format(msg_lines[-1], w=width))
    lines.append(" " + "-" * (width + 2))
    # Print cow
    lines.extend(COW.split("\n"))
    return "\n".join(lines)


if __name__ == "__main__":
    print(cowsay("Hello cow!", 40))
    print(cowsay("Hello cow! " * 20, 50))
    print(cowsay("Dear fellow cattle,\nthis message was brought to you by the 'yabs-cowsay' extension."))
