import treelib

def add_nodes(tree_obj, remaining_dict, parent_node=None):

    from treelib.exceptions import DuplicatedNodeIdError

    for key, value in remaining_dict.items():
        # Create the root node, if we are at root
        if parent_node is None:
            tree_obj.create_node(key, key)
        #Otherwise, we create a child node
        else:
            try:
                tree_obj.create_node(key,key, parent=parent_node)

            # procedure for handling duplicated node id's
            except DuplicatedNodeIdError:
                created = False
                counter=0

                # keep adding to the numeral we append until we find an id
                # which has not been used yet

                while not created:

                    try:
                        string_append = str(counter)
                        node_id = key + string_append
                        tree_obj.create_node(key, node_id, parent=parent_node)
                        created = True

                    except DuplicatedNodeIdError:
                        counter+=1

        if isinstance(value, dict):
            tree_obj = add_nodes(tree_obj, value, parent_node=key)
        else:
            pass
    return tree_obj

def create_tree_from_json(jsonDict):
    tree = treelib.Tree()

    # Create root node
    if len(jsonDict.keys())==1:
        rootNodeName = list(jsonDict.keys())[0]

    else:
        rootNodeName = "Root"

    tree.create_node(rootNodeName, rootNodeName)

    tree = add_nodes(tree, jsonDict, parent_node=rootNodeName)
    return tree
