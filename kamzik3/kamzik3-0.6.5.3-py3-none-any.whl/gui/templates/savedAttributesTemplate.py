# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'savedAttributesTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(974, 644)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.button_set_value = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_set_value.sizePolicy().hasHeightForWidth())
        self.button_set_value.setSizePolicy(sizePolicy)
        self.button_set_value.setMinimumSize(QtCore.QSize(35, 35))
        self.button_set_value.setMaximumSize(QtCore.QSize(40, 40))
        self.button_set_value.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/target.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_set_value.setIcon(icon)
        self.button_set_value.setIconSize(QtCore.QSize(25, 25))
        self.button_set_value.setObjectName("button_set_value")
        self.verticalLayout.addWidget(self.button_set_value)
        spacerItem1 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.button_change_color = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_change_color.sizePolicy().hasHeightForWidth())
        self.button_change_color.setSizePolicy(sizePolicy)
        self.button_change_color.setMinimumSize(QtCore.QSize(35, 35))
        self.button_change_color.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_change_color.setFont(font)
        self.button_change_color.setStyleSheet("QPushButton {color:red}")
        self.button_change_color.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/color_picker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_change_color.setIcon(icon1)
        self.button_change_color.setIconSize(QtCore.QSize(25, 25))
        self.button_change_color.setObjectName("button_change_color")
        self.verticalLayout.addWidget(self.button_change_color)
        self.button_move_top = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_move_top.sizePolicy().hasHeightForWidth())
        self.button_move_top.setSizePolicy(sizePolicy)
        self.button_move_top.setMinimumSize(QtCore.QSize(35, 35))
        self.button_move_top.setMaximumSize(QtCore.QSize(40, 40))
        self.button_move_top.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_top.setIcon(icon2)
        self.button_move_top.setIconSize(QtCore.QSize(25, 25))
        self.button_move_top.setObjectName("button_move_top")
        self.verticalLayout.addWidget(self.button_move_top)
        self.button_move_up = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_move_up.sizePolicy().hasHeightForWidth())
        self.button_move_up.setSizePolicy(sizePolicy)
        self.button_move_up.setMinimumSize(QtCore.QSize(35, 35))
        self.button_move_up.setMaximumSize(QtCore.QSize(40, 40))
        self.button_move_up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_up.setIcon(icon3)
        self.button_move_up.setIconSize(QtCore.QSize(25, 25))
        self.button_move_up.setCheckable(False)
        self.button_move_up.setChecked(False)
        self.button_move_up.setObjectName("button_move_up")
        self.verticalLayout.addWidget(self.button_move_up)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.button_remove = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_remove.sizePolicy().hasHeightForWidth())
        self.button_remove.setSizePolicy(sizePolicy)
        self.button_remove.setMinimumSize(QtCore.QSize(35, 35))
        self.button_remove.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_remove.setFont(font)
        self.button_remove.setStyleSheet("QPushButton {color:red}")
        self.button_remove.setIconSize(QtCore.QSize(0, 0))
        self.button_remove.setObjectName("button_remove")
        self.verticalLayout.addWidget(self.button_remove)
        self.button_add = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        self.button_add.setMinimumSize(QtCore.QSize(35, 35))
        self.button_add.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("QPushButton {color:green}")
        self.button_add.setIconSize(QtCore.QSize(0, 0))
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.button_move_down = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_move_down.sizePolicy().hasHeightForWidth())
        self.button_move_down.setSizePolicy(sizePolicy)
        self.button_move_down.setMinimumSize(QtCore.QSize(35, 35))
        self.button_move_down.setMaximumSize(QtCore.QSize(40, 40))
        self.button_move_down.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_down.setIcon(icon4)
        self.button_move_down.setIconSize(QtCore.QSize(25, 25))
        self.button_move_down.setObjectName("button_move_down")
        self.verticalLayout.addWidget(self.button_move_down)
        self.button_move_bottom = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_move_bottom.sizePolicy().hasHeightForWidth())
        self.button_move_bottom.setSizePolicy(sizePolicy)
        self.button_move_bottom.setMinimumSize(QtCore.QSize(35, 35))
        self.button_move_bottom.setMaximumSize(QtCore.QSize(40, 40))
        self.button_move_bottom.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move_bottom.setIcon(icon5)
        self.button_move_bottom.setIconSize(QtCore.QSize(25, 25))
        self.button_move_bottom.setObjectName("button_move_bottom")
        self.verticalLayout.addWidget(self.button_move_bottom)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.tab_groups = QtWidgets.QTabWidget(Form)
        self.tab_groups.setObjectName("tab_groups")
        self.gridLayout.addWidget(self.tab_groups, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_reset_all = QtWidgets.QPushButton(Form)
        self.button_reset_all.setToolTip("")
        self.button_reset_all.setStyleSheet("QPushButton { background-color: #ff4e00 }\\\\nQPushButton:pressed { background-color: #ff4e00 }\\\\nQPushButton:!enabled{background:silver;}QPushButton:checked{background:red;}\\nQPushButton:disabled{ background:silver;color:grey }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/reset_bw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_reset_all.setIcon(icon6)
        self.button_reset_all.setIconSize(QtCore.QSize(16, 16))
        self.button_reset_all.setObjectName("button_reset_all")
        self.horizontalLayout.addWidget(self.button_reset_all)
        self.button_load = QtWidgets.QPushButton(Form)
        self.button_load.setToolTip("")
        self.button_load.setStyleSheet("QPushButton { background-color: #00b4ff }\\nQPushButton:pressed { background-color: #28a900 }\\nQPushButton:!enabled{background:silver;}QPushButton:checked{background:red;}\n"
"QPushButton:disabled{ background:silver;color:grey }")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/load_bw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_load.setIcon(icon7)
        self.button_load.setIconSize(QtCore.QSize(16, 16))
        self.button_load.setObjectName("button_load")
        self.horizontalLayout.addWidget(self.button_load)
        self.checkbox_allow_double_click = QtWidgets.QCheckBox(Form)
        self.checkbox_allow_double_click.setObjectName("checkbox_allow_double_click")
        self.horizontalLayout.addWidget(self.checkbox_allow_double_click)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.checkbox_synced_with_server = QtWidgets.QCheckBox(Form)
        self.checkbox_synced_with_server.setEnabled(False)
        self.checkbox_synced_with_server.setCheckable(True)
        self.checkbox_synced_with_server.setChecked(False)
        self.checkbox_synced_with_server.setObjectName("checkbox_synced_with_server")
        self.horizontalLayout.addWidget(self.checkbox_synced_with_server)
        self.button_save = QtWidgets.QPushButton(Form)
        self.button_save.setToolTip("")
        self.button_save.setStyleSheet("QPushButton { background-color: #00b4ff }\\nQPushButton:pressed { background-color: #28a900 }\\nQPushButton:!enabled{background:silver;}QPushButton:checked{background:red;}\n"
"QPushButton:disabled{ background:silver;color:grey }")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/save_bw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save.setIcon(icon8)
        self.button_save.setIconSize(QtCore.QSize(16, 16))
        self.button_save.setObjectName("button_save")
        self.horizontalLayout.addWidget(self.button_save)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.groups_frame = QtWidgets.QFrame(Form)
        self.groups_frame.setStyleSheet("QFrame#groups_frame {background-color:#f6b442}")
        self.groups_frame.setObjectName("groups_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groups_frame)
        self.horizontalLayout_3.setContentsMargins(6, 2, 6, 2)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_saved_groups = QtWidgets.QLabel(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_saved_groups.sizePolicy().hasHeightForWidth())
        self.label_saved_groups.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_saved_groups.setFont(font)
        self.label_saved_groups.setObjectName("label_saved_groups")
        self.horizontalLayout_3.addWidget(self.label_saved_groups)
        self.combo_preset = QtWidgets.QComboBox(self.groups_frame)
        self.combo_preset.setMinimumSize(QtCore.QSize(200, 0))
        self.combo_preset.setObjectName("combo_preset")
        self.horizontalLayout_3.addWidget(self.combo_preset)
        self.button_remove_preset_group = QtWidgets.QPushButton(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_remove_preset_group.sizePolicy().hasHeightForWidth())
        self.button_remove_preset_group.setSizePolicy(sizePolicy)
        self.button_remove_preset_group.setMinimumSize(QtCore.QSize(25, 0))
        self.button_remove_preset_group.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_remove_preset_group.setFont(font)
        self.button_remove_preset_group.setStyleSheet("QPushButton {color:red}")
        self.button_remove_preset_group.setIconSize(QtCore.QSize(0, 0))
        self.button_remove_preset_group.setObjectName("button_remove_preset_group")
        self.horizontalLayout_3.addWidget(self.button_remove_preset_group)
        self.button_add_preset_group = QtWidgets.QPushButton(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add_preset_group.sizePolicy().hasHeightForWidth())
        self.button_add_preset_group.setSizePolicy(sizePolicy)
        self.button_add_preset_group.setMinimumSize(QtCore.QSize(25, 0))
        self.button_add_preset_group.setMaximumSize(QtCore.QSize(69, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_add_preset_group.setFont(font)
        self.button_add_preset_group.setStyleSheet("QPushButton {color:green}")
        self.button_add_preset_group.setIconSize(QtCore.QSize(0, 0))
        self.button_add_preset_group.setObjectName("button_add_preset_group")
        self.horizontalLayout_3.addWidget(self.button_add_preset_group)
        self.button_add_preset_group_from_selected_rows = QtWidgets.QPushButton(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add_preset_group_from_selected_rows.sizePolicy().hasHeightForWidth())
        self.button_add_preset_group_from_selected_rows.setSizePolicy(sizePolicy)
        self.button_add_preset_group_from_selected_rows.setMinimumSize(QtCore.QSize(25, 0))
        self.button_add_preset_group_from_selected_rows.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_add_preset_group_from_selected_rows.setFont(font)
        self.button_add_preset_group_from_selected_rows.setStyleSheet("QPushButton {color:green}")
        self.button_add_preset_group_from_selected_rows.setIconSize(QtCore.QSize(0, 0))
        self.button_add_preset_group_from_selected_rows.setObjectName("button_add_preset_group_from_selected_rows")
        self.horizontalLayout_3.addWidget(self.button_add_preset_group_from_selected_rows)
        self.button_confirm_rows_selection = QtWidgets.QPushButton(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_confirm_rows_selection.sizePolicy().hasHeightForWidth())
        self.button_confirm_rows_selection.setSizePolicy(sizePolicy)
        self.button_confirm_rows_selection.setMinimumSize(QtCore.QSize(25, 0))
        self.button_confirm_rows_selection.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_confirm_rows_selection.setFont(font)
        self.button_confirm_rows_selection.setStyleSheet("QPushButton {color:green}")
        self.button_confirm_rows_selection.setIconSize(QtCore.QSize(0, 0))
        self.button_confirm_rows_selection.setObjectName("button_confirm_rows_selection")
        self.horizontalLayout_3.addWidget(self.button_confirm_rows_selection)
        self.button_cancel_rows_selection = QtWidgets.QPushButton(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel_rows_selection.sizePolicy().hasHeightForWidth())
        self.button_cancel_rows_selection.setSizePolicy(sizePolicy)
        self.button_cancel_rows_selection.setMinimumSize(QtCore.QSize(25, 0))
        self.button_cancel_rows_selection.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_cancel_rows_selection.setFont(font)
        self.button_cancel_rows_selection.setStyleSheet("QPushButton {color:red}")
        self.button_cancel_rows_selection.setIconSize(QtCore.QSize(0, 0))
        self.button_cancel_rows_selection.setObjectName("button_cancel_rows_selection")
        self.horizontalLayout_3.addWidget(self.button_cancel_rows_selection)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.gridLayout.addWidget(self.groups_frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tab_groups.setCurrentIndex(-1)
        self.button_move_top.clicked.connect(Form.move_rows_top)
        self.button_move_up.clicked.connect(Form.move_rows_up)
        self.button_move_down.clicked.connect(Form.move_rows_down)
        self.button_move_bottom.clicked.connect(Form.move_rows_bottom)
        self.button_remove.clicked.connect(Form.remove_rows)
        self.button_add.clicked.connect(Form.add_row)
        self.button_save.clicked.connect(Form.save)
        self.button_load.clicked.connect(Form.load)
        self.button_reset_all.clicked.connect(Form.reset_all)
        self.button_change_color.clicked.connect(Form.select_color)
        self.button_set_value.clicked.connect(Form.set_attribute_value)
        self.button_add_preset_group.clicked.connect(Form.add_preset_group)
        self.button_remove_preset_group.clicked.connect(Form.remove_preset_group)
        self.button_add_preset_group_from_selected_rows.clicked['bool'].connect(Form.add_preset_group_from_selected)
        self.combo_preset.currentIndexChanged['QString'].connect(Form.preset_group_changed)
        self.button_confirm_rows_selection.clicked.connect(Form.confirm_rows_selection)
        self.button_cancel_rows_selection.clicked.connect(Form.cancel_rows_selection)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_set_value.setToolTip(_translate("Form", "Set attribute to saved value"))
        self.button_change_color.setToolTip(_translate("Form", "Change row color"))
        self.button_move_top.setToolTip(_translate("Form", "Move row to the top"))
        self.button_move_up.setToolTip(_translate("Form", "Move row up"))
        self.button_remove.setToolTip(_translate("Form", "Remove row"))
        self.button_remove.setText(_translate("Form", "-"))
        self.button_add.setToolTip(_translate("Form", "Add row"))
        self.button_add.setText(_translate("Form", "+"))
        self.button_move_down.setToolTip(_translate("Form", "Move row down"))
        self.button_move_bottom.setToolTip(_translate("Form", "Move row to the bottom"))
        self.button_reset_all.setText(_translate("Form", "Reset"))
        self.button_load.setText(_translate("Form", "Load from file"))
        self.checkbox_allow_double_click.setText(_translate("Form", "Double click sets value"))
        self.checkbox_synced_with_server.setText(_translate("Form", "Synced"))
        self.button_save.setText(_translate("Form", "Save to file"))
        self.label_saved_groups.setText(_translate("Form", "Preset groups:"))
        self.button_remove_preset_group.setToolTip(_translate("Form", "Remove selected group"))
        self.button_remove_preset_group.setText(_translate("Form", "-"))
        self.button_add_preset_group.setToolTip(_translate("Form", "Add new save group"))
        self.button_add_preset_group.setText(_translate("Form", "+ Empty"))
        self.button_add_preset_group_from_selected_rows.setToolTip(_translate("Form", "Add new save group"))
        self.button_add_preset_group_from_selected_rows.setText(_translate("Form", "+ From selected rows"))
        self.button_confirm_rows_selection.setToolTip(_translate("Form", "Add new save group"))
        self.button_confirm_rows_selection.setText(_translate("Form", "Confirm selected rows"))
        self.button_cancel_rows_selection.setToolTip(_translate("Form", "Add new save group"))
        self.button_cancel_rows_selection.setText(_translate("Form", "Cancel"))

from kamzik3 import resource_kamzik3_rc
