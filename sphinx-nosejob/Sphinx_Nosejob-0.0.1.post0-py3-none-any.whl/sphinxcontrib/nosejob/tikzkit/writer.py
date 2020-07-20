import dominate
from dominate import svg
from dominate.tags import *

def parseResult2internalSVG(result) :
  """Convert the parse results from the TikZ parser into an SVG element"""

def parseResult2externalSVG(result) :
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

