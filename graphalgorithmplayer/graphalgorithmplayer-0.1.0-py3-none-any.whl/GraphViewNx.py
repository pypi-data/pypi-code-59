import ipywidgets
import networkx
import matplotlib.pyplot as plt
from IPython.utils import capture
from collections.abc import Iterable
#GraphViewNetworkx
class GraphViewNx(ipywidgets.Output):
    """
        Draw a graph with Networkx
    """
    def __init__(self,graph, variables,edgeLabels=None, nodeLabels=None):
        """
            Initialization of the class
            
            Parameters:
            -----------
            graph : the graph to draw
            variables : (type=list(dict())) the variables defining possible colors and labels for the nodes and edges
            edgeLabels : (type=dict()) Labels for edges to keep throught the entire algorithm
            nodeLabels : (type=dict()) Labels for nodes to keep throught the entire algorithm
            
        """
        self.__graph=graph
        if graph!=None:
            if not isinstance(graph, (networkx.Graph, networkx.DiGraph)):
                self.__graph = graph.networkx()
            self.__nodeLabels=nodeLabels
            self.__pos=networkx.spring_layout(self.__graph)
        self.__variables=variables
        self.__edgeLabels=edgeLabels
        ipywidgets.Output.__init__(self)
        if graph!=None:
            with capture.capture_output() as c:
                self.make()
            self.clear_output(wait=True)
            with self:
                c()
            
    def newGraph(self,graph, variables):
        """
            Display a new graph
            
            Parameters:
            -----------
            graph : the new graph
            variables : variables to initialize the vizualisation with
            
        """
        self.clear_output(wait=True)
        if not isinstance(graph, (networkx.Graph, networkx.DiGraph)):
            graph = graph.networkx()
        self.__graph=graph
        self.__pos=networkx.spring_layout(self.__graph)
        self.__variables=variables
        self.__edgeLabels=None
        self.__nodeLabels=None
        with capture.capture_output() as c:
            self.make()
        self.clear_output(wait=True)
        with self:
            c()
        
        
    def update(self,variables):
        """
            Update the vizualisation and display it
            
            Parameters
            -----------
            variables : the variables defining the colors and labels of nodes and edges
            
        """
        self.__variables=variables
        if self.__graph!=None:
            with capture.capture_output() as c:
                self.make()
            self.clear_output(wait=True)
            with self:
                c()
    
    def make(self):
        """
            Make the vizualisation in Networkx
        """
        nodes=list(self.__graph.nodes)
        edges=list(self.__graph.edges)
        networkx.draw_networkx_nodes(self.__graph,self.__pos,nodelist=nodes,node_color='grey')
        networkx.draw_networkx_edges(self.__graph, self.__pos, edgelist=edges, edge_color='black')
        drawLabels=True
        for v in self.__variables:
            mytype=v['type']
            value=v['value']
            if mytype=='edge_property' and v.get('style')=='label' and value!=None:
                networkx.draw_networkx_edge_labels(self.__graph,self.__pos,value)
            if mytype=='node_property' and v.get('style')=='label' and value!=None:
                networkx.draw_networkx_labels(self.__graph,self.__pos,value)
                drawLabels=False
            elif self.__edgeLabels!=None:
                networkx.draw_networkx_edge_labels(self.__graph,self.__pos,self.__edgeLabels)
            if v.get('color')!=None :
                color=v['color']
                if (mytype=='nodes' or mytype=='node') and value!=None:
                    if mytype=='node':
                        value=[value]
                    networkx.draw_networkx_nodes(self.__graph,self.__pos,nodelist=value,node_color=color)
                elif (mytype=='edges' or mytype=='edge') and value!=None:
                    if mytype=='edge':
                        value=[value]
                    networkx.draw_networkx_edges(self.__graph, self.__pos, edgelist=value,width=2, alpha=0.5, edge_color=color)
        if self.__nodeLabels!=None and drawLabels==True:
            networkx.draw_networkx_labels(self.__graph,self.__pos,self.__nodeLabels)
        elif drawLabels==True:
            networkx.draw_networkx_labels(self.__graph,self.__pos)
        plt.show()