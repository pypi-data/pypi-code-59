import io

class Node:
    # a node class
    def __init__(self, _id):
        self.id = _id
        self.parent = set()
        self.path = []

def add_next_ancestor(node, nodes, output): # one step towards the root in all paths
    return_value = False
    if len(node.parent) > 1: # we are only interested in nodes with >1 upstream neighbors, because other nodes cannot have redundant upstream edges
        # we must try to expand all discovered paths AND we must store new path(s) if we discover them along the way,
        # hence backwards enumeration
        for path_index in range(len(node.path)-1, -1, -1): # iterate through all discovered paths except ones we might add while iterating
            grandparent_found = False # reset flag ("grandparent found")
            for this_grandparent in nodes[node.path[path_index][-1]].parent: # define this_grandparent as a parent of the last discovered ancestor in this path
                if this_grandparent in node.path[path_index]: # if we've already seen this grandparent in this path,
                    return False # stop right there, it's a loop!
                if grandparent_found: # if this is not the first grandparent (grandparent_found flag is up => path diverges here),
                    node.path.append(node.path[path_index]) # then we add new path to this node which is the clone of this_path,
                    node.path[-1].append(this_grandparent) # and add this grandparent to this new path (which is now the last one)
                else: # if this is the first grandparent, then just add it to this path
                    node.path[path_index].append(this_grandparent)
                if this_grandparent in node.parent: # if this grandparent is found among the parents of this node, then that's it!
                    output.add((node.id, this_grandparent)) # let's output this redundant edge
                grandparent_found = True # set grandparent_found flag to True when at least 1 grandparent is encountered
                return_value = True # set return value for the function to True when a path has grown at least once
    return return_value

def process_list(graph):
    ret = set()
    nodes = {}
    for (child_id, parent_id) in graph:
        if child_id not in nodes:
            nodes[child_id] = Node(child_id)
        nodes[child_id].parent.add(parent_id)
        nodes[child_id].path.append([parent_id])
        if not parent_id in nodes:
            nodes[parent_id] = Node(parent_id)
    for node_id in nodes:
        while add_next_ancestor(nodes[node_id], nodes, ret):
            pass
    return ret

def process_dict(graph):
    ret = set()
    nodes = {}
    for child_id in graph:
        if child_id not in nodes:
            nodes[child_id] = Node(child_id)
        for parent_id in graph[child_id]:
            nodes[child_id].parent.add(parent_id)
            nodes[child_id].path.append([parent_id])
            if not parent_id in nodes:
                nodes[parent_id] = Node(parent_id)
    for node_id in nodes:
        while add_next_ancestor(nodes[node_id], nodes, ret):
            pass
    return ret

def process_tabfile(graph):
    ret = set()
    nodes = {}
    for line in graph:
        child_id, parent_id = line.strip('\n').split('\t')[:2]
        if child_id not in nodes:
            nodes[child_id] = Node(child_id)
        nodes[child_id].parent.add(parent_id)
        nodes[child_id].path.append([parent_id])
        if not parent_id in nodes:
            nodes[parent_id] = Node(parent_id)
    for node_id in nodes:
        while add_next_ancestor(nodes[node_id], nodes, ret):
            pass
    return ret

def transitive_edges(graph):
    def iterable(obj):
        try:
            iter(obj)
        except Exception:
            return False
        else:
            return True
    if not iterable(graph):
        raise ValueError
    if isinstance(graph, list) or isinstance(graph, tuple):
        return process_list(graph)
    elif isinstance(graph, dict):
        return process_dict(graph)
    elif isinstance(graph, io.TextIOWrapper):
        return process_tabfile(graph)
    else:
        raise ValueError
