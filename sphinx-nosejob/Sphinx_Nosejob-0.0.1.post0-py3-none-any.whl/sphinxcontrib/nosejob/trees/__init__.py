"""
sphinxcontrib.nosejob.trees
---------------------------

A collection of directives to support tree structures within Sphinx
"""
# Meta Information
from .__meta__ import *
# Nodes
from sphinxcontrib.nosejob.trees.nodes import pathTree, visit_pathtree_node, depart_pathtree_node
# from sphinxcontrib.nosejob.trees.nodes import tabbing as TabbingNode, visit_tabbing_node, depart_tabbing_node
# Directives
from sphinxcontrib.nosejob.trees.directives import PathTree as PathTreeDirective, Tree as TreeDirective, Tabbing as TabbingDirective

def setup(app):
    # Nodes
    app.add_node(pathTree,
                 html=(visit_pathtree_node, depart_pathtree_node),
                 latex=(visit_pathtree_node, depart_pathtree_node),
                 text=(visit_pathtree_node, depart_pathtree_node))
    # app.add_node(TabbingNode,
    #              html= (visit_tabbing_node, depart_tabbing_node),
    #              latex=(visit_tabbing_node, depart_tabbing_node),
    #              text= (visit_tabbing_node, depart_tabbing_node))
    # Directives
    app.add_directive("paths",    PathTreeDirective)
    app.add_directive("tree",     TreeDirective)
    app.add_directive("tabbing",  TabbingDirective)
    # Registration
    return {'parallel_read_safe' : True,
            'parallel_write_safe': True,
            'version'            : __version__}
