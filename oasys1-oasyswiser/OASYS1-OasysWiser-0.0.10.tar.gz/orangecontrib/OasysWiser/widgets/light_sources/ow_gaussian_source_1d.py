import sys
import numpy
from scipy.stats import norm
from orangewidget import gui
from orangewidget.settings import Setting
from oasys.widgets import gui as oasysgui
from oasys.widgets import congruence

from PyQt5.QtGui import QPalette, QColor, QFont

from LibWiser import Optics
import LibWiser.FermiSource as Fermi
from LibWiser.Foundation import PositioningDirectives

from WofryWiser.propagator.propagator1D.wise_propagator import WisePropagationElements

from WofryWiser.beamline.beamline_elements import WiserBeamlineElement, WiserOpticalElement

from orangecontrib.OasysWiser.util.wise_objects import WiserData
from orangecontrib.OasysWiser.widgets.gui.ow_wise_widget import WiserWidget, ElementType, PositioningDirectivesPhrases


class PositioningDirectivesSource:
    class Type:
        Custom = 'Absolute'

    class Orientation:
        Isotropic = 'Isotropic'
        Horizontal = 'Horizontal'
        Vertical = 'Vertical'
        Any = 'Any'

positioning_directives_what = [PositioningDirectives.What.Centre,
                               PositioningDirectives.What.UpstreamFocus,
                               PositioningDirectives.What.DownstreamFocus]

positioning_directives_where = [PositioningDirectives.Where.Centre,
                                PositioningDirectives.Where.UpstreamFocus,
                                PositioningDirectives.Where.DownstreamFocus]

positioning_directives_refer_to = [PositioningDirectives.ReferTo.AbsoluteReference,
                                   PositioningDirectives.ReferTo.UpstreamElement,
                                   PositioningDirectives.ReferTo.DownstreamElement,
                                   PositioningDirectives.ReferTo.DoNotMove,
                                   PositioningDirectives.ReferTo.Source]

positioning_directives_which_angle = [Optics.TypeOfAngle.GrazingNominal,
                                      Optics.TypeOfAngle.InputNominal,
                                      Optics.TypeOfAngle.OutputNominal,
                                      Optics.TypeOfAngle.SelfFrameOfReference,
                                      Optics.TypeOfAngle.NormalAbsolute,
                                      Optics.TypeOfAngle.TangentAbsolute]

positioning_directives_source = [PositioningDirectivesSource.Type.Custom]

positioning_directives_orientation = [PositioningDirectivesPhrases.Orientation.Isotropic,
                                      PositioningDirectivesPhrases.Orientation.Horizontal,
                                      PositioningDirectivesPhrases.Orientation.Vertical,
                                      PositioningDirectivesPhrases.Orientation.Any]

