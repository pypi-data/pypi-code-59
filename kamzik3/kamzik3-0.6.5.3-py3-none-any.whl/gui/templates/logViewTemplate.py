# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logViewTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(911, 604)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/kamzik.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
" font-weight:bold\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
" font-weight:bold\n"
"   \n"
"}\n"
"\n"
"\n"
"QSplitter::handle:horizontal {\n"
"  image: url(:/icons/icons/splitter.png);\n"
"  width:13px;\n"
"  height:13px;\n"
"  background: #f6b442;\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(11)
        self.splitter.setObjectName("splitter")
        self.tabs_tools = QtWidgets.QTabWidget(self.splitter)
        self.tabs_tools.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabs_tools.setObjectName("tabs_tools")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 0, 2, 1, 1)
        self.input_max_selected_rows = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_max_selected_rows.sizePolicy().hasHeightForWidth())
        self.input_max_selected_rows.setSizePolicy(sizePolicy)
        self.input_max_selected_rows.setMinimum(1)
        self.input_max_selected_rows.setMaximum(25)
        self.input_max_selected_rows.setProperty("value", 25)
        self.input_max_selected_rows.setObjectName("input_max_selected_rows")
        self.gridLayout_6.addWidget(self.input_max_selected_rows, 0, 1, 1, 1)
        self.input_header_items = QtWidgets.QListView(self.groupBox_2)
        self.input_header_items.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.input_header_items.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.input_header_items.setObjectName("input_header_items")
        self.gridLayout_6.addWidget(self.input_header_items, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_list_view = QtWidgets.QPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/viewList.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_list_view.setIcon(icon1)
        self.button_list_view.setCheckable(True)
        self.button_list_view.setChecked(True)
        self.button_list_view.setAutoRepeat(False)
        self.button_list_view.setAutoExclusive(True)
        self.button_list_view.setDefault(True)
        self.button_list_view.setObjectName("button_list_view")
        self.horizontalLayout_2.addWidget(self.button_list_view)
        self.button_zoom_view = QtWidgets.QPushButton(self.groupBox_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/viewZoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_zoom_view.setIcon(icon2)
        self.button_zoom_view.setCheckable(True)
        self.button_zoom_view.setAutoExclusive(True)
        self.button_zoom_view.setObjectName("button_zoom_view")
        self.horizontalLayout_2.addWidget(self.button_zoom_view)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.tabs_view_tools = QtWidgets.QStackedWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs_view_tools.sizePolicy().hasHeightForWidth())
        self.tabs_view_tools.setSizePolicy(sizePolicy)
        self.tabs_view_tools.setObjectName("tabs_view_tools")
        self.page_zoom = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_zoom.sizePolicy().hasHeightForWidth())
        self.page_zoom.setSizePolicy(sizePolicy)
        self.page_zoom.setObjectName("page_zoom")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_zoom)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_6 = QtWidgets.QLabel(self.page_zoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.page_zoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 3, 0, 1, 1)
        self.input_to_dt = QtWidgets.QDateTimeEdit(self.page_zoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_to_dt.sizePolicy().hasHeightForWidth())
        self.input_to_dt.setSizePolicy(sizePolicy)
        self.input_to_dt.setReadOnly(True)
        self.input_to_dt.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.input_to_dt.setObjectName("input_to_dt")
        self.gridLayout_7.addWidget(self.input_to_dt, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_zoom)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page_zoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 1, 0, 1, 1)
        self.input_from_dt = QtWidgets.QDateTimeEdit(self.page_zoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_from_dt.sizePolicy().hasHeightForWidth())
        self.input_from_dt.setSizePolicy(sizePolicy)
        self.input_from_dt.setReadOnly(True)
        self.input_from_dt.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.input_from_dt.setObjectName("input_from_dt")
        self.gridLayout_7.addWidget(self.input_from_dt, 1, 1, 1, 1)
        self.readout_diff_dt = QtWidgets.QLineEdit(self.page_zoom)
        self.readout_diff_dt.setReadOnly(True)
        self.readout_diff_dt.setObjectName("readout_diff_dt")
        self.gridLayout_7.addWidget(self.readout_diff_dt, 3, 1, 1, 1)
        self.input_master_row = QtWidgets.QComboBox(self.page_zoom)
        self.input_master_row.setObjectName("input_master_row")
        self.gridLayout_7.addWidget(self.input_master_row, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_zoom)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 5, 0, 1, 2)
        self.input_zoom_follow = QtWidgets.QCheckBox(self.page_zoom)
        self.input_zoom_follow.setChecked(True)
        self.input_zoom_follow.setObjectName("input_zoom_follow")
        self.gridLayout_7.addWidget(self.input_zoom_follow, 4, 0, 1, 2)
        self.tabs_view_tools.addWidget(self.page_zoom)
        self.page_list = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_list.sizePolicy().hasHeightForWidth())
        self.page_list.setSizePolicy(sizePolicy)
        self.page_list.setObjectName("page_list")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_list)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.input_view_scale_plots = QtWidgets.QCheckBox(self.page_list)
        self.input_view_scale_plots.setChecked(True)
        self.input_view_scale_plots.setObjectName("input_view_scale_plots")
        self.gridLayout_8.addWidget(self.input_view_scale_plots, 0, 0, 1, 1)
        self.input_view_plot_height = QtWidgets.QSpinBox(self.page_list)
        self.input_view_plot_height.setEnabled(False)
        self.input_view_plot_height.setMinimum(5)
        self.input_view_plot_height.setMaximum(100)
        self.input_view_plot_height.setProperty("value", 25)
        self.input_view_plot_height.setObjectName("input_view_plot_height")
        self.gridLayout_8.addWidget(self.input_view_plot_height, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 2, 0, 1, 1)
        self.tabs_view_tools.addWidget(self.page_list)
        self.gridLayout_3.addWidget(self.tabs_view_tools, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.tabs_tools.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 3, 0, 1, 1)
        self.input_plot_height = QtWidgets.QSpinBox(self.groupBox_4)
        self.input_plot_height.setMaximum(99999999)
        self.input_plot_height.setProperty("value", 600)
        self.input_plot_height.setObjectName("input_plot_height")
        self.gridLayout_9.addWidget(self.input_plot_height, 3, 1, 1, 1)
        self.input_plot_width = QtWidgets.QSpinBox(self.groupBox_4)
        self.input_plot_width.setMaximum(99999999)
        self.input_plot_width.setProperty("value", 1600)
        self.input_plot_width.setObjectName("input_plot_width")
        self.gridLayout_9.addWidget(self.input_plot_width, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout_9.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_4, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem4, 1, 0, 1, 1)
        self.tabs_tools.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.input_windowed_plots = QtWidgets.QCheckBox(self.groupBox)
        self.input_windowed_plots.setChecked(True)
        self.input_windowed_plots.setObjectName("input_windowed_plots")
        self.gridLayout_5.addWidget(self.input_windowed_plots, 0, 0, 1, 1)
        self.input_keep_tiled = QtWidgets.QCheckBox(self.groupBox)
        self.input_keep_tiled.setChecked(True)
        self.input_keep_tiled.setObjectName("input_keep_tiled")
        self.gridLayout_5.addWidget(self.input_keep_tiled, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        self.tabs_tools.addTab(self.tab_3, "")
        self.mdi_area = QtWidgets.QMdiArea(self.splitter)
        self.mdi_area.setLineWidth(0)
        self.mdi_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdi_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdi_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mdi_area.setViewMode(QtWidgets.QMdiArea.SubWindowView)
        self.mdi_area.setDocumentMode(False)
        self.mdi_area.setTabsClosable(False)
        self.mdi_area.setObjectName("mdi_area")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabs_tools.setCurrentIndex(0)
        self.tabs_view_tools.setCurrentIndex(1)
        self.input_max_selected_rows.valueChanged['int'].connect(Form.slot_set_max_selected_rows)
        self.pushButton.clicked.connect(self.input_header_items.clearSelection)
        self.input_windowed_plots.toggled['bool'].connect(Form.slot_set_windowed_plots)
        self.input_header_items.pressed['QModelIndex'].connect(Form.slot_selection_changed)
        self.input_master_row.currentTextChanged['QString'].connect(Form.slot_master_row_changed)
        self.splitter.splitterMoved['int','int'].connect(Form.slot_splitter_moved)
        self.input_view_scale_plots.toggled['bool'].connect(self.input_view_plot_height.setDisabled)
        self.button_list_view.toggled['bool'].connect(Form.slot_set_list_mode)
        self.button_zoom_view.toggled['bool'].connect(Form.slot_set_zoom_mode)
        self.input_view_plot_height.editingFinished.connect(Form.slot_set_list_min_height)
        self.input_view_scale_plots.clicked.connect(Form.slot_set_list_min_height)
        self.pushButton.clicked.connect(Form.slot_selection_changed)
        self.pushButton_2.clicked.connect(Form.slot_reset_zoom)
        self.input_keep_tiled.toggled['bool'].connect(Form.slot_keep_tiled_changed)
        self.pushButton_3.clicked.connect(Form.slot_export_to_pdf)
        self.pushButton_4.clicked.connect(Form.slot_export_to_csv)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Rows"))
        self.pushButton.setText(_translate("Form", "Clear"))
        self.label.setText(_translate("Form", "Max selected rows:"))
        self.groupBox_3.setTitle(_translate("Form", "View type"))
        self.button_list_view.setText(_translate("Form", " List"))
        self.button_zoom_view.setText(_translate("Form", " Zoom"))
        self.label_6.setText(_translate("Form", "To datetime:"))
        self.label_16.setText(_translate("Form", "Diff:"))
        self.input_to_dt.setDisplayFormat(_translate("Form", "MM/dd/yy hh:mm:ss"))
        self.label_2.setText(_translate("Form", "Master row:"))
        self.label_5.setText(_translate("Form", "From datetime:"))
        self.input_from_dt.setDisplayFormat(_translate("Form", "MM/dd/yy hh:mm:ss"))
        self.pushButton_2.setText(_translate("Form", "Reset zoom"))
        self.input_zoom_follow.setText(_translate("Form", "Zoom follow active window"))
        self.input_view_scale_plots.setText(_translate("Form", "Scale plots to fit windows"))
        self.input_view_plot_height.setSuffix(_translate("Form", " %"))
        self.input_view_plot_height.setPrefix(_translate("Form", "Plot height: "))
        self.tabs_tools.setTabText(self.tabs_tools.indexOf(self.tab), _translate("Form", "View"))
        self.groupBox_4.setTitle(_translate("Form", "Plots export"))
        self.label_3.setText(_translate("Form", "Width:"))
        self.label_4.setText(_translate("Form", "Height:"))
        self.input_plot_height.setSuffix(_translate("Form", " px"))
        self.input_plot_width.setSuffix(_translate("Form", " px"))
        self.pushButton_4.setText(_translate("Form", "Export to csv"))
        self.pushButton_3.setText(_translate("Form", "Export to pdf"))
        self.tabs_tools.setTabText(self.tabs_tools.indexOf(self.tab_2), _translate("Form", "Export"))
        self.groupBox.setTitle(_translate("Form", "Subplots"))
        self.input_windowed_plots.setText(_translate("Form", "Windowed plots"))
        self.input_keep_tiled.setText(_translate("Form", "Keep tiled"))
        self.tabs_tools.setTabText(self.tabs_tools.indexOf(self.tab_3), _translate("Form", "Settings"))
from kamzik3 import resource_kamzik3_rc
