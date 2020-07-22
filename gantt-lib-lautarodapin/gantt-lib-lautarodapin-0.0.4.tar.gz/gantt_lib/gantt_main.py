from gantt import *

from gantt.gantt import __LOG__, _font_attributes, _not_worked_days, _my_svgwrite_drawing_wrapper, mm, cm


class _svgwrite_generator(svgwrite.Drawing):
    """ svgwrite generator wrapper
    """

    def generate_svg_code(self, width='100%', height='100%'):   
        """ generate svg code

        Args:
            width (str, optional): width of the svg. Defaults to '100%'.
            height (str, optional): height of the svg. Defaults to '100%'.

        Returns:
            svg (str): code XLM in string format
        """
        self['height'] = height
        self['width'] = width     
        svg = '<?xml version="1.0" encoding="utf-8" ?>\n'
        stylesheet_template =  '<?xml-stylesheet href="%s" type="text/css" ' \
                'title="%s" alternate="%s" media="%s"?>\n'
        for stylesheet in self._stylesheets:
            svg += stylesheet_template % stylesheet
        svg += self.tostring()
        return svg 



class ProjectSpanish(Project):
    """ Inherits from Project, some translations of months and days. """

    def get_string_svg_for_tasks(self, today=None, start=None, end=None, scale=DRAW_WITH_DAILY_SCALE, title_align_on_left=False, offset=0):
        """
        Draw gantt of tasks and outputs the svg in str format. If start or end are
        given, use them as reference, otherwise use project first and last day

        Keyword arguments:
        today -- datetime.date of day marked as a reference
        start -- datetime.date of first day to draw
        end -- datetime.date of last day to draw
        scale -- drawing scale (d: days, w: weeks, m: months, q: quaterly)
        title_align_on_left -- boolean, align task title on left
        offset -- X offset from image border to start of drawing zone
        """
        if len(self.tasks) == 0:
            __LOG__.warning('** Empty project : {0}'.format(self.name))
            return


        self._reset_coord()

        if start is None:
            start_date = self.start_date()    
        else:
            start_date = start

        if end is None:
            end_date = self.end_date() 
        else:
            end_date = end


        if start_date > end_date:
            __LOG__.critical('start date {0} > end_date {1}'.format(start_date, end_date))
            sys.exit(1)

        ldwg = svgwrite.container.Group()
        psvg, pheight = self.svg(prev_y=2, start=start_date, end=end_date, color = self.color, scale=scale, title_align_on_left=title_align_on_left, offset=offset)
        if psvg is not None:
            ldwg.add(psvg)
            
        dep = self.svg_dependencies(self)
        if dep is not None:
            ldwg.add(dep)

        if scale == DRAW_WITH_DAILY_SCALE:
            # how many dayss do we need to draw ?
            maxx = (end_date - start_date).days
        elif scale == DRAW_WITH_WEEKLY_SCALE:
            # how many weeks do we need to draw ?
            maxx = 0
            guess = start_date

            guess = start_date
            while guess.weekday() != 0:
                guess = guess + dateutil.relativedelta.relativedelta(days=-1)

            while end_date.weekday() != 6:
                end_date = end_date + dateutil.relativedelta.relativedelta(days=+1)
            
            while guess <= end_date:
                maxx += 1
                guess = guess + dateutil.relativedelta.relativedelta(weeks=+1)
        elif scale == DRAW_WITH_MONTHLY_SCALE:
            # how many months do we need to draw ?
            if dateutil.relativedelta.relativedelta(end_date, start_date).days == 0:
                maxx = dateutil.relativedelta.relativedelta(end_date, start_date).months + dateutil.relativedelta.relativedelta(end_date, start_date).years*12
            else:
                maxx = dateutil.relativedelta.relativedelta(end_date, start_date).months + dateutil.relativedelta.relativedelta(end_date, start_date).years*12 + 1
        elif scale == DRAW_WITH_QUATERLY_SCALE:
            # how many quarter do we need to draw ?
            __LOG__.critical('DRAW_WITH_QUATERLY_SCALE not implemented yet')
            sys.exit(1)
            
        dwg = _svgwrite_generator()
        dwg.add(svgwrite.shapes.Rect(
                    insert=((0)*cm, 0*cm),
                    size=((maxx+1+offset/10)*cm, (pheight+3)*cm),
                    fill='white',
                    stroke_width=0,
                    opacity=1
                    ))
        dwg.add(self._svg_calendar(maxx, pheight, start_date, today, scale, offset=offset))
        dwg.add(ldwg)

        
        return dwg.generate_svg_code(width=(maxx+1+offset/10)*cm, height=(pheight+3)*cm)



    def _svg_calendar(self, maxx, maxy, start_date, today=None, scale=DRAW_WITH_DAILY_SCALE, offset=0):
        """
        Draw calendar in svg, begining at start_date for maxx days, containing
        maxy lines. If today is given, draw a blue line at date

        Keyword arguments:
        maxx -- number of days, weeks, months or quarters (depending on scale) to draw
        maxy -- number of lines to draw
        start_date -- datetime.date of the first day to draw
        today -- datetime.date of day as today reference
        scale -- drawing scale (d: days, w: weeks, m: months, q: quaterly)
        offset -- X offset from image border to start of drawing zone
        """
        dwg = svgwrite.container.Group()

        cal = {0: 'Lu', 1: 'Ma', 2: 'Xe', 3: 'Ju', 4: 'Vi', 5: 'Sa', 6: 'Do'}

        maxx += 1

        vlines = dwg.add(svgwrite.container.Group(
            id='vlines', stroke='lightgray'))
        for x in range(maxx):
            vlines.add(svgwrite.shapes.Line(
                start=((x+offset/10)*cm, 2*cm), end=((x+offset/10)*cm, (maxy+2)*cm)))
            if scale == DRAW_WITH_DAILY_SCALE:
                jour = start_date + datetime.timedelta(days=x)
            elif scale == DRAW_WITH_WEEKLY_SCALE:
                jour = start_date + \
                    dateutil.relativedelta.relativedelta(weeks=+x)
            elif scale == DRAW_WITH_MONTHLY_SCALE:
                jour = start_date + \
                    dateutil.relativedelta.relativedelta(months=+x)
            elif scale == DRAW_WITH_QUATERLY_SCALE:
                # how many quarter do we need to draw ?
                __LOG__.critical(
                    'DRAW_WITH_QUATERLY_SCALE not implemented yet')
                sys.exit(1)

            if not today is None and today == jour:
                vlines.add(svgwrite.shapes.Rect(
                    insert=((x+0.4+offset)*cm, 2*cm),
                    size=(0.2*cm, (maxy)*cm),
                    fill='#76e9ff',
                    stroke='lightgray',
                    stroke_width=0,
                    opacity=0.8
                ))

            if scale == DRAW_WITH_DAILY_SCALE:
                # draw vacations
                if (start_date + datetime.timedelta(days=x)).weekday() in _not_worked_days() or (start_date + datetime.timedelta(days=x)) in VACATIONS:
                    vlines.add(svgwrite.shapes.Rect(
                        insert=((x+offset/10)*cm, 2*cm),
                        size=(1*cm, maxy*cm),
                        fill='gray',
                        stroke='lightgray',
                        stroke_width=1,
                        opacity=0.7,
                    ))

                # Current day
                vlines.add(svgwrite.text.Text('{1} {0:02}'.format(jour.day, cal[jour.weekday()][0]),
                                              insert=(
                                                  (x*10+1+offset)*mm, 19*mm),
                                              fill='black', stroke='black', stroke_width=0,
                                              font_family=_font_attributes()['font_family'], font_size=15-3))
                # Year
                if jour.day == 1 and jour.month == 1:
                    vlines.add(svgwrite.text.Text('{0}'.format(jour.year),
                                                  insert=(
                                                      (x*10+1+offset)*mm, 5*mm),
                                                  fill='#400000', stroke='#400000', stroke_width=0,
                                                  font_family=_font_attributes(
                    )['font_family'], font_size=15+5,
                        font_weight="bold"))
                # Month name
                if jour.day == 1:
                    vlines.add(svgwrite.text.Text('{0}'.format(jour.strftime("%B")),
                                                  insert=(
                                                      (x*10+1+offset)*mm, 10*mm),
                                                  fill='#800000', stroke='#800000', stroke_width=0,
                                                  font_family=_font_attributes(
                    )['font_family'], font_size=15+3,
                        font_weight="bold"))
                # Week number
                if jour.weekday() == 0:
                    vlines.add(svgwrite.text.Text('{0:02}'.format(jour.isocalendar()[1]),
                                                  insert=(
                                                      (x*10+1+offset)*mm, 15*mm),
                                                  fill='black', stroke='black', stroke_width=0,
                                                  font_family=_font_attributes()[
                        'font_family'],
                        font_size=15+1,
                        font_weight="bold"))

            elif scale == DRAW_WITH_WEEKLY_SCALE:
                # Year
                if jour.isocalendar()[1] == 1 and jour.month == 1:
                    vlines.add(svgwrite.text.Text('{0}'.format(jour.year),
                                                  insert=(
                                                      (x*10+1+offset)*mm, 5*mm),
                                                  fill='#400000', stroke='#400000', stroke_width=0,
                                                  font_family=_font_attributes()['font_family'], font_size=15+5, font_weight="bold"))
                # Month name
                if jour.day <= 7:
                    vlines.add(svgwrite.text.Text('{0}'.format(jour.strftime("%B")),
                                                  insert=(
                                                      (x*10+1+offset)*mm, 10*mm),
                                                  fill='#800000', stroke='#800000', stroke_width=0,
                                                  font_family=_font_attributes()['font_family'], font_size=15+3, font_weight="bold"))
                vlines.add(svgwrite.text.Text('{0:02}'.format(jour.isocalendar()[1]),
                                              insert=(
                                                  (x*10+1+offset)*mm, 15*mm),
                                              fill='black', stroke='black', stroke_width=0,
                                              font_family=_font_attributes()['font_family'], font_size=15+1, font_weight="bold"))

            elif scale == DRAW_WITH_MONTHLY_SCALE:
                # Month number
                vlines.add(svgwrite.text.Text('{0}'.format(jour.strftime("%m")),
                                              insert=(
                                                  (x*10+1+offset)*mm, 19*mm),
                                              fill='black', stroke='black', stroke_width=0,
                                              font_family=_font_attributes()['font_family'], font_size=15-3))
                # Year
                if jour.month == 1:
                    vlines.add(svgwrite.text.Text('{0}'.format(jour.year),
                                                  insert=(
                                                      (x*10+1+offset)*mm, 5*mm),
                                                  fill='#400000', stroke='#400000', stroke_width=0,
                                                  font_family=_font_attributes()['font_family'], font_size=15+5, font_weight="bold"))

            elif scale == DRAW_WITH_QUATERLY_SCALE:
                # how many quarter do we need to draw ?
                __LOG__.critical(
                    'DRAW_WITH_QUATERLY_SCALE not implemented yet')
                sys.exit(1)

        vlines.add(svgwrite.shapes.Line(start=((maxx+offset/10)*cm,
                                               2*cm), end=((maxx+offset/10)*cm, (maxy+2)*cm)))

        hlines = dwg.add(svgwrite.container.Group(
            id='hlines', stroke='lightgray'))

        dwg.add(svgwrite.shapes.Line(start=((0+offset/10)*cm, (2)*cm),
                                     end=((maxx+offset/10)*cm, (2)*cm), stroke='black'))
        dwg.add(svgwrite.shapes.Line(start=((0+offset/10)*cm, (maxy+2)*cm),
                                     end=((maxx+offset/10)*cm, (maxy+2)*cm), stroke='black'))

        for y in range(2, maxy+3):
            hlines.add(svgwrite.shapes.Line(
                start=((0+offset/10)*cm, y*cm), end=((maxx+offset/10)*cm, y*cm)))

        return dwg


