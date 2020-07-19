import pyllk.ebnf.decoder as decoder
import pyllk.ebnf.parser as ebnf_parser
import pyllk.ebnf.resolver as resolver
import pyllk.token


def load(path, token_fn, action_fn=None):
    """Loads an EBNF context-free grammar and returns a pyllk grammar object

    Args:
        path (string): The path to the grammar file to load
        token_fn (typing.Callable[[dict], pyllk.token.TerminalToken]): A producer of terminal tokens from a config map
        action_fn (typing.Callable[[dict], typing.Callable]): A producer of actions from a config map
    """
    result = ebnf_parser.parse(path)
    result = resolver.resolve(result, path)
    result = decoder.decode(result, token_fn, action_fn)
    return result


TerminalToken = pyllk.token.TerminalToken
