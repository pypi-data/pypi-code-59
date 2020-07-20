# Docutils
from docutils.parsers.rst import directives
# Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes    import set_source_info
# Extention
from . import nodes
from . import utils

def figure_wrapper(directive, node, caption = None, alignment = None) :
    """
    Note :
    
        This is adapted from the `sphinx.ext.grphviz` figure wrapper.
    """
    figure = nodes.figure('', node)
    if alignment:
        figure['align'] = alignment
    if caption :
        inodes, messages = directive.state.inline_text(caption, directive.lineno)
        caption = nodes.caption(caption, '', *inodes)
        caption.extend(messages)
        set_source_info(directive, caption)
        figure += caption
    return figure


class Tigure(SphinxDirective):
    # Presenty inheriting sphinx.util.docutil.SphinxDirective; should also consider docutils.parsers.rst.Directive
    # Arguments : (name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
    """
    Run when the inheritance_diagram directive is first encountered.
    """

    has_content = True                  #: Sets whether or not the directive can have an indented block of content
    required_arguments = 0              #: Controls whether or not the directive has any required arguments `.. DIRECTIVE:: ARGUMENT(S)`
    optional_arguments = 1              #: Controls whether or not the directive has any optional arguments `.. DIRECTIVE:: [ARGUMENT(S)]`
    final_argument_whitespace = True    #: Not entirely sure to be honest

    option_spec = {
#         'parts': int,
#         'private-bases': directives.flag,
        'caption': directives.unchanged,
        'width' : directives.unchanged_required,
        'height': directives.unchanged_required,
    }

    def run(self) :
        """Replace the directive with a TikzFigure in the output"""
        node = nodes.Tigure()
        node["code"] = '\n'.join(self.content) # Code appears to be conventional in Sphinx/Docutils
        node["width"]  = self.options.get("width",  "400")
        node["height"] = self.options.get("height", "300")
        figure_wrapper(self, node, 
            caption = self.options.get("caption", None), 
            alignment = self.options.get("align", None))
#         node['options'] = {}
#         node['options']["caption"] = self.options.get("caption", None)
#         node['options']["align"]   = self.options.get("caption", None)
#         node['options']["align"]   = self.options.get("caption", None)
        return [node]
