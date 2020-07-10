#    Formatter.py
#
#    ------------------------------------------------------------
#    Copyright 2002, 2004 by Samuel Reynolds. All rights reserved.
#
#    Permission to use, copy, modify, and distribute this software and its
#    documentation for any purpose and without fee is hereby granted,
#    provided that the above copyright notice appear in all copies and that
#    both that copyright notice and this permission notice appear in
#    supporting documentation, and that the name of Samuel Reynolds
#    not be used in advertising or publicity pertaining to distribution
#    of the software without specific, written prior permission.
#
#    SAMUEL REYNOLDS DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
#    INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
#    EVENT SHALL SAMUEL REYNOLDS BE LIABLE FOR ANY SPECIAL, INDIRECT, OR
#    CONSEQUENTIAL DAMAGES, OR FOR ANY DAMAGES WHATSOEVER RESULTING FROM
#    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
#    NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
#    WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#    ------------------------------------------------------------
"""
Formatters for converting and validating data values.
"""

import os, sys, errno, copy, re
import six
import wx


class Formatter(object):
    """
    Formatter/validator for data values.
    """
    def __init__(self, *args, **kwargs):
        pass

    # Default (dummy) validate routine
    def validate(self, str_value):
        """
        Return true if value is valid for the field.
        value is a string from the UI.
        """
        return True

    # Default (dummy) format routine
    def format(self, value):
        """Format a value for presentation in the UI."""
        if value is None:
            return ''
        return str(value)

    # Default (dummy) coerce routine
    def coerce(self, str_value):
        """Convert a string from the UI into a storable value."""
        return str_value


class ChoiceFormatter(Formatter):
    """
    Formatter for choice data values.
    """
    def __init__(self, mapping, sort=None, *args, **kwargs):

        super(ChoiceFormatter, self).__init__(*args, **kwargs)
        # if mapping is a list, convert it to a dict
        if isinstance(mapping, list):
            mapping = {v: str(v) for v in mapping}
        self.mapping = mapping
        self.mapping_reverse = {v: k for k, v in six.iteritems(self.mapping)}
        self.sort = sort

    def validValues(self):
        """
        Return list of valid value (id,label) pairs.
        """
        items = list(six.iteritems(self.mapping))
        if self.sort:

            def sort_by_label(item):
                return item[1]

            key = None
            if self.sort == 'label':
                key = sort_by_label
            items.sort(key=key)
        return items

    def validate(self, str_value):
        """
        Return true if value is valid for the field.
        value is a string from the UI.
        """
        vv = [s for i, s in self.validValues()]
        return str_value in vv

    def format(self, value):
        """Format a value for presentation in the UI."""
        return self.mapping[value]

    def coerce(self, str_value):
        """Convert a string from the UI into a storable value."""
        return self.mapping_reverse[str_value]


class EnumFormatter(Formatter):
    """
    Formatter for enumerated (EnumType) data values.
    """
    def __init__(self, enumeration, sort=None, *args, **kwargs):

        super(EnumFormatter, self).__init__(*args, **kwargs)

        self.enumeration = enumeration
        self.sort = sort

    def validValues(self):
        """
        Return list of valid value (id,label) pairs.
        """
        items = copy.copy(self.enumeration.items())
        if self.sort:

            def sort_by_label(item):
                return item[1]

            key = None
            if self.sort == 'label':
                key = sort_by_label
            items.sort(key=key)
        return items

    def validate(self, str_value):
        """
        Return true if value is valid for the field.
        value is a string from the UI.
        """
        vv = [s for i, s in self.validValues()]
        return str_value in vv

    def format(self, value):
        """Format a value for presentation in the UI."""
        return self.enumeration[value]

    def coerce(self, str_value):
        """Convert a string from the UI into a storable value."""
        return getattr(self.enumeration, str_value)