class HyperLinkedTask(Task):
    """ Inherits from Task, adds some link functionality to the title, resource, and lateral box """

    def __init__(self, name, link_name=None, link_lateral=None, link_resource=None, start=None, stop=None, duration=None, depends_of=None, resources=None, percent_done=0, color=None, fullname=None, display=True, state=''):
        """Hyper linked task

        Args:
            name (str): name of the task
            link_name (str, optional): link over the name of the task. Defaults to None.
            link_lateral (str, optional): link over the side box. Defaults to None.
            link_resource (str, optional): link over the resource. Defaults to None.
            start ([type], optional): [description]. Defaults to None.
            stop ([type], optional): [description]. Defaults to None.
            duration ([type], optional): [description]. Defaults to None.
            depends_of ([type], optional): [description]. Defaults to None.
            resources ([type], optional): [description]. Defaults to None.
            percent_done (int, optional): [description]. Defaults to 0.
            color ([type], optional): [description]. Defaults to None.
            fullname ([type], optional): [description]. Defaults to None.
            display (bool, optional): [description]. Defaults to True.
            state (str, optional): [description]. Defaults to ''.
        """
        super().__init__(name, start, stop, duration, depends_of, resources, percent_done, color, fullname, display, state)
        self.link_name = link_name
        self.link_resource = link_resource
        self.link_lateral = link_lateral

    def svg(self, prev_y=0, link=None, start=None, end=None, color=None, level=None, scale=DRAW_WITH_DAILY_SCALE, title_align_on_left=False, offset=0):
        """
        Return SVG for drawing this task.

        Keyword arguments:
        prev_y -- int, line to start to draw
        start -- datetime.date of first day to draw
        end -- datetime.date of last day to draw
        color -- string of color for drawing the project
        level -- int, indentation level of the project, not used here
        scale -- drawing scale (d: days, w: weeks, m: months, q: quaterly)
        title_align_on_left -- boolean, align task title on left
        offset -- X offset from image border to start of drawing zone
        """

        if not self.display:
            return(None, 0)

        add_modified_begin_mark = False
        add_modified_end_mark = False

        if start is None:
            start = self.start_date()

        if self.start is not None and self.start_date() != self.start:
            add_modified_begin_mark = True

        if end is None:
            end = self.end_date()

        if self.stop is not None and self.end_date() != self.stop:
            add_modified_end_mark = True

        # override project color if defined
        if self.color is not None:
            color = self.color

        add_begin_mark = False
        add_end_mark = False

        y = prev_y * 10

        if scale == DRAW_WITH_DAILY_SCALE:
            def _time_diff(e, s):
                return (e - s).days

            def _time_diff_d(e, s):
                return _time_diff(e, s) + 1

        elif scale == DRAW_WITH_WEEKLY_SCALE:
            def _time_diff(end_date, start_date):
                td = 0
                guess = start_date
                while guess.weekday() != 0:
                    guess = guess + \
                        dateutil.relativedelta.relativedelta(days=-1)

                while end_date.weekday() != 6:
                    end_date = end_date + \
                        dateutil.relativedelta.relativedelta(days=+1)

                while guess + dateutil.relativedelta.relativedelta(days=+6) < end_date:
                    td += 1
                    guess = guess + \
                        dateutil.relativedelta.relativedelta(weeks=+1)

                return td

            def _time_diff_d(e, s):
                return _time_diff(e, s) + 1

        elif scale == DRAW_WITH_MONTHLY_SCALE:
            def _time_diff(end_date, start_date):
                return dateutil.relativedelta.relativedelta(end_date, start_date).months + dateutil.relativedelta.relativedelta(end_date, start_date).years*12

            def _time_diff_d(e, s):
                return _time_diff(e, s) + 1

        elif scale == DRAW_WITH_QUATERLY_SCALE:
            sys.exit(1)

        # cas 1 -s--S==E--e-
        if self.start_date() >= start and self.end_date() <= end:
            x = _time_diff(self.start_date(), start) * 10
            d = _time_diff_d(self.end_date(), self.start_date()) * 10
            self.drawn_x_begin_coord = x
            self.drawn_x_end_coord = x+d
        # cas 5 -s--e--S==E-
        elif self.start_date() > end:
            return (None, 0)
        # cas 6 -S==E-s--e-
        elif self.end_date() < start:
            return (None, 0)
        # cas 2 -S==s==E--e-
        elif self.start_date() < start and self.end_date() <= end:
            x = 0
            d = _time_diff_d(self.end_date(), start) * 10
            self.drawn_x_begin_coord = x
            self.drawn_x_end_coord = x+d
            add_begin_mark = True
        # cas 3 -s--S==e==E-
        elif self.start_date() >= start and self.end_date() > end:
            x = _time_diff(self.start_date(), start) * 10
            d = _time_diff_d(end, self.start_date()) * 10
            self.drawn_x_begin_coord = x
            self.drawn_x_end_coord = x+d
            add_end_mark = True
        # cas 4 -S==s==e==E-
        elif self.start_date() < start and self.end_date() > end:
            x = 0
            d = _time_diff_d(end, start) * 10
            self.drawn_x_begin_coord = x
            self.drawn_x_end_coord = x+d
            add_end_mark = True
            add_begin_mark = True
        else:
            return (None, 0)

        self.drawn_y_coord = y

        svg = svgwrite.container.Group(id=re.sub(r"[ ,'\/()]", '_', self.name))
        
        # Marca lateral izquierda para link a OT
        link = None
        linea_lateral = svgwrite.shapes.Rect(
                                            insert=((x+1+offset)*mm-(3+offset)*mm, (y+1)*mm),
                                            size=((3+offset)*mm, 8*mm),
                                            fill='#dadada',
                                            stroke=color,
                                            stroke_width=2,
                                            opacity=0.85,
                                            )
        if self.link_lateral:
            link = svg.add(svgwrite.container.Hyperlink(href=self.link_lateral))
            link.add(svgwrite.base.Title('Link a OT'))
        if link:
            link.add(linea_lateral)

        # Cuadrado de atras
        svg.add(svgwrite.shapes.Rect(
                insert=((x+1+offset)*mm, (y+1)*mm),
                size=((d-2)*mm, 8*mm),
                fill=color,
                stroke=color,
                stroke_width=2,
                opacity=0.85,
                ))
        svg.add(svgwrite.shapes.Rect(
                insert=((x+1+offset)*mm, (y+6)*mm),
                size=(((d-2))*mm, 3*mm),
                fill="#909090",
                stroke=color,
                stroke_width=1,
                opacity=0.2,
                ))

        if add_modified_begin_mark:
            svg.add(svgwrite.shapes.Rect(
                    insert=((x+1)*mm, (y+1)*mm),
                    size=(5*mm, 4*mm),
                    fill="#0000FF",
                    stroke=color,
                    stroke_width=1,
                    opacity=0.35,
                    ))

        if add_modified_end_mark:
            svg.add(svgwrite.shapes.Rect(
                    insert=((x+d-7+1)*mm, (y+1)*mm),
                    size=(5*mm, 4*mm),
                    fill="#0000FF",
                    stroke=color,
                    stroke_width=1,
                    opacity=0.35,
                    ))

        if add_begin_mark:
            svg.add(svgwrite.shapes.Rect(
                    insert=((x+1)*mm, (y+1)*mm),
                    size=(5*mm, 8*mm),
                    fill="#000000",
                    stroke=color,
                    stroke_width=1,
                    opacity=0.2,
                    ))
        if add_end_mark:
            svg.add(svgwrite.shapes.Rect(
                    insert=((x+d-7+1)*mm, (y+1)*mm),
                    size=(5*mm, 8*mm),
                    fill="#000000",
                    stroke=color,
                    stroke_width=1,
                    opacity=0.2,
                    ))

        if self.percent_done is not None and self.percent_done > 0:
            # Bar shade
            svg.add(svgwrite.shapes.Rect(
                    insert=((x+1+offset)*mm, (y+6)*mm),
                    size=(((d-2)*self.percent_done/100)*mm, 3*mm),
                    fill="#F08000",
                    stroke=color,
                    stroke_width=1,
                    opacity=0.35,
                    ))

        if not title_align_on_left:
            tx = x+2
        else:
            tx = 5
        link=None
        titulo = svgwrite.text.Text(self.fullname, insert=((tx)*mm, (y + 5)*mm), fill=_font_attributes()['fill'], stroke=_font_attributes()[
                    'stroke'], stroke_width=_font_attributes()['stroke_width'], font_family=_font_attributes()['font_family'], font_size=15)
        if self.link_name:
            link = svg.add(svgwrite.container.Hyperlink(href=self.link_name))
            link.add(svgwrite.base.Title('Ir a equipo'))
        if link:
            link.add(titulo)
        else:
            svg.add(titulo)
       

        if self.resources is not None:
            t = " / ".join(["{0}".format(r.name) for r in self.resources])
            link = None
            recurso = svgwrite.text.Text("{0}".format(t), insert=(tx*mm, (y + 8.5)*mm), fill='purple', stroke=_font_attributes()[
                    'stroke'], stroke_width=_font_attributes()['stroke_width'], font_family=_font_attributes()['font_family'], font_size=15-5)
            if self.link_resource:
                link = svg.add(svgwrite.container.Hyperlink(href=self.link_resource))
                link.add(svgwrite.base.Title('Ir a grupo'))
            if link:
                link.add(recurso)
            else:
                svg.add(recurso)
        return (svg, 1)


