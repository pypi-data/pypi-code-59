import ipywidgets
import traitlets
import copy
import networkx
from .GraphViewNetworkx import GraphViewNetworkx
from .GraphViewBQPlot import GraphViewBQPlot
from .VariablesView import VariablesView

class GraphAlgorithmView(ipywidgets.VBox):
    """
        Class to display a graph and the variables of a given algorithm
    """
    value = traitlets.Dict()
    def __init__(self, graph=None, view='networkx', variables=[], nodeLabels=None, edgeLabels=None):
        """
            Initialization
            
            Parameters
            -----------
            graph : the graph to display
            view : the library we use to display teh graph, either 'networkx' or 'bqplot'
            variables : defines the local variables we are interested in
            nodeLabels : labels for the nodes to keep throught the entire algorithm (only with networkx)
            edgeLabels : labels for the edges to keep throught the entire algorithm (only with networkx)
            
        """
        self._graph=graph
        if graph!=None and not isinstance(graph, (networkx.Graph, networkx.DiGraph)):
            graph = graph.networkx()
        for v in variables :
            if v.get('type')=='graph':
                self.graphName=v['name']
                if self.value.get(self.graphName)!=None:
                    self._graph=self.value.get(self.graphName)
        self._variables = variables
        self.__tool=view
        fig_layout = ipywidgets.Layout(width='600px', height='450px')
        self.out=ipywidgets.Output()
        self.variables_view=VariablesView(self.mk_variables())
        if self.__tool=='networkx':
            self.__view=GraphViewNetworkx(self._graph,self.mk_variables(),edgeLabels=edgeLabels, nodeLabels=nodeLabels)
        elif self.__tool=='bqplot':
            self.__view=GraphViewBQPlot(self._graph,self.mk_variables())
        ipywidgets.VBox.__init__(self, [self.__view, self.variables_view], layout=fig_layout)
        self.update()
    
    @property
    def graph(self):  return self._graph
    
    @traitlets.default('value')
    def _default_value(self):
        return {}

    @traitlets.observe('value')
    def _observe_value(self, change):
        self.update()
    
    def mk_variables(self):
        """
            Add values to the list of dict for the view
        """
        var=copy.deepcopy(self._variables)
        for i in range (0,len(self._variables)):
            var[i]['value']=self.value.get(self._variables[i]['name'])
        return var
    
    def update(self):
        """
            Updates both the GraphView and the VariablesView
        """
        if self.value.get(self.graphName)!=None and (self._graph==None or (self.value.get(self.graphName).nodes!=self._graph.nodes or self.value.get(self.graphName).edges!=self._graph.edges)) :
            self.newGraph(self.value.get(self.graphName))
        else: 
            self.__view.update(self.mk_variables())
            self.variables_view.update(self.mk_variables())
    
    def newGraph(self, G):
        """
            Display a new graph
            
            Parameter
            ----------
            G : the new graph
            
        """
        self._graph=G
        var=copy.deepcopy(self._variables)
        for i in range (0,len(self._variables)):
            var[i]['value']=None
        self.__view.newGraph(self._graph, var)