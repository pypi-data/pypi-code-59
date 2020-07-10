# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

import optparse
import sys
import time


# pylint: disable=abstract-method; by design?
class _ManHelpFormatter(optparse.HelpFormatter):
    def __init__(
        self, indent_increment=0, max_help_position=24, width=79, short_first=0
    ):
        optparse.HelpFormatter.__init__(
            self, indent_increment, max_help_position, width, short_first
        )

    def format_heading(self, heading):
        return ".SH %s\n" % heading.upper()

    def format_description(self, description):
        return description

    def format_option(self, option):
        try:
            optstring = option.option_strings
        except AttributeError:
            optstring = self.format_option_strings(option)
        if option.help:
            help_text = self.expand_default(option)
            help_string = " ".join([l.strip() for l in help_text.splitlines()])
            help_string = help_string.replace("\\", "\\\\")
            help_string = help_string.replace("[current:", "[default:")
        else:
            help_string = ""
        return """.IP "%s"
%s
""" % (
            optstring,
            help_string,
        )

    def format_head(self, optparser, pkginfo, section=1):
        long_desc = ""
        try:
            pgm = optparser._get_prog_name()
        except AttributeError:
            # py >= 2.4.X (dunno which X exactly, at least 2)
            pgm = optparser.get_prog_name()
        short_desc = self.format_short_description(pgm, pkginfo.description)
        if hasattr(pkginfo, "long_desc"):
            long_desc = self.format_long_description(pgm, pkginfo.long_desc)
        return "%s\n%s\n%s\n%s" % (
            self.format_title(pgm, section),
            short_desc,
            self.format_synopsis(pgm),
            long_desc,
        )

    @staticmethod
    def format_title(pgm, section):
        date = "%d-%02d-%02d" % time.localtime()[:3]
        return '.TH %s %s "%s" %s' % (pgm, section, date, pgm)

    @staticmethod
    def format_short_description(pgm, short_desc):
        return """.SH NAME
.B %s
\\- %s
""" % (
            pgm,
            short_desc.strip(),
        )

    @staticmethod
    def format_synopsis(pgm):
        return (
            """.SH SYNOPSIS
.B  %s
[
.I OPTIONS
] [
.I <arguments>
]
"""
            % pgm
        )

    @staticmethod
    def format_long_description(pgm, long_desc):
        long_desc = "\n".join(line.lstrip() for line in long_desc.splitlines())
        long_desc = long_desc.replace("\n.\n", "\n\n")
        if long_desc.lower().startswith(pgm):
            long_desc = long_desc[len(pgm) :]
        return """.SH DESCRIPTION
.B %s
%s
""" % (
            pgm,
            long_desc.strip(),
        )

    @staticmethod
    def format_tail(pkginfo):
        tail = """.SH SEE ALSO
/usr/share/doc/pythonX.Y-%s/

.SH BUGS
Please report bugs on the project\'s mailing list:
%s

.SH AUTHOR
%s <%s>
""" % (
            getattr(pkginfo, "debian_name", "pylint"),
            pkginfo.mailinglist,
            pkginfo.author,
            pkginfo.author_email,
        )

        if hasattr(pkginfo, "copyright"):
            tail += (
                """
.SH COPYRIGHT
%s
"""
                % pkginfo.copyright
            )

        return tail


def _generate_manpage(optparser, pkginfo, section=1, stream=sys.stdout, level=0):
    formatter = _ManHelpFormatter()
    formatter.output_level = level
    formatter.parser = optparser
    print(formatter.format_head(optparser, pkginfo, section), file=stream)
    print(optparser.format_option_help(formatter), file=stream)
    print(formatter.format_tail(pkginfo), file=stream)