class HiperLinkedProject(ProjectSpanish):    
    """ Inherits from ProjectSpanish, adds some link functionality to the title """

    def __init__(self, name="", link=None, color=None):
        """Hiper linked project

        Args:
            name (str, optional): [description]. Defaults to "".
            link ([type], optional): [description]. Defaults to None.
            color ([type], optional): [description]. Defaults to None.
        """
        super().__init__(name, color)
        self.link = link



    def svg(self, prev_y=0, start=None, end=None, color=None, level=0, scale=DRAW_WITH_DAILY_SCALE, title_align_on_left=False, offset=0):
        """
        Return (SVG code, number of lines drawn) for the project. Draws all
        tasks and add project name with a purple bar on the left side.

        Keyword arguments:
        prev_y -- int, line to start to draw
        start -- datetime.date of first day to draw
        end -- datetime.date of last day to draw
        color -- string of color for drawing the project
        level -- int, indentation level of the project
        scale -- drawing scale (d: days, w: weeks, m: months, q: quaterly)
        title_align_on_left -- boolean, align task title on left
        offset -- X offset from image border to start of drawing zone
        """
        if start is None:
            start = self.start_date()
        if end is None:
            end = self.end_date()
        if color is None or self.color is not None:
            color = self.color


        cy = prev_y + 1*(self.name != "")

        prj = svgwrite.container.Group()

        for t in self.tasks:
            trepr, theight = t.svg(cy, start=start, end=end, color=color, level=level+1, scale=scale, title_align_on_left=title_align_on_left, offset=offset)
            if trepr is not None:
                prj.add(trepr)
                cy += theight

        fprj = svgwrite.container.Group()
        prj_bar = False
        if self.name != "":
            # if ((self.start_date() >= start and self.end_date() <= end) 
            #     or (self.start_date() >= start and (self.end_date() <= end or self.start_date() <= end))) or level == 1: 
            if ((self.start_date() >= start and self.end_date() <= end) 
                or ((self.end_date() >=start and self.start_date() <= end))) or level == 1: 
          
                link = None
                titulo = svgwrite.text.Text('{0}'.format(self.name), insert=((6*level+3+offset)*mm, ((prev_y)*10+7)*mm), fill=_font_attributes()['fill'], stroke=_font_attributes()['stroke'], stroke_width=_font_attributes()['stroke_width'], font_family=_font_attributes()['font_family'], font_size=15+3)
                if self.link:
                    link = fprj.add(svgwrite.container.Hyperlink(href=self.link))
                    link.add(svgwrite.base.Title('Ir a equipo'))
                if link:
                    link.add(titulo)
                else:
                    fprj.add(titulo)

                fprj.add(svgwrite.shapes.Rect(
                        insert=((6*level+0.8+offset)*mm, (prev_y+0.5)*cm),
                        size=(0.2*cm, ((cy-prev_y-1)+0.4)*cm),
                        fill='purple',
                        stroke='lightgray',
                        stroke_width=0,
                        opacity=0.5
                        ))
                prj_bar = True
            else:
                cy -= 1

        # Do not display empty tasks
        if (cy - prev_y) == 0 or ((cy - prev_y) == 1 and prj_bar):
            return (None, 0)

        fprj.add(prj)

        return (fprj, cy-prev_y)