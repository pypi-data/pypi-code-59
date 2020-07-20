import dominate
from dominate import svg
from dominate.tags import *
from . import readers
from . import nodes
from . import utils

def node2svg(txr, dxv, dom, ast):
    # Attributes
    print(ast.asDict())
    content    = ast.pop("content") if "content" in ast else [""] # Content is already a list of words
    if "cartesian" in ast :
        coordinates = ast.pop("cartesian")
        x, y = coordinates[0]["value"], coordinates[1]["value"]
    elif "polar"   in ast :
        coordinates     = ast.pop("polar")
        a, r = coordinates[0]["value"], coordinates[1]["value"]
    else :
        coordinates = {'cartesian' : [{"value" : 0}, {"value"  : 0}]} # Tikz, uses 0,0 as the default location
        x = y = 0
    paragraph  = utils.paragraph(content)
    # TODO : `content` really should be typeset as a paragraph and the resulting text measured to determine both the width and height of the box before contructing it
    width       = max(map(len,[" ".join(line) for line in paragraph])) + 2*(1) # (node["options"]["inner sep"] or txr.builder.config.tikzkit_inner_sep)
    height      = len(paragraph)                                       + 2*(1) # (node["options"]["inner sep"] or txr.builder.config.tikzkit_inner_sep)
    # The following structure is necessary for the text to appear within a rect
    with dom :
      with svg.g(x=x, y=y):
        svg.rect(width="{}em".format(width), height="{}em".format(height), fill="red") # , stroke="red", stroke_width="3px"
        with svg.svg(width="{}em".format(width), height="{}em".format(height)):
            svg.text(content, text_length=len(content), x="50%", y="50%", dominant_baseline="middle", text_anchor="middle")
        # , font_family = "Verdana", font_size = "35", fill = "blue"
        # ,stroke="black", stroke_width="1px")
        # svg.text(node["content"], text_length=len(" ".join(node['content'])), x="50%", y="50%", dominant_baseline="middle", text_anchor="middle",stroke="red")


def parseResult2internalSVG(translator, directive, ast) :
    """Convert the parse results from the TikZ parser into an SVG element"""
    nodes = {}
    with svg.svg(width=directive.get("width",translator.builder.config.tikzkit_width), height=directive.get("height",translator.builder.config.tikzkit_height)) as image :
#       for path in ast :
#         for node in path :
        node = ast["node"]
        # Label
        if "label" in node :
            nodes[" ".join(node.pop("label"))] = node
        node2svg(translator, directive, image, node)
    return image

def parseResult2externalSVG(ast) :
  """Convert the parse results from the TikZ parser into an SVG document"""

  doc  = dominate.document(title='Dominate your HTML')

  nodes = {}
  with doc.body:
      with svg.svg(width="400px", height="300px") :
          # Produce a node
          if "label" in node :
              nodes[" ".join(node.pop("label"))] = node
          # The following structure is necessary for the text to appear within a rect
          with svg.g(x="150", y="150"):
              svg.rect(width="200", height="50", fill="red") # , stroke="red", stroke_width="3px"
              with svg.svg(width="200", height="50"):
                  svg.text(node["content"], text_length=len(" ".join(node['content'])), x="50%", y="50%", dominant_baseline="middle", text_anchor="middle")
              # , font_family = "Verdana", font_size = "35", fill = "blue"
              # ,stroke="black", stroke_width="1px")
              # svg.text(node["content"], text_length=len(" ".join(node['content'])), x="50%", y="50%", dominant_baseline="middle", text_anchor="middle",stroke="red")

  print(nodes)
  print(doc.render())
  with open("page.html","wt+") as file:
      file.write(doc.render())

  # <svg width="400px" height="300px">
  #   <g transform="translate(50,50)">
  #     <rect rx="5" ry="5" width="200" height="100" stroke="green" fill="none" stroke-width="10"/>
  #     <svg width="200px" height="100px">
  #       <text x="50%" y="50%" alignment-baseline="middle" text-anchor="middle">CORRECT BORDER</text>
  #     </svg>
  #   </g>
  # </svg>

  # <svg width="400px" height="300px" style="border:1px solid black">
  #   <g>
  #     <rect rx="5" ry="5" width="200" height="100" stroke="green" fill="none" stroke-width="10"/>
  #     <text x="50%" y="0%" alignment-baseline="middle" text-anchor="middle">CORRECT BORDER</text>
  #   </g>
  #   <g>
  #     <rect x="0" y="0" width="100" height="100" fill="red"></rect>
  #     <text x="0" y="50" font-family="Verdana" font-size="35" fill="blue">Hello</text>
  #   </g>
  # </svg>

def html_writer(self, node) :
    """Given the graph node"""
    # (self: HTMLTranslator, node: graphviz, code: str, options: Dict, prefix: str = 'graphviz', imgcls: str = None, alt: str = None) -> Tuple[str, str]
    html = parseResult2internalSVG(self, node, readers.tikz.parseString(node["code"]))
    print(html)
    self.body.append((html.render()))
    raise nodes.SkipNode # This tells Sphinx/Docutils to skip this node; It should really return some other node e.g. an SVG node or something similar.

def latex_writer (self, node, code, options, prefix, imgcls, alt) :
    """"""
    # (self: LaTeXTranslator, node: graphviz, code: str, options: Dict, prefix: str = 'graphviz', imgcls: str = None, alt: str = None) -> Tuple[str, str]
#     self.body.append{"\\begin{tikzpicture}"}
    self.body.append(readers.Tigure(node["code"]))
#     self.body.append{"\\end{tikzpicture}"}
