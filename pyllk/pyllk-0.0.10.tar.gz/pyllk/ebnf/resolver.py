import os
from pathlib import Path

import pyllk.ebnf.parser as parser


class ImportException(Exception):
    pass


def resolve(grammar_description, base_path, __imports_table=None):
    """Resolves imports in the given grammar description

    Args:
        grammar_description (dict): The grammar description to resolve
        base_path (dict): The path to the original grammar file
    """

    if "imports" in grammar_description:
        imports = grammar_description["imports"]
        for dependency in imports:
            source = dependency["source"]
            names = dependency["names"]
            __resolve_import(grammar_description, source, names, base_path, __imports_table if __imports_table is not None else [])

        del grammar_description["imports"]

    return grammar_description


def __resolve_import(grammar_description, source, names, base_path, imports_table):
    """Resolves a single import in place

    Args:
        grammar_description (dict): The grammar description to resolve
        source (string): The path to the imported grammar
        names (list[string]): The names to import
        base_path (dict): The path to the original grammar file
        imports_table (list): A list of imported grammars to help break cycles
    """
    imports_table.append(base_path)

    folder = Path(os.path.dirname(base_path))
    imported_grammar_path = Path(folder / source).absolute()

    if imported_grammar_path in imports_table:
        raise ImportException(f"Import cycle detected {imported_grammar_path} from {base_path}")

    other = parser.parse(imported_grammar_path)
    other = resolve(other, imported_grammar_path, __imports_table=imports_table)

    terminals = other["definitions"] if "definitions" in other else {}
    non_terminals = other["productionRules"] if "productionRules" in other else {}
    for name in names:
        if name in terminals:
            if name in grammar_description["productionRules"]:
                raise ImportException(f"Import conflict: Tryng to import {name} from {imported_grammar_path} as terminal but it already exists in {base_path} as a non-terminal.")
            grammar_description["definitions"][name] = terminals[name]
        if name in non_terminals:
            if name in grammar_description["definitions"]:
                raise ImportException(f"Import conflict: Tryng to import {name} from {imported_grammar_path} as non-terminal but it already exists in {base_path} as a terminal.")
            grammar_description["productionRules"][name] = non_terminals[name]
