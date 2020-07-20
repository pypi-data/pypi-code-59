# Extention
from .__meta__ import __version__
# from . import readers # tikzParser
from . import writers # parseResult2internalSVG, parseResult2externalSVG
from . import directives
from . import nodes

# class tikzExeption

def setup(app) :
    # app.setup_extention() # Added another extention
    app.add_node(nodes.Tigure,
                 html=(writers.html_writer, None),
                 latex=(writers.latex_writer, None)) # Setup an additional extention 
    app.add_config_value('tikzkit_width',  '400px', 'html')
    app.add_config_value('tikzkit_height', '300px', 'html')
#     app.add_css_file('file.css')
    app.add_directive("tikzkit", directives.Tigure)
    return {'parallel_read_safe' : True,
            'parallel_write_safe': True,
            'version'            : __version__}
    