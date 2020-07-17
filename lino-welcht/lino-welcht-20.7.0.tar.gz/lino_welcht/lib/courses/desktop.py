# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import _
from lino_xl.lib.courses.desktop import *

Enrolments.detail_layout = """
request_date user
course pupil
remark workflow_buttons printed
motivation problems
"""


EnrolmentsByPupil.column_names = 'request_date course workflow_buttons *'
EnrolmentsByPupil.insert_layout = """
course_area
course
places option
remark
request_date user
"""

    
    


class BasicCourses(Activities):
    _course_area = CourseAreas.default


class JobCourses(Activities):
    _course_area = CourseAreas.job


# class IntegEnrolmentsByPupil(EnrolmentsByPupil):
#     _course_area = CourseAreas.integ


class BasicEnrolmentsByPupil(EnrolmentsByPupil):
    _course_area = CourseAreas.default


class JobEnrolmentsByPupil(EnrolmentsByPupil):
    _course_area = CourseAreas.job


class ActiveCourses(ActiveCourses):
    label = _("Active workshops")
    column_names = 'detail_link enrolments free_places room description *'
    hide_sums = True


class DraftCourses(DraftCourses):
    label = _("Draft workshops")
    column_names = 'detail_link room description *'


class InactiveCourses(InactiveCourses):
    label = _("Inactive workshops")


class ClosedCourses(ClosedCourses):
    label = _("Closed workshops")
    