class FormatterMeta(type):
    """
    Metaclass for subclasses of Formatter.

    Each instance class MUST define either validate(self, value) method
    or re_validation regular expression string.

    If the latter, the validate method will be autogenerated.

    If re_validation is defined, validate method is overridden to
    validate the string value against the regular expression.

    If re_validation_flags is defined, the flags will be
    used when the re_validation regular expression string is compiled.

    Each instance class MAY define:
    -    format(self, value) method.
    -    coerce(self, value) method.
    """
    def __new__(cls, classname, bases, classdict):
        newdict = copy.copy(classdict)

        # Generate __init__ method
        # Direct descendants of Formatter automatically get __init__.
        # Indirect descendants don't automatically get one.
        if '__init__' not in newdict:
            if Formatter in bases:

                def __init__(self, *args, **kwargs):
                    Formatter.__init__(self, *args, **kwargs)
                    initialize = getattr(self, 'initialize', None)
                    if initialize:
                        initialize(*args, **kwargs)

                newdict['__init__'] = __init__
            else:

                def __init__(self, *args, **kwargs):
                    super(self.__class__, self).__init__(*args, **kwargs)
                    initialize = getattr(self, 'initialize', None)
                    if initialize:
                        initialize(*args, **kwargs)

                newdict['__init__'] = __init__

        # Generate validate-by-RE method if specified
        re_validation = newdict.get('re_validation', None)
        if re_validation:
            # Override validate method
            re_validation_flags = newdict.get('re_validation_flags', 0)
            newdict['_re_validation'] = re.compile(re_validation,
                                                   re_validation_flags)

            def validate(self, str_value):
                return self._re_validation.match(str_value) != None

            newdict['validate'] = validate

        # Delegate class creation to the expert
        return type.__new__(cls, classname, bases, newdict)


class ObjectIdFormatter(six.with_metaclass(FormatterMeta, Formatter)):
    """
    Object ID is assumed to be a large (32 bit?) unsigned integer.
    """
    re_validation = '^[0-9]+$'

    def coerce(self, str_value):
        if str_value:
            return int(str_value)
        return str_value


class StringFormatter(six.with_metaclass(FormatterMeta, Formatter)):
    pass


class AlphaFormatter(StringFormatter):
    """Alphabetic characters only."""
    re_validation = '^[a-zA-Z]*$'


class AlphaNumericFormatter(StringFormatter):
    """Alphanumeric characters only."""
    re_validation = '^[a-zA-Z0-9]*$'


class EmailFormatter(StringFormatter):
    """Internet email addresses (more or less)."""
    # This regex does not match all legal email addresses, but
    # it does a pretty good job.
    # Strangely enough, '/' is legal in email addresses.
    # However, I've never seen it used, so I prefer to leave it out.
    _re_subs = {
        'sub1': r'[a-zA-Z~_-][a-zA-Z0-9_:~-]*',
        'sub2': r'(\.[a-zA-Z0-9_:~-]+)*',
        'sfx': r'\.[a-zA-Z]{2,3}'
    }
    re_validation = '^%(sub1)s%(sub2)s[@]%(sub1)s%(sub2)s%(sfx)s$' % _re_subs


class MoneyFormatter(StringFormatter):
    """Assumes decimal money, but doesn't assume currency."""
    re_validation = '^(([0-9]+([.][0-9]{2})?)|([0-9]*[.][0-9]{2}))$'


class IntFormatter(six.with_metaclass(FormatterMeta, Formatter)):
    """Signed or unsigned integer."""

    #re_validation = '^[-+]?[0-9]+$'

    def __init__(self, min_val=0, max_val=2**31 - 1, **kwargs):
        super(IntFormatter, self).__init__(min_val, max_val, **kwargs)

        self.max_val = max_val
        self.min_val = min_val

    def validate(self, str_value):
        try:
            v = self.coerce(str_value)
            if self.max_val is not None and v > self.max_val:
                return False
            if self.min_val is not None and v < self.min_val:
                return False
            return True
        except:
            return False

    def coerce(self, str_value):
        if str_value:
            return int(str_value)
        return str_value


