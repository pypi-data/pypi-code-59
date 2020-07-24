import plotly.io as _pio
import plotly.graph_objects as _go
import pandas as _pd
import webcolors as _wc
import re
from ZSAdvancedViz.zscolorscale import colors_scale

class zsadvancedviz:

    def __init__(self):

        _pio.templates["ZS_theme"] = _go.layout.Template(
            #     layout_plot_bgcolor= '#86C8BC',
            #     layout_paper_bgcolor= '#86C8BC',
            layout_font={'family': 'Roboto', 'color': '#53565A'},
            layout_title={
                'text': 'Plot Title',
                'font': {
                    'family': 'Roboto',
                    'color': '#53565A',
                    'size': 20
                },
                # 'x': 0.1,
            },
            layout_xaxis={
                'automargin': True,
                'title': 'x axis title',
                'titlefont_size': 15,
                'titlefont_color': '#83868b',
                'linecolor': '#6600cc',
                'ticks': '',
                'zerolinecolor': '#283442',
                'zerolinewidth': 0,
                'showgrid': False,
                'showline': True,
                'linecolor': "grey",
                'linewidth': 0.5,
                # 'gridcolor': '#283442'
            },
            layout_yaxis={
                'automargin': True,
                'title': 'y axis title',
                'titlefont_size': 15,
                'titlefont_color': '#83868b',
                'linecolor': '#83868b',
                'ticks': '',
                'zerolinecolor': '#283442',
                'zerolinewidth': 0,
                'showgrid': False,
                'showline': True,
                'linecolor': "grey",
                'linewidth': 0.5,
                # 'gridcolor': '#283442'
            },
            layout_colorway=[
                '#86C8BC', '#00629B', '#6E2B62', '#B8CC7B', '#01A6DC', '#A3B2AA', '#A0AFC6', '#B6E880', '#FF97FF',
                '#FECB52'
            ],
            layout_coloraxis={
                'colorbar': {'outlinewidth': 0,
                             'ticks': ''}
            },
            layout_hovermode='closest',
            layout_hoverlabel={'align': 'left',
                               'bgcolor': 'white',
                               'font_size': 13,
                               'font_color': '#53565A',
                               # 'bordercolor':'#86C8BC'
                               },
            layout_legend={
                # 'x': 0,
                # 'y': 1,
                # 'traceorder': "normal",
                # 'font': dict(
                #   family="sans-serif",
                #  size=12,
                #   color="black"
                # ),
                # 'bgcolor':"LightSteelBlue",
                # 'bordercolor':"Black",
                # 'borderwidth':2
            },
            layout_legend_orientation='h'

        )
        self.theme = "ZS_theme"
        # hover template - do define what to show on tooltip
        # plotly_template = _pio.templates["ZS_theme"]
        # plotly_template.layout

    def line_chart(self,
                   data,
                   x_data_col: str,
                   y_data_col: str,
                   chart_attr: dict = {}):
        '''
        This method is used to plot line chart
        :param data: dict of data containing the x_data_col and y_data_col names as keys and its corresponding values in list or pandas data frame of the data.
        dict :
            {'x_data_col_name': ['A','B','C'],
            'y_data_col_name': [10,20,30]}

        ( or )
        pandas data frame :

                x_data_col_name    y_data_col_name
            0           A               10

            1           B               20

            2           C               25

            3           D               30
        :param x_data_col: x_axis column name form the data frame
        :param y_data_col: y_axis column name form the data frame
        :param chart_attr: dict which contains the parameters x_axis_title, y_axis_title, chart_title
                            x_axis_title: title to represent the x_axis. Default value is ""
                            y_axis_title: title to represent the y_axis. Default value is ""
                            chart_title: title to represent the chart. Default value is "Line Chart"
        :return: plotly fig of Line Chart
        '''
        # checks for the data type
        if not isinstance(x_data_col, str):
            raise ValueError("The type of x_data_col is " + str(type(x_data_col)) + ", where as expected type is str")
        if not isinstance(y_data_col, str):
            raise ValueError("The type of y_data_col is " + str(type(y_data_col)) + ", where as expected type is str")
        if not isinstance(chart_attr, dict):
            raise ValueError("The type of chart_attr is " + str(type(chart_attr)) + ", where as expected type is dict")

        fig = _go.Figure(data=_go.Scatter(x=data[x_data_col],
                                          y=data[y_data_col],
                                          mode="markers+lines"),
                         layout=_go.Layout(title=chart_attr.get("chart_title", "Line Chart"),
                                           xaxis={'title': chart_attr.get("x_axis_title", "")},
                                           yaxis={'title': chart_attr.get("y_axis_title", "")},
                                           template=self.theme))

        return fig

    def multiline_chart(self,
                        data,
                        x_data_col: str,
                        y_data_col: list,
                        chart_attr: dict = {},
                        legend_name: list = []):
        '''
        This method is used to plot multiline chart
        :param data: dict of data containing the x_data_col and y_data_col names as keys and its corresponding values in list or pandas data frame of the data.
        dict :
            {'x_data_col_name': ['A','B','C'],
            'y_data_col_name_1': [10,20,30],
            'y_data_col_name_2': [15,10,40],
            'y_data_col_name_3': [20,30,10]}

        ( or )

        pandas data frame :

                x_data_col_name    y_data_col_name_1   y_data_col_name_2
            0           A               10                 15

            1           B               20                 10

            2           C               25                 40

            3           D               30                 20
        :param x_data_col: x_axis column name form the data frame
        :param y_data_col: list of y_axis column names form the data frame
        :param chart_attr: dict which contains the parameters x_axis_title, y_axis_title, chart_title
                            x_axis_title: title to represent the x_axis. Default value is ""
                            y_axis_title: title to represent the y_axis. Default value is ""
                            chart_title: title to represent the chart. Default value is "Line Chart"
        :param legend_name: list of legend names that should be shown on the graph with respect to the y_axis_column names.
                            y_axis_col names are the default legend names
        :return: plotly fig of MultiLine Chart
        '''
        # checks for the data type
        if not isinstance(x_data_col, str):
            raise ValueError("The type of x_data_col is " + str(type(x_data_col)) + ", where as expected type is str")
        if not isinstance(y_data_col, list):
            raise ValueError("The type of y_data_col is " + str(type(y_data_col)) + ", where as expected type is list")
        if not isinstance(chart_attr, dict):
            raise ValueError("The type of chart_attr is " + str(type(chart_attr)) + ", where as expected type is dict")
        if not isinstance(legend_name, list):
            raise ValueError(
                "The type of legend_name is " + str(type(legend_name)) + ", where as expected type is list")

        # initilization of multiline data
        multi_line_data = []
        # iterates each y_axis_column and assigns the scatter and legend
        for index in range(len(y_data_col)):
            # checks the length of legend_name and assigns the column_name to legend
            if len(legend_name) == 0:
                multi_line_data.append(_go.Scatter(x=data[x_data_col],
                                                   y=data[y_data_col[index]],
                                                   mode="markers+lines",
                                                   name=y_data_col[index]))
            # if length of legend_name is greater than the y_axis_col names list then assigns the first n legend names
            elif len(y_data_col) <= len(legend_name):
                multi_line_data.append(_go.Scatter(x=data[x_data_col],
                                                   y=data[y_data_col[index]],
                                                   mode="markers+lines",
                                                   name=legend_name[index]))
            # if legend_names are less tha the y_axis_col names
            elif len(y_data_col) > len(legend_name):
                # assigns legend_name if the length is less than y_axis_col
                if index < len(legend_name):
                    multi_line_data.append(_go.Scatter(x=data[x_data_col],
                                                       y=data[y_data_col[index]],
                                                       mode="markers+lines",
                                                       name=legend_name[index]))
                # assigns the y_axis_col name if the length of legend_name is less
                else:
                    multi_line_data.append(_go.Scatter(x=data[x_data_col],
                                                       y=data[y_data_col[index]],
                                                       mode="markers+lines",
                                                       name=y_data_col[index]))

        fig = _go.Figure(data=multi_line_data,
                         layout=_go.Layout(title=chart_attr.get("chart_title", "MultiLine Chart"),
                                           xaxis={'title': chart_attr.get("x_axis_title", "")},
                                           yaxis={'title': chart_attr.get("y_axis_title", "")},
                                           template=self.theme))

        return fig

    def bar_chart(self,
                  data,
                  x_data_col: str,
                  y_data_col: str,
                  chart_attr: dict = {}):

        '''
        This method is used to plot bar chart
        :param data: dict of data containing the x_data_col and y_data_col names as keys and its corresponding values in list or pandas data frame of the data.
        dict :
            {'x_data_col_name': ['A','B','C'],
            'y_data_col_name_1': [10,20,30]}

        ( or )

        pandas data frame :

                x_data_col_name    y_data_col_name
            0           A               10

            1           B               20

            2           C               25

            3           D               30
        :param x_data_col: x_axis column name form the data frame
        :param y_data_col: y_axis column name form the data frame
        :param chart_attr: dict which contains the parameters x_axis_title, y_axis_title, chart_title
                            x_axis_title: title to represent the x_axis. Default value is ""
                            y_axis_title: title to represent the y_axis. Default value is ""
                            chart_title: title to represent the chart. Default value is "Bar Chart"
        :return: plotly fig of Bar chart
        '''
        # checks for the data type
        if not isinstance(x_data_col, str):
            raise ValueError("The type of x_data_col is " + str(type(x_data_col)) + ", where as expected type is str")
        if not isinstance(y_data_col, str):
            raise ValueError("The type of y_data_col is " + str(type(y_data_col)) + ", where as expected type is str")
        if not isinstance(chart_attr, dict):
            raise ValueError("The type of chart_attr is " + str(type(chart_attr)) + ", where as expected type is dict")

        fig = _go.Figure(data=_go.Bar(x=data[x_data_col],
                                      y=data[y_data_col]),
                         layout=_go.Layout(title=chart_attr.get("chart_title", "Bar Chart"),
                                           xaxis={'title': chart_attr.get("x_axis_title", "")},
                                           yaxis={'title': chart_attr.get("y_axis_title", "")},
                                           template=self.theme))

        return fig

    def multibar_chart(self,
                       data,
                       x_data_col: str,
                       y_data_col: list,
                       chart_attr: dict = {},
                       legend_name: list = [],
                       bar_type: str = "group"):
        '''
        This method is used to plot multi bar chart
        :param data: dict of data containing the x_data_col and y_data_col names as keys and its corresponding values in list or pandas data frame of the data.
        dict :
            {'x_data_col_name': ['A','B','C'],
            'y_data_col_name_1': [10,20,30],
            'y_data_col_name_2': [15,10,40],
            'y_data_col_name_3': [20,30,10]}

        ( or )

        pandas data frame :

                x_data_col_name    y_data_col_name_1   y_data_col_name_2
            0           A               10                 15

            1           B               20                 10

            2           C               25                 40

            3           D               30                 20
        :param x_data_col: x_axis column name form the data frame
        :param y_data_col: list of y_axis column names form the data frame
        :param chart_attr: dict which contains the parameters x_axis_title, y_axis_title, chart_title
                            x_axis_title: title to represent the x_axis. Default value is ""
                            y_axis_title: title to represent the y_axis. Default value is ""
                            chart_title: title to represent the chart. Default value is "Multi Bar Chart"
        :param legend_name: list of legend names that should be shown on the graph with respect to the y_axis_column names.
                            y_axis_col names are the default legend names
        :param bar_type: Determines how bars at the same location coordinate are displayed on the graph.
                         With "stack", the bars are stacked on top of one another.
                         With "relative", the bars are stacked on top of one another, with negative values below the axis, positive values above.
                         With "group", the bars are plotted next to one another centered around the shared location.
                         Default is the "group"
        :return: plotly fig of Multi Bar chart
        '''
        # checks for the data type
        if not isinstance(x_data_col, str):
            raise ValueError("The type of x_data_col is " + str(type(x_data_col)) + ", where as expected type is str")
        if not isinstance(y_data_col, list):
            raise ValueError("The type of y_data_col is " + str(type(y_data_col)) + ", where as expected type is list")
        if not isinstance(chart_attr, dict):
            raise ValueError("The type of chart_attr is " + str(type(chart_attr)) + ", where as expected type is dict")
        if not isinstance(legend_name, list):
            raise ValueError(
                "The type of legend_name is " + str(type(legend_name)) + ", where as expected type is list")
        if not isinstance(bar_type, str):
            raise ValueError("The type of bar_type is " + str(type(bar_type)) + ", where as expected type is str")

        # initilization of multilbar data
        multi_bar_data = []
        # iterates each y_axis_column and assigns the bar and legend
        for index in range(len(y_data_col)):
            # checks the length of legend_name and assigns the column_name to legend
            if len(legend_name) == 0:
                multi_bar_data.append(_go.Bar(x=data[x_data_col],
                                              y=data[y_data_col[index]],
                                              name=y_data_col[index]))
            # if length of legend_name is greater than the y_axis_col names list then assigns the first n legend names
            elif len(y_data_col) <= len(legend_name):
                multi_bar_data.append(_go.Bar(x=data[x_data_col],
                                              y=data[y_data_col[index]],
                                              name=legend_name[index]))
            # if legend_names are less tha the y_axis_col names
            elif len(y_data_col) > len(legend_name):
                # assigns legend_name if the length is less than y_axis_col
                if index < len(legend_name):
                    multi_bar_data.append(_go.Bar(x=data[x_data_col],
                                                  y=data[y_data_col[index]],
                                                  name=legend_name[index]))
                # assigns the y_axis_col name if the length of legend_name is less
                else:
                    multi_bar_data.append(_go.Bar(x=data[x_data_col],
                                                  y=data[y_data_col[index]],
                                                  name=y_data_col[index]))

        fig = _go.Figure(data=multi_bar_data,
                         layout=_go.Layout(barmode=bar_type,
                                           title=chart_attr.get("chart_title", "Multi Bar Chart"),
                                           xaxis={'title': chart_attr.get("x_axis_title", "")},
                                           yaxis={'title': chart_attr.get("y_axis_title", "")},
                                           template=self.theme))

        return fig

    def pie_chart(self,
                  data,
                  label_col: str,
                  value_col: str,
                  chart_attr: dict = {}):
        '''
        This method is used to plot pie chart
        :param data: dict of data containing the x_data_col and y_data_col names as keys and its corresponding values in list or pandas data frame of the data.
        dict :
            {'label_col_name': ['A','B','C'],
            'value_col_name': [10,20,30]}

        ( or )

        pandas data frame :

                label_col_name    value_col_name
            0           A               10

            1           B               20

            2           C               25

            3           D               30
        :param label_col: label column name form the data frame
        :param value_col: value column name form the data frame
        :param chart_attr: dict which contains the parameters x_axis_title, y_axis_title, chart_title
                            chart_title: title to represent the chart. Default value is "Multi Bar Chart"
        :return: plotly fig of pie chart
        '''
        # checks for the data type
        if not isinstance(label_col, str):
            raise ValueError("The type of label_col is " + str(type(label_col)) + ", where as expected type is str")
        if not isinstance(value_col, str):
            raise ValueError("The type of value_col is " + str(type(value_col)) + ", where as expected type is str")
        if not isinstance(chart_attr, dict):
            raise ValueError("The type of chart_attr is " + str(type(chart_attr)) + ", where as expected type is dict")

        fig = _go.Figure(data=_go.Pie(labels=data[label_col],
                                      values=data[value_col],
                                      textposition='none',  # ( "inside" | "outside" | "auto" | "none" )
                                      textinfo="none",
                                      # "label", "text", "value", "percent" joined with a "+" OR "none".
                                      ),
                         layout=_go.Layout(title=chart_attr.get("chart_title", "Pie Chart"),
                                           template=self.theme))

        return fig

    def donut_chart(self,
                    data,
                    label_col: str,
                    value_col: str,
                    hole_value: float = 0.3,
                    chart_attr: dict = {}):
        '''
        This method is used to plot donut chart
        :param data: dict of data containing the x_data_col and y_data_col names as keys and its corresponding values in list or pandas data frame of the data.
        dict :
            {'label_col_name': ['A','B','C'],
            'value_col_name': [10,20,30]}

        ( or )

        pandas data frame :

                label_col_name    value_col_name
            0           A               10

            1           B               20

            2           C               25

            3           D               30
        :param label_col: label column name form the data frame
        :param value_col: value column name form the data frame
        :param hole_value: number between 0 and 1
                            Default: 0.3
                            Sets the fraction of the radius to cut.
        :param chart_attr: dict which contains the parameters x_axis_title, y_axis_title, chart_title
                            chart_title: title to represent the chart. Default value is "Multi Bar Chart"
        :return: plotly fig of donut chart
        '''
        # checks for the data type
        if not isinstance(label_col, str):
            raise ValueError("The type of label_col is " + str(type(label_col)) + ", where as expected type is str")
        if not isinstance(value_col, str):
            raise ValueError("The type of value_col is " + str(type(value_col)) + ", where as expected type is str")
        if not isinstance(hole_value, float):
            raise ValueError("The type of hole_value is " + str(type(hole_value)) + ", where as expected type is float")
        if not isinstance(chart_attr, dict):
            raise ValueError("The type of chart_attr is " + str(type(chart_attr)) + ", where as expected type is dict")

        fig = _go.Figure(data=_go.Pie(labels=data[label_col],
                                      values=data[value_col],
                                      textposition='none',  # ( "inside" | "outside" | "auto" | "none" )
                                      textinfo="none",
                                      # "label", "text", "value", "percent" joined with a "+" OR "none".
                                      hole=hole_value
                                      ),
                         layout=_go.Layout(title=chart_attr.get("chart_title", "Donut Chart"),
                                           template=self.theme))

        return fig

    def sankey_chart(self,
                     data,
                     source_column: str,
                     target_column: str,
                     value_column: str,
                     label_column: str = "",
                     valuesuffix: str = "",
                     decimal_points: int = 2,
                     chart_attr: dict = {}):
        """
        This method is used to plot sankey chart
        :param data: pandas data frame of the data which is used to plot the graph.
        One can refer the below data frame for the reference of the data that to be passed.

                  Source    Target     Value      Label(optional)
            0     AB          EF      20.007243    Line 1

            1     CD          GH      12           Line 2

            2     AB          GH      5.001095     Line 3

            3     HI          JK      0.063865     Line 4

            4     HI          EF      0.005332     Line 5
        :param source_column: source column name from the data frame
        :param target_column: target column name from the data frame
        :param value_column: value column name from the data frame
        :param label_column: label column name from the data frame. This value is shown on the hover of the links in the graph.
                            Default is "". It shows empty label
        :param valuesuffix: suffix will be appended to the value in the graph.
                            Default is "".
        :param decimal_points: Number of decimal points to be shown in the graph.
                               Default is 2. it shows 2 digits after the decimals.
        :param chart_attr: dict which contains the parameters x_axis_title, y_axis_title, chart_title
                            chart_title: title to represent the chart. Default value is "Sankey Chart"
        :return: plotly fig of sankey chart
        """
        # checks for the data type
        if not isinstance(data, _pd.core.frame.DataFrame):
            raise ValueError("The type of data is " + str(type(data)) + ". Where as expected pandas dataframe")
        if not isinstance(source_column, str):
            raise ValueError(
                "The type of source_column is " + str(type(source_column)) + ", where as expected type is str")
        if not isinstance(target_column, str):
            raise ValueError(
                "The type of target_column is " + str(type(target_column)) + ", where as expected type is str")
        if not isinstance(value_column, str):
            raise ValueError(
                "The type of value_column is " + str(type(value_column)) + ", where as expected type is str")
        if not isinstance(label_column, str):
            raise ValueError(
                "The type of label_column is " + str(type(label_column)) + ", where as expected type is str")
        if not isinstance(decimal_points, int):
            raise ValueError(
                "The type of decimal_points is " + str(type(decimal_points)) + ", where as expected type is int")
        if not isinstance(chart_attr, dict):
            raise ValueError("The type of chart_attr is " + str(type(chart_attr)) + ", where as expected type is dict")

        label_data = []
        # appends the empty label
        if len(label_column) == 0:
            for a in data[source_column]:
                label_data.append("")
        else:
            label_data = data[label_column]

        # appends source_data, target_data and clears the duplicate values
        node_label = list(set(data[source_column]))
        node_label.extend(list(set(data[target_column])))
        node_label = list(set(node_label))

        source = []
        target = []

        # creates the sankey required source data from node_label
        for source_value in data[source_column]:
            for a in range(len(node_label)):
                if source_value == node_label[a]:
                    source.append(a)

        # creates the sankey required target data from node_label
        for target_value in data[target_column]:
            for a in range(len(node_label)):
                if target_value == node_label[a]:
                    target.append(a)

        # color_scale from zs_theme_colors
        colors = colors_scale(node_label)

        # creates the colors that to be given to links between source and target
        # reduces the alpha of rgba by 0.25 in each color
        # generates the colors with less alpha to colors which are given to source
        # re.search(r"(1)\)|0.([0-9]*)\)" - searces for the alpha which starts with either 1 or 0. in rgba
        # .group(0).split(")")[0] - splits the alpha value into the number
        link_color = [
            colors[src].replace(", " + re.search(r"(1)\)|0.([0-9]*)\)", colors[src]).group(0).split(")")[0] + ")",
                                ", " + str(round(
                                    float(re.search(r"(1)\)|0.([0-9]*)\)", colors[src]).group(0).split(")")[0]) - 0.25,
                                    3)) + ")") for src in source]

        fig = _go.Figure(data=[_go.Sankey(
            valueformat="." + str(decimal_points) + "f",  # ".2f"
            valuesuffix=valuesuffix,  # " $"
            orientation="h",  ### h/v
            # Define nodes
            node=dict(
                pad=5,
                thickness=15,
                line=dict(color="grey", width=0.1),
                label=node_label,
                color=colors
            ),
            # Add links
            link=dict(
                line=dict(color="grey", width=0.2),
                source=source,
                target=target,
                value=data[value_column],
                label=label_data,
                color=link_color
            ),
        )])

        fig.update_layout(title_text=chart_attr.get("chart_title", "Sankey Chart"),
                          template=self.theme)

        return fig

    def bitmap(self,
               data,
               x_axis_order_list: list,
               x_axis_column: str,
               y_axis_column: str,
               values_data_column: str,
               intensity_column: str = "",
               config_data={},
               color_column: str = "color",
               symbols_column: str = "symbol",
               values_data_config_column: str = "value",
               chart_attr: dict = {}):

        """
        This method is used to plot Bit Map chart
        :param data: pandas data frame of the data which is used to plot the graph.
        One can refer the below data frame for the reference of the data that to be passed.

                y_axis_label    Value    x_axis_label    Intensity
            0   Patient 1         AR           M-1            1

            1   Patient 1         MR           Start          3

            2   Patient 1         GR           M 1            2

            3   Patient 2         AR           M-2            1

            4   Patient 2         GR           Start          2

            5   Patient 3         GR           M-8            3

            6   Patient 3         AR           M-7            1

            7   Patient 3         MR           M 2            2
        :param x_axis_order_list: list of x_axis values in an order that should be shown on the garph.
                                  As per the above data frame the the x_axis labels can be arranged in random manner on the x_axis.
                                  To have an arranged order of x_axis, pass the list of values in an order that to be represented on x_axis.
                                  i.e. ['M-8','M-7','M-2','M-1','Start','M 1','M 2']

        :param x_axis_column: x_axis column name form the data frame
        :param y_axis_column: y_axis column name form the data frame
        :param values_data_column: value column name form the data frame of the data point (x,y)
        :param config_data: pandas data frame of the config file which is used to assign the symbol and color for each value
        One can refer the below data frame for the reference. Color code should be in HEX

                value    symbol    color
            0   AR       0         #00ffff

            1   MR       1         #000000

            2   GR       2         #0000ff
        symbol accepts only numbers from the list: [0,1,2,3,4,5,17,18,19,21,22,23,33,34,35,100,101,102,105,117,118]
        :param color_column: color column name from the config data frame. Default value is "color"
        :param symbols_column: symbol column name from the config data frame. Default value is "symbol"
        :param values_data_config_column: value column name from the config data frame. Default vaue is "value"
        :param intensity_column: Intensity column name from the data frame to represent in the graph
                                 Assign 1- High, 2- Medium, 3- Low in the data frame and pass the column of intensity
                                 Accepts only above integers as the value. If the intensity column is not provided, Default is 1-High.
        :param chart_attr: dict which contains the parameters x_axis_title, y_axis_title, chart_title
                            chart_title: title to represent the chart. Default value is "Bit Map"
        :return: plotly fig of bit map
        """

        zs_symbols = [0, 1, 2, 3, 4, 5, 17, 18, 19, 21, 22, 23, 33, 34, 35, 100, 101, 102, 105, 117, 118]

        zs_colors = ["rgba(0, 98, 155, 1)", "rgba(1, 166, 220, 1)", "rgba(110, 43, 98, 1)", "rgba(134, 200, 188, 1)",
                     "rgba(160, 175, 198, 1)", "rgba(163, 178, 170, 1)", "rgba(182, 232, 128, 1)",
                     "rgba(184, 204, 123, 1)",
                     "rgba(254, 203, 82, 1)", "rgba(255, 151, 255, 1)", "rgba(99, 110, 250, 1)", "rgba(239, 85, 59, 1)",
                     "rgba(0, 204, 150, 1)", "rgba(171, 99, 250, 1)", "rgba(255, 161, 90, 1)", "rgba(25, 211, 243, 1)",
                     "rgba(255, 102, 146, 1)", "rgba(182, 232, 128, 1)", "rgba(255, 151, 255, 1)",
                     "rgba(254, 203, 82, 1)"]

        # checks for the data type
        if not isinstance(data, _pd.core.frame.DataFrame):
            raise ValueError("The type of data is " + str(type(data)) + ". Where as expected pandas dataframe")
        if not isinstance(x_axis_order_list, list):
            raise ValueError(
                "The type of x_axis_order_list is " + str(type(x_axis_order_list)) + ", where as expected type is list")
        if not isinstance(x_axis_column, str):
            raise ValueError(
                "The type of x_axis_column is " + str(type(x_axis_column)) + ", where as expected type is str")
        if not isinstance(y_axis_column, str):
            raise ValueError(
                "The type of y_axis_column is " + str(type(y_axis_column)) + ", where as expected type is str")
        if not isinstance(values_data_column, str):
            raise ValueError("The type of values_data_column is " + str(
                type(values_data_column)) + ", where as expected type is str")
        if not isinstance(intensity_column, str):
            raise ValueError(
                "The type of intensity_column is " + str(type(intensity_column)) + ", where as expected type is str")
        if not isinstance(color_column, str):
            raise ValueError(
                "The type of color_column is " + str(type(color_column)) + ", where as expected type is str")
        if not isinstance(symbols_column, str):
            raise ValueError(
                "The type of symbols_column is " + str(type(symbols_column)) + ", where as expected type is str")
        if not isinstance(values_data_config_column, str):
            raise ValueError("The type of values_data_config_column is " + str(
                type(values_data_config_column)) + ", where as expected type is str")
        if not isinstance(chart_attr, dict):
            raise ValueError("The type of chart_attr is " + str(type(chart_attr)) + ", where as expected type is dict")

        # fill the NaN with empty string
        pandas_dataframe = data.fillna('')

        x_axis_order_list = x_axis_order_list
        y_axis_data_column_name = y_axis_column
        x_axis_data_column_name = x_axis_column
        values_data_column_name = values_data_column
        color_intensity_column_name = intensity_column

        values_data_config_column_name = values_data_config_column
        symbols_column_name = symbols_column
        color_column_name = color_column

        if len(config_data) != 0:
            # checks for the data type
            if not isinstance(config_data, _pd.core.frame.DataFrame):
                raise ValueError(
                    "The type of config_data is " + str(type(config_data)) + ". Where as expected pandas dataframe")
            # checks for the existing of column in config data frame
            else:
                if values_data_config_column_name not in list(config_data.columns):
                    raise ValueError(
                        "The column name: " + values_data_config_column_name + " is not present in the given config data.")
                elif symbols_column_name not in list(config_data.columns):
                    raise ValueError(
                        "The column name: " + symbols_column_name + " is not present in the given config data.")
                elif color_column_name not in list(config_data.columns):
                    raise ValueError(
                        "The column name: " + color_column_name + " is not present in the given config data.")

        # initilization of config_data
        pandas_dataframe_1 = {}

        if len(config_data) != 0:
            # fill the NaN with empty string
            pandas_dataframe_1 = config_data.fillna('')

            # checks wheter the values are repeated in config data
            if len(list(pandas_dataframe_1[values_data_config_column_name])) != len(
                    set(pandas_dataframe_1[values_data_config_column_name])):
                raise ValueError(
                    "Data in column: " + values_data_config_column_name + " is repeated. Place unique values in this column")

            # checks whether there is any empty value present in symbols
            if '' in list(pandas_dataframe_1[symbols_column_name]):
                raise ValueError("There is an empty value in the " + symbols_column_name + " column")
            # checks whether the type of value in symbol column is int
            elif str(pandas_dataframe_1[symbols_column_name].dtypes) != 'int64':
                for symbol in list(pandas_dataframe_1[symbols_column_name]):
                    if not isinstance(symbol, int):
                        raise ValueError("There is an invalid data: " + str(
                            symbol) + " in the column: " + symbols_column_name + ". Expected only integers from list " + str(
                            zs_symbols))
            # checks whether the type of value in symbol column is int
            elif str(pandas_dataframe_1[symbols_column_name].dtypes) == 'int64':
                # iterates each symbol and checks whether the number is valid
                for symbol in list(pandas_dataframe_1[symbols_column_name]):
                    if symbol not in zs_symbols:
                        raise ValueError("Given symbol number: " + str(
                            symbol) + " is invalid. choose the symbol number from symbols list " + str(zs_symbols))

            # hex colors from config data
            hex_colors_list = list(pandas_dataframe_1[color_column_name])
            rgb_colors_list = []

            # iterates each hex color and converts it into rgba
            for hex_color in hex_colors_list:
                # checks for the valid hex color code
                if re.match(r'^[#][0-9A-Za-z]{6}$', str(hex_color)):
                    rgb_colors_list.append(
                        str(_wc.hex_to_rgb(str(hex_color))).replace("IntegerRGB", "rgba").replace("red=", "").replace(
                            "green=", "").replace("blue=", "").replace(")", ", 1)"))
                else:
                    raise ValueError(
                        "Entered wrong Hex code: " + str(hex_color) + " in the data. Enter the correct hex code")

            # appends the rgba column to the config data frame
            updated_rgba_color_df = _pd.DataFrame({color_column_name: rgb_colors_list})
            pandas_dataframe_1[color_column_name] = updated_rgba_color_df

        else:
            # initialising the config data
            config_data_dict = {}

            # list of unique values in ascending order
            unique_values_list = list(set(pandas_dataframe[values_data_column_name]))
            unique_values_list.sort()

            # updates the config_data with values list
            config_data_dict.update({values_data_config_column_name: unique_values_list})
            # colors and symbols initiulization
            pre_colors = []
            pre_symbols = []
            # counters initilization
            color_counter = 0
            symbol_counter = 0
            # iterates each value and assign the color and symbol form default symbols and colors
            for value in unique_values_list:
                # if counter is greater than the length of existing colors then it resets the counter and assigns the colors in repeating mode
                if color_counter >= (len(zs_colors) - 1):
                    color_counter = 0
                    pre_colors.append(zs_colors[color_counter])
                    color_counter += 1
                else:
                    pre_colors.append(zs_colors[color_counter])
                    color_counter += 1
                # if counter is greater than the length of existing symbols then it resets the counter and assigns the symbols in repeating mode
                if symbol_counter >= (len(zs_symbols) - 1):
                    symbol_counter = 0
                    pre_symbols.append(zs_symbols[symbol_counter])
                    symbol_counter += 1
                else:
                    pre_symbols.append(zs_symbols[symbol_counter])
                    symbol_counter += 1
            # updates config_data and converts to pandas data frame
            config_data_dict.update({symbols_column_name: pre_symbols, color_column_name: pre_colors})
            pandas_dataframe_1 = _pd.DataFrame(config_data_dict)

        # list of unique y_axis data
        unique_y_axis_params = list(set(pandas_dataframe[y_axis_data_column_name]))
        unique_y_axis_params.sort()

        y_axis_data = []
        x_axis_data = []
        symbols = []
        colors = []
        text_list = []

        # iterates each value in y_axis params
        for y_axis_param in unique_y_axis_params:
            # fetches the data of y_axis param from whole data
            y_axis_param_data = pandas_dataframe.loc[pandas_dataframe[y_axis_data_column_name] == y_axis_param]
            # iterates each value in x_axis order
            for x_axis_order_param in x_axis_order_list:
                # fetches the data of x_axis param from y_axis param data
                y_axis_detail_param_data = y_axis_param_data.loc[
                    y_axis_param_data[x_axis_data_column_name] == x_axis_order_param]
                # check for empty data set
                if len(y_axis_detail_param_data) == 0:
                    y_axis_data.append(y_axis_param)
                    x_axis_data.append(x_axis_order_param)
                    # open circle is assigned
                    symbols.append(100)
                    # white doesn't appear on graph
                    colors.append("white")
                    # no text is shown
                    text_list.append("")
                else:
                    y_axis_data.append(y_axis_param)
                    x_axis_data.append(x_axis_order_param)
                    # fetches the data of the value form config data
                    config_data_of_value = pandas_dataframe_1.loc[pandas_dataframe_1[values_data_config_column_name] ==
                                                                  list(y_axis_detail_param_data[
                                                                           values_data_column_name])[0]]
                    # fetches the assigned symbol for the value
                    symbols.append(list(config_data_of_value[symbols_column_name])[0])
                    # checks whether the user provided the intensity column
                    if color_intensity_column_name != "":
                        # checks whether the given intensity is correct
                        # 1- High, 2- Medium, 3- Low
                        if list(y_axis_detail_param_data[color_intensity_column_name])[0] in [1, 2, 3]:
                            if list(y_axis_detail_param_data[color_intensity_column_name])[0] == 1:
                                colors.append(list(config_data_of_value[color_column_name])[0])
                                # text list to show on the hover
                                text_list.append("value: " + str(
                                    list(y_axis_detail_param_data[values_data_column_name])[
                                        0]) + "<br>Intensity: 1-High")

                            elif list(y_axis_detail_param_data[color_intensity_column_name])[0] == 2:
                                medium_intensity_color = list(config_data_of_value[color_column_name])[0].replace(" 1)",( " " + str(0.7) + ")"))
                                colors.append(medium_intensity_color)
                                # text list to show on the hover
                                text_list.append("value: " + str(
                                    list(y_axis_detail_param_data[values_data_column_name])[
                                        0]) + "<br>Intensity: 2-Medium")

                            elif list(y_axis_detail_param_data[color_intensity_column_name])[0] == 3:
                                low_intensity_color = list(config_data_of_value[color_column_name])[0].replace(" 1)", (
                                        " " + str(0.4) + ")"))
                                colors.append(low_intensity_color)
                                # text list to show on the hover
                                text_list.append("value: " + str(
                                    list(y_axis_detail_param_data[values_data_column_name])[
                                        0]) + "<br>Intensity: 3-Low")
                        # considering high if intensity is left blank/empty
                        elif list(y_axis_detail_param_data[color_intensity_column_name])[0] == "":
                            colors.append(list(config_data_of_value[color_column_name])[0])
                            # text list to show on the hover
                            text_list.append("value: " + str(
                                list(y_axis_detail_param_data[values_data_column_name])[0]) + "<br>Intensity: 1-High")

                        # raise exception if value is other than 1,2,3
                        else:
                            raise ValueError("The Intensity: " + str(
                                list(y_axis_detail_param_data[color_intensity_column_name])[
                                    0]) + " is invalid. Enter 1 -High, 2 -Medium, 3 -Low")
                    else:
                        colors.append(list(config_data_of_value[color_column_name])[0])
                        # text list to show on the hover
                        text_list.append("value: " + str(list(y_axis_detail_param_data[values_data_column_name])[0]))

        fig = _go.Figure(_go.Scatter(mode="markers",
                                     x=x_axis_data,
                                     y=y_axis_data,
                                     marker_symbol=symbols,
                                     marker_line_color=colors,
                                     marker_color=colors,
                                     marker_line_width=1.5,
                                     marker_size=10,
                                     text=text_list
                                     ))
        fig.update_layout(title=chart_attr.get("chart_title", "Bit Map"),
                          template=self.theme)

        return fig


zsgraph_objects = zsadvancedviz()
