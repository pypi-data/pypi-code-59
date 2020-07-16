def trueCountOperator(count, params):
    """Requires that at least `count` params are true.
    """

    total = 0
    for param in params:
        if param:
            total += 1
        
        if total >= count:
            return True
    
    return False

operators = {
    # comparisons
    ">": (lambda left, right: left > right),
    "<": (lambda left, right: left < right),
    ">=": (lambda left, right: left >= right),
    "<=": (lambda left, right: left <= right),
    "=": (lambda left, right: left == right), # include both of these bc why not
    "==": (lambda left, right: left == right),
    "!=": (lambda left, right: left != right),

    # math
    "+": (lambda *vals: sum(vals)),
    "-": (lambda left, right: left - right),
    "*": (lambda left, right: left * right),
    "/": (lambda left, right: left / right),
    "//": (lambda left, right: left // right),

    # boolean operators
    "not": (lambda var: not var),
    "all": (lambda *vars: all(vars)),
    "any": (lambda *vars: any(vars)),
    "none": (lambda *vars: not any(vars)),
    "some": trueCountOperator
}
