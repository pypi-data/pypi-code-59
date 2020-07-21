import json
from pygments import highlight, lexers, formatters


def pretty_print(unpretty_json):
    formatted_json = json.dumps(json.loads(unpretty_json), sort_keys=True,
                                indent=4)
    colorful_json = highlight(unicode(formatted_json, 'UTF-8'),
                              lexers.JsonLexer(),
                              formatters.TerminalFormatter())
    print(colorful_json)