class HexFormatter(IntFormatter):
    def format(self, value):
        return hex(value)

    def coerce(self, str_value):
        return int(str_value, 16)


class BinFormatter(IntFormatter):
    def format(self, value):
        return bin(value)

    def coerce(self, str_value):
        return int(str_value, 2)


class BoolFormatter(IntFormatter):
    def format(self, value):
        return str(bool(value))

    def coerce(self, str_value):
        str_value = str_value.strip()
        if str_value.lower() == 'true':
            return 1
        return 0


class Int8Formatter(IntFormatter):
    def __init__(self, min_val=-2**7, max_val=2**7 - 1, **kwargs):
        super(Int8Formatter, self).__init__(min_val, max_val, **kwargs)


class Int16Formatter(IntFormatter):
    def __init__(self, min_val=-2**15, max_val=2**15 - 1, **kwargs):
        super(Int16Formatter, self).__init__(min_val, max_val, **kwargs)


class Int24Formatter(IntFormatter):
    def __init__(self, min_val=-2**23, max_val=2**23 - 1, **kwargs):
        super(Int24Formatter, self).__init__(min_val, max_val, **kwargs)


class Int32Formatter(IntFormatter):
    def __init__(self, min_val=-2**31, max_val=2**31 - 1, **kwargs):
        super(Int32Formatter, self).__init__(min_val, max_val, **kwargs)


class Int64Formatter(IntFormatter):
    def __init__(self, min_val=-2**63, max_val=2**63 - 1, **kwargs):
        super(Int64Formatter, self).__init__(min_val, max_val, **kwargs)


class UIntFormatter(IntFormatter):
    """Unsigned integer."""
    def __init__(self, min_val=None, max_val=None, **kwargs):
        super(UIntFormatter, self).__init__(min_val, max_val, **kwargs)

        self.min_val = max(0, min_val)


class UInt8Formatter(UIntFormatter):
    def __init__(self, min_val=0, max_val=2**8 - 1, **kwargs):
        super(UInt8Formatter, self).__init__(min_val, max_val, **kwargs)


class UInt16Formatter(UIntFormatter):
    def __init__(self, min_val=0, max_val=2**16 - 1, **kwargs):
        super(UInt16Formatter, self).__init__(min_val, max_val, **kwargs)


class UInt24Formatter(UIntFormatter):
    def __init__(self, min_val=0, max_val=2**24 - 1, **kwargs):
        super(UInt24Formatter, self).__init__(min_val, max_val, **kwargs)


class UInt32Formatter(UIntFormatter):
    def __init__(self, min_val=0, max_val=2**32 - 1, **kwargs):
        super(UInt32Formatter, self).__init__(min_val, max_val, **kwargs)


class FloatFormatter(Formatter):
    """Signed or unsigned floating-point number."""
    def __init__(self, min_val=None, max_val=None, **kwargs):
        super(FloatFormatter, self).__init__(min_val, max_val, **kwargs)

        self.max_val = max_val
        self.min_val = min_val

    def validate(self, str_value):
        try:
            v = self.coerce(str_value)
            if self.max_val is not None and v > self.max_val:
                return False
            if self.min_val is not None and v < self.min_val:
                return False
            return True
        except:
            return False

    def coerce(self, str_value):
        if str_value:
            return float(str_value)
        return str_value


class DoubleFormatter(FloatFormatter):
    pass


class UFloatFormatter(FloatFormatter):
    """Unsigned floating-point number."""
    def __init__(self, min_val=None, max_val=None, **kwargs):
        super(UFloatFormatter, self).__init__(min_val, max_val, **kwargs)
        self.min_val = max(0, min_val)


class UDoubleFormatter(UFloatFormatter):
    pass


class TextFormatter(six.with_metaclass(FormatterMeta, Formatter)):
    pass


