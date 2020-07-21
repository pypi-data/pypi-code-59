import inspect,json

class GraphEvaluator:
    verbose = True
    node_stack = []
    
    @staticmethod
    def evaluate(node):
        if node.state == NodeState.CALCULATING:
            nodes = " depends on\n".join([str(n) for n in GraphEvaluator.node_stack + [node]])
            raise Exception("Circular reference: \n%s" % nodes)
        if len(GraphEvaluator.node_stack):
            parent = GraphEvaluator.node_stack[-1]
            parent.deps.add(node)
            node.precedents.add(parent)
        GraphEvaluator.node_stack.append(node)
        if GraphEvaluator.verbose:
            arrows = "o" * (len(GraphEvaluator.node_stack) -1 ) * 3 + "> "
            print(f"{arrows} evaluating {node}")
        try:
            if node.state != NodeState.VALID:
                node.state = NodeState.CALCULATING
                node.value = node.cb()
                node.state = NodeState.VALID
            if GraphEvaluator.verbose:
                print(f"{arrows} calculated {node}")
            GraphEvaluator.node_stack.pop()
        #print(f"Children of {node}: {node.deps}")
        except Exception as e:
            node.value = e
            node.state = NodeState.INVALID
            GraphEvaluator.node_stack = []
            raise e
        return node.value
        

        
def node_helper(fn):
    def node_fn(*args):
        self = args[0]
        if len(args)>1:
            others = json.dumps(args[1:])
            others = f"({others[1:-1]})"
        else:
            others = ""
        tag = f'{self}.{fn.__name__}{others}'
        return Node.create(tag,lambda: fn(*args), obj=self,name=fn.__name__)
    return node_fn

### decorators
def node(fn):
    return property(node_helper(fn))

def nodefn(fn):
    return node_helper(fn)

class NodeState:
    INVALID = 'NODESTATE_INVALID'
    VALID = 'NODESTATE_VALID'
    CALCULATING = 'NODESTATE_CALCULATING'
    
    
class Node:
    def __init__(self,tag,cb, obj=None,name=None, scenario = None):
        self.tag = tag
        self.cb = cb
        self.deps = set()
        self.precedents = set()
        self.state = NodeState.INVALID
        self.value = None
        self.obj = obj
        self.name = name
        self.scenario = scenario

    def invalidate(self):
        if self.state == NodeState.INVALID:
            return
        if GraphEvaluator.verbose:
            print(f"Invalidating {self}")
        self.state = NodeState.INVALID
        self.value = None
        for node in self.precedents:
            node.invalidate()

    @property
    def Deps(self):
        return list(self.deps)

    @property
    def Precedents(self):
        return list(self.precedents)

    def In(self,scenario):
        return Node.create(self.tag,self.cb,self.obj,self.name,scenario)
    
    @staticmethod
    def create(tag,cb,obj,name,scenario = None):
        if scenario is None:
            scenario = ScenarioContext.CurrentScenario()
        if tag not in scenario.cache:
            scenario.cache[tag] = Node(tag,cb,obj=obj,name=name, scenario=scenario)
        return scenario.cache[tag]
    
    def set(self,cb):
        self.invalidate()
        if type(cb) != type(lambda: None):
            self.cb = lambda: cb
        else:
            self.cb = cb

    def reset(self):
        self.invalidate()
        del self.scenario.cache[self.name]
        
    def recalculate(self):
        self.invalidate()
        return self()
    
    def __repr__(self):
        return f'Node[{self.state}|{self.scenario}|{self.name}={self.value}]'
    def evaluate(self):
        return GraphEvaluator.evaluate(self)
    def __call__(self):
        return self.scenario.Evaluate(self)

def fn():
    raise Exception("Error calculating")
    

class ScenarioContext:
    Stack = []
    
    @staticmethod
    def CurrentScenario():
        return ScenarioContext.Stack[-1]


class Scenario:
    _source = None
    def __init__(self,source):
        self._source = source
        self.cache = {}
    
    @property
    def Source(self):
        return self._source

    def ProvidesFormula(self, node):
        raise NotImplementedError("Needs to be implemented in derived class")
    def Formula(self, node):
        raise NotImplementedError("Needs to be implemented in derived class")

    def Evaluate(self, node):
        ScenarioContext.Stack.append(self)
        if self.ProvidesFormula(node):
            value = self.Formula(node)()
        else:
            value = self.Source.Evaluate(node)
        ScenarioContext.Stack.pop()
        return value
    
class BaseScenario(Scenario):
    def __init__(self):
        self.cache = {}
    
    def Evaluate(self, node):
        return node.evaluate()
