# Copyright (c) 2019 Jonathan Sambrook and Codethink Ltd.
#
#    This file is part of Topplot.
#
#    Topplot is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Topplot is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Topplot.  If not, see <https://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
#
# TODO:  'x)' indicates implemented/fixed
#        'W)' indicates (probably) won't fix
#        'L)' indicates problem with mpl (or other library) that might (?) be looked upon favourably by upstream
#        '*)' indicates remains outstanding
#        '?)' indicates brain(storm|fart)
#
#       ?) Mouseover POI menu for process info
#          Attach enter/leave events to all POI graph legend text artists
#          Only these don't exist...  so look in to "motion_notify_event" for the fig's canvas?
#          Enter sets of a timer-with-closure which if not cancelled by the Leave event, would track down info from
#          from the topplot file's process dict (needs to be made accessible from here) and display it.
#
#       ?) Single one-to-many legend for multi-core figures
#
#       L) mpl Legend should either toggle marker visibility when line visibility is toggled, or have get_markers() as a parallel to get_lines() and get_texts()
#       L) mpl Legend should have get_title_text() to allow picking it without skirting the API
#       L) mpl Legend dragging would be better if it was right button only
#       L) mpl Legends dragged and left over different subplots lose interactivity, including being able to be dragged
#       L) mpl events could/should be consumeable according to return value of callback
#
# -----------------------------------------------------------------------------
# Grapher has one or more FigManagers.
# FigManager has one figure with one or more plots/subplots and implements per-figure functionality.
# Grapher constructs figures, plots the data, and performs supra-FigManager functions too.
# -----------------------------------------------------------------------------

import math
import re
import shutil
import subprocess
import sys
import tkinter as tk

import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from topplot_ import FigManager
from topplot_ import LineStyler
from topplot_ import die, get_curr_screen_dimensions

try:
    import mplcursors

    mplcursors_present = True
except ImportError:
    print(
        "The mplcursors Python module is not installed, so annotations are not available. Hint: pip3 install mplcursors"
    )
    mplcursors_present = False

# -----------------------------------------------------------------------------
# Select GUI toolkit

mpl.use("TKAgg")

# -----------------------------------------------------------------------------
# Add mplcursors annotation capability for the given axis' lines, if available.


def add_annotations(figman, ax):
    if "mplcursors" in sys.modules:
        c = mplcursors.Cursor(hover=False, multiple=True, artists=tuple(ax.get_lines()))

        # At the time of writing (mpl 3.1.0) mpl doesn't allow consuming of gui events, so they're propogated to all hooks.
        # Which means that mplcursors annotations are triggered even when they are underneath legends.
        # This on_add closure callback fixes that situation.
        def on_add(sel):
            # Convert from data co-ords to display co-ords
            x, y = ax.transData.transform(tuple(sel.target))

            # Cycle through axes' legends checking for hits
            fake_event = mpl.backend_bases.MouseEvent("dummy", figman.fig.canvas, x, y)

            for legend in figman.get_legends():
                result, _ = legend.contains(fake_event)

                # Remove sel on hit
                if result:
                    c.remove_selection(sel)

        c.connect("add", on_add)


# -----------------------------------------------------------------------------
# Customize MatPlotLib rcParams for topplot


def override_rcParams():
    mpl.rcParams["legend.facecolor"] = "white"  # Doesn't work
    mpl.rcParams["legend.fancybox"] = True
    mpl.rcParams["legend.shadow"] = True
    # Disable keystrokes for toggling log scales
    mpl.rcParams["keymap.xscale"] = []
    mpl.rcParams["keymap.yscale"] = []


# -----------------------------------------------------------------------------
# Dump MatPlotLib rcParams


def rcParams():
    # Override defaults
    override_rcParams()

    # Dump state
    for k, v in mpl.rcParams.items():
        print(f"mpl.rcParams['{k}'] = {v}")


# -----------------------------------------------------------------------------
# Turn on H:M:S date format for the given axis


def set_x_axis_time_formatting(ax):
    ax.xaxis.axis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))


# -----------------------------------------------------------------------------
# Class to encapsulate the graphing side of topplot


