from .operators import operators

class Parser:
    def __init__(self, handler, api=None, params={}):
        self.handler = handler
        self.api = api
        
        # initialize the labels with the params that were sent in
        self.labels = params

    ### MATH ###
    def eval_condition(self, cond_statement):
        operator = cond_statement['operator']
        operator_fn = operators[operator]
        params = self.eval_all(cond_statement['params'])

        return operator_fn(*params)

    def eval_math(self, math_statement):
        fn = math_statement['fn']
        operator_fn = operators[fn]

        params = self.eval_all(math_statement['params'])

        return operator_fn(*params)

    ### INDICATORS EVALUATION ###
    def eval_preset(self, preset_reference):
        from . import presets

        preset_id = preset_reference['id']
        preset_expression = presets.get(preset_id, {})
        return self.eval(preset_expression)

    def eval_indicator(self, indicator_reference):
        from . import Indicator

        indicator_id = indicator_reference['id']
        settings = indicator_reference.get('settings', {})
        
        indicator = Indicator.from_api(indicator_id, self.api)
        try:
            return indicator.evaluate(self.handler.get_data(), settings)
        except Exception as e:
            return {"type": "error", "error_source": "indicator", "exception": e}

    ### COMMANDS/CONTROL FLOW ###
    def eval_if(self, if_statement):
        condition_true = self.eval_condition(if_statement['condition'])
        if condition_true:
            if 'true' in if_statement:
                return self.exec(if_statement['true'])
        else:
            if 'false' in if_statement:
                return self.exec(if_statement['false'])

    def eval_order(self, order):
        quantity = order['qty']

        # Enter/exit conditions for the order
        # if none, doesn't wait for a condition to enter, and holds pos
        # indefinitely (doesn't exit)
        # enter = order.get('enter')
        # exit_ = order.get('exit')

        return self.handler.order(quantity)

    def exec(self, command_list):
        for command in command_list:
            val = self.eval_command(command)
            if val is not None:
                if val['type'] == 'return':
                    return val['value']
                elif val['type'] == 'error':
                    return val

    def eval_command(self, command):
        if command['type'] == 'if':
            return self.eval_if(command)

        elif command['type'] == 'order':
            return {'type': 'order', 'value': self.eval_order(command)}

        elif command['type'] == 'return':
            return {'type': 'return', 'value': self.eval(command['value'])}

        elif command['type'] == 'setlabel':
            self.labels[command['label']] = self.eval(command['value'])

    ### GENERAL EVAL FUNCTIONS
    def eval_all(self, objects):
        return [self.eval(object) for object in objects]
    
    ### Evaluates an expression
    def eval(self, expression):
        if type(expression) in [int, float, str]:
            return expression

        if expression['type'] == 'condition':
            return self.eval_condition(expression)

        elif expression['type'] == 'indicator':
            return self.eval_indicator(expression)

        elif expression['type'] == 'number':
            return expression['value']

        elif expression['type'] == 'math':
            return self.eval_math(expression)

        elif expression['type'] == 'getlabel':
            return self.labels[expression['label']]

### When it receives orders, it just logs them
class LogHandler:
    def __init__(self):
        self.log = []

    def place_order(self, side, stock, quantity, enter=None, exit=None):
        self.log.append({
            'side': side,
            'stock': stock,
            'quantity': quantity,
            'enter': enter,
            'exit': exit
        })

#### USAGE
if __name__ == "__main__":
    code = [
        {'type': 'order', 'qty': 10, 'stock': 'AAPL'}
    ]

    # the Handler is what provides the stock data and what receives the orders
    log = LogHandler()

    parser = Parser(log)

    parser.exec(code)

    print(log.log)