class OWGaussianSource1d(WiserWidget):
    name = "GaussianSource1d"
    id = "GaussianSource1d"
    description = "GaussianSource1d"
    icon = "icons/gaussian_source_1d.png"
    priority = 1
    category = ""
    keywords = ["wise", "gaussian"]

    WhatWhereReferTo = Setting(PositioningDirectivesSource.Type.Custom)
    ReferTo = Setting(PositioningDirectives.ReferTo.AbsoluteReference)
    What = Setting(PositioningDirectives.What.Centre)
    Where = Setting(PositioningDirectives.Where.Centre)

    source_name = Setting("Gaussian Source")

    source_lambda = Setting(10)
    XYCentre_checked = Setting(1)

    waist_calculation = Setting(0)
    source_waist = Setting(180)

    def build_positioning_directive_box(self, container_box, width, element_type=ElementType.SOURCE):

        box = oasysgui.widgetBox(container_box, "", orientation="vertical", width=width - 20)

        box_combos = oasysgui.widgetBox(box, "", orientation="vertical", width=width - 20)

        box_Distance = oasysgui.widgetBox(box, "", orientation="vertical", width=width - 20)

        '''
        box_GrazingAngle = oasysgui.widgetBox(box, "", orientation="horizontal", width=width-20)
        box_GrazingAngle_check = oasysgui.widgetBox(box_GrazingAngle, "", orientation="horizontal", width=20)
        box_GrazingAngle_value = oasysgui.widgetBox(box_GrazingAngle, "", orientation="horizontal")

        box_Angle = oasysgui.widgetBox(box, "", orientation="horizontal", width=width-20)
        box_Angle_check = oasysgui.widgetBox(box_Angle, "", orientation="horizontal", width=20)
        box_Angle_value = oasysgui.widgetBox(box_Angle, "", orientation="horizontal")

        def set_WhichAngle():
            box_GrazingAngle.setVisible(getattr(self, "WhichAngle") == positioning_directives_which_angle[0])
            box_Angle.setVisible(getattr(self, "WhichAngle") != positioning_directives_which_angle[0])
        '''

        def set_Distance_checked():
            box_Distance_value.setEnabled(getattr(self, "Distance_checked") == 1)

        def set_XYCentre_checked():
            box_XYCentre_value.setEnabled(getattr(self, "XYCentre_checked") == 1)

        '''
        def set_GrazingAngle_checked():
            box_GrazingAngle_value.setEnabled(getattr(self, "GrazingAngle_checked") == 1)

        def set_Angle_checked():
            box_Angle_value.setEnabled(getattr(self, "Angle_checked") == 1)
        '''

        def set_positioning_directives():
            '''
            This function correctly sets the positioning directives by setting correct
            settings for self.What, self.Where and self.ReferTo from the descriptive
            phrases.
            Possibilities are:
                Autofocus - self.What='centre', self.Where='downstream focus', self.ReferTo='upstream'
                DistanceFromPrevious - self.What='centre', self.Where='centre', self.ReferTo='upstream'
                DistanceFromSource - self.What='centre', self.Where='centre', self.ReferTo='source'
                Custom - allows you to set your own self.What, self.Where and self.ReferTo
            '''

            self.set_Orientation()

            if self.WhatWhereReferTo == PositioningDirectivesSource.Type.Custom:
                self.Distance_checked = 0
                self.UseDistance = 0
                self.UseDefocus = 0
                self.UseCustom = 1
                self.What = None
                self.Where = None
                self.ReferTo = PositioningDirectives.ReferTo.AbsoluteReference
                pass

            else:
                raise ValueError("Wrong PositioningDirectives, source can only have Custom!")

            self.use_distance_box.setVisible(self.UseDistance)
            self.use_distance_box_empty.setVisible(self.UseDistance)

            self.use_defocus_box.setVisible(self.UseDefocus)
            self.use_defocus_box_empty.setVisible(self.UseDefocus)

            self.use_custom_box.setVisible(self.UseCustom)
            self.use_custom_box_empty.setVisible(self.UseCustom)

            pass
            # set_WhichAngle()

        # Build a combo box with the choice of positioning directions phrases

        le = oasysgui.lineEdit(box_Distance, self, "ReferenceOE", "Reference O.E.", labelWidth=220,
                               valueType=str, orientation="horizontal")

        le.setReadOnly(True)
        font = QFont(le.font())
        # font.setBold(True)
        le.setFont(font)
        palette = QPalette(le.palette())
        palette.setColor(QPalette.Text, QColor('grey'))
        palette.setColor(QPalette.Base, QColor(243, 240, 140))
        le.setPalette(palette)

        box_orientation = oasysgui.widgetBox(box_combos, "", orientation="horizontal", width=width - 20)
        gui.label(box_orientation, self, label="Orientation", labelWidth=87)
        gui.comboBox(box_orientation, self, "OrientationGUI",
                     items=positioning_directives_orientation,
                     sendSelectedValue=True, orientation="horizontal", callback=set_positioning_directives)

        box_type = oasysgui.widgetBox(box_combos, "", orientation="horizontal", width=width - 20)
        gui.label(box_type, self, label="Position", labelWidth=87)
        gui.comboBox(box_type, self, "WhatWhereReferTo",
                     items=positioning_directives_source,
                     sendSelectedValue=True, orientation="horizontal",
                     callback=set_positioning_directives)  # Send the value

        gui.separator(box_combos)

        self.use_distance_box = oasysgui.widgetBox(box_Distance, "", orientation="horizontal", width=width - 20)
        self.use_distance_box_empty = oasysgui.widgetBox(box_Distance, "", orientation="horizontal", width=width - 20)

        self.le_Distance_default = oasysgui.lineEdit(self.use_distance_box, self, "Distance", "Distance",
                                                     labelWidth=220, valueType=float, orientation="horizontal")

        self.use_defocus_box = oasysgui.widgetBox(box_Distance, "", orientation="horizontal", width=width - 20)
        self.use_defocus_box_empty = oasysgui.widgetBox(box_Distance, "", orientation="horizontal", width=width - 20)

        self.le_defocus = oasysgui.lineEdit(self.use_defocus_box, self, "Distance", "Defocus", labelWidth=220,
                                            valueType=float, orientation="horizontal")

        self.use_custom_box = oasysgui.widgetBox(box, "", orientation="vertical", width=width - 20)
        self.use_custom_box_empty = oasysgui.widgetBox(box, "", orientation="vertical", width=width - 20)
        box_XYDistance = oasysgui.widgetBox(self.use_custom_box, "", orientation="horizontal", width=width - 20)
        box_Distance_check = oasysgui.widgetBox(box_XYDistance, "", orientation="horizontal", width=20)
        box_Distance_value = oasysgui.widgetBox(box_XYDistance, "", orientation="vertical")
        box_XYCentre = oasysgui.widgetBox(self.use_custom_box, "", orientation="horizontal", width=width - 20)
        box_XYCentre_check = oasysgui.widgetBox(box_XYCentre, "", orientation="horizontal", width=20)
        box_XYCentre_value = oasysgui.widgetBox(box_XYCentre, "", orientation="vertical")
        # = oasysgui.widgetBox(box_Distance, "", orientation="vertical", width=width - 20)
        #    	self.use_custom_box_empty = oasysgui.widgetBox(box_Distance, "", orientation="horizontal", width=width - 20)

        box_what = oasysgui.widgetBox(self.use_custom_box, "", orientation="horizontal")
        gui.label(box_what, self, label="Place", labelWidth=87)
        gui.comboBox(box_what, self, "What", label="",
                     items=positioning_directives_what,
                     sendSelectedValue=True, orientation="horizontal", callback=set_positioning_directives)
        gui.label(box_what, self, label=" of this O.E.", labelWidth=80)

        box_where = oasysgui.widgetBox(self.use_custom_box, "", orientation="horizontal")
        gui.label(box_where, self, label="at", labelWidth=87)
        gui.comboBox(box_where, self, "Where", label="",
                     items=positioning_directives_where,
                     sendSelectedValue=True, orientation="horizontal", callback=set_positioning_directives)
        gui.label(box_where, self, label=" of", labelWidth=80)

        box_refer_to = oasysgui.widgetBox(self.use_custom_box, "", orientation="horizontal")
        gui.label(box_refer_to, self, label=" ", labelWidth=87)
        gui.comboBox(box_refer_to, self, "ReferTo", label="",
                     items=positioning_directives_refer_to,
                     sendSelectedValue=True, orientation="horizontal", callback=set_positioning_directives)
        gui.label(box_refer_to, self, label=" O.E.", labelWidth=80)

        '''
        gui.comboBox(box_combos, self, "WhichAngle", label="Type Of Angle",
                     items=positioning_directives_which_angle, labelWidth=box_combos.width()-150,
                     sendSelectedValue=True, orientation="horizontal", callback=set_WhichAngle)
        '''

        gui.checkBox(box_Distance_check, self, "Distance_checked", "", callback=set_Distance_checked)
        gui.checkBox(box_XYCentre_check, self, "XYCentre_checked", "", callback=set_XYCentre_checked)
        '''
        gui.checkBox(box_GrazingAngle_check, self, "GrazingAngle_checked", "", callback=set_GrazingAngle_checked)
        gui.checkBox(box_Angle_check, self, "Angle_checked", "", callback=set_Angle_checked)
        '''

        set_Distance_checked()
        set_XYCentre_checked()
        '''
        set_Angle_checked()
        set_GrazingAngle_checked()
        '''

        self.le_Distance = oasysgui.lineEdit(box_Distance_value, self, "Distance", "Distance", labelWidth=196,
                                             valueType=float, orientation="horizontal")
        self.le_XCentre = oasysgui.lineEdit(box_XYCentre_value, self, "XCentre", "X Centre", labelWidth=196,
                                            valueType=float, orientation="horizontal")
        self.le_YCentre = oasysgui.lineEdit(box_XYCentre_value, self, "YCentre", "Y Centre", labelWidth=196,
                                            valueType=float, orientation="horizontal")

        '''
        oasysgui.lineEdit(box_Angle_value, self, "Angle", "Angle [deg]", labelWidth=200, valueType=float, orientation="horizontal")
        oasysgui.lineEdit(box_GrazingAngle_value, self, "GrazingAngle", "Grazing Angle [deg]", labelWidth=200, valueType=float, orientation="horizontal")
        '''
        set_positioning_directives()

    def build_gui(self):

        main_box = oasysgui.widgetBox(self.controlArea, "Gaussian Source 1D Input Parameters", orientation="vertical", width=self.CONTROL_AREA_WIDTH-5)

        source_box = oasysgui.widgetBox(main_box, "Source Settings", orientation="vertical", width=self.CONTROL_AREA_WIDTH-25)

        oasysgui.lineEdit(source_box, self, "source_name", "Source Name", labelWidth=120, valueType=str, orientation="horizontal")

        self.le_source_wl = oasysgui.lineEdit(source_box, self, "source_lambda", "Wavelength [nm]", labelWidth=260, valueType=float, orientation="horizontal", callback=self.set_WaistCalculation)

        gui.comboBox(source_box, self, "waist_calculation", label="Preset Waist",
                     items=["None", "Fermi FEL1-like", "Fermi FEL2-like", "Fermi Auto"], labelWidth=260,
                     callback=self.set_WaistCalculation, sendSelectedValue=False, orientation="horizontal")

        self.le_source_waist = oasysgui.lineEdit(source_box, self, "source_waist", "Waist [um]", labelWidth=260, valueType=float, orientation="horizontal")

        position_box = oasysgui.widgetBox(main_box, "Position Settings", orientation="vertical", width=self.CONTROL_AREA_WIDTH-25)

        self.build_positioning_directive_box(container_box=position_box,
                                             width=self.CONTROL_AREA_WIDTH-25,
                                             element_type=ElementType.SOURCE)

    def set_WaistCalculation(self):
        if self.source_lambda > 0.0:
            self.source_waist = round(Fermi.Waist0E(self.source_lambda, str( self.waist_calculation))/self.workspace_units_to_m, 8)

    def after_change_workspace_units(self):
        super(OWGaussianSource1d, self).after_change_workspace_units()

        # self.source_lambda = self.source_lambda / self.workspace_units_to_m
        # self.source_waist = self.source_waist / self.workspace_units_to_m

        # label = self.le_source_wl.parent().layout().itemAt(0).widget()
        # label.setText(label.text() + " [" + self.workspace_units_label + "]")

        # label = self.le_source_waist.parent().layout().itemAt(0).widget()
        # label.setText(label.text() + " [" + self.workspace_units_label + "]")

    def check_fields(self):
        self.source_lambda = congruence.checkStrictlyPositiveNumber(self.source_lambda, "Wavelength")
        self.source_waist = congruence.checkStrictlyPositiveNumber(self.source_waist, "Waist")

    def do_wise_calculation(self):
        position_directives = self.get_PositionDirectives()
        position_directives.WhichAngle = Optics.TypeOfAngle.SelfFrameOfReference
        position_directives.Angle = 0.0

        wise_source = WiserOpticalElement(name=self.source_name,
                                          boundary_shape=None,
                                          native_CoreOptics=Optics.SourceGaussian(self.source_lambda*1e-9,
                                                                                  self.source_waist*1e-6),
                                          isSource=True,
                                          native_PositioningDirectives=position_directives)

        data_to_plot = numpy.zeros((2, 100))

        sigma = self.source_waist/2
        mu = 0.0 if self.XYCentre_checked else self.YCentre

        data_to_plot[0, :] = numpy.linspace((-5*sigma) + mu, mu + (5*sigma), 100)
        data_to_plot[1, :] = (norm.pdf(data_to_plot[0, :], mu, sigma))**2

        return wise_source, data_to_plot

    def getTitles(self):
        return ["Gaussian Source Intensity"]

    def getXTitles(self):
        return ["Y [" + self.workspace_units_label + "]"]

    def getYTitles(self):
        return ["Intensity [arbitrary units]"]

    def extract_plot_data_from_calculation_output(self, calculation_output):
        return calculation_output[1]

    def extract_wise_data_from_calculation_output(self, calculation_output):
        beamline = WisePropagationElements()
        beamline.add_beamline_element(WiserBeamlineElement(optical_element=calculation_output[0]))

        return WiserData(wise_wavefront=None, wise_beamline=beamline)

from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog
import sys

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWGaussianSource1d()
    ow.show()
    a.exec_()
    ow.saveSettings()