class Grapher:

    # -------------------------------------------------------------------------

    def __init__(self, graph_map, args, cores, mem_unit, mem_cached_or_available):
        self.args = args
        self.cores = cores
        self.mem_unit = mem_unit
        self.graph_map = graph_map

        self.display_legends = True

        self.linestyler = LineStyler()

        self.fig_manager = {"overview": None, "cpu_by_cpu": None, "poi_by_cpu": None}

        self.mem_cached_or_available = mem_cached_or_available.replace("_", " ")
        self.mplcursors_present = mplcursors_present

        self.colours = {
            "combined": "red",
            "poi_cpu": "red",
            "poi_mem": "blue",
            "user": "green",
            "system": "red",
            "nice": "blue",
            "idle": (0.3, 0.3, 0.3),
            "wait": "black",
            "hw irq": "orange",
            "sw irq": "cyan",
            "steal": "gray",
            "exec": "chartreuse",
            "task running": "green",
            "task sleeping": "blue",
            "task stopped": "red",
            "task zombie": "black",
            "mem used": "blue",
            "mem free": "green",
            "mem buffers": "pink",
            self.mem_cached_or_available: "green",
            "swap free": "purple",
            "load average": "purple",
            "fig_face": (0.95, 0.95, 0.90),
        }

        self.markers = {
            "user": "$u$",
            "system": "$s$",
            "nice": "$n$",
            "idle": "$i$",
            "wait": "$w$",
            "hw irq": "$hw$",
            "sw irq": "$sw$",
            "steal": "$st$",
            "exec": "$x$",
        }

        if cores > 1:
            for core in range(cores):
                tmp = {}
                for (k, v) in self.markers.items():
                    tmp[f"{core}{k}"] = f"{v}{core}"
                if len(tmp):
                    self.markers.update(tmp)

        self.cartesian_map = [[None, None], [None, None]]

    # -------------------------------------------------------------------------
    # Convert from four-by-one array index to two-by-two array index

    def ordinal_to_cartesian_map(self, n):
        x = int(n / 2)
        y = n % 2
        return self.cartesian_map[x][y]

    # -------------------------------------------------------------------------
    # Apply the relevant style to the lines on the given axis/axes

    def style_lines(self, *axes):
        legends = []
        for ax in axes:
            prefix = ""
            label = ax.get_yaxis().get_label().get_text()
            if label is not None:
                prefix = label
            for line in ax.get_lines():
                self.linestyler.style(prefix + line.get_label(), line)

    # -------------------------------------------------------------------------
    # Common title formatting

    def title(self, str):
        return f"topplot : {self.args.toplog_filename} : {str}"

    # -------------------------------------------------------------------------
    # Styles for any/all axes

    def common_axes(self, figman, ax):
        ax.set_facecolor("white")
        ax.margins(0)
        ax.set_xlabel("")
        set_x_axis_time_formatting(ax)
        add_annotations(figman, ax)

    # -------------------------------------------------------------------------
    # Styles for 'primary' axes

    def common_ax1(self, figman, ax):
        self.common_axes(figman, ax)
        ax.grid(linestyle=":", linewidth="0.5", color="black", alpha=0.5)

    # -------------------------------------------------------------------------
    # Styles for 'secondary' axes

    def common_ax2(self, figman, ax):
        self.common_axes(figman, ax)
        ax.grid(linestyle="--", linewidth="0.5", color="black", alpha=0.75)

    # -------------------------------------------------------------------------
    # Map legend lines to plotted lines
    # An mpl API workaround is required

    def pickable_legend_lines(
        self, figman, legend, ax1, ax2=None, len1=None, *, otm=False
    ):
        leglines = legend.get_lines()
        legtexts = legend.get_texts()

        # WARNING: going off mpl API here to get the legend's handles
        leghandles = legend.legendHandles

        # WARNING: going off mpl API here to access the artist of the legend's title box
        title = legend._legend_title_box._text

        if len1 is None:
            len1 = len(ax1.get_lines())

        if len1 > 0:
            figman.map_legend_lines(
                ax1,
                title,
                leglines=leglines[:len1],
                legtexts=legtexts[:len1],
                leghandles=leghandles[:len1],
            )

        if ax2 is not None:
            figman.map_legend_lines(
                ax2,
                title,
                leglines=leglines[len1:],
                legtexts=legtexts[len1:],
                leghandles=leghandles[len1:],
            )

    # -------------------------------------------------------------------------
    # Produce a legend for a single axis

    def single_legend(self, figman, title, legtitle, ax_ylabel, ax, *, cap=None):
        # Set furniture text
        ax.set_title(title)
        ax.set_ylabel(ax_ylabel)

        # Get legend lines ready
        handles, labels = ax.get_legend_handles_labels()

        if cap is not None:
            handles = handles[0:cap]
            labels = labels[0:cap]

        # Generate new legend
        legend = ax.legend(handles, labels, loc="upper right", title=legtitle)
        legend.set_draggable(True)

        self.pickable_legend_lines(figman, legend, ax)

    # -------------------------------------------------------------------------
    # Produce an extra one-to-many (otm) legend to enable togging of a particular
    # measurement in a single plot displaying all CPU cores.

    def otm_legend(
        self,
        figman,
        legtitle,
        prefix,
        ax,
        src_legend,
        *,
        loc="upper left",
        copy_markers=True,
    ):
        regex = rf"^{prefix}\d+ (.+)"
        re_prefix = re.compile(regex)
        re_trailing_digits = re.compile(r"\d+$")

        bins = {}

        # Sort out toggleable elements
        for (legline, handle, text) in zip(
            src_legend.get_lines(), src_legend.legendHandles, src_legend.texts
        ):
            label = text.get_text()
            match = re_prefix.match(label)
            if match is not None:
                bin = match.group(1)
                legelts = [figman.legtexts[legline], figman.legmarkers[legline]]
                if bin not in bins:
                    marker = handle._legmarker.get_marker()
                    marker = re_trailing_digits.sub("", marker, 1)
                    bins[bin] = {
                        "lines": [handle],
                        "legelts": legelts,
                        "colour": handle.get_color(),
                        "marker": marker,
                    }
                else:
                    bins[bin]["lines"].append(handle)
                    bins[bin]["legelts"] += legelts

        # Create shiney new legend lines
        new_handles = []
        new_labels = []
        for bin in bins.keys():
            extra_args = {}
            if copy_markers:
                extra_args["marker"] = bins[bin]["marker"]
            line = mpl.lines.Line2D(
                [], [], color=bins[bin]["colour"], label=bin, **extra_args
            )
            new_handles.append(line)
            new_labels.append(bin)

        # Generate new legend
        legend = plt.legend(new_handles, new_labels, loc=loc, title=legtitle)
        figman.register_legend(ax, legtitle, legend)
        legend.set_draggable(True)

        for (line, text) in zip(legend.get_lines(), legend.get_texts()):
            label = line.get_label()
            line.set_picker(10)
            text.set_picker(10)
            figman.legotm[line] = bins[label]["lines"]
            figman.legotm[text] = bins[label]["lines"]

        # Re-add src legend since it will have been detached by the plt.legend([..]) call above
        ax.add_artist(src_legend)

        return legend

    # -------------------------------------------------------------------------
    # Combine legends from both axes in to single axis

    def combined_legend(
        self,
        figman,
        title,
        legtitle,
        ax1_ylabel,
        ax2_ylabel,
        ax1,
        ax2,
        *,
        cap1=None,
        cap2=None,
    ):
        # Set furniture text
        ax2.set_title(title)
        ax1.set_ylabel(ax1_ylabel)
        ax2.set_ylabel(ax2_ylabel)

        # Get legend lines ready
        handles1, labels1 = ax1.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()

        if cap1 is not None:
            handles1 = handles1[0:cap1]
            labels1 = labels1[0:cap1]

        if cap2 is not None:
            handles2 = handles2[0:cap2]
            labels2 = labels2[0:cap2]

        # Remove original legends from drawing tree
        ax1.get_legend().remove()
        ax2.get_legend().remove()

        # Generate new legend
        legend = ax2.legend(
            handles1 + handles2, labels1 + labels2, loc="upper right", title=legtitle
        )
        legend.set_draggable(True)
        ax2.get_legend().set_draggable(True)

        self.pickable_legend_lines(figman, legend, ax1, ax2, len1=len(handles1))

        return legend

    # -------------------------------------------------------------------------
    # Draw the load average and CPU graph
    #
    # Forcing a single cpu core isn't the same as there being no multicore data.
    # Forcing a single core displays the core's index in labels, and removes the
    # load average display since that's not relevant to a single core out of multiple cores.

    def graph_cpus(
        grapher, figman, df, ax_in, title, *, x_bounds=None, force_single_core=None
    ):
        if force_single_core is None:
            ax_loadavg = ax_in
            ax_cpu = ax_loadavg.twinx()
            legend_title = "cpu/load"
        else:
            ax_cpu = ax_in
            legend_title = "cpu"

        if force_single_core is None:
            df.plot(
                y="load average",
                color=grapher.colours["load average"],
                ax=ax_loadavg,
                lw=3,
            )

        common_args = {}
        common_args["markersize"] = 8

        # Calculate offsets for markers so that they don't cluster
        total_markers = 10
        markeveries = {}
        clustering = True

        # Loop if offsets are (still) clustered and another attempt makes sense
        while clustering and total_markers >= 1:
            offset_prev = None
            markevery = int(len(df) / total_markers)
            for core in range(grapher.cores):
                offset = int(markevery / grapher.cores) * core
                if offset_prev is not None and offset_prev != offset:
                    clustering = False
                offset_prev = offset
                markeveries[core] = (offset, markevery)
            total_markers -= 1

        measures = ["user", "system", "nice", "idle", "wait", "hw irq", "sw irq"]

        if grapher.args.with_cpu_steal:
            measures.append("steal")

        core_test = 0 if force_single_core is None else force_single_core
        colname_test = "cpu exec" if grapher.cores == 1 else f"cpu{core_test} exec"
        if colname_test in df.columns:
            measures = ["exec"] + measures

        if grapher.cores > 1 or force_single_core is not None:
            for core in (
                range(0, grapher.cores)
                if force_single_core is None
                else [force_single_core]
            ):
                for measure in measures:
                    extra_args = common_args
                    if force_single_core is None:
                        extra_args[
                            "marker"
                        ] = f"${core}$"  # grapher.markers[f"{core}{measure}"]
                        extra_args["markevery"] = markeveries[core]

                    df.plot(
                        y=f"cpu{core} {measure}",
                        color=grapher.colours[measure],
                        ax=ax_cpu,
                        **extra_args,
                    )
        else:
            for measure in measures:
                df.plot(
                    y=f"cpu {measure}",
                    color=grapher.colours[measure],
                    ax=ax_cpu,
                    **common_args,
                )

        if force_single_core is None:
            combined_legend = grapher.combined_legend(
                figman, title, legend_title, "loadavg", "cpu (%)", ax_loadavg, ax_cpu
            )  # , cap2=len(measures))
            if grapher.cores > 1:
                grapher.otm_legend(
                    figman,
                    "cpu (grouped)",
                    "cpu",
                    ax_cpu,
                    combined_legend,
                    copy_markers=False,
                )
        else:
            grapher.single_legend(figman, title, legend_title, "cpu (%)", ax_cpu)

        if force_single_core is None:
            ax_loadavg.tick_params("x", which="minor", bottom=False)
            grapher.common_ax1(figman, ax_loadavg)
            ax_loadavg.set_ybound(lower=0, upper=df["load average"].max() * 105.0 / 100)

        if x_bounds is not None:
            min_timestamp, max_timestamp = x_bounds
            ax_cpu.set_xbound(lower=min_timestamp, upper=max_timestamp)

        grapher.common_ax2(figman, ax_cpu)
        ax_cpu.set_ybound(lower=0, upper=100)

    # -------------------------------------------------------------------------
    # Draw the task summary graph

    def graph_tasks(grapher, figman, df_in, ax_sleeping, title):

        ax_others = ax_sleeping.twinx()

        df = df_in.rename(columns=lambda x: x[5:] if x[:5] == "task " else x)
        df.filter(items=["sleeping"]).plot(
            ax=ax_sleeping, color=grapher.colours["task sleeping"], x_compat=True
        )

        task_colours = []
        items = ["running", "stopped", "zombie"]
        for item in items:
            task_colours.append(grapher.colours["task " + item])
        df.filter(items=items).plot(ax=ax_others, color=task_colours, x_compat=True)

        grapher.combined_legend(
            figman,
            title,
            "tasks",
            "sleeping tasks",
            "running, stopped, and zombie tasks",
            ax_sleeping,
            ax_others,
        )
        grapher.common_ax1(figman, ax_sleeping)
        grapher.common_ax2(figman, ax_others)
        ax_others.set_ybound(lower=0)
        ax_sleeping.set_ybound(lower=0, upper=df["sleeping"].max() * 105.0 / 100)

    # -------------------------------------------------------------------------
    # Draw the memory summary graph

    def graph_mem(grapher, figman, df, ax1, title):
        ax1.set_title(title)

        mem_colours = []

        # Draw 'mem free' lowest in z-order, unless 'mem availble' is needed there
        lowest_mem = (
            "mem free"
            if grapher.mem_cached_or_available == "mem cached"
            else "mem available"
        )

        items = [lowest_mem, "mem used", "mem buffers"]
        for item in items:
            mem_colours.append(grapher.colours[item])
        df.filter(items=items).plot.area(ax=ax1, color=mem_colours)

        # Inform the user if it looks like top's scale was set too high
        if df.iloc[[0, -1]].sum(axis=1).sum() == 0.0:
            msg = "The memory and swap values for the first and last cycles are all zero. Was top's scale set too high?\nToggle through the available scales by pressing uppercase 'E' in top's Interactive mode's main page.\nThen save the config by press uppercase 'W'."
            figman.display_msg(msg, 5)
            print(f"WARNING: {msg}")

        # 'mem used' includes 'mem cached' which is pants, since that memory is
        # available to use immediately, although if the VFS is asked for its old
        # contents and they're still valid, it will (immediately) be put back to use
        # as that data instead.  ('mem available' handles this better.)
        #
        # Indicate this state of affairs by colouring cached memory using the colours
        # for 'mem free' hatched with 'mem used'

        if grapher.mem_cached_or_available == "mem cached":
            # Overwrite the overlapping part of 'mem used' with 'mem cached'
            df.filter(items=["mem free", "mem cached"]).plot.area(
                ax=ax1, color=grapher.colours["mem free"]
            )
            chatch = ax1.collections[-1]

            # Knock out confusing repeat 'mem free' legend
            c = ax1.collections[-2]
            c.set_label("")
        else:
            # Overwrite the overlapping part of 'mem available' with 'mem free'
            df.filter(items=["mem free"]).plot.area(
                ax=ax1, color=grapher.colours["mem free"]
            )
            chatch = ax1.collections[0]
            chatch.set_label("mem cached")

        hatches = [".", "/", "\\", None, "\\\\", "*"]
        chatch.set_facecolor(grapher.colours["mem free"])
        chatch.set_edgecolor(grapher.colours["mem used"])
        chatch.set_hatch("//")

        df.filter(items=["swap free"]).plot(
            ax=ax1, color=grapher.colours["swap free"], lw=3
        )

        grapher.common_ax1(figman, ax1)

        l1 = ax1.legend(loc="upper right", title="memory")
        l1.set_draggable(True)
        ax1.set_ylabel(f"mem ({grapher.mem_unit})")

    # -------------------------------------------------------------------------
    # Draw the graph of Processes of Interest (POI) using the given DataFrame

    def graph_poi(
        grapher,
        figman,
        df,
        ax,
        title,
        *,
        x_bounds=None,
        mem_bounds=None,
        single_core=None,
    ):
        max_cpu = 100
        max_mem = None

        # Convenience aliasing
        plot_cpu_lines = grapher.args.plot_poi_cpu_lines
        plot_cpu_sum = grapher.args.plot_poi_cpu_sum
        plot_mem_lines = grapher.args.plot_poi_mem_lines
        plot_mem_sum = grapher.args.plot_poi_mem_sum

        if (plot_mem_lines or plot_mem_sum) and grapher.args.include_process_mem:
            ax_cpu = ax.twinx()
            ax_mem = ax
        else:
            ax_cpu = ax
            ax_mem = ax.twinx()

        figman.ax_name_map[ax_cpu] = "ax_cpu"
        figman.ax_name_map[ax_mem] = "ax_mem"

        if (
            (plot_cpu_lines or plot_cpu_sum)
            and grapher.args.include_process_cpu
            and (plot_mem_lines or plot_cpu_sum)
            and grapher.args.include_process_mem
        ):
            figman.ax_pairs.append(ax_cpu, ax_mem)

        # ---------------------------------------------------------------------

        def style_line(
            ax, index, colour, alpha, linestyle, marker=None, mark_every=None
        ):
            line = ax.get_lines()[index]
            line.set_color(colour)
            line.set_alpha(alpha)
            line.set_linestyle(linestyle)
            if marker is None:
                marker = ""
            line.set_marker(marker)
            if mark_every is None:
                mark_every = 10
            line.set_markevery(mark_every)

        # ---------------------------------------------------------------------

        def max_cpu_fu(column_name):
            max_cpu = df[column_name].max()
            if max_cpu > 100:
                max_cpu = 100 * math.ceil((max_cpu + 0.1) / 100.0)
            else:
                max_cpu = 110
            return max_cpu

        # ---------------------------------------------------------------------

        def max_mem_fu(column_name):
            max_mem = df[column_name].max()
            return 10 * math.ceil((max_mem + 0.1) / 10.0)

        # ---------------------------------------------------------------------

        def handle_data(
            df,
            ax,
            separate_cores,
            plot_data_lines,
            plot_summary,
            plot_at_all,
            mode,
            summary_line_style,
            max_fu,
            max_fu_default,
            x_bounds,
        ):
            plotted = False
            if (plot_data_lines or plot_summary) and plot_at_all:
                summary_title = f"poi {mode} sum - {mode}"
                if plot_summary and not separate_cores:
                    # Create summary column if not already present
                    if summary_title not in df.columns.to_list():
                        summary = grapher.args.poi_df.filter(regex=f" - {mode}$").sum(
                            axis=1
                        )
                        df.insert(0, summary_title, summary)

                # Select columns by regex
                if not plot_data_lines:
                    regex = f"^{summary_title}$"
                else:
                    regex = f"- {mode}$"

                # Strip trailing category from names then plot
                foo = lambda x: x[:-6] if x[-6:] == f" - {mode}" else x
                df = df.filter(regex=regex)
                if not df.empty:
                    df.rename(columns=foo).plot(ax=ax, xlim=x_bounds)
                    plotted = True
                ax.set_ylabel(f"{mode} (%)")
                grapher.style_lines(ax)

                # Override summary line
                if plot_summary and not separate_cores:
                    colour, alpha, linestyle, marker, mark_every = summary_line_style
                    style_line(ax, 0, colour, alpha, linestyle, marker, mark_every)
                    return (plotted, max_fu(summary_title))

            return (plotted, max_fu_default)

        # ---------------------------------------------------------------------

        total_markers = 7.5
        mark_every = int(len(df) / total_markers)
        alpha = 0.33
        cpu_summary_line_style = (
            "mediumvioletred",
            alpha,
            (1, (1, 2, 1, 3)),
            "$c$",
            mark_every,
        )
        mem_summary_line_style = (
            "dodgerblue",
            alpha,
            (0, (2, 6, 2, 2)),
            "$m$",
            mark_every,
        )

        cpu_plotted, max_cpu = handle_data(
            df,
            ax_cpu,
            x_bounds is not None,
            plot_cpu_lines,
            plot_cpu_sum,
            grapher.args.include_process_cpu,
            "cpu",
            cpu_summary_line_style,
            max_cpu_fu,
            100 if single_core else 110,
            x_bounds,
        )

        mem_plotted, max_mem = handle_data(
            df,
            ax_mem,
            x_bounds is not None,
            plot_mem_lines,
            plot_mem_sum,
            grapher.args.include_process_mem,
            "mem",
            mem_summary_line_style,
            max_mem_fu,
            None,
            x_bounds,
        )

        # Handle legends
        l_mem_cuckoo = None

        # Handle mem
        if (plot_mem_lines or plot_mem_sum) and grapher.args.include_process_mem:
            # ax_mem's legend shouldn't be overwritten by lines on ax_cpu
            # Sadly they are being overwritten, so ensure they're not by adding them to ax_cpu
            if (
                (plot_cpu_lines or plot_cpu_sum)
                and grapher.args.include_process_cpu
                and cpu_plotted
            ):
                handles, labels = ax_mem.get_legend_handles_labels()
                # Remove old legend's artists from drawing tree to avoid bitching about artist reuse
                # Note: doesn't delete legend object
                old_l_mem = ax_mem.legend()
                old_l_mem.remove()
                l_mem_cuckoo = plt.legend(
                    handles, labels, loc="upper left", title="mem"
                )

            else:
                ax_mem.legend(loc="upper left", title="mem")
                ax_cpu.set_visible(False)

                l_mem = ax_mem.get_legend()
                # WARNING: accessing internal mpl details here
                label = l_mem._legend_title_box._text
                figman.map_legend_lines(ax_mem, label, l_mem)
                l_mem.set_draggable(True)
                ax_mem.xaxis.set_visible(True)
                ax_mem.patch.set_visible(True)

        # Handle cpu
        if (plot_cpu_lines or plot_cpu_sum) and grapher.args.include_process_cpu:
            l_cpu = ax_cpu.legend(loc="upper right", title="cpu")
            # WARNING: accessing internal mpl details here
            label = l_cpu._legend_title_box._text
            figman.map_legend_lines(ax_cpu, label, l_cpu)
            l_cpu.set_draggable(True)

            if (
                not plot_mem_lines and not plot_mem_sum
            ) or not grapher.args.include_process_mem:
                ax_mem.set_visible(False)

        if l_mem_cuckoo is not None:
            ax_cpu.add_artist(l_mem_cuckoo)
            figman.register_legend(ax_cpu, "cuckoo", l_mem_cuckoo)
            # WARNING: accessing internal mpl details here
            label = l_mem_cuckoo._legend_title_box._text
            figman.map_legend_lines(ax_mem, label, l_mem_cuckoo)
            l_mem_cuckoo.set_draggable(True)

        # Handle furniture
        ax_cpu.set_title(title)
        ax_mem.set_title(title)

        grapher.common_ax1(figman, ax_mem)
        grapher.common_ax2(figman, ax_cpu)

        if x_bounds is None:
            x_bounds = (df.head(1).index[0], df.tail(1).index[0])
        ax_cpu.set_xlim(x_bounds)

        ax_cpu.set_ybound(lower=0, upper=max_cpu)

        if mem_bounds is not None:
            min_mem, max_mem = mem_bounds
            ax_mem.set_ybound(lower=min_mem, upper=max_mem)
        elif max_mem is not None:
            ax_mem.set_ybound(lower=0, upper=max_mem)

    # -------------------------------------------------------------------------
    # Draw the requested graph from the Big Four overview graphs in its own Fig

    def graph_by_overview_ordinal(self, n):
        figman_name = f"overview_{n}"

        if figman_name in self.fig_manager:
            self.fig_manager[figman_name].show()
        else:
            title = self.ordinal_to_cartesian_map(n)["title"]

            def setup(figman):
                ax = (
                    figman.plots
                )  # Note necessary absence of cartesian indexing for single subplot
                self.graph_map[title]["fn"](
                    figman, self.graph_map[title]["data"], ax, figman.subtitle
                )

            figman = FigManager(
                figman_name, self, self.title(title), self.window_size, 1, 1
            )

            figman.setup_graphing(setup)

            self.fig_manager[figman_name] = figman

    # -------------------------------------------------------------------------
    # Draw the cpu data in separate plots for each CPU core

    def graph_cpu_per_cpu(self):
        figman_name = "cpu_by_cpu"
        if self.fig_manager[figman_name] is not None:
            self.fig_manager[figman_name].show()
        else:
            # Find the nearest integer square that will fit the plots
            sqrt = math.ceil(math.sqrt(int(self.cores)))

            # Account for this possibly being a row larger than needed
            excess_rows = 0
            if (sqrt * sqrt) > (self.cores + sqrt - 1):
                excess_rows = 1

            def setup(figman):
                min_timestamp = self.args.poi_df.head(1).index[0]
                max_timestamp = self.args.poi_df.tail(1).index[0]

                for core in range(self.cores):
                    x = int(core / sqrt)
                    y = core % sqrt

                    ax = figman.plots[x][y]
                    df = self.args.cpus_df.filter(regex=f"^cpu{core}")

                    self.graph_cpus(
                        figman,
                        df,
                        ax,
                        f"core {core}",
                        x_bounds=(min_timestamp, max_timestamp),
                        force_single_core=core,
                    )

            figman = FigManager(
                figman_name,
                self,
                self.title("cpu data by cpu core"),
                self.window_size,
                sqrt - excess_rows,
                sqrt,
                setup,
            )

            figman.setup_graphing(setup)

            self.fig_manager[figman_name] = figman

    # -------------------------------------------------------------------------
    # Draw the Processes of Interest in separate plots for each CPU core

    def graph_poi_per_cpu(self):
        figman_name = "poi_by_cpu"
        if self.fig_manager[figman_name] is not None:
            self.fig_manager[figman_name].show()
        else:
            # Find the nearest integer square that will fit the plots
            sqrt = math.ceil(math.sqrt(int(self.cores)))

            # Account for this possibly being a row larger than needed
            excess_rows = 0
            if (sqrt * sqrt) > (self.cores + sqrt - 1):
                excess_rows = 1

            def setup(figman):
                min_timestamp = self.args.poi_df.head(1).index[0]
                max_timestamp = self.args.poi_df.tail(1).index[0]

                max_mem = 0
                for core in range(self.cores):
                    max_mem = max(
                        max_mem,
                        self.args.core_dfs[core].filter(regex=" - mem$").max().max(),
                    )

                for core in range(self.cores):
                    x = int(core / sqrt)
                    y = core % sqrt
                    ax = figman.plots[x][y]
                    self.graph_poi(
                        figman,
                        self.args.core_dfs[core],
                        ax,
                        f"core {core}",
                        x_bounds=(min_timestamp, max_timestamp),
                        mem_bounds=(0, max_mem),
                        single_core=core,
                    )

            figman = FigManager(
                figman_name,
                self,
                self.title(f"poi by cpu core\n{self.args.poi_categories}"),
                self.window_size,
                sqrt - excess_rows,
                sqrt,
                setup,
                subtitle=True,
            )

            figman.setup_graphing(setup)

            self.fig_manager[figman_name] = figman

    # -------------------------------------------------------------------------
    # Draw the four overview graphs on a single Fig

    def graph_overview(self):
        figman_name = "overview"
        if self.fig_manager[figman_name] is not None:
            self.fig_manager[figman_name].show()
        else:

            def setup(figman):
                for (x, y, title) in zip(
                    [0, 0, 1, 1], [0, 1, 0, 1], self.graph_map.keys()
                ):
                    ax = figman.plots[x][y]
                    self.graph_map[title]["fn"](
                        figman, self.graph_map[title]["data"], ax, title
                    )

            figman = FigManager(
                figman_name, self, self.title("overview"), self.window_size, 2, 2
            )

            figman.setup_graphing(setup)
            self.fig_manager[figman_name] = figman

    # -------------------------------------------------------------------------
    # Save pngs of all the open windows' figs

    def save_all_figs(self):
        for fig_name in self.fig_manager.keys():
            figman = self.fig_manager[fig_name]
            if figman is not None:
                figman.save()

    # -------------------------------------------------------------------------
    # Main function for setting things up and running

    def doit(self):

        self.window_size = get_curr_screen_dimensions(0.9)

        override_rcParams()

        for (x, y, title) in zip([0, 0, 1, 1], [0, 1, 0, 1], self.graph_map.keys()):
            self.cartesian_map[x][y] = {"title": title}

        if self.args.which_graph is not None:
            if len(self.args.which_graph) != 1:
                die("Need a single character.")

            if self.args.which_graph.isnumeric():
                i = int(self.args.which_graph)
                if i == 0:
                    self.graph_overview()

                elif i >= 1 and i <= 4:
                    self.graph_by_overview_ordinal(i - 1)

                else:
                    die("Need a number from 0 to 4.")

            elif self.args.which_graph == "c":
                if self.cores < 2:
                    die("No multi-core data available.")

                if not self.args.plot_poi_cpu_lines:
                    die("'-g c' and '--dont-graph-cpu-lines' are incompatible.")

                self.graph_poi_per_cpu()

            elif self.args.which_graph == "C":
                self.graph_cpu_per_cpu() if self.cores > 1 else die(
                    "No multi-core data available."
                )

            else:
                die(
                    f"The character '{self.args.which_graph}' doesn't represent a graph."
                )

        else:
            self.graph_overview()

        plt.show()


# -----------------------------------------------------------------------------
# vi: sw=4:ts=4:et
