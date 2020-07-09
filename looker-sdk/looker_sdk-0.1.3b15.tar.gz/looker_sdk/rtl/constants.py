# The MIT License (MIT)
#
# Copyright (c) 2019 Looker Data Sciences, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

looker_version = "7.10"
api_version = "4.0"
sdk_version = f"{api_version}.{looker_version}"
environment_prefix = "LOOKERSDK"

RESPONSE_STRING_MODE = (
    r"(^application/.*"
    r"(\bjson\b|\bxml\b|\bsql\b|\bgraphql\b|\bjavascript\b|\bx-www-form-urlencoded\b)"
    r"|^text/|.*\+xml\b|;.*charset=)"
)

# note: string mode must be checked first
RESPONSE_BINARY_MODE = r"^image/|^audio/|^video/|^font/|^application/|^multipart/"
