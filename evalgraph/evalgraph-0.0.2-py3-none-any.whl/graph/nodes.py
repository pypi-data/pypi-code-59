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
        return Node.create(tag,lambda: fn(*args))
    return node_fn

def node(fn):
    return property(node_helper(fn))

def nodefn(fn):
    return node_helper(fn)

def staticnode(fn):
    class_name = inspect.stack()[1].function
    def node_fn():
        tag = f'{class_name}.{fn.__name__}'
        return Node.create(tag,fn)
        
    return node_fn


class NodeState:
    INVALID = 'NODESTATE_INVALID'
    VALID = 'NODESTATE_VALID'
    CALCULATING = 'NODESTATE_CALCULATING'
    
    
class Node:
    cache = {}
    
    def __init__(self,name,cb):
        self.name = name
        self.cb = cb
        self.deps = set()
        self.precedents = set()
        self.state = NodeState.INVALID
        self.value = None

    def invalidate(self):
        if self.state == NodeState.INVALID:
            return
        if GraphEvaluator.verbose:
            print(f"Invalidating {self}")
        self.state = NodeState.INVALID
        self.value = None
        for node in self.precedents:
            node.invalidate()

    @staticmethod
    def create(name,cb):
        if name not in Node.cache:
            Node.cache[name] = Node(name,cb)
        return Node.cache[name]
    
    def set(self,cb):
        self.invalidate()
        if type(cb) != type(lambda: None):
            self.cb = lambda: cb
        else:
            self.cb = cb

    def reset(self):
        self.invalidate()
        del Node.cache[self.name]
        
    def recalculate(self):
        self.invalidate()
        return self()
    
    def __repr__(self):
        return f'Node[{self.state}|{self.name}={self.value}]'
    def __call__(self):
        return GraphEvaluator.evaluate(self)

def fn():
    raise Exception("Error calculating")
    