class PathFormatter(TextFormatter):
    ERROR_INVALID_NAME = 123

    def __init__(self, exist=False, types=None, **kwargs):
        super(PathFormatter, self).__init__(**kwargs)
        self.exist = exist
        self.types = types

    def validate(self, str_value):
        if self.exist:
            if self.types == 'folder':
                return os.path.isdir(str_value)
            elif self.types == 'file':
                return os.path.isfile(str_value)
            else:
                return os.path.exists(str_value)
        else:
            return self.is_path_exists_or_creatable(str_value)

    def is_pathname_valid(self, pathname):
        '''
        `True` if the passed pathname is a valid pathname for the current OS;
        `False` otherwise.
        '''
        #https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta/9532586
        # If this pathname is either not a string or is but is empty, this pathname
        # is invalid.
        try:
            if not isinstance(pathname, six.string_types) or not pathname:
                return False

            # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
            # if any. Since Windows prohibits path components from containing `:`
            # characters, failing to strip this `:`-suffixed prefix would
            # erroneously invalidate all valid absolute Windows pathnames.
            _, pathname = os.path.splitdrive(pathname)

            # Directory guaranteed to exist. If the current OS is Windows, this is
            # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
            # environment variable); else, the typical root directory.
            root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
                if sys.platform == 'win32' else os.path.sep
            assert os.path.isdir(
                root_dirname)  # ...Murphy and her ironclad Law

            # Append a path separator to this directory if needed.
            root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

            # Test whether each path component split from this pathname is valid or
            # not, ignoring non-existent and non-readable path components.
            for pathname_part in pathname.split(os.path.sep):
                try:
                    os.lstat(root_dirname + pathname_part)
                # If an OS-specific exception is raised, its error code
                # indicates whether this pathname is valid or not. Unless this
                # is the case, this exception implies an ignorable kernel or
                # filesystem complaint (e.g., path not found or inaccessible).
                #
                # Only the following exceptions indicate invalid pathnames:
                #
                # * Instances of the Windows-specific "WindowsError" class
                #   defining the "winerror" attribute whose value is
                #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
                #   fine-grained and hence useful than the generic "errno"
                #   attribute. When a too-long pathname is passed, for example,
                #   "errno" is "ENOENT" (i.e., no such file or directory) rather
                #   than "ENAMETOOLONG" (i.e., file name too long).
                # * Instances of the cross-platform "OSError" class defining the
                #   generic "errno" attribute whose value is either:
                #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
                #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
                except OSError as exc:
                    if hasattr(exc, 'winerror'):
                        if exc.winerror == self.ERROR_INVALID_NAME:
                            return False
                    elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                        return False
        # If a "TypeError" exception was raised, it almost certainly has the
        # error message "embedded NUL character" indicating an invalid pathname.
        except TypeError as exc:
            return False
        # If no exception was raised, all path components and hence this
        # pathname itself are valid. (Praise be to the curmudgeonly python.)
        else:
            return True
        # If any other exception was raised, this is an unrelated fatal issue
        # (e.g., a bug). Permit this exception to unwind the call stack.
        #
        # Did we mention this should be shipped with Python already?

    def is_path_creatable(self, pathname):
        '''
        `True` if the current user has sufficient permissions to create the passed
        pathname; `False` otherwise.
        '''
        # Parent directory of the passed path. If empty, we substitute the current
        # working directory (CWD) instead.
        dirname = os.path.dirname(pathname) or os.getcwd()
        return os.access(dirname, os.W_OK)

    def is_path_exists_or_creatable(self, pathname):
        '''
        `True` if the passed pathname is a valid pathname for the current OS _and_
        either currently exists or is hypothetically creatable; `False` otherwise.

        This function is guaranteed to _never_ raise exceptions.
        '''
        try:
            # To prevent "os" module calls from raising undesirable exceptions on
            # invalid pathnames, is_pathname_valid() is explicitly called first.
            return self.is_pathname_valid(pathname) and (
                os.path.exists(pathname) or self.is_path_creatable(pathname))
        # Report failure on non-fatal filesystem complaints (e.g., connection
        # timeouts, permissions issues) implying this path to be inaccessible. All
        # other exceptions are unrelated fatal issues and should not be caught here.
        except OSError:
            return False


