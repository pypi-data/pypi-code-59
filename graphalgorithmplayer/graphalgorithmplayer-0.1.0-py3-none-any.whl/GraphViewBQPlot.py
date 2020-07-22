import bqplot.marks
import ipywidgets
import traitlets
import networkx
import warnings
from collections.abc import Iterable

class GraphViewBQPlot(ipywidgets.Output):
    """
        Display a graph with BQPlot
    """
    def __init__(self, graph, variables):
        """
            Initialization of the class
            
            Parameters
            -----------
            graph : the graph to display
            variables : (type=list(dict())) defines the color of each node
            
        """
        if graph!=None and not isinstance(graph, (networkx.Graph, networkx.DiGraph)):
            graph = graph.networkx()
        ipywidgets.Output.__init__(self)
        self._graph=graph
        if graph!=None:
            self.newGraph(graph,variables)

    value = traitlets.Dict()
    
    def newGraph(self, graph, variables):
        """
            Change the graph to display
            
            Parameters
            -----------
            graph : the new graph
            variables : define the color for each node 
        """
        self.clear_output(wait=True)
        if not isinstance(graph, (networkx.Graph, networkx.DiGraph)):
            graph = graph.networkx()
        self._graph = graph
        self._variables = variables
        nodes = self._graph.vertices()
        self._rank = { v: i for i,v in enumerate(nodes) }
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                layout = networkx.planar_layout(self._graph)
        except networkx.NetworkXException:
            layout = networkx.spring_layout(self._graph)
        xs = bqplot.LinearScale()
        ys = bqplot.LinearScale()
        cs = bqplot.ColorScale(scheme='Reds')
        x = [layout[node][0] for node in nodes]
        y = [layout[node][1] for node in nodes]
        
        fig_layout = ipywidgets.Layout(width='400px', height='300px')
        self._mark = mark = bqplot.marks.Graph(
            node_data = self.node_data(),
            link_type='line', directed=self._graph.is_directed(),
            scales={'x': xs, 'y': ys, 'link_color': cs},
            x=x, y=y,
            charge=-600,
            colors=self.colors())
        
        self.__fig = bqplot.Figure(marks=[mark], layout=fig_layout)
        self.clear_output(wait=True)
        with self:
            display(self.__fig)
        self.make()
        

    def colors(self):
        """
            Color the node in the graph
        """
        rank = self._rank
        colors = ['white'] * len(rank)
        for variable in self._variables:
            #name  = variable['name']
            mytype  = variable['type']
            if (mytype=='nodes' or mytype=='node') and variable.get('color')!=None : 
                color = variable['color']
                values = variable['value']
                if values is None:
                    continue
                if mytype=='node':
                    nodes = [values]
                elif mytype=='nodes':
                    nodes = values
                for node in nodes:
                    colors[rank[node]] = color
        return colors

    def node_data(self):
        return [str(i) for i in self._graph.nodes() ]
        # Fails: get a white image after the first image
        return [{'label': str(i)} for i in self._graph.nodes() ]
        # Fails: garbled edges after the first image
        def shape(i):
            if i == self.value.get('source', None):
                return "rect"
            elif i == self.value.get('target', None):
                return "ellipse"
            else:
                return "circle"
        return [ {'label':str(i),
                  'shape':shape(i)
                 }
                 for i in self._graph.nodes() ]

    def link_data(self):
        rank = self._rank
        return [{'source': rank[edge[0]],
                 'target': rank[edge[1]],
                }
                for edge in self._graph.edges()]
    
    def update(self,variables):
        """
            Update the vizualisation with the new values in variables
            
        """
        self._variables=variables
        if self._graph!=None:
            self.make()
    
    def make(self):
        """
            Make the vizualisation
        """
        link_data = self._mark.link_data
        self._mark.colors = self.colors()
        self._mark.link_data = link_data + [{'source':0, 'target':0}]
        self._mark.link_data = self.link_data()