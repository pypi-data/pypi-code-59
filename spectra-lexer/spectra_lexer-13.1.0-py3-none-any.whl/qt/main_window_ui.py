# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectra_lexer\qt\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 470)
        self.w_central = QtWidgets.QWidget(MainWindow)
        self.w_central.setObjectName("w_central")
        self.lt_central = QtWidgets.QGridLayout(self.w_central)
        self.lt_central.setContentsMargins(6, 6, 6, 6)
        self.lt_central.setObjectName("lt_central")
        self.w_input = QtWidgets.QLineEdit(self.w_central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_input.sizePolicy().hasHeightForWidth())
        self.w_input.setSizePolicy(sizePolicy)
        self.w_input.setReadOnly(False)
        self.w_input.setObjectName("w_input")
        self.lt_central.addWidget(self.w_input, 0, 0, 1, 1)
        self.w_title = QtWidgets.QLineEdit(self.w_central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_title.sizePolicy().hasHeightForWidth())
        self.w_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.w_title.setFont(font)
        self.w_title.setObjectName("w_title")
        self.lt_central.addWidget(self.w_title, 0, 1, 1, 1)
        self.w_matches = StringListView(self.w_central)
        self.w_matches.setAutoScroll(False)
        self.w_matches.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.w_matches.setProperty("showDropIndicator", False)
        self.w_matches.setObjectName("w_matches")
        self.lt_central.addWidget(self.w_matches, 1, 0, 1, 1)
        self.w_graph = HyperlinkTextBrowser(self.w_central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_graph.sizePolicy().hasHeightForWidth())
        self.w_graph.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.w_graph.setFont(font)
        self.w_graph.setMouseTracking(True)
        self.w_graph.setFrameShape(QtWidgets.QFrame.Box)
        self.w_graph.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.w_graph.setUndoRedoEnabled(False)
        self.w_graph.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.w_graph.setOpenLinks(False)
        self.w_graph.setObjectName("w_graph")
        self.lt_central.addWidget(self.w_graph, 1, 1, 1, 1)
        self.f_mappings = QtWidgets.QFrame(self.w_central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_mappings.sizePolicy().hasHeightForWidth())
        self.f_mappings.setSizePolicy(sizePolicy)
        self.f_mappings.setObjectName("f_mappings")
        self.lt_mappings = QtWidgets.QVBoxLayout(self.f_mappings)
        self.lt_mappings.setContentsMargins(0, 0, 0, 0)
        self.lt_mappings.setObjectName("lt_mappings")
        self.w_mappings = StringListView(self.f_mappings)
        self.w_mappings.setAutoScroll(False)
        self.w_mappings.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.w_mappings.setProperty("showDropIndicator", False)
        self.w_mappings.setObjectName("w_mappings")
        self.lt_mappings.addWidget(self.w_mappings)
        self.f_options = QtWidgets.QFrame(self.f_mappings)
        self.f_options.setObjectName("f_options")
        self.lt_options = QtWidgets.QHBoxLayout(self.f_options)
        self.lt_options.setContentsMargins(0, 3, 0, 3)
        self.lt_options.setObjectName("lt_options")
        self.f_chk = QtWidgets.QFrame(self.f_options)
        self.f_chk.setObjectName("f_chk")
        self.lt_chk = QtWidgets.QVBoxLayout(self.f_chk)
        self.lt_chk.setContentsMargins(0, 0, 0, 0)
        self.lt_chk.setObjectName("lt_chk")
        self.w_strokes = QtWidgets.QCheckBox(self.f_chk)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_strokes.sizePolicy().hasHeightForWidth())
        self.w_strokes.setSizePolicy(sizePolicy)
        self.w_strokes.setObjectName("w_strokes")
        self.lt_chk.addWidget(self.w_strokes)
        self.w_regex = QtWidgets.QCheckBox(self.f_chk)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_regex.sizePolicy().hasHeightForWidth())
        self.w_regex.setSizePolicy(sizePolicy)
        self.w_regex.setObjectName("w_regex")
        self.lt_chk.addWidget(self.w_regex)
        self.lt_options.addWidget(self.f_chk)
        self.ln_options = QtWidgets.QFrame(self.f_options)
        self.ln_options.setFrameShape(QtWidgets.QFrame.VLine)
        self.ln_options.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ln_options.setObjectName("ln_options")
        self.lt_options.addWidget(self.ln_options)
        self.f_sl = QtWidgets.QFrame(self.f_options)
        self.f_sl.setObjectName("f_sl")
        self.lt_sl = QtWidgets.QVBoxLayout(self.f_sl)
        self.lt_sl.setContentsMargins(0, 0, 0, 0)
        self.lt_sl.setObjectName("lt_sl")
        self.sl0 = QtWidgets.QLabel(self.f_sl)
        self.sl0.setObjectName("sl0")
        self.lt_sl.addWidget(self.sl0)
        self.sl1 = QtWidgets.QLabel(self.f_sl)
        self.sl1.setObjectName("sl1")
        self.lt_sl.addWidget(self.sl1)
        self.sl2 = QtWidgets.QLabel(self.f_sl)
        self.sl2.setObjectName("sl2")
        self.lt_sl.addWidget(self.sl2)
        self.lt_options.addWidget(self.f_sl)
        self.w_slider = QtWidgets.QSlider(self.f_options)
        self.w_slider.setMaximum(2)
        self.w_slider.setProperty("value", 2)
        self.w_slider.setOrientation(QtCore.Qt.Vertical)
        self.w_slider.setInvertedAppearance(True)
        self.w_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.w_slider.setObjectName("w_slider")
        self.lt_options.addWidget(self.w_slider)
        self.lt_mappings.addWidget(self.f_options)
        self.lt_mappings.setStretch(0, 100)
        self.lt_mappings.setStretch(1, 1)
        self.lt_central.addWidget(self.f_mappings, 2, 0, 1, 1)
        self.f_info = QtWidgets.QFrame(self.w_central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_info.sizePolicy().hasHeightForWidth())
        self.f_info.setSizePolicy(sizePolicy)
        self.f_info.setFrameShape(QtWidgets.QFrame.Box)
        self.f_info.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_info.setObjectName("f_info")
        self.lt_info = QtWidgets.QGridLayout(self.f_info)
        self.lt_info.setContentsMargins(6, 6, 6, 6)
        self.lt_info.setObjectName("lt_info")
        self.lt_info_main = QtWidgets.QVBoxLayout()
        self.lt_info_main.setSpacing(2)
        self.lt_info_main.setObjectName("lt_info_main")
        self.w_caption = QtWidgets.QLabel(self.f_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_caption.sizePolicy().hasHeightForWidth())
        self.w_caption.setSizePolicy(sizePolicy)
        self.w_caption.setMaximumSize(QtCore.QSize(16777215, 64))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.w_caption.setFont(font)
        self.w_caption.setAlignment(QtCore.Qt.AlignCenter)
        self.w_caption.setWordWrap(True)
        self.w_caption.setObjectName("w_caption")
        self.lt_info_main.addWidget(self.w_caption)
        self.w_board = PictureWidget(self.f_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_board.sizePolicy().hasHeightForWidth())
        self.w_board.setSizePolicy(sizePolicy)
        self.w_board.setMinimumSize(QtCore.QSize(0, 100))
        self.w_board.setObjectName("w_board")
        self.lt_info_main.addWidget(self.w_board)
        self.lt_info.addLayout(self.lt_info_main, 0, 0, 2, 1)
        self.lt_info_links = QtWidgets.QHBoxLayout()
        self.lt_info_links.setObjectName("lt_info_links")
        self.w_link_save = QtWidgets.QLabel(self.f_info)
        self.w_link_save.setTextFormat(QtCore.Qt.RichText)
        self.w_link_save.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.w_link_save.setObjectName("w_link_save")
        self.lt_info_links.addWidget(self.w_link_save)
        self.w_link_examples = QtWidgets.QLabel(self.f_info)
        self.w_link_examples.setTextFormat(QtCore.Qt.RichText)
        self.w_link_examples.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.w_link_examples.setObjectName("w_link_examples")
        self.lt_info_links.addWidget(self.w_link_examples)
        self.lt_info.addLayout(self.lt_info_links, 1, 0, 1, 1)
        self.lt_info.setRowStretch(0, 1)
        self.lt_central.addWidget(self.f_info, 2, 1, 1, 1)
        self.lt_central.setColumnMinimumWidth(0, 150)
        self.lt_central.setColumnMinimumWidth(1, 250)
        self.lt_central.setRowMinimumHeight(0, 22)
        self.lt_central.setRowMinimumHeight(1, 150)
        self.lt_central.setRowMinimumHeight(2, 150)
        self.lt_central.setColumnStretch(0, 1)
        self.lt_central.setColumnStretch(1, 100)
        self.lt_central.setRowStretch(0, 1)
        self.lt_central.setRowStretch(1, 100)
        self.lt_central.setRowStretch(2, 80)
        MainWindow.setCentralWidget(self.w_central)
        self.w_menubar = QtWidgets.QMenuBar(MainWindow)
        self.w_menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.w_menubar.setObjectName("w_menubar")
        MainWindow.setMenuBar(self.w_menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spectra Lexer"))
        self.w_input.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.w_graph.setPlaceholderText(_translate("MainWindow", "Search for any word to see its breakdown."))
        self.w_strokes.setText(_translate("MainWindow", "Stroke Search"))
        self.w_regex.setText(_translate("MainWindow", "Regex Search"))
        self.sl0.setText(_translate("MainWindow", "Key"))
        self.sl1.setText(_translate("MainWindow", "Snd"))
        self.sl2.setText(_translate("MainWindow", "Txt"))
        self.w_link_save.setText(_translate("MainWindow", "<a href=\'dummy\'>Save</a>"))
        self.w_link_examples.setText(_translate("MainWindow", "<a href=\'dummy\'>More Examples</a>"))
from .widgets import HyperlinkTextBrowser, PictureWidget, StringListView