class TimeElapsedFormatter(six.with_metaclass(FormatterMeta, Formatter)):
    """Elapsed time string (HH:MM:SS)."""
    re_validation = '^([1][0-2]|[0]?[0-9]):[0-5][0-9](:[0-5][0-9])?$'


class DateFormatter(Formatter):
    """
    Date string (YYYY-MM-DD).

    Storage format:      wx.DateTime
    Presentation format: YYYY-MM-DD

    Accepts only YYYY-MM-DD format (allows variant separators '/' and '.').
    Accepts dates in range (1000-2999)-(01-12)-(01-31).
    Leading zeros optional in month and day.
    Does not enforce # of days in month.
    """
    def __init__(self, fmt='%Y-%m-%d', **kwargs):
        super(DateFormatter, self).__init__(**kwargs)
        self.str_format = fmt

    def validate(self, str_value):
        value = wx.DateTime()
        return value.ParseDate(str_value) != -1

    def format(self, value):
        return value.Format(self.str_format)

    def coerce(self, str_value):
        """Convert alternate date separators to '-'."""
        value = wx.DateTime()
        value.ParseDate(str_value)
        return value


class DateFormatterMDY(DateFormatter):
    """Alternate date string (MM-DD-YYYY).

    Presentation format: MM-DD-YYYY

    Accepts only MM-DD-YYYY format  (allows variant separators '/' and '.').
    Accepts dates in range (01-12)-(01-31)-(1000-2999).
    Leading zeros optional in month and day.
    Does not enforce # of days in month.
    """
    def __init__(self, fmt='%m-%d-%Y', **kwargs):
        super(DateFormatterMDY, self).__init__(fmt, **kwargs)


class TimeFormatter(DateFormatter):
    """
    Time string (12-hour or 24-hour format, with or without seconds or am/pm).

    Storage format:      HH:MM:SS -- 24-hour format.
    Presentation format: HH:MM    -- 24-hour format.

    Accepts 12-hour or 24-hour format, with or without seconds or am/pm.
    """
    def __init__(self, fmt='%H:%M:%S', **kwargs):
        super(TimeFormatter, self).__init__(fmt, **kwargs)

    def validate(self, str_value):
        value = wx.DateTime()
        return value.ParseTime(str_value) != -1

    def coerce(self, str_value):
        """Convert alternate date separators to '-'."""
        value = wx.DateTime()
        value.ParseTime(str_value)
        return value


class TimeFormatter12H(TimeFormatter):
    """
    Alternate time string (12-hour format, without seconds).

    Storage format:      HH:MM(:SS) -- 24-hour format.
    Presentation format: HH:MM(aa) -- 12-hour format.
                         (aa may be 'am' or 'pm')
    """
    def __init__(self, fmt='%I:%M:%S %p', **kwargs):
        super(TimeFormatter12H, self).__init__(fmt, **kwargs)


class DateTimeFormatter(DateFormatter):
    """
    Date/time string.

    Uses a DateFormatter and a TimeFormatter.
    """

    # Storage format: YYYY-MM-DD HH:MM:SS -- 24-hour format.
    # Presentation format: same as storage format.
    def __init__(self, fmt='%Y-%m-%d %H:%M:%S', **kwargs):
        super(DateTimeFormatter, self).__init__(fmt, **kwargs)

    def validate(self, str_value):
        value = wx.DateTime()
        return value.ParseDateTime(str_value) != -1

    def coerce(self, str_value):
        """Convert alternate date separators to '-'."""
        value = wx.DateTime()
        value.ParseDateTime(str_value)
        return value


