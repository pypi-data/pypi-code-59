import ipywidgets

class VariablesView(ipywidgets.GridBox):
    """
        Display some variables' names and their values in a GridBox
    """
    def __init__(self, variables):
        """
            Initialization
        """
        self._variable_views={}
        variables_boxes = []
        for v in variables:
            if v.get('display')==True:
                label  = ipywidgets.Label(v['name'])
                output = ipywidgets.Label(value='')
                self._variable_views[v['name']] = output
                variables_boxes.extend([label, output])
        ipywidgets.GridBox.__init__(self,variables_boxes, layout = ipywidgets.Layout(grid_template_columns='1fr 1fr'))
    
    def update(self, variables):
        """
            Update the values
        """
        for variable in variables:
            if variable.get('display')==True:
                name  = variable['name']
                value = variable['value']
                output = self._variable_views[name]
                if value is not None:
                    output.value=str(value)
                else:
                    output.value=""