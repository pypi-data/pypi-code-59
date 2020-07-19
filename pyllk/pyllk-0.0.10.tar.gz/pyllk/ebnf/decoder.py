from pyllk.grammar import Grammar as PyllkGrammar
from pyllk.production_rule import ProductionRule
from pyllk.token import NonTerminalToken


def decode(json_grammar, token_fn, action_fn):
    """Decodes a JSON grammar dictionary into a native pyllk grammar

    Args:
        json_grammar (dict): The JSON grammar to decode
        token_fn (typing.Callable[[dict], pyllk.token.TerminalToken]): A producer of terminal tokens from a config map
        action_fn (typing.Callable[[dict], typing.Callable]): A producer of actions from a config map
    """

    rules = []

    definitions = json_grammar["definitions"]
    production_rules = json_grammar["productionRules"]

    terminals = {}

    # Get all the terminal token definitions first
    for terminal in definitions:
        terminal_token = token_fn(definitions[terminal])
        terminals[terminal] = terminal_token

    for non_terminal in production_rules:
        for production_rule in production_rules[non_terminal]:
            tokens = production_rule['tokens']
            tokens_list = []
            for token in tokens:
                if token in terminals:
                    # It's a terminal token
                    tokens_list.append(terminals[token])
                else:
                    # It looks like a non-terminal token
                    tokens_list.append(NonTerminalToken(token))

            if "action" not in production_rule:
                rules.append(ProductionRule(NonTerminalToken(non_terminal), tokens_list))
            else:
                action = action_fn(production_rule["action"]) if action_fn else None
                rules.append(ProductionRule(NonTerminalToken(non_terminal), tokens_list, action=action, data=production_rule["action"]))

    pyllkGrammar = PyllkGrammar(rules)

    return pyllkGrammar