class ColorFormatter(Formatter):
    # Storage formate: wx.Colour
    # Presentation format HTML-like syntax: #xxxxxx.
    def validate(self, str_value):
        clr = wx.Colour()
        return clr.Set(str_value)

    def format(self, value):
        if isinstance(value, six.string_types):
            return value
        elif isinstance(value, wx.Colour):
            return value.GetAsString(wx.C2S_HTML_SYNTAX)
        return ""

    def coerce(self, str_value):
        try:
            clr = wx.Colour()
            clr.Set(str_value)
            return clr.GetAsString(wx.C2S_HTML_SYNTAX)
        except:
            return ""


class FontFormatter(Formatter):
    # Storage formate: wx.Font
    def validate(self, str_value):
        font = wx.Font(str_value)
        return font.IsOk()

    def format(self, value):
        if isinstance(value, six.string_types):
            return value
        elif isinstance(value, wx.Font):
            return value.GetNativeFontInfoDesc()
        return ""

    def coerce(self, str_value):
        font = wx.Font(str_value)
        return font


if __name__ == '__main__':

    from .enumtype import EnumType

    def test(tests, fmt, msg):
        print(msg)
        failed, passed = 0, 0
        for t, r in tests:
            actual = fmt.validate(t)
            if actual == r:
                passed += 1
            else:
                print('failed test: {0}, expect {1}, returned {2}'.format(
                    t, r, actual))
                failed += 1
        print('\tPASS: %d tests' % passed)
        print('\tFAIL: %d tests' % failed)

    # ========== EnumFormatter ==========
    print('EnumFormatter')
    TestEnum = EnumType('A', 'B', 'C', D=3)
    formatter = EnumFormatter(TestEnum)
    passCount = 0
    failCount = 0

    # formatter.validValues
    expectedValidValues = [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]
    temp = formatter.validValues()
    if temp == expectedValidValues:
        passCount += 1
    else:
        failCount += 1
        print('formatter.validValues() = %r -- WRONG -- expected %r' %
              (temp, expectedValidValues))

    # formatter.format and formatter.coerce
    for id, name in TestEnum.items():
        # formatter.format
        temp = formatter.format(id)
        if temp == name:
            passCount += 1
        else:
            failCount += 1
            print('formatter.format(%d) = %r -- WRONG -- expected %r' %
                  (id, temp, name))
        # formatter.coerce
        temp = formatter.coerce(name)
        if temp == id:
            passCount += 1
        else:
            failCount += 1
            print('formatter.coerce(%r) = %r -- WRONG -- expected %r' %
                  (name, temp, id))
    if failCount == 0:
        print('\tPASS (%d tests)' % passCount)

    tests = [
        ('a@b.com', True),
        ('a@b', False),
        ('@b', False),
        ('@b.c', False),
        ('@b.us', False),
        ('a@b.us', True),
        ('~joe_public-73@bozo.net', True),
    ]
    test(tests, EmailFormatter(), 'EmailFormatter')

    tests = [('10', True), ('0', True), ('100', True), ('-1', False)]
    test(tests, IntFormatter(0, 100), 'IntFormatter')
    test(tests, UIntFormatter(-1, 100), 'UIntFormatter')
    test(tests, FloatFormatter(0, 100), 'FloatFormatter')
    test(tests, UFloatFormatter(0, 100), 'UFloatFormatter')

    tests = [('0x0a', True), ('0x00', True), ('0x64', True), ('-0x1', False)]
    test(tests, HexFormatter(0, 100), 'HexFormatter')

    tests = [('0b1010', True), ('0b0', True), ('0b1100100', True),
             ('-0b1', False)]
    test(tests, BinFormatter(0, 100), 'BinFormatter')

    tests = [
        ('10', True),
        ('0', True),
        ('127', True),
        ('128', False),
        ('-1', True),
        ('-128', True),
        ('-129', False),
    ]
    test(tests, Int8Formatter(), 'Int8Formatter')
    tests = [
        ('10', True),
        ('0', True),
        ('127', True),
        ('255', True),
        ('256', False),
        ('-1', False),
    ]
    test(tests, UInt8Formatter(), 'UInt8Formatter')
