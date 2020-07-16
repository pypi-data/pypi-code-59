import plotly.graph_objects as go

def get_angle(measurement, p1, p2, p3, line_color):
    
    midpoint = p2

    triangle = go.Mesh3d(x=[p1[0],p2[0],p3[0]],
                         y=[p1[1],p2[1],p3[1]],
                         z=[p1[2],p2[2],p3[2]],
                         alphahull = 0,
                         opacity = 1, 
                         color="lightpink")

    # label = go.Scatter3d(x=[midpoint[0]], y=[midpoint[1]], z=[midpoint[2]], 
    #                     mode="text",
    #                     text=measurement,
    #                     textposition="middle center")
     
#    figure.add_trace(label)
    return triangle
#    figure.add_trace(triangle)


def get_line(measurement, p1, p2, line_width, line_color):

    midpoint = (p1 + p2)/2

    line = go.Scatter3d(x=[p1[0], p2[0]],y=[p1[1],p2[1]],z=[p1[2],p2[2]], 
                        mode="lines",
                        line={"width": line_width,
                              "color": line_color, 
                              "dash" : "dashdot"},
                        )
    # label = go.Scatter3d(x=[midpoint[0]], y=[midpoint[1]], z=[midpoint[2]], 
    #                     mode="text",
    #                     text=measurement,
    #                     textposition="middle center")
    #figure.add_trace(line)
    # figure.add_trace(label)

    return line