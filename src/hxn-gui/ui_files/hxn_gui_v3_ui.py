# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hxn_gui_v3.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from qtpy.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from qtpy.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolBox, QVBoxLayout,
    QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(1334, 1741)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        window.setFont(font)
        icon = QIcon()
        icon.addFile(u":/hxnlogo/Profile-NEW-NSLS-II.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        window.setWindowIcon(icon)
        window.setStyleSheet(u"")
        window.setAnimated(True)
        window.setTabShape(QTabWidget.Rounded)
        self.actionScreenshot_tool = QAction(window)
        self.actionScreenshot_tool.setObjectName(u"actionScreenshot_tool")
        self.actionWeb_Browser = QAction(window)
        self.actionWeb_Browser.setObjectName(u"actionWeb_Browser")
        self.actionImagej = QAction(window)
        self.actionImagej.setObjectName(u"actionImagej")
        self.actionImage_Correlation_tool = QAction(window)
        self.actionImage_Correlation_tool.setObjectName(u"actionImage_Correlation_tool")
        self.actionOpen_a_Batch_File = QAction(window)
        self.actionOpen_a_Batch_File.setObjectName(u"actionOpen_a_Batch_File")
        self.actionSave_Batch_File = QAction(window)
        self.actionSave_Batch_File.setObjectName(u"actionSave_Batch_File")
        self.actionClose_Application = QAction(window)
        self.actionClose_Application.setObjectName(u"actionClose_Application")
        self.actionRestart = QAction(window)
        self.actionRestart.setObjectName(u"actionRestart")
        self.actionExit = QAction(window)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.TabFocus)
        self.centralwidget.setStyleSheet(u"\n"
"QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } \n"
"\n"
"")
        self.gridLayout_98 = QGridLayout(self.centralwidget)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.pbar_flyscan = QProgressBar(self.centralwidget)
        self.pbar_flyscan.setObjectName(u"pbar_flyscan")
        self.pbar_flyscan.setEnabled(False)
        self.pbar_flyscan.setStyleSheet(u"selection-color: rgb(78, 154, 6);")
        self.pbar_flyscan.setValue(0)

        self.gridLayout_98.addWidget(self.pbar_flyscan, 3, 0, 1, 1)

        self.label_scanStatus = QLabel(self.centralwidget)
        self.label_scanStatus.setObjectName(u"label_scanStatus")
        self.label_scanStatus.setAlignment(Qt.AlignCenter)

        self.gridLayout_98.addWidget(self.label_scanStatus, 5, 0, 1, 1)

        self.gridLayout_52 = QGridLayout()
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setStyleSheet(u"font: 30pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 225, 172);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.label_14, 0, 0, 2, 1)

        self.gridLayout_45 = QGridLayout()
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_97 = QGridLayout()
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.db_flytube_p = QDoubleSpinBox(self.centralwidget)
        self.db_flytube_p.setObjectName(u"db_flytube_p")
        self.db_flytube_p.setStyleSheet(u"font: 75 22pt \"C059\";")
        self.db_flytube_p.setReadOnly(True)
        self.db_flytube_p.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_flytube_p.setDecimals(1)
        self.db_flytube_p.setMinimum(-3.000000000000000)
        self.db_flytube_p.setValue(1.000000000000000)

        self.gridLayout_97.addWidget(self.db_flytube_p, 0, 1, 1, 1)

        self.label_138 = QLabel(self.centralwidget)
        self.label_138.setObjectName(u"label_138")
        sizePolicy1.setHeightForWidth(self.label_138.sizePolicy().hasHeightForWidth())
        self.label_138.setSizePolicy(sizePolicy1)
        self.label_138.setStyleSheet(u"font: 75 15pt \"Cantarell\";")
        self.label_138.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_97.addWidget(self.label_138, 0, 0, 1, 1)


        self.gridLayout_45.addLayout(self.gridLayout_97, 0, 0, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_79 = QLabel(self.centralwidget)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"font: 75 15pt \"Cantarell\";")
        self.label_79.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_79, 0, 0, 1, 1)

        self.lcd_scanNumber = QDoubleSpinBox(self.centralwidget)
        self.lcd_scanNumber.setObjectName(u"lcd_scanNumber")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lcd_scanNumber.sizePolicy().hasHeightForWidth())
        self.lcd_scanNumber.setSizePolicy(sizePolicy2)
        self.lcd_scanNumber.setStyleSheet(u"font: 75 22pt \"C059\";")
        self.lcd_scanNumber.setReadOnly(True)
        self.lcd_scanNumber.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lcd_scanNumber.setDecimals(0)
        self.lcd_scanNumber.setMinimum(1.000000000000000)
        self.lcd_scanNumber.setMaximum(999999.000000000000000)
        self.lcd_scanNumber.setValue(222222.000000000000000)

        self.gridLayout_21.addWidget(self.lcd_scanNumber, 0, 1, 1, 1)


        self.gridLayout_45.addLayout(self.gridLayout_21, 0, 1, 1, 1)

        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_122 = QLabel(self.centralwidget)
        self.label_122.setObjectName(u"label_122")
        sizePolicy1.setHeightForWidth(self.label_122.sizePolicy().hasHeightForWidth())
        self.label_122.setSizePolicy(sizePolicy1)
        self.label_122.setStyleSheet(u"font: 75 20pt \"Cantarell\";")
        self.label_122.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_44.addWidget(self.label_122, 0, 0, 1, 1)

        self.lcd_ic3 = QDoubleSpinBox(self.centralwidget)
        self.lcd_ic3.setObjectName(u"lcd_ic3")
        sizePolicy2.setHeightForWidth(self.lcd_ic3.sizePolicy().hasHeightForWidth())
        self.lcd_ic3.setSizePolicy(sizePolicy2)
        self.lcd_ic3.setStyleSheet(u"font: 75 22pt \"C059\";")
        self.lcd_ic3.setReadOnly(True)
        self.lcd_ic3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lcd_ic3.setDecimals(0)
        self.lcd_ic3.setMaximum(99999999.000000000000000)
        self.lcd_ic3.setValue(333333.000000000000000)

        self.gridLayout_44.addWidget(self.lcd_ic3, 0, 1, 1, 1)


        self.gridLayout_45.addLayout(self.gridLayout_44, 0, 2, 1, 1)

        self.gridLayout_93 = QGridLayout()
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.lcd_monoE = QDoubleSpinBox(self.centralwidget)
        self.lcd_monoE.setObjectName(u"lcd_monoE")
        self.lcd_monoE.setStyleSheet(u"font: 75 22pt \"C059\";")
        self.lcd_monoE.setReadOnly(True)
        self.lcd_monoE.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lcd_monoE.setDecimals(3)
        self.lcd_monoE.setMinimum(4.000000000000000)
        self.lcd_monoE.setValue(12.000000000000000)

        self.gridLayout_93.addWidget(self.lcd_monoE, 0, 1, 1, 1)

        self.label_123 = QLabel(self.centralwidget)
        self.label_123.setObjectName(u"label_123")
        sizePolicy1.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy1)
        self.label_123.setStyleSheet(u"font: 75 15pt \"Cantarell\";")
        self.label_123.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_93.addWidget(self.label_123, 0, 0, 1, 1)


        self.gridLayout_45.addLayout(self.gridLayout_93, 0, 3, 1, 1)


        self.gridLayout_52.addLayout(self.gridLayout_45, 0, 1, 1, 1)

        self.gridLayout_50 = QGridLayout()
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setHorizontalSpacing(40)
        self.gridLayout_50.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(12)
        self.pb_open_b_shutter = QPushButton(self.centralwidget)
        self.pb_open_b_shutter.setObjectName(u"pb_open_b_shutter")
        sizePolicy2.setHeightForWidth(self.pb_open_b_shutter.sizePolicy().hasHeightForWidth())
        self.pb_open_b_shutter.setSizePolicy(sizePolicy2)
        self.pb_open_b_shutter.setStyleSheet(u"color: rgb(78, 154, 6);\n"
"background-color: rgb(186, 189, 182);")

        self.gridLayout_9.addWidget(self.pb_open_b_shutter, 0, 0, 1, 1)

        self.pb_close_b_shutter = QPushButton(self.centralwidget)
        self.pb_close_b_shutter.setObjectName(u"pb_close_b_shutter")
        sizePolicy2.setHeightForWidth(self.pb_close_b_shutter.sizePolicy().hasHeightForWidth())
        self.pb_close_b_shutter.setSizePolicy(sizePolicy2)
        self.pb_close_b_shutter.setStyleSheet(u"color: rgb(164, 0, 0);\n"
"background-color: rgb(186, 189, 182);")

        self.gridLayout_9.addWidget(self.pb_close_b_shutter, 0, 1, 1, 1)


        self.gridLayout_50.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.gridLayout_49 = QGridLayout()
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setHorizontalSpacing(12)
        self.pb_open_c_shutter = QPushButton(self.centralwidget)
        self.pb_open_c_shutter.setObjectName(u"pb_open_c_shutter")
        sizePolicy2.setHeightForWidth(self.pb_open_c_shutter.sizePolicy().hasHeightForWidth())
        self.pb_open_c_shutter.setSizePolicy(sizePolicy2)
        self.pb_open_c_shutter.setStyleSheet(u"color: rgb(78, 154, 6);\n"
"background-color: rgb(186, 189, 182);")

        self.gridLayout_49.addWidget(self.pb_open_c_shutter, 0, 1, 1, 1)

        self.pb_close_c_shutter = QPushButton(self.centralwidget)
        self.pb_close_c_shutter.setObjectName(u"pb_close_c_shutter")
        sizePolicy2.setHeightForWidth(self.pb_close_c_shutter.sizePolicy().hasHeightForWidth())
        self.pb_close_c_shutter.setSizePolicy(sizePolicy2)
        self.pb_close_c_shutter.setStyleSheet(u"color: rgb(164, 0, 0);\n"
"background-color: rgb(186, 189, 182);")

        self.gridLayout_49.addWidget(self.pb_close_c_shutter, 0, 2, 1, 1)


        self.gridLayout_50.addLayout(self.gridLayout_49, 0, 1, 1, 1)


        self.gridLayout_52.addLayout(self.gridLayout_50, 1, 1, 1, 1)


        self.gridLayout_98.addLayout(self.gridLayout_52, 0, 0, 1, 1)

        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.HXN_GUI_tabs = QTabWidget(self.centralwidget)
        self.HXN_GUI_tabs.setObjectName(u"HXN_GUI_tabs")
        self.HXN_GUI_tabs.setEnabled(True)
        sizePolicy.setHeightForWidth(self.HXN_GUI_tabs.sizePolicy().hasHeightForWidth())
        self.HXN_GUI_tabs.setSizePolicy(sizePolicy)
        self.HXN_GUI_tabs.setFont(font)
        self.HXN_GUI_tabs.setFocusPolicy(Qt.StrongFocus)
        self.HXN_GUI_tabs.setLayoutDirection(Qt.LeftToRight)
        self.HXN_GUI_tabs.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #555;\n"
"border-radius: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.1,\n"
"fx: 0.7, fy: 0.1,\n"
"radius: 1, stop: 0 #fff, stop: 1 #888);\n"
"	background-color: rgb(188, 191, 185);\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: green;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position:top  left;\n"
"}\n"
"\n"
"QGroupBox { \n"
"     border: 1.5px solid gray; \n"
"     border-radius: 3px; \n"
"	 font-size:18px;\n"
"	 font-weight: bold;\n"
" } \n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 0); \n"
"	}\n"
"\n"
"QPushButton:pressed{ \n"
"	background-color: rgb(0,255, 0); \n"
"	}\n"
"\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	w"
                        "idth: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(255, 200, 0);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(0,200, 0);\n"
"	border: 3px solid rgb(0,0,0);	\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background: 3px solid rgb(255,255, 255);\n"
"	border: 3px solid rgb(0,0, 0);	\n"
"}\n"
"\n"
"\n"
"	")
        self.HXN_GUI_tabs.setTabPosition(QTabWidget.North)
        self.HXN_GUI_tabs.setDocumentMode(True)
        self.HXN_GUI_tabs.setTabsClosable(False)
        self.HXN_GUI_tabs.setMovable(True)
        self.HXN_GUI_tabs.setTabBarAutoHide(False)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_142 = QGridLayout(self.tab_4)
        self.gridLayout_142.setObjectName(u"gridLayout_142")
        self.groupBox_7 = QGroupBox(self.tab_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_40 = QGridLayout(self.groupBox_7)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setVerticalSpacing(25)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(25)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_update_xrf_elems = QPushButton(self.groupBox_7)
        self.pb_update_xrf_elems.setObjectName(u"pb_update_xrf_elems")
        sizePolicy2.setHeightForWidth(self.pb_update_xrf_elems.sizePolicy().hasHeightForWidth())
        self.pb_update_xrf_elems.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.pb_update_xrf_elems)

        self.pb_import_xrf_elem_list = QPushButton(self.groupBox_7)
        self.pb_import_xrf_elem_list.setObjectName(u"pb_import_xrf_elem_list")

        self.horizontalLayout_4.addWidget(self.pb_import_xrf_elem_list)

        self.pb_export_xrf_elem_list = QPushButton(self.groupBox_7)
        self.pb_export_xrf_elem_list.setObjectName(u"pb_export_xrf_elem_list")

        self.horizontalLayout_4.addWidget(self.pb_export_xrf_elem_list)


        self.gridLayout_40.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setVerticalSpacing(12)
        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.le_roi_elems = QLineEdit(self.groupBox_7)
        self.le_roi_elems.setObjectName(u"le_roi_elems")

        self.gridLayout_35.addWidget(self.le_roi_elems, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_35.addWidget(self.label_16, 0, 0, 1, 1)


        self.gridLayout_38.addLayout(self.gridLayout_35, 0, 0, 1, 1)

        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_36.addWidget(self.label_19, 0, 0, 1, 1)

        self.sb_live_elem_num = QSpinBox(self.groupBox_7)
        self.sb_live_elem_num.setObjectName(u"sb_live_elem_num")
        sizePolicy.setHeightForWidth(self.sb_live_elem_num.sizePolicy().hasHeightForWidth())
        self.sb_live_elem_num.setSizePolicy(sizePolicy)
        self.sb_live_elem_num.setMinimum(2)
        self.sb_live_elem_num.setMaximum(8)
        self.sb_live_elem_num.setSingleStep(2)
        self.sb_live_elem_num.setValue(4)

        self.gridLayout_36.addWidget(self.sb_live_elem_num, 0, 1, 1, 1)

        self.le_live_elems = QLineEdit(self.groupBox_7)
        self.le_live_elems.setObjectName(u"le_live_elems")

        self.gridLayout_36.addWidget(self.le_live_elems, 0, 3, 1, 1)

        self.label_25 = QLabel(self.groupBox_7)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_36.addWidget(self.label_25, 0, 2, 1, 1)


        self.gridLayout_38.addLayout(self.gridLayout_36, 1, 0, 1, 1)

        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.le_line_elem = QLineEdit(self.groupBox_7)
        self.le_line_elem.setObjectName(u"le_line_elem")

        self.gridLayout_37.addWidget(self.le_line_elem, 0, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_7)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_37.addWidget(self.label_20, 0, 0, 1, 1)


        self.gridLayout_38.addLayout(self.gridLayout_37, 2, 0, 1, 1)


        self.gridLayout_40.addLayout(self.gridLayout_38, 3, 0, 1, 1)

        self.xrf_elem_cb_widget = QGroupBox(self.groupBox_7)
        self.xrf_elem_cb_widget.setObjectName(u"xrf_elem_cb_widget")
        sizePolicy2.setHeightForWidth(self.xrf_elem_cb_widget.sizePolicy().hasHeightForWidth())
        self.xrf_elem_cb_widget.setSizePolicy(sizePolicy2)
        self.gridLayout_41 = QGridLayout(self.xrf_elem_cb_widget)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setVerticalSpacing(15)
        self.label_22 = QLabel(self.xrf_elem_cb_widget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_41.addWidget(self.label_22, 0, 1, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_23 = QLabel(self.xrf_elem_cb_widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_23)

        self.cb_elem_1 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_1.setObjectName(u"cb_elem_1")

        self.verticalLayout_22.addWidget(self.cb_elem_1)


        self.gridLayout_41.addLayout(self.verticalLayout_22, 1, 0, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_24 = QLabel(self.xrf_elem_cb_widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_24)

        self.cb_elem_2 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_2.setObjectName(u"cb_elem_2")

        self.verticalLayout_23.addWidget(self.cb_elem_2)


        self.gridLayout_41.addLayout(self.verticalLayout_23, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_38 = QLabel(self.xrf_elem_cb_widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_38)

        self.cb_elem_3 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_3.setObjectName(u"cb_elem_3")

        self.verticalLayout.addWidget(self.cb_elem_3)


        self.gridLayout_41.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_33 = QLabel(self.xrf_elem_cb_widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_33)

        self.cb_elem_4 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_4.setObjectName(u"cb_elem_4")

        self.verticalLayout_3.addWidget(self.cb_elem_4)


        self.gridLayout_41.addLayout(self.verticalLayout_3, 1, 3, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_35 = QLabel(self.xrf_elem_cb_widget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_35)

        self.cb_elem_5 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_5.setObjectName(u"cb_elem_5")

        self.verticalLayout_4.addWidget(self.cb_elem_5)


        self.gridLayout_41.addLayout(self.verticalLayout_4, 1, 4, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_30 = QLabel(self.xrf_elem_cb_widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_30)

        self.cb_elem_6 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_6.setObjectName(u"cb_elem_6")

        self.verticalLayout_10.addWidget(self.cb_elem_6)


        self.gridLayout_41.addLayout(self.verticalLayout_10, 1, 5, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_36 = QLabel(self.xrf_elem_cb_widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_36)

        self.cb_elem_7 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_7.setObjectName(u"cb_elem_7")

        self.verticalLayout_12.addWidget(self.cb_elem_7)


        self.gridLayout_41.addLayout(self.verticalLayout_12, 1, 6, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_31 = QLabel(self.xrf_elem_cb_widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_31)

        self.cb_elem_8 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_8.setObjectName(u"cb_elem_8")

        self.verticalLayout_13.addWidget(self.cb_elem_8)


        self.gridLayout_41.addLayout(self.verticalLayout_13, 1, 7, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_37 = QLabel(self.xrf_elem_cb_widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_37)

        self.cb_elem_9 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_9.setObjectName(u"cb_elem_9")

        self.verticalLayout_14.addWidget(self.cb_elem_9)


        self.gridLayout_41.addLayout(self.verticalLayout_14, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_34 = QLabel(self.xrf_elem_cb_widget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_34)

        self.cb_elem_10 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_10.setObjectName(u"cb_elem_10")

        self.verticalLayout_15.addWidget(self.cb_elem_10)


        self.gridLayout_41.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_29 = QLabel(self.xrf_elem_cb_widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_29)

        self.cb_elem_11 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_11.setObjectName(u"cb_elem_11")

        self.verticalLayout_16.addWidget(self.cb_elem_11)


        self.gridLayout_41.addLayout(self.verticalLayout_16, 2, 2, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_28 = QLabel(self.xrf_elem_cb_widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_28)

        self.cb_elem_12 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_12.setObjectName(u"cb_elem_12")

        self.verticalLayout_18.addWidget(self.cb_elem_12)


        self.gridLayout_41.addLayout(self.verticalLayout_18, 2, 3, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_26 = QLabel(self.xrf_elem_cb_widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_26)

        self.cb_elem_13 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_13.setObjectName(u"cb_elem_13")

        self.verticalLayout_17.addWidget(self.cb_elem_13)


        self.gridLayout_41.addLayout(self.verticalLayout_17, 2, 4, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_39 = QLabel(self.xrf_elem_cb_widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_39)

        self.cb_elem_14 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_14.setObjectName(u"cb_elem_14")

        self.verticalLayout_19.addWidget(self.cb_elem_14)


        self.gridLayout_41.addLayout(self.verticalLayout_19, 2, 5, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_40 = QLabel(self.xrf_elem_cb_widget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_40)

        self.cb_elem_15 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_15.setObjectName(u"cb_elem_15")

        self.verticalLayout_20.addWidget(self.cb_elem_15)


        self.gridLayout_41.addLayout(self.verticalLayout_20, 2, 6, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_41 = QLabel(self.xrf_elem_cb_widget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_41)

        self.cb_elem_16 = QComboBox(self.xrf_elem_cb_widget)
        self.cb_elem_16.setObjectName(u"cb_elem_16")

        self.verticalLayout_21.addWidget(self.cb_elem_16)


        self.gridLayout_41.addLayout(self.verticalLayout_21, 2, 7, 1, 1)


        self.gridLayout_40.addWidget(self.xrf_elem_cb_widget, 2, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_7)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_40.addWidget(self.label_21, 0, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.groupBox_7)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy3)
        self.textEdit_2.setStyleSheet(u"")
        self.textEdit_2.setReadOnly(True)

        self.gridLayout_40.addWidget(self.textEdit_2, 5, 0, 1, 1)


        self.gridLayout_142.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_142.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_34 = QGridLayout(self.groupBox_5)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_66 = QLabel(self.groupBox_5)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_34.addWidget(self.label_66, 2, 0, 1, 1)

        self.pb_create_user = QPushButton(self.groupBox_5)
        self.pb_create_user.setObjectName(u"pb_create_user")
        sizePolicy.setHeightForWidth(self.pb_create_user.sizePolicy().hasHeightForWidth())
        self.pb_create_user.setSizePolicy(sizePolicy)

        self.gridLayout_34.addWidget(self.pb_create_user, 5, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 15, -1)
        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.le_sample_name = QLineEdit(self.groupBox_5)
        self.le_sample_name.setObjectName(u"le_sample_name")

        self.horizontalLayout.addWidget(self.le_sample_name)


        self.gridLayout_34.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_69 = QLabel(self.groupBox_5)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_16.addWidget(self.label_69)

        self.le_pdf_name = QLineEdit(self.groupBox_5)
        self.le_pdf_name.setObjectName(u"le_pdf_name")

        self.horizontalLayout_16.addWidget(self.le_pdf_name)


        self.gridLayout_34.addLayout(self.horizontalLayout_16, 4, 0, 1, 1)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(15, -1, -1, -1)
        self.pb_insert_user_image = QPushButton(self.groupBox_5)
        self.pb_insert_user_image.setObjectName(u"pb_insert_user_image")
        sizePolicy.setHeightForWidth(self.pb_insert_user_image.sizePolicy().hasHeightForWidth())
        self.pb_insert_user_image.setSizePolicy(sizePolicy)

        self.gridLayout_33.addWidget(self.pb_insert_user_image, 0, 0, 1, 1)

        self.le_image_path = QLineEdit(self.groupBox_5)
        self.le_image_path.setObjectName(u"le_image_path")

        self.gridLayout_33.addWidget(self.le_image_path, 0, 1, 1, 1)


        self.gridLayout_34.addLayout(self.gridLayout_33, 4, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.le_experimenters = QLineEdit(self.groupBox_5)
        self.le_experimenters.setObjectName(u"le_experimenters")

        self.horizontalLayout_2.addWidget(self.le_experimenters)


        self.gridLayout_34.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)

        self.le_proposal_num = QLineEdit(self.groupBox_5)
        self.le_proposal_num.setObjectName(u"le_proposal_num")

        self.gridLayout_34.addWidget(self.le_proposal_num, 2, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.groupBox_5)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setEnabled(True)
        self.gridLayout_141 = QGridLayout(self.groupBox_16)
        self.gridLayout_141.setObjectName(u"gridLayout_141")
        self.cb_technique_diff = QCheckBox(self.groupBox_16)
        self.cb_technique_diff.setObjectName(u"cb_technique_diff")

        self.gridLayout_141.addWidget(self.cb_technique_diff, 3, 0, 1, 1)

        self.cb_technique_xanes = QCheckBox(self.groupBox_16)
        self.cb_technique_xanes.setObjectName(u"cb_technique_xanes")

        self.gridLayout_141.addWidget(self.cb_technique_xanes, 4, 0, 1, 1)

        self.cb_technique_xrf = QCheckBox(self.groupBox_16)
        self.cb_technique_xrf.setObjectName(u"cb_technique_xrf")
        self.cb_technique_xrf.setChecked(True)

        self.gridLayout_141.addWidget(self.cb_technique_xrf, 1, 0, 1, 1)

        self.cb_technique_ptycho = QCheckBox(self.groupBox_16)
        self.cb_technique_ptycho.setObjectName(u"cb_technique_ptycho")

        self.gridLayout_141.addWidget(self.cb_technique_ptycho, 2, 0, 1, 1)

        self.label_50 = QLabel(self.groupBox_16)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_141.addWidget(self.label_50, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_16, 0, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_34.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 15, -1)
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.le_username = QLineEdit(self.groupBox_5)
        self.le_username.setObjectName(u"le_username")

        self.horizontalLayout_3.addWidget(self.le_username)


        self.gridLayout_34.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.pb_create_new_pdf_log = QPushButton(self.groupBox_5)
        self.pb_create_new_pdf_log.setObjectName(u"pb_create_new_pdf_log")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pb_create_new_pdf_log.sizePolicy().hasHeightForWidth())
        self.pb_create_new_pdf_log.setSizePolicy(sizePolicy4)

        self.gridLayout_34.addWidget(self.pb_create_new_pdf_log, 5, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_34.addWidget(self.label_15, 0, 0, 1, 1)

        self.pb_get_proposal_info = QPushButton(self.groupBox_5)
        self.pb_get_proposal_info.setObjectName(u"pb_get_proposal_info")

        self.gridLayout_34.addWidget(self.pb_get_proposal_info, 2, 2, 1, 1)

        self.pb_move_data_to_globus = QPushButton(self.groupBox_5)
        self.pb_move_data_to_globus.setObjectName(u"pb_move_data_to_globus")

        self.gridLayout_34.addWidget(self.pb_move_data_to_globus, 5, 0, 1, 1)


        self.gridLayout_142.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.HXN_GUI_tabs.addTab(self.tab_4, "")
        self.scan_tab = QWidget()
        self.scan_tab.setObjectName(u"scan_tab")
        self.gridLayout_91 = QGridLayout(self.scan_tab)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.frame_2 = QFrame(self.scan_tab)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_92 = QGridLayout(self.frame_2)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_17, 0, 1, 1, 1)

        self.cb_dets = QComboBox(self.groupBox_3)
        self.cb_dets.setObjectName(u"cb_dets")
        sizePolicy.setHeightForWidth(self.cb_dets.sizePolicy().hasHeightForWidth())
        self.cb_dets.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.cb_dets, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_2, 1, 1, 1, 1)

        self.cb_motor1 = QComboBox(self.groupBox_3)
        self.cb_motor1.setObjectName(u"cb_motor1")
        sizePolicy.setHeightForWidth(self.cb_motor1.sizePolicy().hasHeightForWidth())
        self.cb_motor1.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.cb_motor1, 1, 2, 1, 1)

        self.cb_motor2 = QComboBox(self.groupBox_3)
        self.cb_motor2.setObjectName(u"cb_motor2")
        sizePolicy.setHeightForWidth(self.cb_motor2.sizePolicy().hasHeightForWidth())
        self.cb_motor2.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.cb_motor2, 1, 3, 1, 1)

        self.label_32 = QLabel(self.groupBox_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_32, 2, 1, 1, 1)

        self.x_start = QDoubleSpinBox(self.groupBox_3)
        self.x_start.setObjectName(u"x_start")
        sizePolicy.setHeightForWidth(self.x_start.sizePolicy().hasHeightForWidth())
        self.x_start.setSizePolicy(sizePolicy)
        self.x_start.setPrefix(u"")
        self.x_start.setDecimals(3)
        self.x_start.setMinimum(-14.000000000000000)
        self.x_start.setMaximum(14.000000000000000)
        self.x_start.setSingleStep(1.000000000000000)
        self.x_start.setValue(-5.000000000000000)

        self.gridLayout_8.addWidget(self.x_start, 2, 2, 1, 1)

        self.y_start = QDoubleSpinBox(self.groupBox_3)
        self.y_start.setObjectName(u"y_start")
        self.y_start.setEnabled(True)
        sizePolicy.setHeightForWidth(self.y_start.sizePolicy().hasHeightForWidth())
        self.y_start.setSizePolicy(sizePolicy)
        self.y_start.setPrefix(u"")
        self.y_start.setDecimals(3)
        self.y_start.setMinimum(-14.000000000000000)
        self.y_start.setMaximum(14.000000000000000)
        self.y_start.setSingleStep(1.000000000000000)
        self.y_start.setValue(-5.000000000000000)

        self.gridLayout_8.addWidget(self.y_start, 2, 3, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_18, 3, 1, 1, 1)

        self.x_end = QDoubleSpinBox(self.groupBox_3)
        self.x_end.setObjectName(u"x_end")
        sizePolicy.setHeightForWidth(self.x_end.sizePolicy().hasHeightForWidth())
        self.x_end.setSizePolicy(sizePolicy)
        self.x_end.setSuffix(u"um")
        self.x_end.setDecimals(3)
        self.x_end.setMinimum(-14.000000000000000)
        self.x_end.setMaximum(14.000000000000000)
        self.x_end.setSingleStep(1.000000000000000)
        self.x_end.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.x_end, 3, 2, 1, 1)

        self.y_end = QDoubleSpinBox(self.groupBox_3)
        self.y_end.setObjectName(u"y_end")
        sizePolicy.setHeightForWidth(self.y_end.sizePolicy().hasHeightForWidth())
        self.y_end.setSizePolicy(sizePolicy)
        self.y_end.setSuffix(u"um")
        self.y_end.setDecimals(3)
        self.y_end.setMinimum(-14.000000000000000)
        self.y_end.setMaximum(14.000000000000000)
        self.y_end.setSingleStep(1.000000000000000)
        self.y_end.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.y_end, 3, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_5, 4, 1, 1, 1)

        self.x_step = QSpinBox(self.groupBox_3)
        self.x_step.setObjectName(u"x_step")
        sizePolicy.setHeightForWidth(self.x_step.sizePolicy().hasHeightForWidth())
        self.x_step.setSizePolicy(sizePolicy)
        self.x_step.setMinimum(1)
        self.x_step.setMaximum(10000)
        self.x_step.setSingleStep(10)
        self.x_step.setValue(50)

        self.gridLayout_8.addWidget(self.x_step, 4, 2, 1, 1)

        self.y_step = QSpinBox(self.groupBox_3)
        self.y_step.setObjectName(u"y_step")
        sizePolicy.setHeightForWidth(self.y_step.sizePolicy().hasHeightForWidth())
        self.y_step.setSizePolicy(sizePolicy)
        self.y_step.setMinimum(1)
        self.y_step.setMaximum(10000)
        self.y_step.setSingleStep(10)
        self.y_step.setValue(50)

        self.gridLayout_8.addWidget(self.y_step, 4, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_9, 5, 1, 1, 1)

        self.dwell = QDoubleSpinBox(self.groupBox_3)
        self.dwell.setObjectName(u"dwell")
        sizePolicy.setHeightForWidth(self.dwell.sizePolicy().hasHeightForWidth())
        self.dwell.setSizePolicy(sizePolicy)
        self.dwell.setSuffix(u"sec")
        self.dwell.setDecimals(4)
        self.dwell.setMinimum(0.001000000000000)
        self.dwell.setMaximum(0.500000000000000)
        self.dwell.setSingleStep(0.005000000000000)
        self.dwell.setValue(0.005000000000000)

        self.gridLayout_8.addWidget(self.dwell, 5, 2, 1, 1)

        self.widget_2 = QWidget(self.groupBox_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.rb_1d = QRadioButton(self.widget_2)
        self.rb_1d.setObjectName(u"rb_1d")
        sizePolicy.setHeightForWidth(self.rb_1d.sizePolicy().hasHeightForWidth())
        self.rb_1d.setSizePolicy(sizePolicy)
        self.rb_1d.setStyleSheet(u"")
        self.rb_1d.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.rb_1d)

        self.rb_2d = QRadioButton(self.widget_2)
        self.rb_2d.setObjectName(u"rb_2d")
        sizePolicy.setHeightForWidth(self.rb_2d.sizePolicy().hasHeightForWidth())
        self.rb_2d.setSizePolicy(sizePolicy)
        self.rb_2d.setStyleSheet(u"")
        self.rb_2d.setChecked(True)
        self.rb_2d.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.rb_2d)


        self.gridLayout_8.addWidget(self.widget_2, 0, 0, 6, 1)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pb_3030 = QPushButton(self.groupBox_2)
        self.pb_3030.setObjectName(u"pb_3030")
        sizePolicy4.setHeightForWidth(self.pb_3030.sizePolicy().hasHeightForWidth())
        self.pb_3030.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.pb_3030)

        self.pb_66 = QPushButton(self.groupBox_2)
        self.pb_66.setObjectName(u"pb_66")
        sizePolicy4.setHeightForWidth(self.pb_66.sizePolicy().hasHeightForWidth())
        self.pb_66.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.pb_66)


        self.gridLayout_6.addLayout(self.verticalLayout_6, 2, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pb_2020 = QPushButton(self.groupBox_2)
        self.pb_2020.setObjectName(u"pb_2020")
        sizePolicy4.setHeightForWidth(self.pb_2020.sizePolicy().hasHeightForWidth())
        self.pb_2020.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.pb_2020)

        self.pb_22 = QPushButton(self.groupBox_2)
        self.pb_22.setObjectName(u"pb_22")
        sizePolicy4.setHeightForWidth(self.pb_22.sizePolicy().hasHeightForWidth())
        self.pb_22.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.pb_22)


        self.gridLayout_6.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.label_136 = QLabel(self.groupBox_2)
        self.label_136.setObjectName(u"label_136")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy5)

        self.gridLayout_6.addWidget(self.label_136, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_2, 0, 4, 6, 1)


        self.gridLayout_92.addWidget(self.groupBox_3, 0, 1, 2, 1)

        self.toolBox_10 = QToolBox(self.frame_2)
        self.toolBox_10.setObjectName(u"toolBox_10")
        self.toolBox_10Page1 = QWidget()
        self.toolBox_10Page1.setObjectName(u"toolBox_10Page1")
        self.toolBox_10Page1.setGeometry(QRect(0, 0, 574, 327))
        self.gridLayout_111 = QGridLayout(self.toolBox_10Page1)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.pb_abort_fly = QPushButton(self.toolBox_10Page1)
        self.pb_abort_fly.setObjectName(u"pb_abort_fly")

        self.gridLayout_111.addWidget(self.pb_abort_fly, 3, 0, 1, 1)

        self.gridLayout_57 = QGridLayout()
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.pb_batchscan_copy = QPushButton(self.toolBox_10Page1)
        self.pb_batchscan_copy.setObjectName(u"pb_batchscan_copy")
        sizePolicy5.setHeightForWidth(self.pb_batchscan_copy.sizePolicy().hasHeightForWidth())
        self.pb_batchscan_copy.setSizePolicy(sizePolicy5)

        self.gridLayout_57.addWidget(self.pb_batchscan_copy, 0, 2, 1, 1)

        self.pb_scan_copy = QPushButton(self.toolBox_10Page1)
        self.pb_scan_copy.setObjectName(u"pb_scan_copy")
        sizePolicy5.setHeightForWidth(self.pb_scan_copy.sizePolicy().hasHeightForWidth())
        self.pb_scan_copy.setSizePolicy(sizePolicy5)

        self.gridLayout_57.addWidget(self.pb_scan_copy, 0, 1, 1, 1)

        self.text_scan_plan = QLineEdit(self.toolBox_10Page1)
        self.text_scan_plan.setObjectName(u"text_scan_plan")
        sizePolicy2.setHeightForWidth(self.text_scan_plan.sizePolicy().hasHeightForWidth())
        self.text_scan_plan.setSizePolicy(sizePolicy2)

        self.gridLayout_57.addWidget(self.text_scan_plan, 0, 0, 1, 1)


        self.gridLayout_111.addLayout(self.gridLayout_57, 7, 0, 1, 1)

        self.label_scan_info_calc = QLabel(self.toolBox_10Page1)
        self.label_scan_info_calc.setObjectName(u"label_scan_info_calc")
        sizePolicy.setHeightForWidth(self.label_scan_info_calc.sizePolicy().hasHeightForWidth())
        self.label_scan_info_calc.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Modern No. 20"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_scan_info_calc.setFont(font1)
        self.label_scan_info_calc.setStyleSheet(u"color: rgb(73, 91, 255);\n"
"font: 15pt \"Modern No. 20\";\n"
"\n"
"\n"
"")
        self.label_scan_info_calc.setAlignment(Qt.AlignCenter)

        self.gridLayout_111.addWidget(self.label_scan_info_calc, 4, 0, 1, 1)

        self.label_53 = QLabel(self.toolBox_10Page1)
        self.label_53.setObjectName(u"label_53")
        sizePolicy2.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy2)

        self.gridLayout_111.addWidget(self.label_53, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.start = QPushButton(self.toolBox_10Page1)
        self.start.setObjectName(u"start")
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(24)
        font2.setBold(False)
        font2.setItalic(False)
        self.start.setFont(font2)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(167, 255, 180);\n"
"	\n"
"	font: 24pt \"MS Shell Dlg 2\";\n"
"	}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 0); \n"
"	}\n"
"\n"
"QPushButton:pressed{ \n"
"	background-color: rgb(0, 255, 0); \n"
"	}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.start)


        self.gridLayout_111.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.toolBox_10.addItem(self.toolBox_10Page1, u"Scan")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 462, 281))
        self.gridLayout_147 = QGridLayout(self.page)
        self.gridLayout_147.setObjectName(u"gridLayout_147")
        self.gridLayout_56 = QGridLayout()
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.pb_flyplan_to_qserver = QPushButton(self.page)
        self.pb_flyplan_to_qserver.setObjectName(u"pb_flyplan_to_qserver")
        self.pb_flyplan_to_qserver.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_flyplan_to_qserver.sizePolicy().hasHeightForWidth())
        self.pb_flyplan_to_qserver.setSizePolicy(sizePolicy)

        self.gridLayout_56.addWidget(self.pb_flyplan_to_qserver, 0, 0, 1, 1)

        self.label_52 = QLabel(self.page)
        self.label_52.setObjectName(u"label_52")
        sizePolicy5.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy5)

        self.gridLayout_56.addWidget(self.label_52, 0, 1, 1, 1)

        self.le_qplan_name = QLineEdit(self.page)
        self.le_qplan_name.setObjectName(u"le_qplan_name")
        sizePolicy2.setHeightForWidth(self.le_qplan_name.sizePolicy().hasHeightForWidth())
        self.le_qplan_name.setSizePolicy(sizePolicy2)

        self.gridLayout_56.addWidget(self.le_qplan_name, 0, 2, 1, 1)

        self.cb_queue_use_curr_pos = QCheckBox(self.page)
        self.cb_queue_use_curr_pos.setObjectName(u"cb_queue_use_curr_pos")
        self.cb_queue_use_curr_pos.setChecked(True)

        self.gridLayout_56.addWidget(self.cb_queue_use_curr_pos, 1, 0, 1, 1)


        self.gridLayout_147.addLayout(self.gridLayout_56, 0, 0, 1, 1)

        self.gb_queue_server_plan = QGroupBox(self.page)
        self.gb_queue_server_plan.setObjectName(u"gb_queue_server_plan")
        self.gb_queue_server_plan.setEnabled(False)
        sizePolicy.setHeightForWidth(self.gb_queue_server_plan.sizePolicy().hasHeightForWidth())
        self.gb_queue_server_plan.setSizePolicy(sizePolicy)
        self.gb_queue_server_plan.setStyleSheet(u"")
        self.gridLayout_146 = QGridLayout(self.gb_queue_server_plan)
        self.gridLayout_146.setObjectName(u"gridLayout_146")
        self.dsb_zpssz_manual_roi = QDoubleSpinBox(self.gb_queue_server_plan)
        self.dsb_zpssz_manual_roi.setObjectName(u"dsb_zpssz_manual_roi")
        sizePolicy.setHeightForWidth(self.dsb_zpssz_manual_roi.sizePolicy().hasHeightForWidth())
        self.dsb_zpssz_manual_roi.setSizePolicy(sizePolicy)
        self.dsb_zpssz_manual_roi.setPrefix(u"")
        self.dsb_zpssz_manual_roi.setDecimals(3)
        self.dsb_zpssz_manual_roi.setMinimum(-14.000000000000000)
        self.dsb_zpssz_manual_roi.setMaximum(14.000000000000000)
        self.dsb_zpssz_manual_roi.setSingleStep(1.000000000000000)
        self.dsb_zpssz_manual_roi.setValue(-5.000000000000000)

        self.gridLayout_146.addWidget(self.dsb_zpssz_manual_roi, 1, 6, 1, 1)

        self.dsb_zpssy_manual_roi = QDoubleSpinBox(self.gb_queue_server_plan)
        self.dsb_zpssy_manual_roi.setObjectName(u"dsb_zpssy_manual_roi")
        sizePolicy.setHeightForWidth(self.dsb_zpssy_manual_roi.sizePolicy().hasHeightForWidth())
        self.dsb_zpssy_manual_roi.setSizePolicy(sizePolicy)
        self.dsb_zpssy_manual_roi.setPrefix(u"")
        self.dsb_zpssy_manual_roi.setDecimals(3)
        self.dsb_zpssy_manual_roi.setMinimum(-14.000000000000000)
        self.dsb_zpssy_manual_roi.setMaximum(14.000000000000000)
        self.dsb_zpssy_manual_roi.setSingleStep(1.000000000000000)
        self.dsb_zpssy_manual_roi.setValue(-5.000000000000000)

        self.gridLayout_146.addWidget(self.dsb_zpssy_manual_roi, 1, 4, 1, 1)

        self.dsb_zpsth_manual_roi = QDoubleSpinBox(self.gb_queue_server_plan)
        self.dsb_zpsth_manual_roi.setObjectName(u"dsb_zpsth_manual_roi")
        sizePolicy2.setHeightForWidth(self.dsb_zpsth_manual_roi.sizePolicy().hasHeightForWidth())
        self.dsb_zpsth_manual_roi.setSizePolicy(sizePolicy2)
        self.dsb_zpsth_manual_roi.setPrefix(u"")
        self.dsb_zpsth_manual_roi.setDecimals(2)
        self.dsb_zpsth_manual_roi.setMinimum(-100.000000000000000)
        self.dsb_zpsth_manual_roi.setMaximum(100.000000000000000)
        self.dsb_zpsth_manual_roi.setSingleStep(100.000000000000000)
        self.dsb_zpsth_manual_roi.setValue(0.000000000000000)

        self.gridLayout_146.addWidget(self.dsb_zpsth_manual_roi, 3, 4, 1, 1)

        self.dsb_smary_manual_roi = QDoubleSpinBox(self.gb_queue_server_plan)
        self.dsb_smary_manual_roi.setObjectName(u"dsb_smary_manual_roi")
        sizePolicy.setHeightForWidth(self.dsb_smary_manual_roi.sizePolicy().hasHeightForWidth())
        self.dsb_smary_manual_roi.setSizePolicy(sizePolicy)
        self.dsb_smary_manual_roi.setPrefix(u"")
        self.dsb_smary_manual_roi.setDecimals(2)
        self.dsb_smary_manual_roi.setMinimum(-6000.000000000000000)
        self.dsb_smary_manual_roi.setMaximum(6000.000000000000000)
        self.dsb_smary_manual_roi.setSingleStep(100.000000000000000)
        self.dsb_smary_manual_roi.setValue(100.000000000000000)

        self.gridLayout_146.addWidget(self.dsb_smary_manual_roi, 2, 4, 1, 1)

        self.dsb_smarx_manual_roi = QDoubleSpinBox(self.gb_queue_server_plan)
        self.dsb_smarx_manual_roi.setObjectName(u"dsb_smarx_manual_roi")
        sizePolicy2.setHeightForWidth(self.dsb_smarx_manual_roi.sizePolicy().hasHeightForWidth())
        self.dsb_smarx_manual_roi.setSizePolicy(sizePolicy2)
        self.dsb_smarx_manual_roi.setPrefix(u"")
        self.dsb_smarx_manual_roi.setDecimals(2)
        self.dsb_smarx_manual_roi.setMinimum(-6000.000000000000000)
        self.dsb_smarx_manual_roi.setMaximum(6000.000000000000000)
        self.dsb_smarx_manual_roi.setSingleStep(100.000000000000000)
        self.dsb_smarx_manual_roi.setValue(100.000000000000000)

        self.gridLayout_146.addWidget(self.dsb_smarx_manual_roi, 2, 2, 1, 1)

        self.pb_get_current_position = QPushButton(self.gb_queue_server_plan)
        self.pb_get_current_position.setObjectName(u"pb_get_current_position")

        self.gridLayout_146.addWidget(self.pb_get_current_position, 7, 5, 1, 2)

        self.label_196 = QLabel(self.gb_queue_server_plan)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.label_196, 1, 1, 1, 1)

        self.dsb_zpz1_manual_roi = QDoubleSpinBox(self.gb_queue_server_plan)
        self.dsb_zpz1_manual_roi.setObjectName(u"dsb_zpz1_manual_roi")
        sizePolicy.setHeightForWidth(self.dsb_zpz1_manual_roi.sizePolicy().hasHeightForWidth())
        self.dsb_zpz1_manual_roi.setSizePolicy(sizePolicy)
        self.dsb_zpz1_manual_roi.setPrefix(u"")
        self.dsb_zpz1_manual_roi.setDecimals(2)
        self.dsb_zpz1_manual_roi.setMinimum(-45.000000000000000)
        self.dsb_zpz1_manual_roi.setMaximum(10.000000000000000)
        self.dsb_zpz1_manual_roi.setSingleStep(100.000000000000000)
        self.dsb_zpz1_manual_roi.setValue(10.000000000000000)

        self.gridLayout_146.addWidget(self.dsb_zpz1_manual_roi, 3, 2, 1, 1)

        self.dsb_zpssx_manual_roi = QDoubleSpinBox(self.gb_queue_server_plan)
        self.dsb_zpssx_manual_roi.setObjectName(u"dsb_zpssx_manual_roi")
        sizePolicy2.setHeightForWidth(self.dsb_zpssx_manual_roi.sizePolicy().hasHeightForWidth())
        self.dsb_zpssx_manual_roi.setSizePolicy(sizePolicy2)
        self.dsb_zpssx_manual_roi.setPrefix(u"")
        self.dsb_zpssx_manual_roi.setDecimals(3)
        self.dsb_zpssx_manual_roi.setMinimum(-14.000000000000000)
        self.dsb_zpssx_manual_roi.setMaximum(14.000000000000000)
        self.dsb_zpssx_manual_roi.setSingleStep(1.000000000000000)
        self.dsb_zpssx_manual_roi.setValue(-5.000000000000000)

        self.gridLayout_146.addWidget(self.dsb_zpssx_manual_roi, 1, 2, 1, 1)

        self.label_209 = QLabel(self.gb_queue_server_plan)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.label_209, 2, 5, 1, 1)

        self.rb_mll_manual_roi = QRadioButton(self.gb_queue_server_plan)
        self.rb_mll_manual_roi.setObjectName(u"rb_mll_manual_roi")
        sizePolicy.setHeightForWidth(self.rb_mll_manual_roi.sizePolicy().hasHeightForWidth())
        self.rb_mll_manual_roi.setSizePolicy(sizePolicy)
        self.rb_mll_manual_roi.setStyleSheet(u"")
        self.rb_mll_manual_roi.setCheckable(False)
        self.rb_mll_manual_roi.setChecked(False)
        self.rb_mll_manual_roi.setAutoExclusive(True)

        self.gridLayout_146.addWidget(self.rb_mll_manual_roi, 7, 2, 1, 1)

        self.label_206 = QLabel(self.gb_queue_server_plan)
        self.label_206.setObjectName(u"label_206")
        sizePolicy2.setHeightForWidth(self.label_206.sizePolicy().hasHeightForWidth())
        self.label_206.setSizePolicy(sizePolicy2)

        self.gridLayout_146.addWidget(self.label_206, 0, 2, 1, 1)

        self.label_193 = QLabel(self.gb_queue_server_plan)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.label_193, 1, 3, 1, 1)

        self.label_210 = QLabel(self.gb_queue_server_plan)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.label_210, 3, 3, 1, 1)

        self.label_208 = QLabel(self.gb_queue_server_plan)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.label_208, 2, 3, 1, 1)

        self.label_207 = QLabel(self.gb_queue_server_plan)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.label_207, 2, 1, 1, 1)

        self.label_211 = QLabel(self.gb_queue_server_plan)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.label_211, 3, 1, 1, 1)

        self.dsb_smarz_manual_roi = QDoubleSpinBox(self.gb_queue_server_plan)
        self.dsb_smarz_manual_roi.setObjectName(u"dsb_smarz_manual_roi")
        sizePolicy.setHeightForWidth(self.dsb_smarz_manual_roi.sizePolicy().hasHeightForWidth())
        self.dsb_smarz_manual_roi.setSizePolicy(sizePolicy)
        self.dsb_smarz_manual_roi.setPrefix(u"")
        self.dsb_smarz_manual_roi.setDecimals(2)
        self.dsb_smarz_manual_roi.setMinimum(-6000.000000000000000)
        self.dsb_smarz_manual_roi.setMaximum(6000.000000000000000)
        self.dsb_smarz_manual_roi.setSingleStep(100.000000000000000)
        self.dsb_smarz_manual_roi.setValue(100.000000000000000)

        self.gridLayout_146.addWidget(self.dsb_smarz_manual_roi, 2, 6, 1, 1)

        self.label_194 = QLabel(self.gb_queue_server_plan)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setAlignment(Qt.AlignCenter)

        self.gridLayout_146.addWidget(self.label_194, 1, 5, 1, 1)

        self.rb_zp_manual_roi = QRadioButton(self.gb_queue_server_plan)
        self.rb_zp_manual_roi.setObjectName(u"rb_zp_manual_roi")
        self.rb_zp_manual_roi.setCheckable(False)
        self.rb_zp_manual_roi.setChecked(False)

        self.gridLayout_146.addWidget(self.rb_zp_manual_roi, 7, 4, 1, 1)


        self.gridLayout_147.addWidget(self.gb_queue_server_plan, 1, 0, 1, 1)

        self.toolBox_10.addItem(self.page, u"QueueServer")

        self.gridLayout_92.addWidget(self.toolBox_10, 0, 2, 2, 1)


        self.gridLayout_91.addWidget(self.frame_2, 0, 0, 1, 2)

        self.groupBox_6 = QGroupBox(self.scan_tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_11 = QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tabWidget = QTabWidget(self.groupBox_6)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setDocumentMode(True)
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_20 = QGridLayout(self.tab_8)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.groupBox_37 = QGroupBox(self.tab_8)
        self.groupBox_37.setObjectName(u"groupBox_37")
        sizePolicy1.setHeightForWidth(self.groupBox_37.sizePolicy().hasHeightForWidth())
        self.groupBox_37.setSizePolicy(sizePolicy1)
        self.gridLayout_120 = QGridLayout(self.groupBox_37)
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_163 = QLabel(self.groupBox_37)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_163)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_164 = QLabel(self.groupBox_37)
        self.label_164.setObjectName(u"label_164")
        sizePolicy2.setHeightForWidth(self.label_164.sizePolicy().hasHeightForWidth())
        self.label_164.setSizePolicy(sizePolicy2)
        self.label_164.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_164)

        self.le_sid_position_zp = QLineEdit(self.groupBox_37)
        self.le_sid_position_zp.setObjectName(u"le_sid_position_zp")
        sizePolicy2.setHeightForWidth(self.le_sid_position_zp.sizePolicy().hasHeightForWidth())
        self.le_sid_position_zp.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.le_sid_position_zp)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.pb_recover_scan_pos_zp = QPushButton(self.groupBox_37)
        self.pb_recover_scan_pos_zp.setObjectName(u"pb_recover_scan_pos_zp")
        sizePolicy2.setHeightForWidth(self.pb_recover_scan_pos_zp.sizePolicy().hasHeightForWidth())
        self.pb_recover_scan_pos_zp.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.pb_recover_scan_pos_zp)

        self.cb_sid_moveZPZ = QCheckBox(self.groupBox_37)
        self.cb_sid_moveZPZ.setObjectName(u"cb_sid_moveZPZ")

        self.verticalLayout_8.addWidget(self.cb_sid_moveZPZ)

        self.pb_show_scan_pos_zp = QPushButton(self.groupBox_37)
        self.pb_show_scan_pos_zp.setObjectName(u"pb_show_scan_pos_zp")
        sizePolicy2.setHeightForWidth(self.pb_show_scan_pos_zp.sizePolicy().hasHeightForWidth())
        self.pb_show_scan_pos_zp.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.pb_show_scan_pos_zp)

        self.pb_print_scan_meta_zp = QPushButton(self.groupBox_37)
        self.pb_print_scan_meta_zp.setObjectName(u"pb_print_scan_meta_zp")
        sizePolicy2.setHeightForWidth(self.pb_print_scan_meta_zp.sizePolicy().hasHeightForWidth())
        self.pb_print_scan_meta_zp.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.pb_print_scan_meta_zp)


        self.gridLayout_120.addLayout(self.verticalLayout_8, 1, 1, 1, 1)

        self.gridLayout_121 = QGridLayout()
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.gridLayout_122 = QGridLayout()
        self.gridLayout_122.setObjectName(u"gridLayout_122")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pb_save_pos_zp = QPushButton(self.groupBox_37)
        self.pb_save_pos_zp.setObjectName(u"pb_save_pos_zp")
        sizePolicy2.setHeightForWidth(self.pb_save_pos_zp.sizePolicy().hasHeightForWidth())
        self.pb_save_pos_zp.setSizePolicy(sizePolicy2)
        self.pb_save_pos_zp.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.pb_save_pos_zp)


        self.gridLayout_122.addLayout(self.horizontalLayout_38, 0, 0, 1, 1)

        self.pb_move_pos_zp = QPushButton(self.groupBox_37)
        self.pb_move_pos_zp.setObjectName(u"pb_move_pos_zp")
        sizePolicy2.setHeightForWidth(self.pb_move_pos_zp.sizePolicy().hasHeightForWidth())
        self.pb_move_pos_zp.setSizePolicy(sizePolicy2)
        self.pb_move_pos_zp.setStyleSheet(u"")

        self.gridLayout_122.addWidget(self.pb_move_pos_zp, 3, 0, 1, 1)

        self.pb_copy_curr_pos_zp = QPushButton(self.groupBox_37)
        self.pb_copy_curr_pos_zp.setObjectName(u"pb_copy_curr_pos_zp")

        self.gridLayout_122.addWidget(self.pb_copy_curr_pos_zp, 1, 0, 1, 1)


        self.gridLayout_121.addLayout(self.gridLayout_122, 0, 0, 1, 1)

        self.zp_sample_roi_list_widget = QListWidget(self.groupBox_37)
        self.zp_sample_roi_list_widget.setObjectName(u"zp_sample_roi_list_widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.zp_sample_roi_list_widget.sizePolicy().hasHeightForWidth())
        self.zp_sample_roi_list_widget.setSizePolicy(sizePolicy6)

        self.gridLayout_121.addWidget(self.zp_sample_roi_list_widget, 1, 0, 1, 1)

        self.gridLayout_123 = QGridLayout()
        self.gridLayout_123.setObjectName(u"gridLayout_123")
        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.pb_roiList_export_zp = QPushButton(self.groupBox_37)
        self.pb_roiList_export_zp.setObjectName(u"pb_roiList_export_zp")

        self.horizontalLayout_80.addWidget(self.pb_roiList_export_zp)

        self.pb_roiList_import_zp = QPushButton(self.groupBox_37)
        self.pb_roiList_import_zp.setObjectName(u"pb_roiList_import_zp")

        self.horizontalLayout_80.addWidget(self.pb_roiList_import_zp)


        self.gridLayout_123.addLayout(self.horizontalLayout_80, 0, 0, 1, 1)

        self.pb_roiList_clear_zp = QPushButton(self.groupBox_37)
        self.pb_roiList_clear_zp.setObjectName(u"pb_roiList_clear_zp")

        self.gridLayout_123.addWidget(self.pb_roiList_clear_zp, 2, 0, 1, 1)

        self.pb_roiList_clear_sel_zp = QPushButton(self.groupBox_37)
        self.pb_roiList_clear_sel_zp.setObjectName(u"pb_roiList_clear_sel_zp")

        self.gridLayout_123.addWidget(self.pb_roiList_clear_sel_zp, 1, 0, 1, 1)


        self.gridLayout_121.addLayout(self.gridLayout_123, 2, 0, 1, 1)


        self.gridLayout_120.addLayout(self.gridLayout_121, 1, 0, 1, 1)

        self.label_45 = QLabel(self.groupBox_37)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_120.addWidget(self.label_45, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.groupBox_37, 0, 1, 1, 1)

        self.groupBox_36 = QGroupBox(self.tab_8)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setEnabled(True)
        sizePolicy.setHeightForWidth(self.groupBox_36.sizePolicy().hasHeightForWidth())
        self.groupBox_36.setSizePolicy(sizePolicy)
        self.groupBox_36.setStyleSheet(u"")
        self.gridLayout_69 = QGridLayout(self.groupBox_36)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.db_smarx = QDoubleSpinBox(self.groupBox_36)
        self.db_smarx.setObjectName(u"db_smarx")
        sizePolicy2.setHeightForWidth(self.db_smarx.sizePolicy().hasHeightForWidth())
        self.db_smarx.setSizePolicy(sizePolicy2)
        self.db_smarx.setReadOnly(True)
        self.db_smarx.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_smarx.setDecimals(1)
        self.db_smarx.setMinimum(-99999.000000000000000)
        self.db_smarx.setMaximum(99999.000000000000000)
        self.db_smarx.setValue(1.000000000000000)

        self.gridLayout_69.addWidget(self.db_smarx, 2, 4, 1, 1)

        self.db_move_smarz = QDoubleSpinBox(self.groupBox_36)
        self.db_move_smarz.setObjectName(u"db_move_smarz")
        sizePolicy2.setHeightForWidth(self.db_move_smarz.sizePolicy().hasHeightForWidth())
        self.db_move_smarz.setSizePolicy(sizePolicy2)
        self.db_move_smarz.setDecimals(1)
        self.db_move_smarz.setMinimum(-10000.000000000000000)
        self.db_move_smarz.setMaximum(10000.000000000000000)
        self.db_move_smarz.setSingleStep(5.000000000000000)
        self.db_move_smarz.setValue(10.000000000000000)

        self.gridLayout_69.addWidget(self.db_move_smarz, 4, 2, 1, 1)

        self.pb_move_zpsth_pos_neg = QPushButton(self.groupBox_36)
        self.pb_move_zpsth_pos_neg.setObjectName(u"pb_move_zpsth_pos_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_zpsth_pos_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_zpsth_pos_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_zpsth_pos_neg, 5, 1, 1, 1)

        self.db_smary = QDoubleSpinBox(self.groupBox_36)
        self.db_smary.setObjectName(u"db_smary")
        sizePolicy2.setHeightForWidth(self.db_smary.sizePolicy().hasHeightForWidth())
        self.db_smary.setSizePolicy(sizePolicy2)
        self.db_smary.setReadOnly(True)
        self.db_smary.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_smary.setDecimals(1)
        self.db_smary.setMinimum(-99999.000000000000000)
        self.db_smary.setMaximum(99999.000000000000000)
        self.db_smary.setValue(1.000000000000000)

        self.gridLayout_69.addWidget(self.db_smary, 3, 4, 1, 1)

        self.label_78 = QLabel(self.groupBox_36)
        self.label_78.setObjectName(u"label_78")
        sizePolicy1.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy1)
        self.label_78.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_69.addWidget(self.label_78, 6, 0, 1, 1)

        self.db_smarz = QDoubleSpinBox(self.groupBox_36)
        self.db_smarz.setObjectName(u"db_smarz")
        sizePolicy2.setHeightForWidth(self.db_smarz.sizePolicy().hasHeightForWidth())
        self.db_smarz.setSizePolicy(sizePolicy2)
        self.db_smarz.setReadOnly(True)
        self.db_smarz.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_smarz.setDecimals(1)
        self.db_smarz.setMinimum(-99999.000000000000000)
        self.db_smarz.setMaximum(99999.000000000000000)
        self.db_smarz.setValue(1.000000000000000)

        self.gridLayout_69.addWidget(self.db_smarz, 4, 4, 1, 1)

        self.pb_move_smary_neg = QPushButton(self.groupBox_36)
        self.pb_move_smary_neg.setObjectName(u"pb_move_smary_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_smary_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_smary_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_smary_neg, 3, 1, 1, 1)

        self.db_zpz1 = QDoubleSpinBox(self.groupBox_36)
        self.db_zpz1.setObjectName(u"db_zpz1")
        sizePolicy2.setHeightForWidth(self.db_zpz1.sizePolicy().hasHeightForWidth())
        self.db_zpz1.setSizePolicy(sizePolicy2)
        self.db_zpz1.setReadOnly(True)
        self.db_zpz1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_zpz1.setDecimals(4)
        self.db_zpz1.setMinimum(-10000.000000000000000)
        self.db_zpz1.setMaximum(50000.000000000000000)
        self.db_zpz1.setValue(0.000000000000000)

        self.gridLayout_69.addWidget(self.db_zpz1, 6, 4, 1, 1)

        self.label_158 = QLabel(self.groupBox_36)
        self.label_158.setObjectName(u"label_158")

        self.gridLayout_69.addWidget(self.label_158, 1, 4, 1, 1)

        self.label_159 = QLabel(self.groupBox_36)
        self.label_159.setObjectName(u"label_159")
        sizePolicy1.setHeightForWidth(self.label_159.sizePolicy().hasHeightForWidth())
        self.label_159.setSizePolicy(sizePolicy1)
        self.label_159.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_69.addWidget(self.label_159, 5, 0, 1, 1)

        self.db_move_zpz = QDoubleSpinBox(self.groupBox_36)
        self.db_move_zpz.setObjectName(u"db_move_zpz")
        sizePolicy2.setHeightForWidth(self.db_move_zpz.sizePolicy().hasHeightForWidth())
        self.db_move_zpz.setSizePolicy(sizePolicy2)
        self.db_move_zpz.setDecimals(0)
        self.db_move_zpz.setMinimum(-50000.000000000000000)
        self.db_move_zpz.setMaximum(50000.000000000000000)
        self.db_move_zpz.setSingleStep(100.000000000000000)
        self.db_move_zpz.setValue(100.000000000000000)

        self.gridLayout_69.addWidget(self.db_move_zpz, 6, 2, 1, 1)

        self.pb_move_smarx_pos = QPushButton(self.groupBox_36)
        self.pb_move_smarx_pos.setObjectName(u"pb_move_smarx_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_smarx_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_smarx_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_smarx_pos, 2, 3, 1, 1)

        self.pb_move_smarz_pos = QPushButton(self.groupBox_36)
        self.pb_move_smarz_pos.setObjectName(u"pb_move_smarz_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_smarz_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_smarz_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_smarz_pos, 4, 3, 1, 1)

        self.db_move_zpsth = QDoubleSpinBox(self.groupBox_36)
        self.db_move_zpsth.setObjectName(u"db_move_zpsth")
        sizePolicy2.setHeightForWidth(self.db_move_zpsth.sizePolicy().hasHeightForWidth())
        self.db_move_zpsth.setSizePolicy(sizePolicy2)
        self.db_move_zpsth.setMinimum(-120.000000000000000)
        self.db_move_zpsth.setMaximum(120.000000000000000)
        self.db_move_zpsth.setSingleStep(10.000000000000000)
        self.db_move_zpsth.setValue(10.000000000000000)

        self.gridLayout_69.addWidget(self.db_move_zpsth, 5, 2, 1, 1)

        self.pb_move_zpz_pos = QPushButton(self.groupBox_36)
        self.pb_move_zpz_pos.setObjectName(u"pb_move_zpz_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_zpz_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_zpz_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_zpz_pos, 6, 3, 1, 1)

        self.pb_move_smarz_neg = QPushButton(self.groupBox_36)
        self.pb_move_smarz_neg.setObjectName(u"pb_move_smarz_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_smarz_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_smarz_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_smarz_neg, 4, 1, 1, 1)

        self.pb_move_zpsth_pos = QPushButton(self.groupBox_36)
        self.pb_move_zpsth_pos.setObjectName(u"pb_move_zpsth_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_zpsth_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_zpsth_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_zpsth_pos, 5, 3, 1, 1)

        self.db_move_smary = QDoubleSpinBox(self.groupBox_36)
        self.db_move_smary.setObjectName(u"db_move_smary")
        sizePolicy2.setHeightForWidth(self.db_move_smary.sizePolicy().hasHeightForWidth())
        self.db_move_smary.setSizePolicy(sizePolicy2)
        self.db_move_smary.setDecimals(1)
        self.db_move_smary.setMinimum(-10000.000000000000000)
        self.db_move_smary.setMaximum(10000.000000000000000)
        self.db_move_smary.setSingleStep(5.000000000000000)
        self.db_move_smary.setValue(10.000000000000000)

        self.gridLayout_69.addWidget(self.db_move_smary, 3, 2, 1, 1)

        self.pb_move_smary_pos = QPushButton(self.groupBox_36)
        self.pb_move_smary_pos.setObjectName(u"pb_move_smary_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_smary_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_smary_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_smary_pos, 3, 3, 1, 1)

        self.pb_zp_stop_all_sample = QPushButton(self.groupBox_36)
        self.pb_zp_stop_all_sample.setObjectName(u"pb_zp_stop_all_sample")
        sizePolicy2.setHeightForWidth(self.pb_zp_stop_all_sample.sizePolicy().hasHeightForWidth())
        self.pb_zp_stop_all_sample.setSizePolicy(sizePolicy2)
        self.pb_zp_stop_all_sample.setStyleSheet(u"color: rgb(239, 41, 41);")

        self.gridLayout_69.addWidget(self.pb_zp_stop_all_sample, 0, 3, 1, 2)

        self.pb_move_zpz_neg = QPushButton(self.groupBox_36)
        self.pb_move_zpz_neg.setObjectName(u"pb_move_zpz_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_zpz_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_zpz_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_zpz_neg, 6, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_36)
        self.label_42.setObjectName(u"label_42")
        sizePolicy1.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy1)
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_69.addWidget(self.label_42, 4, 0, 1, 1)

        self.label_129 = QLabel(self.groupBox_36)
        self.label_129.setObjectName(u"label_129")
        sizePolicy2.setHeightForWidth(self.label_129.sizePolicy().hasHeightForWidth())
        self.label_129.setSizePolicy(sizePolicy2)
        self.label_129.setStyleSheet(u"")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.label_129, 1, 2, 1, 1)

        self.label_160 = QLabel(self.groupBox_36)
        self.label_160.setObjectName(u"label_160")
        sizePolicy1.setHeightForWidth(self.label_160.sizePolicy().hasHeightForWidth())
        self.label_160.setSizePolicy(sizePolicy1)
        self.label_160.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_69.addWidget(self.label_160, 2, 0, 1, 1)

        self.pb_move_smarx_neg = QPushButton(self.groupBox_36)
        self.pb_move_smarx_neg.setObjectName(u"pb_move_smarx_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_smarx_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_smarx_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_69.addWidget(self.pb_move_smarx_neg, 2, 1, 1, 1)

        self.db_zpsth = QDoubleSpinBox(self.groupBox_36)
        self.db_zpsth.setObjectName(u"db_zpsth")
        sizePolicy2.setHeightForWidth(self.db_zpsth.sizePolicy().hasHeightForWidth())
        self.db_zpsth.setSizePolicy(sizePolicy2)
        self.db_zpsth.setReadOnly(True)
        self.db_zpsth.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_zpsth.setDecimals(3)
        self.db_zpsth.setMinimum(-200.000000000000000)
        self.db_zpsth.setMaximum(200.000000000000000)
        self.db_zpsth.setValue(10.000000000000000)

        self.gridLayout_69.addWidget(self.db_zpsth, 5, 4, 1, 1)

        self.label_161 = QLabel(self.groupBox_36)
        self.label_161.setObjectName(u"label_161")
        sizePolicy2.setHeightForWidth(self.label_161.sizePolicy().hasHeightForWidth())
        self.label_161.setSizePolicy(sizePolicy2)
        self.label_161.setStyleSheet(u"")
        self.label_161.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.label_161, 1, 0, 1, 1)

        self.db_move_smarx = QDoubleSpinBox(self.groupBox_36)
        self.db_move_smarx.setObjectName(u"db_move_smarx")
        sizePolicy2.setHeightForWidth(self.db_move_smarx.sizePolicy().hasHeightForWidth())
        self.db_move_smarx.setSizePolicy(sizePolicy2)
        self.db_move_smarx.setDecimals(1)
        self.db_move_smarx.setMinimum(-10000.000000000000000)
        self.db_move_smarx.setMaximum(10000.000000000000000)
        self.db_move_smarx.setSingleStep(5.000000000000000)
        self.db_move_smarx.setValue(10.000000000000000)

        self.gridLayout_69.addWidget(self.db_move_smarx, 2, 2, 1, 1)

        self.label_162 = QLabel(self.groupBox_36)
        self.label_162.setObjectName(u"label_162")
        sizePolicy1.setHeightForWidth(self.label_162.sizePolicy().hasHeightForWidth())
        self.label_162.setSizePolicy(sizePolicy1)
        self.label_162.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_69.addWidget(self.label_162, 3, 0, 1, 1)


        self.gridLayout_20.addWidget(self.groupBox_36, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_39 = QGroupBox(self.tab)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setEnabled(True)
        sizePolicy.setHeightForWidth(self.groupBox_39.sizePolicy().hasHeightForWidth())
        self.groupBox_39.setSizePolicy(sizePolicy)
        self.groupBox_39.setStyleSheet(u"")
        self.gridLayout_90 = QGridLayout(self.groupBox_39)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.label_167 = QLabel(self.groupBox_39)
        self.label_167.setObjectName(u"label_167")
        sizePolicy2.setHeightForWidth(self.label_167.sizePolicy().hasHeightForWidth())
        self.label_167.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.label_167, 0, 2, 1, 1)

        self.pb_move_dsz_pos = QPushButton(self.groupBox_39)
        self.pb_move_dsz_pos.setObjectName(u"pb_move_dsz_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_dsz_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_dsz_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_dsz_pos, 4, 4, 1, 1)

        self.pb_move_dth_pos = QPushButton(self.groupBox_39)
        self.pb_move_dth_pos.setObjectName(u"pb_move_dth_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_dth_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_dth_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_dth_pos, 5, 4, 1, 1)

        self.label_43 = QLabel(self.groupBox_39)
        self.label_43.setObjectName(u"label_43")
        sizePolicy1.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy1)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.label_43, 4, 0, 1, 1)

        self.pb_move_dsy_pos = QPushButton(self.groupBox_39)
        self.pb_move_dsy_pos.setObjectName(u"pb_move_dsy_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_dsy_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_dsy_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_dsy_pos, 3, 4, 1, 1)

        self.label_82 = QLabel(self.groupBox_39)
        self.label_82.setObjectName(u"label_82")
        sizePolicy1.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy1)
        self.label_82.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.label_82, 6, 0, 1, 1)

        self.db_move_dsx = QDoubleSpinBox(self.groupBox_39)
        self.db_move_dsx.setObjectName(u"db_move_dsx")
        sizePolicy2.setHeightForWidth(self.db_move_dsx.sizePolicy().hasHeightForWidth())
        self.db_move_dsx.setSizePolicy(sizePolicy2)
        self.db_move_dsx.setDecimals(1)
        self.db_move_dsx.setMinimum(-10000.000000000000000)
        self.db_move_dsx.setMaximum(10000.000000000000000)
        self.db_move_dsx.setSingleStep(5.000000000000000)
        self.db_move_dsx.setValue(10.000000000000000)

        self.gridLayout_90.addWidget(self.db_move_dsx, 2, 2, 1, 1)

        self.db_dsy = QDoubleSpinBox(self.groupBox_39)
        self.db_dsy.setObjectName(u"db_dsy")
        sizePolicy2.setHeightForWidth(self.db_dsy.sizePolicy().hasHeightForWidth())
        self.db_dsy.setSizePolicy(sizePolicy2)
        self.db_dsy.setReadOnly(True)
        self.db_dsy.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_dsy.setDecimals(2)
        self.db_dsy.setMinimum(-9999.000000000000000)
        self.db_dsy.setMaximum(9999.989999999999782)
        self.db_dsy.setValue(500.000000000000000)

        self.gridLayout_90.addWidget(self.db_dsy, 3, 5, 1, 1)

        self.label_131 = QLabel(self.groupBox_39)
        self.label_131.setObjectName(u"label_131")
        sizePolicy2.setHeightForWidth(self.label_131.sizePolicy().hasHeightForWidth())
        self.label_131.setSizePolicy(sizePolicy2)
        self.label_131.setStyleSheet(u"")
        self.label_131.setAlignment(Qt.AlignCenter)

        self.gridLayout_90.addWidget(self.label_131, 1, 2, 1, 1)

        self.pb_move_dsx_pos = QPushButton(self.groupBox_39)
        self.pb_move_dsx_pos.setObjectName(u"pb_move_dsx_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_dsx_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_dsx_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_dsx_pos, 2, 4, 1, 1)

        self.db_dsth = QDoubleSpinBox(self.groupBox_39)
        self.db_dsth.setObjectName(u"db_dsth")
        sizePolicy2.setHeightForWidth(self.db_dsth.sizePolicy().hasHeightForWidth())
        self.db_dsth.setSizePolicy(sizePolicy2)
        self.db_dsth.setReadOnly(True)
        self.db_dsth.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_dsth.setDecimals(3)
        self.db_dsth.setMinimum(-200.000000000000000)
        self.db_dsth.setMaximum(200.000000000000000)
        self.db_dsth.setValue(10.000000000000000)

        self.gridLayout_90.addWidget(self.db_dsth, 5, 5, 1, 1)

        self.label_168 = QLabel(self.groupBox_39)
        self.label_168.setObjectName(u"label_168")

        self.gridLayout_90.addWidget(self.label_168, 1, 5, 1, 1)

        self.label_169 = QLabel(self.groupBox_39)
        self.label_169.setObjectName(u"label_169")
        sizePolicy1.setHeightForWidth(self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy1)
        self.label_169.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.label_169, 5, 0, 1, 1)

        self.db_dsx = QDoubleSpinBox(self.groupBox_39)
        self.db_dsx.setObjectName(u"db_dsx")
        sizePolicy2.setHeightForWidth(self.db_dsx.sizePolicy().hasHeightForWidth())
        self.db_dsx.setSizePolicy(sizePolicy2)
        self.db_dsx.setReadOnly(True)
        self.db_dsx.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_dsx.setDecimals(2)
        self.db_dsx.setMinimum(-9999.000000000000000)
        self.db_dsx.setMaximum(9999.000000000000000)
        self.db_dsx.setValue(500.000000000000000)

        self.gridLayout_90.addWidget(self.db_dsx, 2, 5, 1, 1)

        self.db_move_dsz = QDoubleSpinBox(self.groupBox_39)
        self.db_move_dsz.setObjectName(u"db_move_dsz")
        sizePolicy2.setHeightForWidth(self.db_move_dsz.sizePolicy().hasHeightForWidth())
        self.db_move_dsz.setSizePolicy(sizePolicy2)
        self.db_move_dsz.setDecimals(1)
        self.db_move_dsz.setMinimum(-10000.000000000000000)
        self.db_move_dsz.setMaximum(10000.000000000000000)
        self.db_move_dsz.setSingleStep(5.000000000000000)
        self.db_move_dsz.setValue(10.000000000000000)

        self.gridLayout_90.addWidget(self.db_move_dsz, 4, 2, 1, 1)

        self.db_move_dsy = QDoubleSpinBox(self.groupBox_39)
        self.db_move_dsy.setObjectName(u"db_move_dsy")
        sizePolicy2.setHeightForWidth(self.db_move_dsy.sizePolicy().hasHeightForWidth())
        self.db_move_dsy.setSizePolicy(sizePolicy2)
        self.db_move_dsy.setDecimals(1)
        self.db_move_dsy.setMinimum(-10000.000000000000000)
        self.db_move_dsy.setMaximum(10000.000000000000000)
        self.db_move_dsy.setSingleStep(5.000000000000000)
        self.db_move_dsy.setValue(10.000000000000000)

        self.gridLayout_90.addWidget(self.db_move_dsy, 3, 2, 1, 1)

        self.label_170 = QLabel(self.groupBox_39)
        self.label_170.setObjectName(u"label_170")
        sizePolicy1.setHeightForWidth(self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy1)
        self.label_170.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.label_170, 2, 0, 1, 1)

        self.db_move_sbz = QDoubleSpinBox(self.groupBox_39)
        self.db_move_sbz.setObjectName(u"db_move_sbz")
        sizePolicy2.setHeightForWidth(self.db_move_sbz.sizePolicy().hasHeightForWidth())
        self.db_move_sbz.setSizePolicy(sizePolicy2)
        self.db_move_sbz.setDecimals(0)
        self.db_move_sbz.setMinimum(-50000.000000000000000)
        self.db_move_sbz.setMaximum(50000.000000000000000)
        self.db_move_sbz.setSingleStep(100.000000000000000)
        self.db_move_sbz.setValue(100.000000000000000)

        self.gridLayout_90.addWidget(self.db_move_sbz, 6, 2, 1, 1)

        self.db_dsz = QDoubleSpinBox(self.groupBox_39)
        self.db_dsz.setObjectName(u"db_dsz")
        sizePolicy2.setHeightForWidth(self.db_dsz.sizePolicy().hasHeightForWidth())
        self.db_dsz.setSizePolicy(sizePolicy2)
        self.db_dsz.setReadOnly(True)
        self.db_dsz.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_dsz.setDecimals(2)
        self.db_dsz.setMinimum(-9999.000000000000000)
        self.db_dsz.setMaximum(9999.989999999999782)
        self.db_dsz.setValue(500.000000000000000)

        self.gridLayout_90.addWidget(self.db_dsz, 4, 5, 1, 1)

        self.db_move_dsth = QDoubleSpinBox(self.groupBox_39)
        self.db_move_dsth.setObjectName(u"db_move_dsth")
        sizePolicy2.setHeightForWidth(self.db_move_dsth.sizePolicy().hasHeightForWidth())
        self.db_move_dsth.setSizePolicy(sizePolicy2)
        self.db_move_dsth.setMinimum(-120.000000000000000)
        self.db_move_dsth.setMaximum(120.000000000000000)
        self.db_move_dsth.setSingleStep(10.000000000000000)
        self.db_move_dsth.setValue(10.000000000000000)

        self.gridLayout_90.addWidget(self.db_move_dsth, 5, 2, 1, 1)

        self.db_sbz = QDoubleSpinBox(self.groupBox_39)
        self.db_sbz.setObjectName(u"db_sbz")
        sizePolicy2.setHeightForWidth(self.db_sbz.sizePolicy().hasHeightForWidth())
        self.db_sbz.setSizePolicy(sizePolicy2)
        self.db_sbz.setReadOnly(True)
        self.db_sbz.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_sbz.setDecimals(2)
        self.db_sbz.setMinimum(-10000.000000000000000)
        self.db_sbz.setMaximum(100000.000000000000000)
        self.db_sbz.setValue(0.000000000000000)

        self.gridLayout_90.addWidget(self.db_sbz, 6, 5, 1, 1)

        self.label_171 = QLabel(self.groupBox_39)
        self.label_171.setObjectName(u"label_171")
        sizePolicy2.setHeightForWidth(self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy2)
        self.label_171.setStyleSheet(u"")
        self.label_171.setAlignment(Qt.AlignCenter)

        self.gridLayout_90.addWidget(self.label_171, 1, 0, 1, 1)

        self.label_172 = QLabel(self.groupBox_39)
        self.label_172.setObjectName(u"label_172")
        sizePolicy1.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy1)
        self.label_172.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_90.addWidget(self.label_172, 3, 0, 1, 1)

        self.pb_move_sbz_pos = QPushButton(self.groupBox_39)
        self.pb_move_sbz_pos.setObjectName(u"pb_move_sbz_pos")
        sizePolicy2.setHeightForWidth(self.pb_move_sbz_pos.sizePolicy().hasHeightForWidth())
        self.pb_move_sbz_pos.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_sbz_pos, 6, 4, 1, 1)

        self.pb_move_dsx_neg = QPushButton(self.groupBox_39)
        self.pb_move_dsx_neg.setObjectName(u"pb_move_dsx_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_dsx_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_dsx_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_dsx_neg, 2, 1, 1, 1)

        self.pb_move_dsy_neg = QPushButton(self.groupBox_39)
        self.pb_move_dsy_neg.setObjectName(u"pb_move_dsy_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_dsy_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_dsy_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_dsy_neg, 3, 1, 1, 1)

        self.pb_move_dsz_neg = QPushButton(self.groupBox_39)
        self.pb_move_dsz_neg.setObjectName(u"pb_move_dsz_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_dsz_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_dsz_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_dsz_neg, 4, 1, 1, 1)

        self.pb_move_dth_pos_neg = QPushButton(self.groupBox_39)
        self.pb_move_dth_pos_neg.setObjectName(u"pb_move_dth_pos_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_dth_pos_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_dth_pos_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_dth_pos_neg, 5, 1, 1, 1)

        self.pb_move_sbz_neg = QPushButton(self.groupBox_39)
        self.pb_move_sbz_neg.setObjectName(u"pb_move_sbz_neg")
        sizePolicy2.setHeightForWidth(self.pb_move_sbz_neg.sizePolicy().hasHeightForWidth())
        self.pb_move_sbz_neg.setSizePolicy(sizePolicy2)

        self.gridLayout_90.addWidget(self.pb_move_sbz_neg, 6, 1, 1, 1)

        self.pb_mll_stop_all_sample = QPushButton(self.groupBox_39)
        self.pb_mll_stop_all_sample.setObjectName(u"pb_mll_stop_all_sample")
        sizePolicy.setHeightForWidth(self.pb_mll_stop_all_sample.sizePolicy().hasHeightForWidth())
        self.pb_mll_stop_all_sample.setSizePolicy(sizePolicy)
        self.pb_mll_stop_all_sample.setStyleSheet(u"color: rgb(239, 41, 41);")

        self.gridLayout_90.addWidget(self.pb_mll_stop_all_sample, 0, 4, 1, 2)


        self.gridLayout.addWidget(self.groupBox_39, 0, 0, 1, 1)

        self.groupBox_38 = QGroupBox(self.tab)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.groupBox_38.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.groupBox_38.sizePolicy().hasHeightForWidth())
        self.groupBox_38.setSizePolicy(sizePolicy1)
        self.gridLayout_126 = QGridLayout(self.groupBox_38)
        self.gridLayout_126.setObjectName(u"gridLayout_126")
        self.gridLayout_127 = QGridLayout()
        self.gridLayout_127.setObjectName(u"gridLayout_127")
        self.gridLayout_128 = QGridLayout()
        self.gridLayout_128.setObjectName(u"gridLayout_128")
        self.pb_move_pos_mll = QPushButton(self.groupBox_38)
        self.pb_move_pos_mll.setObjectName(u"pb_move_pos_mll")
        sizePolicy2.setHeightForWidth(self.pb_move_pos_mll.sizePolicy().hasHeightForWidth())
        self.pb_move_pos_mll.setSizePolicy(sizePolicy2)
        self.pb_move_pos_mll.setStyleSheet(u"")

        self.gridLayout_128.addWidget(self.pb_move_pos_mll, 2, 0, 1, 1)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pb_save_pos_mll = QPushButton(self.groupBox_38)
        self.pb_save_pos_mll.setObjectName(u"pb_save_pos_mll")
        sizePolicy2.setHeightForWidth(self.pb_save_pos_mll.sizePolicy().hasHeightForWidth())
        self.pb_save_pos_mll.setSizePolicy(sizePolicy2)
        self.pb_save_pos_mll.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.pb_save_pos_mll)


        self.gridLayout_128.addLayout(self.horizontalLayout_39, 0, 0, 1, 1)

        self.pb_copy_curr_pos_mll = QPushButton(self.groupBox_38)
        self.pb_copy_curr_pos_mll.setObjectName(u"pb_copy_curr_pos_mll")

        self.gridLayout_128.addWidget(self.pb_copy_curr_pos_mll, 1, 0, 1, 1)


        self.gridLayout_127.addLayout(self.gridLayout_128, 0, 0, 1, 1)

        self.mll_sample_roi_list_widget = QListWidget(self.groupBox_38)
        self.mll_sample_roi_list_widget.setObjectName(u"mll_sample_roi_list_widget")
        sizePolicy6.setHeightForWidth(self.mll_sample_roi_list_widget.sizePolicy().hasHeightForWidth())
        self.mll_sample_roi_list_widget.setSizePolicy(sizePolicy6)

        self.gridLayout_127.addWidget(self.mll_sample_roi_list_widget, 1, 0, 1, 1)

        self.gridLayout_129 = QGridLayout()
        self.gridLayout_129.setObjectName(u"gridLayout_129")
        self.pb_roiList_clear_mll = QPushButton(self.groupBox_38)
        self.pb_roiList_clear_mll.setObjectName(u"pb_roiList_clear_mll")

        self.gridLayout_129.addWidget(self.pb_roiList_clear_mll, 2, 0, 1, 1)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.pb_roiList_export_mll = QPushButton(self.groupBox_38)
        self.pb_roiList_export_mll.setObjectName(u"pb_roiList_export_mll")

        self.horizontalLayout_81.addWidget(self.pb_roiList_export_mll)

        self.pb_roiList_import_mll = QPushButton(self.groupBox_38)
        self.pb_roiList_import_mll.setObjectName(u"pb_roiList_import_mll")

        self.horizontalLayout_81.addWidget(self.pb_roiList_import_mll)


        self.gridLayout_129.addLayout(self.horizontalLayout_81, 0, 0, 1, 1)

        self.pb_roiList_clear_sel_mll = QPushButton(self.groupBox_38)
        self.pb_roiList_clear_sel_mll.setObjectName(u"pb_roiList_clear_sel_mll")

        self.gridLayout_129.addWidget(self.pb_roiList_clear_sel_mll, 1, 0, 1, 1)


        self.gridLayout_127.addLayout(self.gridLayout_129, 2, 0, 1, 1)


        self.gridLayout_126.addLayout(self.gridLayout_127, 1, 0, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_126.addItem(self.verticalSpacer_30, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_38, 0, 1, 1, 1)

        self.groupBox_13 = QGroupBox(self.tab)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy1.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy1)
        self.gridLayout_85 = QGridLayout(self.groupBox_13)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_166 = QLabel(self.groupBox_13)
        self.label_166.setObjectName(u"label_166")
        sizePolicy2.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy2)
        self.label_166.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_166)

        self.le_sid_position_mll = QLineEdit(self.groupBox_13)
        self.le_sid_position_mll.setObjectName(u"le_sid_position_mll")
        sizePolicy2.setHeightForWidth(self.le_sid_position_mll.sizePolicy().hasHeightForWidth())
        self.le_sid_position_mll.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.le_sid_position_mll)


        self.gridLayout_85.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.pb_recover_scan_pos_mll = QPushButton(self.groupBox_13)
        self.pb_recover_scan_pos_mll.setObjectName(u"pb_recover_scan_pos_mll")
        self.pb_recover_scan_pos_mll.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pb_recover_scan_pos_mll.sizePolicy().hasHeightForWidth())
        self.pb_recover_scan_pos_mll.setSizePolicy(sizePolicy2)

        self.gridLayout_85.addWidget(self.pb_recover_scan_pos_mll, 2, 0, 1, 1)

        self.cb_sid_move_base_mll = QCheckBox(self.groupBox_13)
        self.cb_sid_move_base_mll.setObjectName(u"cb_sid_move_base_mll")
        sizePolicy2.setHeightForWidth(self.cb_sid_move_base_mll.sizePolicy().hasHeightForWidth())
        self.cb_sid_move_base_mll.setSizePolicy(sizePolicy2)

        self.gridLayout_85.addWidget(self.cb_sid_move_base_mll, 3, 0, 1, 1)

        self.pb_print_scan_meta_mll = QPushButton(self.groupBox_13)
        self.pb_print_scan_meta_mll.setObjectName(u"pb_print_scan_meta_mll")
        sizePolicy2.setHeightForWidth(self.pb_print_scan_meta_mll.sizePolicy().hasHeightForWidth())
        self.pb_print_scan_meta_mll.setSizePolicy(sizePolicy2)

        self.gridLayout_85.addWidget(self.pb_print_scan_meta_mll, 5, 0, 1, 1)

        self.pb_show_scan_pos_mll = QPushButton(self.groupBox_13)
        self.pb_show_scan_pos_mll.setObjectName(u"pb_show_scan_pos_mll")
        sizePolicy2.setHeightForWidth(self.pb_show_scan_pos_mll.sizePolicy().hasHeightForWidth())
        self.pb_show_scan_pos_mll.setSizePolicy(sizePolicy2)

        self.gridLayout_85.addWidget(self.pb_show_scan_pos_mll, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_13, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_11.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_11.addWidget(self.label_6, 0, 0, 1, 1)


        self.gridLayout_91.addWidget(self.groupBox_6, 2, 0, 1, 1)

        self.tabWidget_18 = QTabWidget(self.scan_tab)
        self.tabWidget_18.setObjectName(u"tabWidget_18")
        sizePolicy.setHeightForWidth(self.tabWidget_18.sizePolicy().hasHeightForWidth())
        self.tabWidget_18.setSizePolicy(sizePolicy)
        self.tabWidget_18.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_18Page1 = QWidget()
        self.tabWidget_18Page1.setObjectName(u"tabWidget_18Page1")
        self.gridLayout_136 = QGridLayout(self.tabWidget_18Page1)
        self.gridLayout_136.setObjectName(u"gridLayout_136")
        self.label_130 = QLabel(self.tabWidget_18Page1)
        self.label_130.setObjectName(u"label_130")
        sizePolicy2.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy2)

        self.gridLayout_136.addWidget(self.label_130, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.tabWidget_18Page1)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.gridLayout_117 = QGridLayout(self.groupBox)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.pb_stop_fluor = QPushButton(self.groupBox)
        self.pb_stop_fluor.setObjectName(u"pb_stop_fluor")
        sizePolicy.setHeightForWidth(self.pb_stop_fluor.sizePolicy().hasHeightForWidth())
        self.pb_stop_fluor.setSizePolicy(sizePolicy)
        self.pb_stop_fluor.setStyleSheet(u"color: rgb(239, 41, 41);")

        self.gridLayout_117.addWidget(self.pb_stop_fluor, 1, 0, 1, 1)

        self.label_55 = QLabel(self.groupBox)
        self.label_55.setObjectName(u"label_55")
        sizePolicy2.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy2)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_117.addWidget(self.label_55, 0, 0, 1, 1)

        self.pb_stop_dexela = QPushButton(self.groupBox)
        self.pb_stop_dexela.setObjectName(u"pb_stop_dexela")
        sizePolicy.setHeightForWidth(self.pb_stop_dexela.sizePolicy().hasHeightForWidth())
        self.pb_stop_dexela.setSizePolicy(sizePolicy)
        self.pb_stop_dexela.setStyleSheet(u"color: rgb(239, 41, 41);")

        self.gridLayout_117.addWidget(self.pb_stop_dexela, 2, 0, 1, 1)

        self.pb_stop_cam11 = QPushButton(self.groupBox)
        self.pb_stop_cam11.setObjectName(u"pb_stop_cam11")
        sizePolicy.setHeightForWidth(self.pb_stop_cam11.sizePolicy().hasHeightForWidth())
        self.pb_stop_cam11.setSizePolicy(sizePolicy)
        self.pb_stop_cam11.setStyleSheet(u"color: rgb(239, 41, 41);")

        self.gridLayout_117.addWidget(self.pb_stop_cam11, 3, 0, 1, 1)

        self.pb_stop_merlin = QPushButton(self.groupBox)
        self.pb_stop_merlin.setObjectName(u"pb_stop_merlin")
        sizePolicy.setHeightForWidth(self.pb_stop_merlin.sizePolicy().hasHeightForWidth())
        self.pb_stop_merlin.setSizePolicy(sizePolicy)
        self.pb_stop_merlin.setStyleSheet(u"color: rgb(239, 41, 41);")

        self.gridLayout_117.addWidget(self.pb_stop_merlin, 4, 0, 1, 1)


        self.gridLayout_136.addWidget(self.groupBox, 1, 3, 1, 1)

        self.groupBox1 = QGroupBox(self.tabWidget_18Page1)
        self.groupBox1.setObjectName(u"groupBox1")
        self.gridLayout_7 = QGridLayout(self.groupBox1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_68 = QLabel(self.groupBox1)
        self.label_68.setObjectName(u"label_68")
        sizePolicy2.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.label_68, 0, 0, 1, 1)

        self.gridLayout_124 = QGridLayout()
        self.gridLayout_124.setObjectName(u"gridLayout_124")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pb_cam6IN = QPushButton(self.groupBox1)
        self.pb_cam6IN.setObjectName(u"pb_cam6IN")
        self.pb_cam6IN.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_cam6IN.sizePolicy().hasHeightForWidth())
        self.pb_cam6IN.setSizePolicy(sizePolicy)

        self.gridLayout_16.addWidget(self.pb_cam6IN, 0, 0, 1, 1)

        self.pb_vortexIN = QPushButton(self.groupBox1)
        self.pb_vortexIN.setObjectName(u"pb_vortexIN")
        sizePolicy.setHeightForWidth(self.pb_vortexIN.sizePolicy().hasHeightForWidth())
        self.pb_vortexIN.setSizePolicy(sizePolicy)

        self.gridLayout_16.addWidget(self.pb_vortexIN, 1, 0, 1, 1)

        self.pb_dexela_IN = QPushButton(self.groupBox1)
        self.pb_dexela_IN.setObjectName(u"pb_dexela_IN")
        sizePolicy.setHeightForWidth(self.pb_dexela_IN.sizePolicy().hasHeightForWidth())
        self.pb_dexela_IN.setSizePolicy(sizePolicy)

        self.gridLayout_16.addWidget(self.pb_dexela_IN, 2, 0, 1, 1)

        self.pb_cam11IN = QPushButton(self.groupBox1)
        self.pb_cam11IN.setObjectName(u"pb_cam11IN")
        sizePolicy.setHeightForWidth(self.pb_cam11IN.sizePolicy().hasHeightForWidth())
        self.pb_cam11IN.setSizePolicy(sizePolicy)

        self.gridLayout_16.addWidget(self.pb_cam11IN, 3, 0, 1, 1)

        self.pb_merlinIN = QPushButton(self.groupBox1)
        self.pb_merlinIN.setObjectName(u"pb_merlinIN")
        sizePolicy.setHeightForWidth(self.pb_merlinIN.sizePolicy().hasHeightForWidth())
        self.pb_merlinIN.setSizePolicy(sizePolicy)

        self.gridLayout_16.addWidget(self.pb_merlinIN, 4, 0, 1, 1)


        self.gridLayout_124.addLayout(self.gridLayout_16, 0, 0, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.pb_vortexOUT = QPushButton(self.groupBox1)
        self.pb_vortexOUT.setObjectName(u"pb_vortexOUT")
        sizePolicy.setHeightForWidth(self.pb_vortexOUT.sizePolicy().hasHeightForWidth())
        self.pb_vortexOUT.setSizePolicy(sizePolicy)

        self.gridLayout_24.addWidget(self.pb_vortexOUT, 1, 0, 1, 1)

        self.pb_dexela_OUT = QPushButton(self.groupBox1)
        self.pb_dexela_OUT.setObjectName(u"pb_dexela_OUT")
        sizePolicy.setHeightForWidth(self.pb_dexela_OUT.sizePolicy().hasHeightForWidth())
        self.pb_dexela_OUT.setSizePolicy(sizePolicy)

        self.gridLayout_24.addWidget(self.pb_dexela_OUT, 2, 0, 1, 1)

        self.pb_telescope = QPushButton(self.groupBox1)
        self.pb_telescope.setObjectName(u"pb_telescope")
        self.pb_telescope.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_telescope.sizePolicy().hasHeightForWidth())
        self.pb_telescope.setSizePolicy(sizePolicy)

        self.gridLayout_24.addWidget(self.pb_telescope, 3, 0, 1, 1)

        self.pb_cam6OUT = QPushButton(self.groupBox1)
        self.pb_cam6OUT.setObjectName(u"pb_cam6OUT")
        self.pb_cam6OUT.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_cam6OUT.sizePolicy().hasHeightForWidth())
        self.pb_cam6OUT.setSizePolicy(sizePolicy)

        self.gridLayout_24.addWidget(self.pb_cam6OUT, 0, 0, 1, 1)

        self.pb_merlinOUT = QPushButton(self.groupBox1)
        self.pb_merlinOUT.setObjectName(u"pb_merlinOUT")
        sizePolicy.setHeightForWidth(self.pb_merlinOUT.sizePolicy().hasHeightForWidth())
        self.pb_merlinOUT.setSizePolicy(sizePolicy)

        self.gridLayout_24.addWidget(self.pb_merlinOUT, 4, 0, 1, 1)


        self.gridLayout_124.addLayout(self.gridLayout_24, 0, 1, 1, 1)

        self.gridLayout_100 = QGridLayout()
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.db_fs_det = QDoubleSpinBox(self.groupBox1)
        self.db_fs_det.setObjectName(u"db_fs_det")
        sizePolicy.setHeightForWidth(self.db_fs_det.sizePolicy().hasHeightForWidth())
        self.db_fs_det.setSizePolicy(sizePolicy)
        self.db_fs_det.setReadOnly(True)
        self.db_fs_det.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_fs_det.setDecimals(1)
        self.db_fs_det.setMinimum(-150.000000000000000)
        self.db_fs_det.setValue(1.000000000000000)

        self.gridLayout_100.addWidget(self.db_fs_det, 1, 0, 1, 1)

        self.db_cam06x = QDoubleSpinBox(self.groupBox1)
        self.db_cam06x.setObjectName(u"db_cam06x")
        sizePolicy.setHeightForWidth(self.db_cam06x.sizePolicy().hasHeightForWidth())
        self.db_cam06x.setSizePolicy(sizePolicy)
        self.db_cam06x.setReadOnly(True)
        self.db_cam06x.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_cam06x.setDecimals(1)
        self.db_cam06x.setMinimum(-99.000000000000000)
        self.db_cam06x.setValue(1.000000000000000)

        self.gridLayout_100.addWidget(self.db_cam06x, 0, 0, 1, 1)

        self.label_57 = QLabel(self.groupBox1)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_100.addWidget(self.label_57, 3, 0, 1, 1)

        self.db_dexela = QDoubleSpinBox(self.groupBox1)
        self.db_dexela.setObjectName(u"db_dexela")
        sizePolicy.setHeightForWidth(self.db_dexela.sizePolicy().hasHeightForWidth())
        self.db_dexela.setSizePolicy(sizePolicy)
        self.db_dexela.setReadOnly(True)
        self.db_dexela.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_dexela.setDecimals(1)
        self.db_dexela.setMinimum(-99.000000000000000)
        self.db_dexela.setMaximum(500.000000000000000)
        self.db_dexela.setValue(1.000000000000000)

        self.gridLayout_100.addWidget(self.db_dexela, 2, 0, 1, 1)

        self.db_diffx = QDoubleSpinBox(self.groupBox1)
        self.db_diffx.setObjectName(u"db_diffx")
        sizePolicy.setHeightForWidth(self.db_diffx.sizePolicy().hasHeightForWidth())
        self.db_diffx.setSizePolicy(sizePolicy)
        self.db_diffx.setReadOnly(True)
        self.db_diffx.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_diffx.setDecimals(1)
        self.db_diffx.setMinimum(-1500.000000000000000)
        self.db_diffx.setMaximum(1500.000000000000000)
        self.db_diffx.setValue(1.000000000000000)

        self.gridLayout_100.addWidget(self.db_diffx, 4, 0, 1, 1)


        self.gridLayout_124.addLayout(self.gridLayout_100, 0, 2, 1, 1)

        self.pb_eiger_in = QPushButton(self.groupBox1)
        self.pb_eiger_in.setObjectName(u"pb_eiger_in")

        self.gridLayout_124.addWidget(self.pb_eiger_in, 1, 0, 1, 1)

        self.pb_laser_in = QPushButton(self.groupBox1)
        self.pb_laser_in.setObjectName(u"pb_laser_in")

        self.gridLayout_124.addWidget(self.pb_laser_in, 1, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_124, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_74 = QLabel(self.groupBox1)
        self.label_74.setObjectName(u"label_74")
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_74)

        self.dsb_flur_in_pos = QDoubleSpinBox(self.groupBox1)
        self.dsb_flur_in_pos.setObjectName(u"dsb_flur_in_pos")
        sizePolicy2.setHeightForWidth(self.dsb_flur_in_pos.sizePolicy().hasHeightForWidth())
        self.dsb_flur_in_pos.setSizePolicy(sizePolicy2)
        self.dsb_flur_in_pos.setDecimals(1)
        self.dsb_flur_in_pos.setMinimum(-100.000000000000000)
        self.dsb_flur_in_pos.setMaximum(-7.000000000000000)
        self.dsb_flur_in_pos.setValue(-9.000000000000000)

        self.horizontalLayout_7.addWidget(self.dsb_flur_in_pos)


        self.gridLayout_7.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)


        self.gridLayout_136.addWidget(self.groupBox1, 1, 0, 1, 1)

        self.groupBox_11 = QGroupBox(self.tabWidget_18Page1)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_42 = QGridLayout(self.groupBox_11)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.label_67 = QLabel(self.groupBox_11)
        self.label_67.setObjectName(u"label_67")
        sizePolicy2.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy2)

        self.gridLayout_42.addWidget(self.label_67, 0, 0, 1, 1)

        self.gridLayout_137 = QGridLayout()
        self.gridLayout_137.setObjectName(u"gridLayout_137")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.sp_dexela_xpixel = QSpinBox(self.groupBox_11)
        self.sp_dexela_xpixel.setObjectName(u"sp_dexela_xpixel")
        sizePolicy2.setHeightForWidth(self.sp_dexela_xpixel.sizePolicy().hasHeightForWidth())
        self.sp_dexela_xpixel.setSizePolicy(sizePolicy2)
        self.sp_dexela_xpixel.setMaximum(9999)
        self.sp_dexela_xpixel.setSingleStep(10)
        self.sp_dexela_xpixel.setValue(55)

        self.horizontalLayout_15.addWidget(self.sp_dexela_xpixel)

        self.sp_dexela_ypixel = QSpinBox(self.groupBox_11)
        self.sp_dexela_ypixel.setObjectName(u"sp_dexela_ypixel")
        sizePolicy2.setHeightForWidth(self.sp_dexela_ypixel.sizePolicy().hasHeightForWidth())
        self.sp_dexela_ypixel.setSizePolicy(sizePolicy2)
        self.sp_dexela_ypixel.setMaximum(9999)
        self.sp_dexela_ypixel.setSingleStep(10)
        self.sp_dexela_ypixel.setValue(99)

        self.horizontalLayout_15.addWidget(self.sp_dexela_ypixel)

        self.pb_pos_to_angle = QPushButton(self.groupBox_11)
        self.pb_pos_to_angle.setObjectName(u"pb_pos_to_angle")
        sizePolicy.setHeightForWidth(self.pb_pos_to_angle.sizePolicy().hasHeightForWidth())
        self.pb_pos_to_angle.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.pb_pos_to_angle)


        self.gridLayout_137.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_65 = QLabel(self.groupBox_11)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setLineWidth(0)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_65)

        self.pb_read_dexela_ROI1 = QPushButton(self.groupBox_11)
        self.pb_read_dexela_ROI1.setObjectName(u"pb_read_dexela_ROI1")

        self.horizontalLayout_21.addWidget(self.pb_read_dexela_ROI1)

        self.pb_reset_dexela_ROI1 = QPushButton(self.groupBox_11)
        self.pb_reset_dexela_ROI1.setObjectName(u"pb_reset_dexela_ROI1")

        self.horizontalLayout_21.addWidget(self.pb_reset_dexela_ROI1)


        self.gridLayout_137.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)


        self.gridLayout_42.addLayout(self.gridLayout_137, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sp_diff_det_calc_x = QDoubleSpinBox(self.groupBox_11)
        self.sp_diff_det_calc_x.setObjectName(u"sp_diff_det_calc_x")
        sizePolicy2.setHeightForWidth(self.sp_diff_det_calc_x.sizePolicy().hasHeightForWidth())
        self.sp_diff_det_calc_x.setSizePolicy(sizePolicy2)
        self.sp_diff_det_calc_x.setDecimals(2)
        self.sp_diff_det_calc_x.setValue(0.000000000000000)

        self.horizontalLayout_9.addWidget(self.sp_diff_det_calc_x)

        self.sp_diff_det_calc_y = QDoubleSpinBox(self.groupBox_11)
        self.sp_diff_det_calc_y.setObjectName(u"sp_diff_det_calc_y")
        sizePolicy2.setHeightForWidth(self.sp_diff_det_calc_y.sizePolicy().hasHeightForWidth())
        self.sp_diff_det_calc_y.setSizePolicy(sizePolicy2)
        self.sp_diff_det_calc_y.setMinimum(-5.000000000000000)
        self.sp_diff_det_calc_y.setMaximum(25.000000000000000)
        self.sp_diff_det_calc_y.setValue(0.000000000000000)

        self.horizontalLayout_9.addWidget(self.sp_diff_det_calc_y)


        self.gridLayout_42.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.sp_diff_det_calc_2theta = QDoubleSpinBox(self.groupBox_11)
        self.sp_diff_det_calc_2theta.setObjectName(u"sp_diff_det_calc_2theta")
        sizePolicy2.setHeightForWidth(self.sp_diff_det_calc_2theta.sizePolicy().hasHeightForWidth())
        self.sp_diff_det_calc_2theta.setSizePolicy(sizePolicy2)
        self.sp_diff_det_calc_2theta.setDecimals(1)
        self.sp_diff_det_calc_2theta.setValue(25.000000000000000)

        self.horizontalLayout_8.addWidget(self.sp_diff_det_calc_2theta)

        self.sp_diff_det_r = QDoubleSpinBox(self.groupBox_11)
        self.sp_diff_det_r.setObjectName(u"sp_diff_det_r")
        sizePolicy2.setHeightForWidth(self.sp_diff_det_r.sizePolicy().hasHeightForWidth())
        self.sp_diff_det_r.setSizePolicy(sizePolicy2)
        self.sp_diff_det_r.setMaximum(5000.000000000000000)
        self.sp_diff_det_r.setValue(500.000000000000000)

        self.horizontalLayout_8.addWidget(self.sp_diff_det_r)


        self.gridLayout_42.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_73 = QLabel(self.groupBox_11)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_73)

        self.dsb_move_diff_z_rel_value = QDoubleSpinBox(self.groupBox_11)
        self.dsb_move_diff_z_rel_value.setObjectName(u"dsb_move_diff_z_rel_value")
        self.dsb_move_diff_z_rel_value.setMinimum(-50.000000000000000)
        self.dsb_move_diff_z_rel_value.setMaximum(50.000000000000000)

        self.horizontalLayout_23.addWidget(self.dsb_move_diff_z_rel_value)

        self.pb_move_diff_z = QPushButton(self.groupBox_11)
        self.pb_move_diff_z.setObjectName(u"pb_move_diff_z")

        self.horizontalLayout_23.addWidget(self.pb_move_diff_z)


        self.gridLayout_42.addLayout(self.horizontalLayout_23, 4, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pb_move_diff = QPushButton(self.groupBox_11)
        self.pb_move_diff.setObjectName(u"pb_move_diff")
        sizePolicy.setHeightForWidth(self.pb_move_diff.sizePolicy().hasHeightForWidth())
        self.pb_move_diff.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.pb_move_diff)

        self.pb_abort_diff = QPushButton(self.groupBox_11)
        self.pb_abort_diff.setObjectName(u"pb_abort_diff")
        sizePolicy.setHeightForWidth(self.pb_abort_diff.sizePolicy().hasHeightForWidth())
        self.pb_abort_diff.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.pb_abort_diff)

        self.pb_copy_pos2angle = QPushButton(self.groupBox_11)
        self.pb_copy_pos2angle.setObjectName(u"pb_copy_pos2angle")
        sizePolicy.setHeightForWidth(self.pb_copy_pos2angle.sizePolicy().hasHeightForWidth())
        self.pb_copy_pos2angle.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.pb_copy_pos2angle)

        self.cb_mll_theta_for_diff = QCheckBox(self.groupBox_11)
        self.cb_mll_theta_for_diff.setObjectName(u"cb_mll_theta_for_diff")
        self.cb_mll_theta_for_diff.setChecked(False)

        self.horizontalLayout_13.addWidget(self.cb_mll_theta_for_diff)


        self.gridLayout_42.addLayout(self.horizontalLayout_13, 5, 0, 1, 1)


        self.gridLayout_136.addWidget(self.groupBox_11, 1, 2, 1, 1)

        self.tabWidget_18.addTab(self.tabWidget_18Page1, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_118 = QGridLayout(self.tab_12)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.label_54 = QLabel(self.tab_12)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_118.addWidget(self.label_54, 2, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_12)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_138 = QGridLayout(self.groupBox_14)
        self.gridLayout_138.setObjectName(u"gridLayout_138")
        self.label_63 = QLabel(self.groupBox_14)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_138.addWidget(self.label_63, 2, 0, 1, 1)

        self.pb_cam11_disable_flatfield = QPushButton(self.groupBox_14)
        self.pb_cam11_disable_flatfield.setObjectName(u"pb_cam11_disable_flatfield")
        sizePolicy.setHeightForWidth(self.pb_cam11_disable_flatfield.sizePolicy().hasHeightForWidth())
        self.pb_cam11_disable_flatfield.setSizePolicy(sizePolicy)

        self.gridLayout_138.addWidget(self.pb_cam11_disable_flatfield, 1, 1, 1, 1)

        self.pb_cam11_flatfield = QPushButton(self.groupBox_14)
        self.pb_cam11_flatfield.setObjectName(u"pb_cam11_flatfield")
        sizePolicy.setHeightForWidth(self.pb_cam11_flatfield.sizePolicy().hasHeightForWidth())
        self.pb_cam11_flatfield.setSizePolicy(sizePolicy)

        self.gridLayout_138.addWidget(self.pb_cam11_flatfield, 1, 0, 1, 1)

        self.cb_dets_for_ff_corr = QComboBox(self.groupBox_14)
        self.cb_dets_for_ff_corr.setObjectName(u"cb_dets_for_ff_corr")

        self.gridLayout_138.addWidget(self.cb_dets_for_ff_corr, 2, 1, 1, 1)

        self.label_62 = QLabel(self.groupBox_14)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_138.addWidget(self.label_62, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.groupBox_14)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)

        self.gridLayout_138.addWidget(self.pushButton_12, 3, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.groupBox_14)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)

        self.gridLayout_138.addWidget(self.pushButton_16, 3, 1, 1, 1)


        self.gridLayout_118.addWidget(self.groupBox_14, 0, 1, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_27 = QLabel(self.tab_12)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_24.addWidget(self.label_27)

        self.cb_det_names_for_pos = QComboBox(self.tab_12)
        self.cb_det_names_for_pos.setObjectName(u"cb_det_names_for_pos")
        sizePolicy2.setHeightForWidth(self.cb_det_names_for_pos.sizePolicy().hasHeightForWidth())
        self.cb_det_names_for_pos.setSizePolicy(sizePolicy2)

        self.verticalLayout_24.addWidget(self.cb_det_names_for_pos)

        self.pb_update_dets_pos = QPushButton(self.tab_12)
        self.pb_update_dets_pos.setObjectName(u"pb_update_dets_pos")
        sizePolicy.setHeightForWidth(self.pb_update_dets_pos.sizePolicy().hasHeightForWidth())
        self.pb_update_dets_pos.setSizePolicy(sizePolicy)

        self.verticalLayout_24.addWidget(self.pb_update_dets_pos)


        self.gridLayout_118.addLayout(self.verticalLayout_24, 0, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab_12)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_110 = QGridLayout(self.groupBox_15)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.gridLayout_125 = QGridLayout()
        self.gridLayout_125.setObjectName(u"gridLayout_125")
        self.pb_merlin_filterIN = QPushButton(self.groupBox_15)
        self.pb_merlin_filterIN.setObjectName(u"pb_merlin_filterIN")
        sizePolicy.setHeightForWidth(self.pb_merlin_filterIN.sizePolicy().hasHeightForWidth())
        self.pb_merlin_filterIN.setSizePolicy(sizePolicy)

        self.gridLayout_125.addWidget(self.pb_merlin_filterIN, 1, 0, 1, 1)

        self.pb_merlin_filterOUT = QPushButton(self.groupBox_15)
        self.pb_merlin_filterOUT.setObjectName(u"pb_merlin_filterOUT")
        sizePolicy.setHeightForWidth(self.pb_merlin_filterOUT.sizePolicy().hasHeightForWidth())
        self.pb_merlin_filterOUT.setSizePolicy(sizePolicy)

        self.gridLayout_125.addWidget(self.pb_merlin_filterOUT, 1, 1, 1, 1)

        self.pb_light_OFF = QPushButton(self.groupBox_15)
        self.pb_light_OFF.setObjectName(u"pb_light_OFF")
        sizePolicy.setHeightForWidth(self.pb_light_OFF.sizePolicy().hasHeightForWidth())
        self.pb_light_OFF.setSizePolicy(sizePolicy)

        self.gridLayout_125.addWidget(self.pb_light_OFF, 2, 1, 1, 1)

        self.pb_light_ON = QPushButton(self.groupBox_15)
        self.pb_light_ON.setObjectName(u"pb_light_ON")
        sizePolicy.setHeightForWidth(self.pb_light_ON.sizePolicy().hasHeightForWidth())
        self.pb_light_ON.setSizePolicy(sizePolicy)

        self.gridLayout_125.addWidget(self.pb_light_ON, 2, 0, 1, 1)

        self.label_64 = QLabel(self.groupBox_15)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_125.addWidget(self.label_64, 0, 0, 1, 1)


        self.gridLayout_110.addLayout(self.gridLayout_125, 0, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pb_eiger_filter_a_in = QPushButton(self.groupBox_15)
        self.pb_eiger_filter_a_in.setObjectName(u"pb_eiger_filter_a_in")

        self.horizontalLayout_17.addWidget(self.pb_eiger_filter_a_in)

        self.pb_eiger_filter_a_out = QPushButton(self.groupBox_15)
        self.pb_eiger_filter_a_out.setObjectName(u"pb_eiger_filter_a_out")

        self.horizontalLayout_17.addWidget(self.pb_eiger_filter_a_out)


        self.gridLayout_110.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pb_eiger_filter_b_in = QPushButton(self.groupBox_15)
        self.pb_eiger_filter_b_in.setObjectName(u"pb_eiger_filter_b_in")

        self.horizontalLayout_19.addWidget(self.pb_eiger_filter_b_in)

        self.pb_eiger_filter_b_out = QPushButton(self.groupBox_15)
        self.pb_eiger_filter_b_out.setObjectName(u"pb_eiger_filter_b_out")

        self.horizontalLayout_19.addWidget(self.pb_eiger_filter_b_out)


        self.gridLayout_110.addLayout(self.horizontalLayout_19, 2, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pb_eiger_filter_c_in = QPushButton(self.groupBox_15)
        self.pb_eiger_filter_c_in.setObjectName(u"pb_eiger_filter_c_in")

        self.horizontalLayout_20.addWidget(self.pb_eiger_filter_c_in)

        self.pb_eiger_filter_c_out = QPushButton(self.groupBox_15)
        self.pb_eiger_filter_c_out.setObjectName(u"pb_eiger_filter_c_out")

        self.horizontalLayout_20.addWidget(self.pb_eiger_filter_c_out)


        self.gridLayout_110.addLayout(self.horizontalLayout_20, 3, 0, 1, 1)


        self.gridLayout_118.addWidget(self.groupBox_15, 0, 2, 2, 1)

        self.tabWidget_18.addTab(self.tab_12, "")

        self.gridLayout_91.addWidget(self.tabWidget_18, 1, 0, 1, 2)

        self.groupBox2 = QGroupBox(self.scan_tab)
        self.groupBox2.setObjectName(u"groupBox2")
        sizePolicy.setHeightForWidth(self.groupBox2.sizePolicy().hasHeightForWidth())
        self.groupBox2.setSizePolicy(sizePolicy)
        self.gridLayout_55 = QGridLayout(self.groupBox2)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.label_51 = QLabel(self.groupBox2)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)

        self.gridLayout_55.addWidget(self.label_51, 0, 0, 1, 1)

        self.gridLayout_51 = QGridLayout()
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_48 = QLabel(self.groupBox2)
        self.label_48.setObjectName(u"label_48")
        sizePolicy1.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy1)
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_48, 0, 0, 1, 1)

        self.cb_plot_elem = QComboBox(self.groupBox2)
        self.cb_plot_elem.setObjectName(u"cb_plot_elem")
        sizePolicy2.setHeightForWidth(self.cb_plot_elem.sizePolicy().hasHeightForWidth())
        self.cb_plot_elem.setSizePolicy(sizePolicy2)

        self.gridLayout_10.addWidget(self.cb_plot_elem, 0, 1, 1, 1)


        self.gridLayout_51.addLayout(self.gridLayout_10, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_47 = QLabel(self.groupBox2)
        self.label_47.setObjectName(u"label_47")
        sizePolicy1.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy1)
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_47, 0, 0, 1, 1)

        self.le_plot_sd = QLineEdit(self.groupBox2)
        self.le_plot_sd.setObjectName(u"le_plot_sd")
        sizePolicy2.setHeightForWidth(self.le_plot_sd.sizePolicy().hasHeightForWidth())
        self.le_plot_sd.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.le_plot_sd, 0, 1, 1, 1)

        self.pb_plot_last = QPushButton(self.groupBox2)
        self.pb_plot_last.setObjectName(u"pb_plot_last")
        sizePolicy5.setHeightForWidth(self.pb_plot_last.sizePolicy().hasHeightForWidth())
        self.pb_plot_last.setSizePolicy(sizePolicy5)
        self.pb_plot_last.setMinimumSize(QSize(80, 23))

        self.gridLayout_2.addWidget(self.pb_plot_last, 0, 2, 1, 1)


        self.gridLayout_51.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_55.addLayout(self.gridLayout_51, 1, 0, 1, 2)

        self.gridLayout_54 = QGridLayout()
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pb_erf_fit = QPushButton(self.groupBox2)
        self.pb_erf_fit.setObjectName(u"pb_erf_fit")
        sizePolicy2.setHeightForWidth(self.pb_erf_fit.sizePolicy().hasHeightForWidth())
        self.pb_erf_fit.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.pb_erf_fit, 0, 0, 1, 1)

        self.cb_erf_linear_flag = QCheckBox(self.groupBox2)
        self.cb_erf_linear_flag.setObjectName(u"cb_erf_linear_flag")
        sizePolicy5.setHeightForWidth(self.cb_erf_linear_flag.sizePolicy().hasHeightForWidth())
        self.cb_erf_linear_flag.setSizePolicy(sizePolicy5)
        self.cb_erf_linear_flag.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_5.addWidget(self.cb_erf_linear_flag, 0, 1, 1, 1)


        self.gridLayout_54.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, 0, -1)
        self.label_49 = QLabel(self.groupBox2)
        self.label_49.setObjectName(u"label_49")
        sizePolicy5.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy5)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_49)

        self.dsb_line_center_thre = QDoubleSpinBox(self.groupBox2)
        self.dsb_line_center_thre.setObjectName(u"dsb_line_center_thre")
        sizePolicy5.setHeightForWidth(self.dsb_line_center_thre.sizePolicy().hasHeightForWidth())
        self.dsb_line_center_thre.setSizePolicy(sizePolicy5)
        self.dsb_line_center_thre.setMinimum(0.010000000000000)
        self.dsb_line_center_thre.setMaximum(1.000000000000000)
        self.dsb_line_center_thre.setValue(0.500000000000000)

        self.horizontalLayout_14.addWidget(self.dsb_line_center_thre)


        self.gridLayout_18.addLayout(self.horizontalLayout_14, 0, 1, 1, 1)

        self.pb_plot_line_center = QPushButton(self.groupBox2)
        self.pb_plot_line_center.setObjectName(u"pb_plot_line_center")
        sizePolicy2.setHeightForWidth(self.pb_plot_line_center.sizePolicy().hasHeightForWidth())
        self.pb_plot_line_center.setSizePolicy(sizePolicy2)

        self.gridLayout_18.addWidget(self.pb_plot_line_center, 0, 0, 1, 1)


        self.gridLayout_54.addLayout(self.gridLayout_18, 1, 0, 1, 1)


        self.gridLayout_55.addLayout(self.gridLayout_54, 3, 0, 1, 2)

        self.pb_plot = QPushButton(self.groupBox2)
        self.pb_plot.setObjectName(u"pb_plot")
        sizePolicy2.setHeightForWidth(self.pb_plot.sizePolicy().hasHeightForWidth())
        self.pb_plot.setSizePolicy(sizePolicy2)
        self.pb_plot.setStyleSheet(u"QPushButton:pressed{ \n"
"	background-color: rgb(255, 0, 0); \n"
"	}")

        self.gridLayout_55.addWidget(self.pb_plot, 2, 0, 1, 2)

        self.pb_close_all_plot = QPushButton(self.groupBox2)
        self.pb_close_all_plot.setObjectName(u"pb_close_all_plot")
        sizePolicy2.setHeightForWidth(self.pb_close_all_plot.sizePolicy().hasHeightForWidth())
        self.pb_close_all_plot.setSizePolicy(sizePolicy2)
        self.pb_close_all_plot.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_55.addWidget(self.pb_close_all_plot, 4, 0, 1, 2)


        self.gridLayout_91.addWidget(self.groupBox2, 2, 1, 1, 1)

        self.HXN_GUI_tabs.addTab(self.scan_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_145 = QGridLayout(self.tab_2)
        self.gridLayout_145.setObjectName(u"gridLayout_145")
        self.groupBox_18 = QGroupBox(self.tab_2)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_144 = QGridLayout(self.groupBox_18)
        self.gridLayout_144.setObjectName(u"gridLayout_144")
        self.frame_19 = QFrame(self.groupBox_18)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setStyleSheet(u"")
        self.gridLayout_119 = QGridLayout(self.frame_19)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.cb_det_list_mosaic = QComboBox(self.frame_19)
        self.cb_det_list_mosaic.setObjectName(u"cb_det_list_mosaic")
        sizePolicy.setHeightForWidth(self.cb_det_list_mosaic.sizePolicy().hasHeightForWidth())
        self.cb_det_list_mosaic.setSizePolicy(sizePolicy)

        self.gridLayout_119.addWidget(self.cb_det_list_mosaic, 1, 2, 1, 1)

        self.label_177 = QLabel(self.frame_19)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setAlignment(Qt.AlignCenter)

        self.gridLayout_119.addWidget(self.label_177, 3, 1, 1, 1)

        self.label_179 = QLabel(self.frame_19)
        self.label_179.setObjectName(u"label_179")
        sizePolicy.setHeightForWidth(self.label_179.sizePolicy().hasHeightForWidth())
        self.label_179.setSizePolicy(sizePolicy)
        self.label_179.setFont(font)
        self.label_179.setAlignment(Qt.AlignCenter)

        self.gridLayout_119.addWidget(self.label_179, 1, 1, 1, 1)

        self.sb_yrange_mosaic = QDoubleSpinBox(self.frame_19)
        self.sb_yrange_mosaic.setObjectName(u"sb_yrange_mosaic")
        sizePolicy.setHeightForWidth(self.sb_yrange_mosaic.sizePolicy().hasHeightForWidth())
        self.sb_yrange_mosaic.setSizePolicy(sizePolicy)
        self.sb_yrange_mosaic.setSuffix(u" um")
        self.sb_yrange_mosaic.setDecimals(2)
        self.sb_yrange_mosaic.setMinimum(0.000000000000000)
        self.sb_yrange_mosaic.setMaximum(5000.000000000000000)
        self.sb_yrange_mosaic.setSingleStep(100.000000000000000)
        self.sb_yrange_mosaic.setValue(100.000000000000000)

        self.gridLayout_119.addWidget(self.sb_yrange_mosaic, 3, 2, 1, 1)

        self.sb_xrange_mosaic = QDoubleSpinBox(self.frame_19)
        self.sb_xrange_mosaic.setObjectName(u"sb_xrange_mosaic")
        sizePolicy.setHeightForWidth(self.sb_xrange_mosaic.sizePolicy().hasHeightForWidth())
        self.sb_xrange_mosaic.setSizePolicy(sizePolicy)
        self.sb_xrange_mosaic.setPrefix(u"")
        self.sb_xrange_mosaic.setDecimals(2)
        self.sb_xrange_mosaic.setMinimum(0.000000000000000)
        self.sb_xrange_mosaic.setMaximum(5000.000000000000000)
        self.sb_xrange_mosaic.setSingleStep(100.000000000000000)
        self.sb_xrange_mosaic.setValue(100.000000000000000)

        self.gridLayout_119.addWidget(self.sb_xrange_mosaic, 2, 2, 1, 1)

        self.label_189 = QLabel(self.frame_19)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setAlignment(Qt.AlignCenter)

        self.gridLayout_119.addWidget(self.label_189, 4, 1, 1, 1)

        self.dsb_dwell = QDoubleSpinBox(self.frame_19)
        self.dsb_dwell.setObjectName(u"dsb_dwell")
        sizePolicy.setHeightForWidth(self.dsb_dwell.sizePolicy().hasHeightForWidth())
        self.dsb_dwell.setSizePolicy(sizePolicy)
        self.dsb_dwell.setSuffix(u" sec")
        self.dsb_dwell.setDecimals(4)
        self.dsb_dwell.setMinimum(0.004000000000000)
        self.dsb_dwell.setMaximum(0.500000000000000)
        self.dsb_dwell.setSingleStep(0.005000000000000)
        self.dsb_dwell.setValue(0.005000000000000)

        self.gridLayout_119.addWidget(self.dsb_dwell, 6, 2, 1, 1)

        self.dsb_overlap_mosaic = QDoubleSpinBox(self.frame_19)
        self.dsb_overlap_mosaic.setObjectName(u"dsb_overlap_mosaic")
        self.dsb_overlap_mosaic.setDecimals(1)
        self.dsb_overlap_mosaic.setMaximum(100.000000000000000)

        self.gridLayout_119.addWidget(self.dsb_overlap_mosaic, 4, 2, 1, 1)

        self.sb_stepsize_mosaic = QSpinBox(self.frame_19)
        self.sb_stepsize_mosaic.setObjectName(u"sb_stepsize_mosaic")
        sizePolicy.setHeightForWidth(self.sb_stepsize_mosaic.sizePolicy().hasHeightForWidth())
        self.sb_stepsize_mosaic.setSizePolicy(sizePolicy)
        self.sb_stepsize_mosaic.setMinimum(1)
        self.sb_stepsize_mosaic.setMaximum(10000)
        self.sb_stepsize_mosaic.setSingleStep(10)
        self.sb_stepsize_mosaic.setValue(500)

        self.gridLayout_119.addWidget(self.sb_stepsize_mosaic, 5, 2, 1, 1)

        self.label_190 = QLabel(self.frame_19)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setAlignment(Qt.AlignCenter)

        self.gridLayout_119.addWidget(self.label_190, 2, 1, 1, 1)

        self.label_188 = QLabel(self.frame_19)
        self.label_188.setObjectName(u"label_188")
        sizePolicy.setHeightForWidth(self.label_188.sizePolicy().hasHeightForWidth())
        self.label_188.setSizePolicy(sizePolicy)
        self.label_188.setFont(font)
        self.label_188.setTextFormat(Qt.AutoText)
        self.label_188.setScaledContents(False)
        self.label_188.setAlignment(Qt.AlignCenter)

        self.gridLayout_119.addWidget(self.label_188, 6, 1, 1, 1)

        self.label_191 = QLabel(self.frame_19)
        self.label_191.setObjectName(u"label_191")
        sizePolicy.setHeightForWidth(self.label_191.sizePolicy().hasHeightForWidth())
        self.label_191.setSizePolicy(sizePolicy)
        self.label_191.setFont(font)
        self.label_191.setTextFormat(Qt.AutoText)
        self.label_191.setScaledContents(False)
        self.label_191.setAlignment(Qt.AlignCenter)

        self.gridLayout_119.addWidget(self.label_191, 5, 1, 1, 1)

        self.widget_5 = QWidget(self.frame_19)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.verticalLayout_26 = QVBoxLayout(self.widget_5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.rb_mosaic_mll = QRadioButton(self.widget_5)
        self.rb_mosaic_mll.setObjectName(u"rb_mosaic_mll")
        sizePolicy.setHeightForWidth(self.rb_mosaic_mll.sizePolicy().hasHeightForWidth())
        self.rb_mosaic_mll.setSizePolicy(sizePolicy)
        self.rb_mosaic_mll.setStyleSheet(u"")
        self.rb_mosaic_mll.setChecked(False)
        self.rb_mosaic_mll.setAutoExclusive(True)

        self.verticalLayout_26.addWidget(self.rb_mosaic_mll)

        self.rb_mosaic_zp = QRadioButton(self.widget_5)
        self.rb_mosaic_zp.setObjectName(u"rb_mosaic_zp")
        self.rb_mosaic_zp.setChecked(True)

        self.verticalLayout_26.addWidget(self.rb_mosaic_zp)


        self.gridLayout_119.addWidget(self.widget_5, 1, 0, 6, 1)

        self.le_mosaic_plan_name = QLineEdit(self.frame_19)
        self.le_mosaic_plan_name.setObjectName(u"le_mosaic_plan_name")
        sizePolicy2.setHeightForWidth(self.le_mosaic_plan_name.sizePolicy().hasHeightForWidth())
        self.le_mosaic_plan_name.setSizePolicy(sizePolicy2)

        self.gridLayout_119.addWidget(self.le_mosaic_plan_name, 0, 2, 1, 1)

        self.label_192 = QLabel(self.frame_19)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setAlignment(Qt.AlignCenter)

        self.gridLayout_119.addWidget(self.label_192, 0, 1, 1, 1)


        self.gridLayout_144.addWidget(self.frame_19, 0, 0, 1, 1)

        self.pb_send_mosaic_to_queue = QPushButton(self.groupBox_18)
        self.pb_send_mosaic_to_queue.setObjectName(u"pb_send_mosaic_to_queue")

        self.gridLayout_144.addWidget(self.pb_send_mosaic_to_queue, 1, 0, 1, 1)


        self.gridLayout_145.addWidget(self.groupBox_18, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_145.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_open_mll_tomo_widget = QPushButton(self.groupBox_4)
        self.pb_open_mll_tomo_widget.setObjectName(u"pb_open_mll_tomo_widget")
        sizePolicy4.setHeightForWidth(self.pb_open_mll_tomo_widget.sizePolicy().hasHeightForWidth())
        self.pb_open_mll_tomo_widget.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.pb_open_mll_tomo_widget, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.groupBox_4)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy4.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.pushButton_15, 3, 0, 1, 1)


        self.gridLayout_145.addWidget(self.groupBox_4, 0, 2, 1, 1)

        self.groupBox3 = QGroupBox(self.tab_2)
        self.groupBox3.setObjectName(u"groupBox3")
        self.gridLayout_4 = QGridLayout(self.groupBox3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_5 = QPushButton(self.groupBox3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.pushButton_6, 3, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.groupBox3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy4.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.pushButton_14, 4, 0, 1, 1)


        self.gridLayout_145.addWidget(self.groupBox3, 0, 3, 1, 1)

        self.groupBox_17 = QGroupBox(self.tab_2)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setEnabled(False)
        self.gridLayout_143 = QGridLayout(self.groupBox_17)
        self.gridLayout_143.setObjectName(u"gridLayout_143")
        self.frame_18 = QFrame(self.groupBox_17)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setStyleSheet(u"")
        self.gridLayout_108 = QGridLayout(self.frame_18)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.x_step_end = QDoubleSpinBox(self.frame_18)
        self.x_step_end.setObjectName(u"x_step_end")
        sizePolicy.setHeightForWidth(self.x_step_end.sizePolicy().hasHeightForWidth())
        self.x_step_end.setSizePolicy(sizePolicy)
        self.x_step_end.setSuffix(u"um")
        self.x_step_end.setDecimals(3)
        self.x_step_end.setMinimum(-5000.000000000000000)
        self.x_step_end.setMaximum(5000.000000000000000)
        self.x_step_end.setSingleStep(100.000000000000000)
        self.x_step_end.setValue(100.000000000000000)

        self.gridLayout_108.addWidget(self.x_step_end, 3, 2, 1, 1)

        self.x_step_2 = QSpinBox(self.frame_18)
        self.x_step_2.setObjectName(u"x_step_2")
        sizePolicy.setHeightForWidth(self.x_step_2.sizePolicy().hasHeightForWidth())
        self.x_step_2.setSizePolicy(sizePolicy)
        self.x_step_2.setMinimum(1)
        self.x_step_2.setMaximum(10000)
        self.x_step_2.setSingleStep(10)
        self.x_step_2.setValue(50)

        self.gridLayout_108.addWidget(self.x_step_2, 4, 2, 1, 1)

        self.label_95 = QLabel(self.frame_18)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setAlignment(Qt.AlignCenter)

        self.gridLayout_108.addWidget(self.label_95, 3, 1, 1, 1)

        self.label_92 = QLabel(self.frame_18)
        self.label_92.setObjectName(u"label_92")
        sizePolicy.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy)
        self.label_92.setFont(font)
        self.label_92.setAlignment(Qt.AlignCenter)

        self.gridLayout_108.addWidget(self.label_92, 0, 1, 1, 1)

        self.dwell_2 = QDoubleSpinBox(self.frame_18)
        self.dwell_2.setObjectName(u"dwell_2")
        sizePolicy.setHeightForWidth(self.dwell_2.sizePolicy().hasHeightForWidth())
        self.dwell_2.setSizePolicy(sizePolicy)
        self.dwell_2.setSuffix(u"sec")
        self.dwell_2.setDecimals(4)
        self.dwell_2.setMinimum(0.020000000000000)
        self.dwell_2.setMaximum(100.000000000000000)
        self.dwell_2.setSingleStep(0.100000000000000)
        self.dwell_2.setValue(0.500000000000000)

        self.gridLayout_108.addWidget(self.dwell_2, 5, 2, 1, 1)

        self.label_165 = QLabel(self.frame_18)
        self.label_165.setObjectName(u"label_165")
        sizePolicy.setHeightForWidth(self.label_165.sizePolicy().hasHeightForWidth())
        self.label_165.setSizePolicy(sizePolicy)
        self.label_165.setFont(font)
        self.label_165.setTextFormat(Qt.AutoText)
        self.label_165.setScaledContents(False)
        self.label_165.setAlignment(Qt.AlignCenter)

        self.gridLayout_108.addWidget(self.label_165, 5, 1, 1, 1)

        self.widget_3 = QWidget(self.frame_18)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.rb_step_1d = QRadioButton(self.widget_3)
        self.rb_step_1d.setObjectName(u"rb_step_1d")
        sizePolicy.setHeightForWidth(self.rb_step_1d.sizePolicy().hasHeightForWidth())
        self.rb_step_1d.setSizePolicy(sizePolicy)
        self.rb_step_1d.setStyleSheet(u"")
        self.rb_step_1d.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.rb_step_1d)

        self.rb_step_2d = QRadioButton(self.widget_3)
        self.rb_step_2d.setObjectName(u"rb_step_2d")
        sizePolicy.setHeightForWidth(self.rb_step_2d.sizePolicy().hasHeightForWidth())
        self.rb_step_2d.setSizePolicy(sizePolicy)
        self.rb_step_2d.setStyleSheet(u"")
        self.rb_step_2d.setChecked(True)
        self.rb_step_2d.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.rb_step_2d)


        self.gridLayout_108.addWidget(self.widget_3, 0, 0, 6, 1)

        self.y_step_end = QDoubleSpinBox(self.frame_18)
        self.y_step_end.setObjectName(u"y_step_end")
        sizePolicy.setHeightForWidth(self.y_step_end.sizePolicy().hasHeightForWidth())
        self.y_step_end.setSizePolicy(sizePolicy)
        self.y_step_end.setSuffix(u"um")
        self.y_step_end.setDecimals(3)
        self.y_step_end.setMinimum(-5000.000000000000000)
        self.y_step_end.setMaximum(5000.000000000000000)
        self.y_step_end.setSingleStep(100.000000000000000)
        self.y_step_end.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.y_step_end.setValue(100.000000000000000)

        self.gridLayout_108.addWidget(self.y_step_end, 3, 3, 1, 1)

        self.label_93 = QLabel(self.frame_18)
        self.label_93.setObjectName(u"label_93")
        sizePolicy.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy)
        self.label_93.setFont(font)
        self.label_93.setAlignment(Qt.AlignCenter)

        self.gridLayout_108.addWidget(self.label_93, 1, 1, 1, 1)

        self.cb_step_dets = QComboBox(self.frame_18)
        self.cb_step_dets.setObjectName(u"cb_step_dets")
        sizePolicy.setHeightForWidth(self.cb_step_dets.sizePolicy().hasHeightForWidth())
        self.cb_step_dets.setSizePolicy(sizePolicy)

        self.gridLayout_108.addWidget(self.cb_step_dets, 0, 2, 1, 1)

        self.y_step_start = QDoubleSpinBox(self.frame_18)
        self.y_step_start.setObjectName(u"y_step_start")
        self.y_step_start.setEnabled(False)
        sizePolicy.setHeightForWidth(self.y_step_start.sizePolicy().hasHeightForWidth())
        self.y_step_start.setSizePolicy(sizePolicy)
        self.y_step_start.setPrefix(u"")
        self.y_step_start.setDecimals(3)
        self.y_step_start.setMinimum(-5000.000000000000000)
        self.y_step_start.setMaximum(500.000000000000000)
        self.y_step_start.setSingleStep(100.000000000000000)
        self.y_step_start.setValue(-100.000000000000000)

        self.gridLayout_108.addWidget(self.y_step_start, 2, 3, 1, 1)

        self.y_step_2 = QSpinBox(self.frame_18)
        self.y_step_2.setObjectName(u"y_step_2")
        sizePolicy.setHeightForWidth(self.y_step_2.sizePolicy().hasHeightForWidth())
        self.y_step_2.setSizePolicy(sizePolicy)
        self.y_step_2.setMinimum(1)
        self.y_step_2.setMaximum(10000)
        self.y_step_2.setSingleStep(10)
        self.y_step_2.setValue(50)

        self.gridLayout_108.addWidget(self.y_step_2, 4, 3, 1, 1)

        self.cb_step_motor1 = QComboBox(self.frame_18)
        self.cb_step_motor1.setObjectName(u"cb_step_motor1")
        sizePolicy.setHeightForWidth(self.cb_step_motor1.sizePolicy().hasHeightForWidth())
        self.cb_step_motor1.setSizePolicy(sizePolicy)

        self.gridLayout_108.addWidget(self.cb_step_motor1, 1, 2, 1, 1)

        self.label_94 = QLabel(self.frame_18)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.gridLayout_108.addWidget(self.label_94, 2, 1, 1, 1)

        self.label_96 = QLabel(self.frame_18)
        self.label_96.setObjectName(u"label_96")
        sizePolicy.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy)
        self.label_96.setFont(font)
        self.label_96.setTextFormat(Qt.AutoText)
        self.label_96.setScaledContents(False)
        self.label_96.setAlignment(Qt.AlignCenter)

        self.gridLayout_108.addWidget(self.label_96, 4, 1, 1, 1)

        self.cb_step_motor2 = QComboBox(self.frame_18)
        self.cb_step_motor2.setObjectName(u"cb_step_motor2")
        sizePolicy.setHeightForWidth(self.cb_step_motor2.sizePolicy().hasHeightForWidth())
        self.cb_step_motor2.setSizePolicy(sizePolicy)

        self.gridLayout_108.addWidget(self.cb_step_motor2, 1, 3, 1, 1)

        self.x_step_start = QDoubleSpinBox(self.frame_18)
        self.x_step_start.setObjectName(u"x_step_start")
        sizePolicy.setHeightForWidth(self.x_step_start.sizePolicy().hasHeightForWidth())
        self.x_step_start.setSizePolicy(sizePolicy)
        self.x_step_start.setPrefix(u"")
        self.x_step_start.setDecimals(3)
        self.x_step_start.setMinimum(-5000.000000000000000)
        self.x_step_start.setMaximum(5000.000000000000000)
        self.x_step_start.setSingleStep(100.000000000000000)
        self.x_step_start.setValue(-100.000000000000000)

        self.gridLayout_108.addWidget(self.x_step_start, 2, 2, 1, 1)


        self.gridLayout_143.addWidget(self.frame_18, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_17)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_143.addWidget(self.pushButton_4, 1, 0, 1, 1)


        self.gridLayout_145.addWidget(self.groupBox_17, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 874, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_145.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.HXN_GUI_tabs.addTab(self.tab_2, "")
        self.sample_exchange_tab = QWidget()
        self.sample_exchange_tab.setObjectName(u"sample_exchange_tab")
        self.gridLayout_87 = QGridLayout(self.sample_exchange_tab)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.gridLayout_82 = QGridLayout()
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.pb_start_pressure_live_plot = QPushButton(self.sample_exchange_tab)
        self.pb_start_pressure_live_plot.setObjectName(u"pb_start_pressure_live_plot")
        sizePolicy2.setHeightForWidth(self.pb_start_pressure_live_plot.sizePolicy().hasHeightForWidth())
        self.pb_start_pressure_live_plot.setSizePolicy(sizePolicy2)

        self.gridLayout_82.addWidget(self.pb_start_pressure_live_plot, 1, 0, 1, 1)

        self.pressure_plot_canvas = GraphicsLayoutWidget(self.sample_exchange_tab)
        self.pressure_plot_canvas.setObjectName(u"pressure_plot_canvas")
        sizePolicy6.setHeightForWidth(self.pressure_plot_canvas.sizePolicy().hasHeightForWidth())
        self.pressure_plot_canvas.setSizePolicy(sizePolicy6)

        self.gridLayout_82.addWidget(self.pressure_plot_canvas, 0, 0, 1, 2)

        self.pb_stop_pressure_live_plot = QPushButton(self.sample_exchange_tab)
        self.pb_stop_pressure_live_plot.setObjectName(u"pb_stop_pressure_live_plot")
        sizePolicy2.setHeightForWidth(self.pb_stop_pressure_live_plot.sizePolicy().hasHeightForWidth())
        self.pb_stop_pressure_live_plot.setSizePolicy(sizePolicy2)

        self.gridLayout_82.addWidget(self.pb_stop_pressure_live_plot, 1, 1, 1, 1)


        self.gridLayout_87.addLayout(self.gridLayout_82, 2, 0, 1, 1)

        self.gridLayout_84 = QGridLayout()
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.textEdit = QTextEdit(self.sample_exchange_tab)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy7)
        self.textEdit.setReadOnly(True)

        self.gridLayout_84.addWidget(self.textEdit, 0, 1, 2, 1)

        self.gridLayout_104 = QGridLayout()
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.gridLayout_104.setContentsMargins(20, -1, 20, 25)
        self.sample_ex_tabs = QTabWidget(self.sample_exchange_tab)
        self.sample_ex_tabs.setObjectName(u"sample_ex_tabs")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_105 = QGridLayout(self.tab_6)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.groupBox_22 = QGroupBox(self.tab_6)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_88 = QGridLayout(self.groupBox_22)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gridLayout_68 = QGridLayout()
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.label_71 = QLabel(self.groupBox_22)
        self.label_71.setObjectName(u"label_71")
        sizePolicy1.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy1)
        self.label_71.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_68.addWidget(self.label_71, 0, 0, 1, 1)

        self.dsb_target_p = QDoubleSpinBox(self.groupBox_22)
        self.dsb_target_p.setObjectName(u"dsb_target_p")
        sizePolicy2.setHeightForWidth(self.dsb_target_p.sizePolicy().hasHeightForWidth())
        self.dsb_target_p.setSizePolicy(sizePolicy2)
        self.dsb_target_p.setMinimum(0.100000000000000)
        self.dsb_target_p.setMaximum(765.000000000000000)
        self.dsb_target_p.setSingleStep(0.100000000000000)
        self.dsb_target_p.setValue(1.300000000000000)

        self.gridLayout_68.addWidget(self.dsb_target_p, 0, 1, 1, 1)


        self.gridLayout_88.addLayout(self.gridLayout_68, 1, 0, 1, 1)

        self.cb_sample_ex_cam11_in = QCheckBox(self.groupBox_22)
        self.cb_sample_ex_cam11_in.setObjectName(u"cb_sample_ex_cam11_in")
        self.cb_sample_ex_cam11_in.setChecked(True)

        self.gridLayout_88.addWidget(self.cb_sample_ex_cam11_in, 3, 0, 1, 1)

        self.pb_start_pump = QPushButton(self.groupBox_22)
        self.pb_start_pump.setObjectName(u"pb_start_pump")
        self.pb_start_pump.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_start_pump.sizePolicy().hasHeightForWidth())
        self.pb_start_pump.setSizePolicy(sizePolicy)
        self.pb_start_pump.setStyleSheet(u"")

        self.gridLayout_88.addWidget(self.pb_start_pump, 0, 0, 1, 1)

        self.cb_he_backfill_bool = QCheckBox(self.groupBox_22)
        self.cb_he_backfill_bool.setObjectName(u"cb_he_backfill_bool")
        self.cb_he_backfill_bool.setChecked(True)

        self.gridLayout_88.addWidget(self.cb_he_backfill_bool, 2, 0, 1, 1)


        self.gridLayout_105.addWidget(self.groupBox_22, 0, 0, 2, 2)

        self.groupBox_29 = QGroupBox(self.tab_6)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.gridLayout_103 = QGridLayout(self.groupBox_29)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.pb_start_vent = QPushButton(self.groupBox_29)
        self.pb_start_vent.setObjectName(u"pb_start_vent")
        self.pb_start_vent.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_start_vent.sizePolicy().hasHeightForWidth())
        self.pb_start_vent.setSizePolicy(sizePolicy)
        self.pb_start_vent.setStyleSheet(u"")

        self.gridLayout_103.addWidget(self.pb_start_vent, 0, 0, 1, 1)

        self.cb_sample_ex_det_out = QCheckBox(self.groupBox_29)
        self.cb_sample_ex_det_out.setObjectName(u"cb_sample_ex_det_out")
        self.cb_sample_ex_det_out.setChecked(True)

        self.gridLayout_103.addWidget(self.cb_sample_ex_det_out, 2, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_103.addItem(self.verticalSpacer_16, 1, 0, 1, 1)


        self.gridLayout_105.addWidget(self.groupBox_29, 0, 2, 2, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_105.addItem(self.verticalSpacer_8, 2, 2, 1, 1)

        self.sample_ex_tabs.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_39 = QGridLayout(self.tab_7)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.pb_open_fast_pumps = QPushButton(self.tab_7)
        self.pb_open_fast_pumps.setObjectName(u"pb_open_fast_pumps")
        sizePolicy4.setHeightForWidth(self.pb_open_fast_pumps.sizePolicy().hasHeightForWidth())
        self.pb_open_fast_pumps.setSizePolicy(sizePolicy4)

        self.gridLayout_39.addWidget(self.pb_open_fast_pumps, 1, 0, 1, 1)

        self.pb_stop_vent = QPushButton(self.tab_7)
        self.pb_stop_vent.setObjectName(u"pb_stop_vent")
        sizePolicy.setHeightForWidth(self.pb_stop_vent.sizePolicy().hasHeightForWidth())
        self.pb_stop_vent.setSizePolicy(sizePolicy)

        self.gridLayout_39.addWidget(self.pb_stop_vent, 1, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_39.addItem(self.verticalSpacer_10, 3, 0, 1, 1)

        self.pb_auto_he_fill = QPushButton(self.tab_7)
        self.pb_auto_he_fill.setObjectName(u"pb_auto_he_fill")
        self.pb_auto_he_fill.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_auto_he_fill.sizePolicy().hasHeightForWidth())
        self.pb_auto_he_fill.setSizePolicy(sizePolicy)
        self.pb_auto_he_fill.setStyleSheet(u"")

        self.gridLayout_39.addWidget(self.pb_auto_he_fill, 0, 1, 1, 1)

        self.pb_stop_pump = QPushButton(self.tab_7)
        self.pb_stop_pump.setObjectName(u"pb_stop_pump")
        sizePolicy.setHeightForWidth(self.pb_stop_pump.sizePolicy().hasHeightForWidth())
        self.pb_stop_pump.setSizePolicy(sizePolicy)

        self.gridLayout_39.addWidget(self.pb_stop_pump, 0, 0, 1, 1)

        self.pb_open_he_valve = QPushButton(self.tab_7)
        self.pb_open_he_valve.setObjectName(u"pb_open_he_valve")

        self.gridLayout_39.addWidget(self.pb_open_he_valve, 2, 0, 1, 1)

        self.pb_close_he_valve = QPushButton(self.tab_7)
        self.pb_close_he_valve.setObjectName(u"pb_close_he_valve")

        self.gridLayout_39.addWidget(self.pb_close_he_valve, 2, 1, 1, 1)

        self.sample_ex_tabs.addTab(self.tab_7, "")

        self.gridLayout_104.addWidget(self.sample_ex_tabs, 1, 2, 1, 1)

        self.groupBox_27 = QGroupBox(self.sample_exchange_tab)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setEnabled(True)
        self.gridLayout_101 = QGridLayout(self.groupBox_27)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.gridLayout_101.setContentsMargins(25, -1, 25, -1)
        self.label_44 = QLabel(self.groupBox_27)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_101.addWidget(self.label_44, 0, 2, 2, 1)

        self.groupBox_28 = QGroupBox(self.groupBox_27)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.gridLayout_89 = QGridLayout(self.groupBox_28)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.rb_he_backfill_fail = QRadioButton(self.groupBox_28)
        self.rb_he_backfill_fail.setObjectName(u"rb_he_backfill_fail")
        self.rb_he_backfill_fail.setEnabled(False)
        sizePolicy.setHeightForWidth(self.rb_he_backfill_fail.sizePolicy().hasHeightForWidth())
        self.rb_he_backfill_fail.setSizePolicy(sizePolicy)
        self.rb_he_backfill_fail.setLayoutDirection(Qt.RightToLeft)
        self.rb_he_backfill_fail.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"\n"
"indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(255, 255, 0);\n"
"}")
        self.rb_he_backfill_fail.setAutoExclusive(False)

        self.gridLayout_89.addWidget(self.rb_he_backfill_fail, 3, 0, 1, 1)

        self.rb_fast_vent = QRadioButton(self.groupBox_28)
        self.rb_fast_vent.setObjectName(u"rb_fast_vent")
        self.rb_fast_vent.setEnabled(False)
        sizePolicy.setHeightForWidth(self.rb_fast_vent.sizePolicy().hasHeightForWidth())
        self.rb_fast_vent.setSizePolicy(sizePolicy)
        self.rb_fast_vent.setLayoutDirection(Qt.RightToLeft)
        self.rb_fast_vent.setStyleSheet(u"color: rgb(245, 121, 0);")
        self.rb_fast_vent.setCheckable(True)
        self.rb_fast_vent.setAutoExclusive(False)

        self.gridLayout_89.addWidget(self.rb_fast_vent, 1, 0, 1, 1)

        self.label_145 = QLabel(self.groupBox_28)
        self.label_145.setObjectName(u"label_145")
        sizePolicy5.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy5)

        self.gridLayout_89.addWidget(self.label_145, 0, 0, 1, 1)


        self.gridLayout_101.addWidget(self.groupBox_28, 3, 0, 1, 1)

        self.groupBox_30 = QGroupBox(self.groupBox_27)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.gridLayout_102 = QGridLayout(self.groupBox_30)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.label_147 = QLabel(self.groupBox_30)
        self.label_147.setObjectName(u"label_147")
        sizePolicy5.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy5)

        self.gridLayout_102.addWidget(self.label_147, 1, 0, 1, 1)

        self.rb_pumpB_slow = QRadioButton(self.groupBox_30)
        self.rb_pumpB_slow.setObjectName(u"rb_pumpB_slow")
        self.rb_pumpB_slow.setEnabled(False)
        sizePolicy.setHeightForWidth(self.rb_pumpB_slow.sizePolicy().hasHeightForWidth())
        self.rb_pumpB_slow.setSizePolicy(sizePolicy)
        self.rb_pumpB_slow.setLayoutDirection(Qt.RightToLeft)
        self.rb_pumpB_slow.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"font: 18pt \"Cantarell\";")
        self.rb_pumpB_slow.setAutoExclusive(False)

        self.gridLayout_102.addWidget(self.rb_pumpB_slow, 6, 1, 1, 1)

        self.rb_pumpA_slow = QRadioButton(self.groupBox_30)
        self.rb_pumpA_slow.setObjectName(u"rb_pumpA_slow")
        self.rb_pumpA_slow.setEnabled(False)
        sizePolicy.setHeightForWidth(self.rb_pumpA_slow.sizePolicy().hasHeightForWidth())
        self.rb_pumpA_slow.setSizePolicy(sizePolicy)
        self.rb_pumpA_slow.setLayoutDirection(Qt.RightToLeft)
        self.rb_pumpA_slow.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"font: 18pt \"Cantarell\";")
        self.rb_pumpA_slow.setAutoExclusive(False)

        self.gridLayout_102.addWidget(self.rb_pumpA_slow, 6, 0, 1, 1)


        self.gridLayout_101.addWidget(self.groupBox_30, 3, 2, 2, 1)

        self.label_144 = QLabel(self.groupBox_27)
        self.label_144.setObjectName(u"label_144")
        sizePolicy5.setHeightForWidth(self.label_144.sizePolicy().hasHeightForWidth())
        self.label_144.setSizePolicy(sizePolicy5)

        self.gridLayout_101.addWidget(self.label_144, 1, 0, 1, 1)


        self.gridLayout_104.addWidget(self.groupBox_27, 2, 2, 1, 1)


        self.gridLayout_84.addLayout(self.gridLayout_104, 1, 0, 1, 1)


        self.gridLayout_87.addLayout(self.gridLayout_84, 0, 0, 1, 1)

        self.gridLayout_95 = QGridLayout()
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.gridLayout_95.setContentsMargins(-1, 25, -1, 25)
        self.gridLayout_72 = QGridLayout()
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setContentsMargins(12, -1, 12, -1)
        self.lb_sample_change_action = QLabel(self.sample_exchange_tab)
        self.lb_sample_change_action.setObjectName(u"lb_sample_change_action")
        sizePolicy.setHeightForWidth(self.lb_sample_change_action.sizePolicy().hasHeightForWidth())
        self.lb_sample_change_action.setSizePolicy(sizePolicy)
        self.lb_sample_change_action.setLayoutDirection(Qt.RightToLeft)
        self.lb_sample_change_action.setStyleSheet(u"font: 75 20pt \"C059\";\n"
"color:rgb(51, 184, 141)")
        self.lb_sample_change_action.setAlignment(Qt.AlignCenter)

        self.gridLayout_72.addWidget(self.lb_sample_change_action, 0, 0, 1, 1)

        self.gridLayout_47 = QGridLayout()
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.label_119 = QLabel(self.sample_exchange_tab)
        self.label_119.setObjectName(u"label_119")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_119.sizePolicy().hasHeightForWidth())
        self.label_119.setSizePolicy(sizePolicy8)
        self.label_119.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.label_119, 0, 0, 1, 1)

        self.lcdPressure = QDoubleSpinBox(self.sample_exchange_tab)
        self.lcdPressure.setObjectName(u"lcdPressure")
        sizePolicy.setHeightForWidth(self.lcdPressure.sizePolicy().hasHeightForWidth())
        self.lcdPressure.setSizePolicy(sizePolicy)
        self.lcdPressure.setStyleSheet(u"font: 75 35pt \"C059\";")
        self.lcdPressure.setReadOnly(True)
        self.lcdPressure.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lcdPressure.setDecimals(1)
        self.lcdPressure.setMinimum(0.000000000000000)
        self.lcdPressure.setMaximum(800.000000000000000)
        self.lcdPressure.setValue(12.000000000000000)

        self.gridLayout_47.addWidget(self.lcdPressure, 0, 1, 1, 1)


        self.gridLayout_72.addLayout(self.gridLayout_47, 0, 1, 1, 1)


        self.gridLayout_95.addLayout(self.gridLayout_72, 0, 0, 1, 1)

        self.prb_sample_exchange = QProgressBar(self.sample_exchange_tab)
        self.prb_sample_exchange.setObjectName(u"prb_sample_exchange")
        self.prb_sample_exchange.setAutoFillBackground(False)
        self.prb_sample_exchange.setValue(50)
        self.prb_sample_exchange.setTextVisible(True)
        self.prb_sample_exchange.setInvertedAppearance(False)

        self.gridLayout_95.addWidget(self.prb_sample_exchange, 1, 0, 1, 1)


        self.gridLayout_87.addLayout(self.gridLayout_95, 1, 0, 1, 1)

        self.HXN_GUI_tabs.addTab(self.sample_exchange_tab, "")
        self.alignment_tab = QWidget()
        self.alignment_tab.setObjectName(u"alignment_tab")
        self.label_141 = QLabel(self.alignment_tab)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(9, 295, 16, 20))
        self.label_143 = QLabel(self.alignment_tab)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(9, 577, 16, 20))
        self.gridLayout_115 = QGridLayout(self.alignment_tab)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.tabWidget_3 = QTabWidget(self.alignment_tab)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setEnabled(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_13 = QGridLayout(self.tab_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_21 = QGroupBox(self.tab_5)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy2.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy2)
        self.gridLayout_83 = QGridLayout(self.groupBox_21)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.pb_zpbsy_out = QPushButton(self.groupBox_21)
        self.pb_zpbsy_out.setObjectName(u"pb_zpbsy_out")

        self.gridLayout_83.addWidget(self.pb_zpbsy_out, 2, 0, 1, 1)

        self.pb_osa_in = QPushButton(self.groupBox_21)
        self.pb_osa_in.setObjectName(u"pb_osa_in")
        sizePolicy4.setHeightForWidth(self.pb_osa_in.sizePolicy().hasHeightForWidth())
        self.pb_osa_in.setSizePolicy(sizePolicy4)

        self.gridLayout_83.addWidget(self.pb_osa_in, 1, 1, 1, 1)

        self.pb_osa_out = QPushButton(self.groupBox_21)
        self.pb_osa_out.setObjectName(u"pb_osa_out")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pb_osa_out.sizePolicy().hasHeightForWidth())
        self.pb_osa_out.setSizePolicy(sizePolicy9)

        self.gridLayout_83.addWidget(self.pb_osa_out, 1, 0, 1, 1)

        self.pb_zpbsy_in = QPushButton(self.groupBox_21)
        self.pb_zpbsy_in.setObjectName(u"pb_zpbsy_in")

        self.gridLayout_83.addWidget(self.pb_zpbsy_in, 2, 1, 1, 1)

        self.pb_zp_cam11_view = QPushButton(self.groupBox_21)
        self.pb_zp_cam11_view.setObjectName(u"pb_zp_cam11_view")

        self.gridLayout_83.addWidget(self.pb_zp_cam11_view, 0, 0, 1, 1)

        self.pb_zp_nanobeam = QPushButton(self.groupBox_21)
        self.pb_zp_nanobeam.setObjectName(u"pb_zp_nanobeam")

        self.gridLayout_83.addWidget(self.pb_zp_nanobeam, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_21, 0, 0, 1, 1)

        self.groupBox_24 = QGroupBox(self.tab_5)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.gridLayout_73 = QGridLayout(self.groupBox_24)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.label_135 = QLabel(self.groupBox_24)
        self.label_135.setObjectName(u"label_135")
        sizePolicy2.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy2)

        self.gridLayout_73.addWidget(self.label_135, 0, 0, 1, 1)

        self.gridLayout_79 = QGridLayout()
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.gridLayout_46 = QGridLayout()
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.widget_4 = QWidget(self.groupBox_24)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_61 = QGridLayout(self.widget_4)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_76 = QLabel(self.widget_4)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_76)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_100 = QLabel(self.widget_4)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_63.addWidget(self.label_100)

        self.sb_ZPZ1RelativeStart = QSpinBox(self.widget_4)
        self.sb_ZPZ1RelativeStart.setObjectName(u"sb_ZPZ1RelativeStart")
        sizePolicy2.setHeightForWidth(self.sb_ZPZ1RelativeStart.sizePolicy().hasHeightForWidth())
        self.sb_ZPZ1RelativeStart.setSizePolicy(sizePolicy2)
        self.sb_ZPZ1RelativeStart.setMinimum(-1000)
        self.sb_ZPZ1RelativeStart.setMaximum(1000)
        self.sb_ZPZ1RelativeStart.setSingleStep(10)
        self.sb_ZPZ1RelativeStart.setValue(-50)

        self.horizontalLayout_63.addWidget(self.sb_ZPZ1RelativeStart)


        self.verticalLayout_31.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_102 = QLabel(self.widget_4)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_65.addWidget(self.label_102)

        self.sb_ZPZ1RelativeEnd = QSpinBox(self.widget_4)
        self.sb_ZPZ1RelativeEnd.setObjectName(u"sb_ZPZ1RelativeEnd")
        sizePolicy2.setHeightForWidth(self.sb_ZPZ1RelativeEnd.sizePolicy().hasHeightForWidth())
        self.sb_ZPZ1RelativeEnd.setSizePolicy(sizePolicy2)
        self.sb_ZPZ1RelativeEnd.setMinimum(-1000)
        self.sb_ZPZ1RelativeEnd.setMaximum(1000)
        self.sb_ZPZ1RelativeEnd.setSingleStep(10)
        self.sb_ZPZ1RelativeEnd.setValue(50)

        self.horizontalLayout_65.addWidget(self.sb_ZPZ1RelativeEnd)


        self.verticalLayout_31.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_106 = QLabel(self.widget_4)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_69.addWidget(self.label_106)

        self.sb_ZPZ1Steps = QSpinBox(self.widget_4)
        self.sb_ZPZ1Steps.setObjectName(u"sb_ZPZ1Steps")
        sizePolicy2.setHeightForWidth(self.sb_ZPZ1Steps.sizePolicy().hasHeightForWidth())
        self.sb_ZPZ1Steps.setSizePolicy(sizePolicy2)
        self.sb_ZPZ1Steps.setMinimum(1)
        self.sb_ZPZ1Steps.setMaximum(1000)
        self.sb_ZPZ1Steps.setSingleStep(5)
        self.sb_ZPZ1Steps.setValue(10)

        self.horizontalLayout_69.addWidget(self.sb_ZPZ1Steps)


        self.verticalLayout_31.addLayout(self.horizontalLayout_69)


        self.gridLayout_61.addLayout(self.verticalLayout_31, 0, 0, 1, 2)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_77 = QLabel(self.widget_4)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_77)

        self.cb_foucsScanMotor = QComboBox(self.widget_4)
        self.cb_foucsScanMotor.addItem("")
        self.cb_foucsScanMotor.addItem("")
        self.cb_foucsScanMotor.addItem("")
        self.cb_foucsScanMotor.setObjectName(u"cb_foucsScanMotor")

        self.verticalLayout_39.addWidget(self.cb_foucsScanMotor)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_99 = QLabel(self.widget_4)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_62.addWidget(self.label_99)

        self.sb_FocusScanMtrStart = QDoubleSpinBox(self.widget_4)
        self.sb_FocusScanMtrStart.setObjectName(u"sb_FocusScanMtrStart")
        sizePolicy2.setHeightForWidth(self.sb_FocusScanMtrStart.sizePolicy().hasHeightForWidth())
        self.sb_FocusScanMtrStart.setSizePolicy(sizePolicy2)
        self.sb_FocusScanMtrStart.setMinimum(-15.000000000000000)
        self.sb_FocusScanMtrStart.setMaximum(15.000000000000000)
        self.sb_FocusScanMtrStart.setValue(-1.000000000000000)

        self.horizontalLayout_62.addWidget(self.sb_FocusScanMtrStart)


        self.verticalLayout_39.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_101 = QLabel(self.widget_4)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_64.addWidget(self.label_101)

        self.sb_FocusScanMtrEnd = QDoubleSpinBox(self.widget_4)
        self.sb_FocusScanMtrEnd.setObjectName(u"sb_FocusScanMtrEnd")
        sizePolicy2.setHeightForWidth(self.sb_FocusScanMtrEnd.sizePolicy().hasHeightForWidth())
        self.sb_FocusScanMtrEnd.setSizePolicy(sizePolicy2)
        self.sb_FocusScanMtrEnd.setMinimum(-15.000000000000000)
        self.sb_FocusScanMtrEnd.setMaximum(15.000000000000000)
        self.sb_FocusScanMtrEnd.setValue(1.000000000000000)

        self.horizontalLayout_64.addWidget(self.sb_FocusScanMtrEnd)


        self.verticalLayout_39.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_105 = QLabel(self.widget_4)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_68.addWidget(self.label_105)

        self.sb_FocusScanMtrStep = QSpinBox(self.widget_4)
        self.sb_FocusScanMtrStep.setObjectName(u"sb_FocusScanMtrStep")
        sizePolicy2.setHeightForWidth(self.sb_FocusScanMtrStep.sizePolicy().hasHeightForWidth())
        self.sb_FocusScanMtrStep.setSizePolicy(sizePolicy2)
        self.sb_FocusScanMtrStep.setMinimum(10)
        self.sb_FocusScanMtrStep.setMaximum(1000)
        self.sb_FocusScanMtrStep.setSingleStep(50)
        self.sb_FocusScanMtrStep.setValue(100)

        self.horizontalLayout_68.addWidget(self.sb_FocusScanMtrStep)


        self.verticalLayout_39.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_118 = QLabel(self.widget_4)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_118)

        self.dsb_FocusScanDwell = QDoubleSpinBox(self.widget_4)
        self.dsb_FocusScanDwell.setObjectName(u"dsb_FocusScanDwell")
        sizePolicy2.setHeightForWidth(self.dsb_FocusScanDwell.sizePolicy().hasHeightForWidth())
        self.dsb_FocusScanDwell.setSizePolicy(sizePolicy2)
        self.dsb_FocusScanDwell.setDecimals(3)
        self.dsb_FocusScanDwell.setMinimum(0.005000000000000)
        self.dsb_FocusScanDwell.setMaximum(0.500000000000000)
        self.dsb_FocusScanDwell.setSingleStep(0.010000000000000)
        self.dsb_FocusScanDwell.setValue(0.050000000000000)

        self.horizontalLayout_11.addWidget(self.dsb_FocusScanDwell)


        self.verticalLayout_39.addLayout(self.horizontalLayout_11)


        self.gridLayout_61.addLayout(self.verticalLayout_39, 0, 2, 2, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_56 = QLabel(self.widget_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_56, 1, 1, 1, 1)

        self.dsb_ZPZ1TargetPos = QDoubleSpinBox(self.widget_4)
        self.dsb_ZPZ1TargetPos.setObjectName(u"dsb_ZPZ1TargetPos")
        sizePolicy2.setHeightForWidth(self.dsb_ZPZ1TargetPos.sizePolicy().hasHeightForWidth())
        self.dsb_ZPZ1TargetPos.setSizePolicy(sizePolicy2)
        self.dsb_ZPZ1TargetPos.setDecimals(4)
        self.dsb_ZPZ1TargetPos.setMinimum(-100.000000000000000)
        self.dsb_ZPZ1TargetPos.setMaximum(20.000000000000000)
        self.dsb_ZPZ1TargetPos.setValue(-15.000000000000000)

        self.gridLayout_25.addWidget(self.dsb_ZPZ1TargetPos, 1, 2, 1, 1)


        self.gridLayout_61.addLayout(self.gridLayout_25, 3, 0, 1, 2)

        self.gridLayout_67 = QGridLayout()
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.label_97 = QLabel(self.widget_4)
        self.label_97.setObjectName(u"label_97")
        sizePolicy2.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy2)
        self.label_97.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_67.addWidget(self.label_97, 0, 0, 1, 1)

        self.gridLayout_60 = QGridLayout()
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.cb_linearFlag_zpFocus = QCheckBox(self.widget_4)
        self.cb_linearFlag_zpFocus.setObjectName(u"cb_linearFlag_zpFocus")

        self.gridLayout_60.addWidget(self.cb_linearFlag_zpFocus, 1, 0, 1, 1)

        self.cb_zp_focus_elem = QComboBox(self.widget_4)
        self.cb_zp_focus_elem.setObjectName(u"cb_zp_focus_elem")

        self.gridLayout_60.addWidget(self.cb_zp_focus_elem, 0, 0, 1, 1)


        self.gridLayout_67.addLayout(self.gridLayout_60, 0, 1, 1, 1)


        self.gridLayout_61.addLayout(self.gridLayout_67, 1, 0, 1, 2)

        self.pb_MoveZPZ1AbsPos = QPushButton(self.widget_4)
        self.pb_MoveZPZ1AbsPos.setObjectName(u"pb_MoveZPZ1AbsPos")
        sizePolicy9.setHeightForWidth(self.pb_MoveZPZ1AbsPos.sizePolicy().hasHeightForWidth())
        self.pb_MoveZPZ1AbsPos.setSizePolicy(sizePolicy9)

        self.gridLayout_61.addWidget(self.pb_MoveZPZ1AbsPos, 3, 2, 1, 1)

        self.pb_ZPZFocusScanStart = QPushButton(self.widget_4)
        self.pb_ZPZFocusScanStart.setObjectName(u"pb_ZPZFocusScanStart")
        sizePolicy2.setHeightForWidth(self.pb_ZPZFocusScanStart.sizePolicy().hasHeightForWidth())
        self.pb_ZPZFocusScanStart.setSizePolicy(sizePolicy2)

        self.gridLayout_61.addWidget(self.pb_ZPZFocusScanStart, 2, 1, 1, 1)


        self.gridLayout_46.addWidget(self.widget_4, 0, 0, 1, 1)


        self.gridLayout_79.addLayout(self.gridLayout_46, 2, 0, 1, 1)


        self.gridLayout_73.addLayout(self.gridLayout_79, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_24, 1, 0, 1, 1)

        self.groupBox_34 = QGroupBox(self.tab_5)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.gridLayout_66 = QGridLayout(self.groupBox_34)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.label_156 = QLabel(self.groupBox_34)
        self.label_156.setObjectName(u"label_156")
        sizePolicy2.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy2)

        self.gridLayout_66.addWidget(self.label_156, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.groupBox_34)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_63 = QGridLayout(self.widget_7)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_64 = QGridLayout()
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_108 = QLabel(self.widget_7)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_72.addWidget(self.label_108)

        self.sb_zp_rot_scan_start = QSpinBox(self.widget_7)
        self.sb_zp_rot_scan_start.setObjectName(u"sb_zp_rot_scan_start")
        sizePolicy2.setHeightForWidth(self.sb_zp_rot_scan_start.sizePolicy().hasHeightForWidth())
        self.sb_zp_rot_scan_start.setSizePolicy(sizePolicy2)
        self.sb_zp_rot_scan_start.setMinimum(-15)
        self.sb_zp_rot_scan_start.setMaximum(15)
        self.sb_zp_rot_scan_start.setSingleStep(2)
        self.sb_zp_rot_scan_start.setValue(-12)

        self.horizontalLayout_72.addWidget(self.sb_zp_rot_scan_start)


        self.verticalLayout_43.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_109 = QLabel(self.widget_7)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_73.addWidget(self.label_109)

        self.sb_zp_rot_scan_end = QSpinBox(self.widget_7)
        self.sb_zp_rot_scan_end.setObjectName(u"sb_zp_rot_scan_end")
        sizePolicy2.setHeightForWidth(self.sb_zp_rot_scan_end.sizePolicy().hasHeightForWidth())
        self.sb_zp_rot_scan_end.setSizePolicy(sizePolicy2)
        self.sb_zp_rot_scan_end.setMinimum(-15)
        self.sb_zp_rot_scan_end.setMaximum(15)
        self.sb_zp_rot_scan_end.setSingleStep(2)
        self.sb_zp_rot_scan_end.setValue(12)

        self.horizontalLayout_73.addWidget(self.sb_zp_rot_scan_end)


        self.verticalLayout_43.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_110 = QLabel(self.widget_7)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_74.addWidget(self.label_110)

        self.sb_zp_rot_scan_num = QSpinBox(self.widget_7)
        self.sb_zp_rot_scan_num.setObjectName(u"sb_zp_rot_scan_num")
        sizePolicy2.setHeightForWidth(self.sb_zp_rot_scan_num.sizePolicy().hasHeightForWidth())
        self.sb_zp_rot_scan_num.setSizePolicy(sizePolicy2)
        self.sb_zp_rot_scan_num.setMinimum(1)
        self.sb_zp_rot_scan_num.setMaximum(1000)
        self.sb_zp_rot_scan_num.setValue(100)

        self.horizontalLayout_74.addWidget(self.sb_zp_rot_scan_num)


        self.verticalLayout_43.addLayout(self.horizontalLayout_74)

        self.gridLayout_65 = QGridLayout()
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.label_157 = QLabel(self.widget_7)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_65.addWidget(self.label_157, 0, 0, 1, 1)

        self.sb_zp_rot_scan_exp_time = QDoubleSpinBox(self.widget_7)
        self.sb_zp_rot_scan_exp_time.setObjectName(u"sb_zp_rot_scan_exp_time")
        sizePolicy2.setHeightForWidth(self.sb_zp_rot_scan_exp_time.sizePolicy().hasHeightForWidth())
        self.sb_zp_rot_scan_exp_time.setSizePolicy(sizePolicy2)
        self.sb_zp_rot_scan_exp_time.setDecimals(3)
        self.sb_zp_rot_scan_exp_time.setMinimum(0.005000000000000)
        self.sb_zp_rot_scan_exp_time.setMaximum(0.500000000000000)
        self.sb_zp_rot_scan_exp_time.setSingleStep(0.010000000000000)
        self.sb_zp_rot_scan_exp_time.setValue(0.050000000000000)

        self.gridLayout_65.addWidget(self.sb_zp_rot_scan_exp_time, 0, 1, 1, 1)


        self.verticalLayout_43.addLayout(self.gridLayout_65)


        self.gridLayout_64.addLayout(self.verticalLayout_43, 0, 1, 1, 1)

        self.pb_zp_rot_align_start = QPushButton(self.widget_7)
        self.pb_zp_rot_align_start.setObjectName(u"pb_zp_rot_align_start")
        sizePolicy3.setHeightForWidth(self.pb_zp_rot_align_start.sizePolicy().hasHeightForWidth())
        self.pb_zp_rot_align_start.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.pb_zp_rot_align_start, 2, 0, 1, 2)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_103 = QLabel(self.widget_7)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_66.addWidget(self.label_103)

        self.sb_zp_rot_angle_start = QSpinBox(self.widget_7)
        self.sb_zp_rot_angle_start.setObjectName(u"sb_zp_rot_angle_start")
        sizePolicy9.setHeightForWidth(self.sb_zp_rot_angle_start.sizePolicy().hasHeightForWidth())
        self.sb_zp_rot_angle_start.setSizePolicy(sizePolicy9)
        self.sb_zp_rot_angle_start.setMinimum(-120)
        self.sb_zp_rot_angle_start.setMaximum(120)
        self.sb_zp_rot_angle_start.setSingleStep(10)
        self.sb_zp_rot_angle_start.setValue(-30)
        self.sb_zp_rot_angle_start.setDisplayIntegerBase(10)

        self.horizontalLayout_66.addWidget(self.sb_zp_rot_angle_start)


        self.verticalLayout_42.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_104 = QLabel(self.widget_7)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_67.addWidget(self.label_104)

        self.sb_zp_rot_angle_end = QSpinBox(self.widget_7)
        self.sb_zp_rot_angle_end.setObjectName(u"sb_zp_rot_angle_end")
        sizePolicy9.setHeightForWidth(self.sb_zp_rot_angle_end.sizePolicy().hasHeightForWidth())
        self.sb_zp_rot_angle_end.setSizePolicy(sizePolicy9)
        self.sb_zp_rot_angle_end.setMinimum(-120)
        self.sb_zp_rot_angle_end.setMaximum(120)
        self.sb_zp_rot_angle_end.setSingleStep(10)
        self.sb_zp_rot_angle_end.setValue(30)

        self.horizontalLayout_67.addWidget(self.sb_zp_rot_angle_end)


        self.verticalLayout_42.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_107 = QLabel(self.widget_7)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_70.addWidget(self.label_107)

        self.sb_zp_rot_angle_num = QSpinBox(self.widget_7)
        self.sb_zp_rot_angle_num.setObjectName(u"sb_zp_rot_angle_num")
        sizePolicy9.setHeightForWidth(self.sb_zp_rot_angle_num.sizePolicy().hasHeightForWidth())
        self.sb_zp_rot_angle_num.setSizePolicy(sizePolicy9)
        self.sb_zp_rot_angle_num.setMinimum(1)
        self.sb_zp_rot_angle_num.setMaximum(100)
        self.sb_zp_rot_angle_num.setValue(10)

        self.horizontalLayout_70.addWidget(self.sb_zp_rot_angle_num)


        self.verticalLayout_42.addLayout(self.horizontalLayout_70)


        self.verticalLayout_41.addLayout(self.verticalLayout_42)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_98 = QLabel(self.widget_7)
        self.label_98.setObjectName(u"label_98")

        self.horizontalLayout_71.addWidget(self.label_98)

        self.cb_zp_rot_elem = QComboBox(self.widget_7)
        self.cb_zp_rot_elem.setObjectName(u"cb_zp_rot_elem")

        self.horizontalLayout_71.addWidget(self.cb_zp_rot_elem)


        self.verticalLayout_41.addLayout(self.horizontalLayout_71)


        self.gridLayout_64.addLayout(self.verticalLayout_41, 0, 0, 1, 1)


        self.gridLayout_63.addLayout(self.gridLayout_64, 0, 0, 1, 1)


        self.gridLayout_66.addWidget(self.widget_7, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.groupBox_34)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_62 = QGridLayout(self.widget_8)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.pushButton_10 = QPushButton(self.widget_8)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_78.addWidget(self.pushButton_10)

        self.dsb_rot_align_smarz = QDoubleSpinBox(self.widget_8)
        self.dsb_rot_align_smarz.setObjectName(u"dsb_rot_align_smarz")
        self.dsb_rot_align_smarz.setDecimals(1)
        self.dsb_rot_align_smarz.setMinimum(-1000.000000000000000)
        self.dsb_rot_align_smarz.setMaximum(1000.000000000000000)
        self.dsb_rot_align_smarz.setValue(100.000000000000000)

        self.horizontalLayout_78.addWidget(self.dsb_rot_align_smarz)


        self.gridLayout_62.addLayout(self.horizontalLayout_78, 2, 0, 1, 1)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.pushButton_9 = QPushButton(self.widget_8)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_77.addWidget(self.pushButton_9)

        self.dsb_rot_align_smarx = QDoubleSpinBox(self.widget_8)
        self.dsb_rot_align_smarx.setObjectName(u"dsb_rot_align_smarx")
        self.dsb_rot_align_smarx.setDecimals(1)
        self.dsb_rot_align_smarx.setMinimum(-1000.000000000000000)
        self.dsb_rot_align_smarx.setMaximum(1000.000000000000000)
        self.dsb_rot_align_smarx.setValue(100.000000000000000)

        self.horizontalLayout_77.addWidget(self.dsb_rot_align_smarx)


        self.gridLayout_62.addLayout(self.horizontalLayout_77, 1, 0, 1, 1)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.pushButton_11 = QPushButton(self.widget_8)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_79.addWidget(self.pushButton_11)

        self.dsb_rot_align_zpsth = QDoubleSpinBox(self.widget_8)
        self.dsb_rot_align_zpsth.setObjectName(u"dsb_rot_align_zpsth")
        self.dsb_rot_align_zpsth.setDecimals(1)
        self.dsb_rot_align_zpsth.setMinimum(-120.000000000000000)
        self.dsb_rot_align_zpsth.setMaximum(120.000000000000000)
        self.dsb_rot_align_zpsth.setSingleStep(5.000000000000000)
        self.dsb_rot_align_zpsth.setValue(15.000000000000000)

        self.horizontalLayout_79.addWidget(self.dsb_rot_align_zpsth)


        self.gridLayout_62.addLayout(self.horizontalLayout_79, 0, 0, 1, 1)

        self.pb_apply_zp_rot_align_corr = QPushButton(self.widget_8)
        self.pb_apply_zp_rot_align_corr.setObjectName(u"pb_apply_zp_rot_align_corr")

        self.gridLayout_62.addWidget(self.pb_apply_zp_rot_align_corr, 3, 0, 1, 1)


        self.gridLayout_66.addWidget(self.widget_8, 1, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_34, 2, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_19 = QGridLayout(self.tab_9)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_35 = QGroupBox(self.tab_9)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.groupBox_35.sizePolicy().hasHeightForWidth())
        self.groupBox_35.setSizePolicy(sizePolicy2)
        self.groupBox_35.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gridLayout_94 = QGridLayout(self.groupBox_35)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.pb_mll_osa_out = QPushButton(self.groupBox_35)
        self.pb_mll_osa_out.setObjectName(u"pb_mll_osa_out")
        self.pb_mll_osa_out.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.pb_mll_osa_out.sizePolicy().hasHeightForWidth())
        self.pb_mll_osa_out.setSizePolicy(sizePolicy9)

        self.gridLayout_94.addWidget(self.pb_mll_osa_out, 0, 0, 1, 1)

        self.pb_mll_lens_out = QPushButton(self.groupBox_35)
        self.pb_mll_lens_out.setObjectName(u"pb_mll_lens_out")

        self.gridLayout_94.addWidget(self.pb_mll_lens_out, 2, 0, 1, 1)

        self.pb_mll_bs_out = QPushButton(self.groupBox_35)
        self.pb_mll_bs_out.setObjectName(u"pb_mll_bs_out")

        self.gridLayout_94.addWidget(self.pb_mll_bs_out, 1, 0, 1, 1)

        self.pb_mll_sample_out = QPushButton(self.groupBox_35)
        self.pb_mll_sample_out.setObjectName(u"pb_mll_sample_out")

        self.gridLayout_94.addWidget(self.pb_mll_sample_out, 4, 0, 1, 1)

        self.pb_mll_bs_in = QPushButton(self.groupBox_35)
        self.pb_mll_bs_in.setObjectName(u"pb_mll_bs_in")

        self.gridLayout_94.addWidget(self.pb_mll_bs_in, 1, 1, 1, 1)

        self.pb_mll_cam11_view = QPushButton(self.groupBox_35)
        self.pb_mll_cam11_view.setObjectName(u"pb_mll_cam11_view")
        self.pb_mll_cam11_view.setEnabled(True)

        self.gridLayout_94.addWidget(self.pb_mll_cam11_view, 5, 0, 1, 1)

        self.pb_mll_osa_in = QPushButton(self.groupBox_35)
        self.pb_mll_osa_in.setObjectName(u"pb_mll_osa_in")
        sizePolicy4.setHeightForWidth(self.pb_mll_osa_in.sizePolicy().hasHeightForWidth())
        self.pb_mll_osa_in.setSizePolicy(sizePolicy4)

        self.gridLayout_94.addWidget(self.pb_mll_osa_in, 0, 1, 1, 1)

        self.pb_mll_nanobeam = QPushButton(self.groupBox_35)
        self.pb_mll_nanobeam.setObjectName(u"pb_mll_nanobeam")

        self.gridLayout_94.addWidget(self.pb_mll_nanobeam, 5, 1, 1, 1)

        self.pb_mll_lens_in = QPushButton(self.groupBox_35)
        self.pb_mll_lens_in.setObjectName(u"pb_mll_lens_in")

        self.gridLayout_94.addWidget(self.pb_mll_lens_in, 2, 1, 1, 1)

        self.pb_mll_sample_in = QPushButton(self.groupBox_35)
        self.pb_mll_sample_in.setObjectName(u"pb_mll_sample_in")

        self.gridLayout_94.addWidget(self.pb_mll_sample_in, 4, 1, 1, 1)

        self.pb_mlls_to_upstream = QPushButton(self.groupBox_35)
        self.pb_mlls_to_upstream.setObjectName(u"pb_mlls_to_upstream")

        self.gridLayout_94.addWidget(self.pb_mlls_to_upstream, 3, 0, 1, 1)

        self.pb_mlls_to_downstream = QPushButton(self.groupBox_35)
        self.pb_mlls_to_downstream.setObjectName(u"pb_mlls_to_downstream")

        self.gridLayout_94.addWidget(self.pb_mlls_to_downstream, 3, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_35, 1, 0, 1, 2)

        self.groupBox_40 = QGroupBox(self.tab_9)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setEnabled(True)
        self.gridLayout_17 = QGridLayout(self.groupBox_40)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_131 = QGridLayout()
        self.gridLayout_131.setObjectName(u"gridLayout_131")
        self.gridLayout_48 = QGridLayout()
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.widget_9 = QWidget(self.groupBox_40)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_15 = QGridLayout(self.widget_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_121 = QLabel(self.widget_9)
        self.label_121.setObjectName(u"label_121")

        self.horizontalLayout_88.addWidget(self.label_121)

        self.cb_mll_focus_elem = QComboBox(self.widget_9)
        self.cb_mll_focus_elem.setObjectName(u"cb_mll_focus_elem")

        self.horizontalLayout_88.addWidget(self.cb_mll_focus_elem)

        self.cb_linearflag_mll_focus = QCheckBox(self.widget_9)
        self.cb_linearflag_mll_focus.setObjectName(u"cb_linearflag_mll_focus")

        self.horizontalLayout_88.addWidget(self.cb_linearflag_mll_focus)


        self.gridLayout_15.addLayout(self.horizontalLayout_88, 4, 0, 1, 2)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(20, -1, -1, -1)
        self.cb_mll_z_motor_move = QComboBox(self.widget_9)
        self.cb_mll_z_motor_move.addItem("")
        self.cb_mll_z_motor_move.addItem("")
        self.cb_mll_z_motor_move.addItem("")
        self.cb_mll_z_motor_move.setObjectName(u"cb_mll_z_motor_move")

        self.horizontalLayout_82.addWidget(self.cb_mll_z_motor_move)

        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_82.addWidget(self.label_4)

        self.dsb_mll_z_target_pos = QDoubleSpinBox(self.widget_9)
        self.dsb_mll_z_target_pos.setObjectName(u"dsb_mll_z_target_pos")
        self.dsb_mll_z_target_pos.setDecimals(1)
        self.dsb_mll_z_target_pos.setMinimum(-200.000000000000000)
        self.dsb_mll_z_target_pos.setMaximum(7000.000000000000000)
        self.dsb_mll_z_target_pos.setSingleStep(5.000000000000000)
        self.dsb_mll_z_target_pos.setValue(0.000000000000000)

        self.horizontalLayout_82.addWidget(self.dsb_mll_z_target_pos)


        self.gridLayout_15.addLayout(self.horizontalLayout_82, 7, 1, 1, 2)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_83 = QLabel(self.widget_9)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_83)

        self.cb_mll_foucs_mtr = QComboBox(self.widget_9)
        self.cb_mll_foucs_mtr.addItem("")
        self.cb_mll_foucs_mtr.addItem("")
        self.cb_mll_foucs_mtr.addItem("")
        self.cb_mll_foucs_mtr.setObjectName(u"cb_mll_foucs_mtr")

        self.verticalLayout_45.addWidget(self.cb_mll_foucs_mtr)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_111 = QLabel(self.widget_9)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_75.addWidget(self.label_111)

        self.dsb_mll_foucs_mtr_start = QDoubleSpinBox(self.widget_9)
        self.dsb_mll_foucs_mtr_start.setObjectName(u"dsb_mll_foucs_mtr_start")
        sizePolicy2.setHeightForWidth(self.dsb_mll_foucs_mtr_start.sizePolicy().hasHeightForWidth())
        self.dsb_mll_foucs_mtr_start.setSizePolicy(sizePolicy2)
        self.dsb_mll_foucs_mtr_start.setMinimum(-15.000000000000000)
        self.dsb_mll_foucs_mtr_start.setMaximum(15.000000000000000)
        self.dsb_mll_foucs_mtr_start.setValue(-1.000000000000000)

        self.horizontalLayout_75.addWidget(self.dsb_mll_foucs_mtr_start)


        self.verticalLayout_45.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.label_113 = QLabel(self.widget_9)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_83.addWidget(self.label_113)

        self.dsb_mll_foucs_mtr_end = QDoubleSpinBox(self.widget_9)
        self.dsb_mll_foucs_mtr_end.setObjectName(u"dsb_mll_foucs_mtr_end")
        sizePolicy2.setHeightForWidth(self.dsb_mll_foucs_mtr_end.sizePolicy().hasHeightForWidth())
        self.dsb_mll_foucs_mtr_end.setSizePolicy(sizePolicy2)
        self.dsb_mll_foucs_mtr_end.setMinimum(-15.000000000000000)
        self.dsb_mll_foucs_mtr_end.setMaximum(15.000000000000000)
        self.dsb_mll_foucs_mtr_end.setValue(1.000000000000000)

        self.horizontalLayout_83.addWidget(self.dsb_mll_foucs_mtr_end)


        self.verticalLayout_45.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_114 = QLabel(self.widget_9)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_84.addWidget(self.label_114)

        self.dsb_mll_foucs_mtr_steps = QSpinBox(self.widget_9)
        self.dsb_mll_foucs_mtr_steps.setObjectName(u"dsb_mll_foucs_mtr_steps")
        sizePolicy2.setHeightForWidth(self.dsb_mll_foucs_mtr_steps.sizePolicy().hasHeightForWidth())
        self.dsb_mll_foucs_mtr_steps.setSizePolicy(sizePolicy2)
        self.dsb_mll_foucs_mtr_steps.setMinimum(10)
        self.dsb_mll_foucs_mtr_steps.setMaximum(1000)
        self.dsb_mll_foucs_mtr_steps.setSingleStep(50)
        self.dsb_mll_foucs_mtr_steps.setValue(100)

        self.horizontalLayout_84.addWidget(self.dsb_mll_foucs_mtr_steps)


        self.verticalLayout_45.addLayout(self.horizontalLayout_84)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_120 = QLabel(self.widget_9)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_120)

        self.dsb_mll_foucs_mtr_exp_time = QDoubleSpinBox(self.widget_9)
        self.dsb_mll_foucs_mtr_exp_time.setObjectName(u"dsb_mll_foucs_mtr_exp_time")
        sizePolicy2.setHeightForWidth(self.dsb_mll_foucs_mtr_exp_time.sizePolicy().hasHeightForWidth())
        self.dsb_mll_foucs_mtr_exp_time.setSizePolicy(sizePolicy2)
        self.dsb_mll_foucs_mtr_exp_time.setDecimals(3)
        self.dsb_mll_foucs_mtr_exp_time.setMinimum(0.005000000000000)
        self.dsb_mll_foucs_mtr_exp_time.setMaximum(0.500000000000000)
        self.dsb_mll_foucs_mtr_exp_time.setSingleStep(0.010000000000000)
        self.dsb_mll_foucs_mtr_exp_time.setValue(0.050000000000000)

        self.horizontalLayout_12.addWidget(self.dsb_mll_foucs_mtr_exp_time)


        self.verticalLayout_45.addLayout(self.horizontalLayout_12)


        self.gridLayout_15.addLayout(self.verticalLayout_45, 0, 2, 5, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_84 = QLabel(self.widget_9)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_84, 0, 0, 1, 1)

        self.cb_mll_z_motor = QComboBox(self.widget_9)
        self.cb_mll_z_motor.addItem("")
        self.cb_mll_z_motor.addItem("")
        self.cb_mll_z_motor.addItem("")
        self.cb_mll_z_motor.setObjectName(u"cb_mll_z_motor")

        self.gridLayout_12.addWidget(self.cb_mll_z_motor, 0, 1, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_12, 0, 0, 1, 2)

        self.pb_mll_z_focus_start = QPushButton(self.widget_9)
        self.pb_mll_z_focus_start.setObjectName(u"pb_mll_z_focus_start")
        sizePolicy2.setHeightForWidth(self.pb_mll_z_focus_start.sizePolicy().hasHeightForWidth())
        self.pb_mll_z_focus_start.setSizePolicy(sizePolicy2)

        self.gridLayout_15.addWidget(self.pb_mll_z_focus_start, 5, 0, 1, 3)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_116 = QLabel(self.widget_9)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_86.addWidget(self.label_116)

        self.sb_mll_z_end = QSpinBox(self.widget_9)
        self.sb_mll_z_end.setObjectName(u"sb_mll_z_end")
        sizePolicy2.setHeightForWidth(self.sb_mll_z_end.sizePolicy().hasHeightForWidth())
        self.sb_mll_z_end.setSizePolicy(sizePolicy2)
        self.sb_mll_z_end.setMinimum(-1000)
        self.sb_mll_z_end.setMaximum(1000)
        self.sb_mll_z_end.setSingleStep(10)
        self.sb_mll_z_end.setValue(50)

        self.horizontalLayout_86.addWidget(self.sb_mll_z_end)


        self.gridLayout_15.addLayout(self.horizontalLayout_86, 2, 0, 1, 2)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_115 = QLabel(self.widget_9)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_85.addWidget(self.label_115)

        self.sb_mll_z_start = QSpinBox(self.widget_9)
        self.sb_mll_z_start.setObjectName(u"sb_mll_z_start")
        sizePolicy2.setHeightForWidth(self.sb_mll_z_start.sizePolicy().hasHeightForWidth())
        self.sb_mll_z_start.setSizePolicy(sizePolicy2)
        self.sb_mll_z_start.setMinimum(-1000)
        self.sb_mll_z_start.setMaximum(1000)
        self.sb_mll_z_start.setSingleStep(10)
        self.sb_mll_z_start.setValue(-50)

        self.horizontalLayout_85.addWidget(self.sb_mll_z_start)


        self.gridLayout_15.addLayout(self.horizontalLayout_85, 1, 0, 1, 2)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_117 = QLabel(self.widget_9)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.label_117)

        self.sb_mll_z_steps = QSpinBox(self.widget_9)
        self.sb_mll_z_steps.setObjectName(u"sb_mll_z_steps")
        sizePolicy2.setHeightForWidth(self.sb_mll_z_steps.sizePolicy().hasHeightForWidth())
        self.sb_mll_z_steps.setSizePolicy(sizePolicy2)
        self.sb_mll_z_steps.setMinimum(1)
        self.sb_mll_z_steps.setMaximum(1000)
        self.sb_mll_z_steps.setSingleStep(5)
        self.sb_mll_z_steps.setValue(10)

        self.horizontalLayout_87.addWidget(self.sb_mll_z_steps)


        self.gridLayout_15.addLayout(self.horizontalLayout_87, 3, 0, 1, 2)

        self.pb_mll_z_focus_move = QPushButton(self.widget_9)
        self.pb_mll_z_focus_move.setObjectName(u"pb_mll_z_focus_move")
        sizePolicy4.setHeightForWidth(self.pb_mll_z_focus_move.sizePolicy().hasHeightForWidth())
        self.pb_mll_z_focus_move.setSizePolicy(sizePolicy4)

        self.gridLayout_15.addWidget(self.pb_mll_z_focus_move, 7, 0, 1, 1)

        self.label_61 = QLabel(self.widget_9)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_15.addWidget(self.label_61, 6, 0, 1, 1)


        self.gridLayout_48.addWidget(self.widget_9, 0, 0, 1, 1)


        self.gridLayout_131.addLayout(self.gridLayout_48, 2, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_131, 1, 0, 1, 1)

        self.label_137 = QLabel(self.groupBox_40)
        self.label_137.setObjectName(u"label_137")
        sizePolicy2.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy2)

        self.gridLayout_17.addWidget(self.label_137, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_40, 2, 0, 1, 2)

        self.pb_stop_mll_motion = QPushButton(self.tab_9)
        self.pb_stop_mll_motion.setObjectName(u"pb_stop_mll_motion")
        self.pb_stop_mll_motion.setStyleSheet(u"color: rgb(239, 41, 41);")

        self.gridLayout_19.addWidget(self.pb_stop_mll_motion, 0, 0, 1, 2)

        self.groupBox_41 = QGroupBox(self.tab_9)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.groupBox_41.setEnabled(True)
        self.gridLayout_139 = QGridLayout(self.groupBox_41)
        self.gridLayout_139.setObjectName(u"gridLayout_139")
        self.label_80 = QLabel(self.groupBox_41)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_139.addWidget(self.label_80, 0, 0, 1, 1)

        self.gridLayout_135 = QGridLayout()
        self.gridLayout_135.setObjectName(u"gridLayout_135")
        self.gridLayout_134 = QGridLayout()
        self.gridLayout_134.setObjectName(u"gridLayout_134")
        self.widget_10 = QWidget(self.groupBox_41)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_130 = QGridLayout(self.widget_10)
        self.gridLayout_130.setObjectName(u"gridLayout_130")
        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.label_176 = QLabel(self.widget_10)
        self.label_176.setObjectName(u"label_176")
        sizePolicy2.setHeightForWidth(self.label_176.sizePolicy().hasHeightForWidth())
        self.label_176.setSizePolicy(sizePolicy2)

        self.horizontalLayout_93.addWidget(self.label_176)

        self.sb_mll_rot_scan_exp_time_2 = QDoubleSpinBox(self.widget_10)
        self.sb_mll_rot_scan_exp_time_2.setObjectName(u"sb_mll_rot_scan_exp_time_2")
        sizePolicy2.setHeightForWidth(self.sb_mll_rot_scan_exp_time_2.sizePolicy().hasHeightForWidth())
        self.sb_mll_rot_scan_exp_time_2.setSizePolicy(sizePolicy2)
        self.sb_mll_rot_scan_exp_time_2.setDecimals(3)
        self.sb_mll_rot_scan_exp_time_2.setMinimum(0.005000000000000)
        self.sb_mll_rot_scan_exp_time_2.setMaximum(1.000000000000000)
        self.sb_mll_rot_scan_exp_time_2.setSingleStep(0.010000000000000)
        self.sb_mll_rot_scan_exp_time_2.setValue(0.500000000000000)

        self.horizontalLayout_93.addWidget(self.sb_mll_rot_scan_exp_time_2)


        self.gridLayout_130.addLayout(self.horizontalLayout_93, 6, 0, 1, 1)

        self.label_87 = QLabel(self.widget_10)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.gridLayout_130.addWidget(self.label_87, 0, 0, 1, 1)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.label_175 = QLabel(self.widget_10)
        self.label_175.setObjectName(u"label_175")

        self.horizontalLayout_92.addWidget(self.label_175)

        self.cb_mll_rot_elem = QComboBox(self.widget_10)
        self.cb_mll_rot_elem.setObjectName(u"cb_mll_rot_elem")

        self.horizontalLayout_92.addWidget(self.cb_mll_rot_elem)


        self.gridLayout_130.addLayout(self.horizontalLayout_92, 5, 0, 1, 1)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.label_124 = QLabel(self.widget_10)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_89.addWidget(self.label_124)

        self.sb_mll_rot_angle_start = QSpinBox(self.widget_10)
        self.sb_mll_rot_angle_start.setObjectName(u"sb_mll_rot_angle_start")
        sizePolicy9.setHeightForWidth(self.sb_mll_rot_angle_start.sizePolicy().hasHeightForWidth())
        self.sb_mll_rot_angle_start.setSizePolicy(sizePolicy9)
        self.sb_mll_rot_angle_start.setMinimum(-120)
        self.sb_mll_rot_angle_start.setMaximum(120)
        self.sb_mll_rot_angle_start.setSingleStep(10)
        self.sb_mll_rot_angle_start.setValue(-60)
        self.sb_mll_rot_angle_start.setDisplayIntegerBase(10)

        self.horizontalLayout_89.addWidget(self.sb_mll_rot_angle_start)


        self.gridLayout_130.addLayout(self.horizontalLayout_89, 1, 0, 1, 1)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_173 = QLabel(self.widget_10)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_90.addWidget(self.label_173)

        self.sb_mll_rot_angle_end = QSpinBox(self.widget_10)
        self.sb_mll_rot_angle_end.setObjectName(u"sb_mll_rot_angle_end")
        sizePolicy9.setHeightForWidth(self.sb_mll_rot_angle_end.sizePolicy().hasHeightForWidth())
        self.sb_mll_rot_angle_end.setSizePolicy(sizePolicy9)
        self.sb_mll_rot_angle_end.setMinimum(-120)
        self.sb_mll_rot_angle_end.setMaximum(120)
        self.sb_mll_rot_angle_end.setSingleStep(10)
        self.sb_mll_rot_angle_end.setValue(60)

        self.horizontalLayout_90.addWidget(self.sb_mll_rot_angle_end)


        self.gridLayout_130.addLayout(self.horizontalLayout_90, 3, 0, 1, 1)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.label_174 = QLabel(self.widget_10)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_91.addWidget(self.label_174)

        self.sb_mll_rot_angle_num = QSpinBox(self.widget_10)
        self.sb_mll_rot_angle_num.setObjectName(u"sb_mll_rot_angle_num")
        sizePolicy9.setHeightForWidth(self.sb_mll_rot_angle_num.sizePolicy().hasHeightForWidth())
        self.sb_mll_rot_angle_num.setSizePolicy(sizePolicy9)
        self.sb_mll_rot_angle_num.setMinimum(1)
        self.sb_mll_rot_angle_num.setMaximum(100)
        self.sb_mll_rot_angle_num.setValue(12)

        self.horizontalLayout_91.addWidget(self.sb_mll_rot_angle_num)


        self.gridLayout_130.addLayout(self.horizontalLayout_91, 4, 0, 1, 1)


        self.gridLayout_134.addWidget(self.widget_10, 0, 0, 1, 1)

        self.frame = QFrame(self.groupBox_41)
        self.frame.setObjectName(u"frame")
        self.gridLayout_133 = QGridLayout(self.frame)
        self.gridLayout_133.setObjectName(u"gridLayout_133")
        self.label_85 = QLabel(self.frame)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.gridLayout_133.addWidget(self.label_85, 0, 0, 1, 1)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_112 = QLabel(self.frame)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_76.addWidget(self.label_112)

        self.sb_mll_rot_scan_start_2 = QDoubleSpinBox(self.frame)
        self.sb_mll_rot_scan_start_2.setObjectName(u"sb_mll_rot_scan_start_2")
        sizePolicy2.setHeightForWidth(self.sb_mll_rot_scan_start_2.sizePolicy().hasHeightForWidth())
        self.sb_mll_rot_scan_start_2.setSizePolicy(sizePolicy2)
        self.sb_mll_rot_scan_start_2.setMinimum(-15.000000000000000)
        self.sb_mll_rot_scan_start_2.setMaximum(15.000000000000000)
        self.sb_mll_rot_scan_start_2.setValue(-1.000000000000000)

        self.horizontalLayout_76.addWidget(self.sb_mll_rot_scan_start_2)


        self.gridLayout_133.addLayout(self.horizontalLayout_76, 1, 0, 1, 1)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.label_139 = QLabel(self.frame)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_94.addWidget(self.label_139)

        self.sb_mll_rot_scan_end_2 = QDoubleSpinBox(self.frame)
        self.sb_mll_rot_scan_end_2.setObjectName(u"sb_mll_rot_scan_end_2")
        sizePolicy2.setHeightForWidth(self.sb_mll_rot_scan_end_2.sizePolicy().hasHeightForWidth())
        self.sb_mll_rot_scan_end_2.setSizePolicy(sizePolicy2)
        self.sb_mll_rot_scan_end_2.setMinimum(-15.000000000000000)
        self.sb_mll_rot_scan_end_2.setMaximum(15.000000000000000)
        self.sb_mll_rot_scan_end_2.setValue(1.000000000000000)

        self.horizontalLayout_94.addWidget(self.sb_mll_rot_scan_end_2)


        self.gridLayout_133.addLayout(self.horizontalLayout_94, 2, 0, 1, 1)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_140 = QLabel(self.frame)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_99.addWidget(self.label_140)

        self.sb_mll_rot_scan_num = QSpinBox(self.frame)
        self.sb_mll_rot_scan_num.setObjectName(u"sb_mll_rot_scan_num")
        sizePolicy2.setHeightForWidth(self.sb_mll_rot_scan_num.sizePolicy().hasHeightForWidth())
        self.sb_mll_rot_scan_num.setSizePolicy(sizePolicy2)
        self.sb_mll_rot_scan_num.setMinimum(10)
        self.sb_mll_rot_scan_num.setMaximum(1000)
        self.sb_mll_rot_scan_num.setSingleStep(50)
        self.sb_mll_rot_scan_num.setValue(100)

        self.horizontalLayout_99.addWidget(self.sb_mll_rot_scan_num)


        self.gridLayout_133.addLayout(self.horizontalLayout_99, 3, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_142 = QLabel(self.frame)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_142)

        self.sb_mll_rot_scan_exp_time = QDoubleSpinBox(self.frame)
        self.sb_mll_rot_scan_exp_time.setObjectName(u"sb_mll_rot_scan_exp_time")
        sizePolicy2.setHeightForWidth(self.sb_mll_rot_scan_exp_time.sizePolicy().hasHeightForWidth())
        self.sb_mll_rot_scan_exp_time.setSizePolicy(sizePolicy2)
        self.sb_mll_rot_scan_exp_time.setDecimals(3)
        self.sb_mll_rot_scan_exp_time.setMinimum(0.005000000000000)
        self.sb_mll_rot_scan_exp_time.setMaximum(0.500000000000000)
        self.sb_mll_rot_scan_exp_time.setSingleStep(0.010000000000000)
        self.sb_mll_rot_scan_exp_time.setValue(0.050000000000000)

        self.horizontalLayout_22.addWidget(self.sb_mll_rot_scan_exp_time)


        self.gridLayout_133.addLayout(self.horizontalLayout_22, 4, 0, 1, 1)


        self.gridLayout_134.addWidget(self.frame, 0, 1, 1, 1)

        self.widget_11 = QWidget(self.groupBox_41)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_132 = QGridLayout(self.widget_11)
        self.gridLayout_132.setObjectName(u"gridLayout_132")
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.label_91 = QLabel(self.widget_11)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_101.addWidget(self.label_91)

        self.dsb_rot_align_sbx = QDoubleSpinBox(self.widget_11)
        self.dsb_rot_align_sbx.setObjectName(u"dsb_rot_align_sbx")
        self.dsb_rot_align_sbx.setDecimals(1)
        self.dsb_rot_align_sbx.setMinimum(-1000.000000000000000)
        self.dsb_rot_align_sbx.setMaximum(1000.000000000000000)
        self.dsb_rot_align_sbx.setValue(0.000000000000000)

        self.horizontalLayout_101.addWidget(self.dsb_rot_align_sbx)

        self.pb_rot_align_sbx_move = QPushButton(self.widget_11)
        self.pb_rot_align_sbx_move.setObjectName(u"pb_rot_align_sbx_move")

        self.horizontalLayout_101.addWidget(self.pb_rot_align_sbx_move)


        self.gridLayout_132.addLayout(self.horizontalLayout_101, 4, 0, 1, 1)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.label_88 = QLabel(self.widget_11)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_96.addWidget(self.label_88)

        self.dsb_rot_align_dsth = QDoubleSpinBox(self.widget_11)
        self.dsb_rot_align_dsth.setObjectName(u"dsb_rot_align_dsth")
        self.dsb_rot_align_dsth.setDecimals(1)
        self.dsb_rot_align_dsth.setMinimum(-120.000000000000000)
        self.dsb_rot_align_dsth.setMaximum(120.000000000000000)
        self.dsb_rot_align_dsth.setSingleStep(5.000000000000000)
        self.dsb_rot_align_dsth.setValue(0.000000000000000)

        self.horizontalLayout_96.addWidget(self.dsb_rot_align_dsth)

        self.pb_rot_align_dsth_move = QPushButton(self.widget_11)
        self.pb_rot_align_dsth_move.setObjectName(u"pb_rot_align_dsth_move")

        self.horizontalLayout_96.addWidget(self.pb_rot_align_dsth_move)


        self.gridLayout_132.addLayout(self.horizontalLayout_96, 1, 0, 1, 1)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_90 = QLabel(self.widget_11)
        self.label_90.setObjectName(u"label_90")

        self.horizontalLayout_98.addWidget(self.label_90)

        self.dsb_rot_align_dsz = QDoubleSpinBox(self.widget_11)
        self.dsb_rot_align_dsz.setObjectName(u"dsb_rot_align_dsz")
        self.dsb_rot_align_dsz.setDecimals(1)
        self.dsb_rot_align_dsz.setMinimum(-1000.000000000000000)
        self.dsb_rot_align_dsz.setMaximum(1000.000000000000000)
        self.dsb_rot_align_dsz.setValue(0.000000000000000)

        self.horizontalLayout_98.addWidget(self.dsb_rot_align_dsz)

        self.pb_rot_align_dsz_move = QPushButton(self.widget_11)
        self.pb_rot_align_dsz_move.setObjectName(u"pb_rot_align_dsz_move")

        self.horizontalLayout_98.addWidget(self.pb_rot_align_dsz_move)


        self.gridLayout_132.addLayout(self.horizontalLayout_98, 3, 0, 1, 1)

        self.label_86 = QLabel(self.widget_11)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.gridLayout_132.addWidget(self.label_86, 0, 0, 1, 1)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_89 = QLabel(self.widget_11)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_97.addWidget(self.label_89)

        self.dsb_rot_align_dsx = QDoubleSpinBox(self.widget_11)
        self.dsb_rot_align_dsx.setObjectName(u"dsb_rot_align_dsx")
        self.dsb_rot_align_dsx.setDecimals(1)
        self.dsb_rot_align_dsx.setMinimum(-1000.000000000000000)
        self.dsb_rot_align_dsx.setMaximum(1000.000000000000000)
        self.dsb_rot_align_dsx.setValue(0.000000000000000)

        self.horizontalLayout_97.addWidget(self.dsb_rot_align_dsx)

        self.pb_rot_align_dsx_move = QPushButton(self.widget_11)
        self.pb_rot_align_dsx_move.setObjectName(u"pb_rot_align_dsx_move")

        self.horizontalLayout_97.addWidget(self.pb_rot_align_dsx_move)


        self.gridLayout_132.addLayout(self.horizontalLayout_97, 2, 0, 1, 1)

        self.pb_rot_align_all_move = QPushButton(self.widget_11)
        self.pb_rot_align_all_move.setObjectName(u"pb_rot_align_all_move")

        self.gridLayout_132.addWidget(self.pb_rot_align_all_move, 5, 0, 1, 1)


        self.gridLayout_134.addWidget(self.widget_11, 0, 2, 1, 1)


        self.gridLayout_135.addLayout(self.gridLayout_134, 0, 0, 1, 1)

        self.pb_mll_rot_align_start = QPushButton(self.groupBox_41)
        self.pb_mll_rot_align_start.setObjectName(u"pb_mll_rot_align_start")
        sizePolicy.setHeightForWidth(self.pb_mll_rot_align_start.sizePolicy().hasHeightForWidth())
        self.pb_mll_rot_align_start.setSizePolicy(sizePolicy)

        self.gridLayout_135.addWidget(self.pb_mll_rot_align_start, 1, 0, 1, 1)


        self.gridLayout_139.addLayout(self.gridLayout_135, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_41, 3, 0, 2, 2)

        self.tabWidget_3.addTab(self.tab_9, "")

        self.gridLayout_115.addWidget(self.tabWidget_3, 0, 2, 3, 1)

        self.tabWidget_2 = QTabWidget(self.alignment_tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_81 = QGridLayout(self.tab_11)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.groupBox_26 = QGroupBox(self.tab_11)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.gridLayout_59 = QGridLayout(self.groupBox_26)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.label_7 = QLabel(self.groupBox_26)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.gridLayout_59.addWidget(self.label_7, 0, 0, 1, 2)

        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.pb_S5_Open = QPushButton(self.groupBox_26)
        self.pb_S5_Open.setObjectName(u"pb_S5_Open")
        sizePolicy2.setHeightForWidth(self.pb_S5_Open.sizePolicy().hasHeightForWidth())
        self.pb_S5_Open.setSizePolicy(sizePolicy2)

        self.gridLayout_28.addWidget(self.pb_S5_Open, 0, 0, 1, 1)

        self.pb_S5_Close = QPushButton(self.groupBox_26)
        self.pb_S5_Close.setObjectName(u"pb_S5_Close")
        sizePolicy2.setHeightForWidth(self.pb_S5_Close.sizePolicy().hasHeightForWidth())
        self.pb_S5_Close.setSizePolicy(sizePolicy2)

        self.gridLayout_28.addWidget(self.pb_S5_Close, 0, 1, 1, 1)

        self.pb_S5_HClose = QPushButton(self.groupBox_26)
        self.pb_S5_HClose.setObjectName(u"pb_S5_HClose")
        sizePolicy2.setHeightForWidth(self.pb_S5_HClose.sizePolicy().hasHeightForWidth())
        self.pb_S5_HClose.setSizePolicy(sizePolicy2)

        self.gridLayout_28.addWidget(self.pb_S5_HClose, 1, 0, 1, 1)

        self.pb_S5_VClose = QPushButton(self.groupBox_26)
        self.pb_S5_VClose.setObjectName(u"pb_S5_VClose")
        sizePolicy2.setHeightForWidth(self.pb_S5_VClose.sizePolicy().hasHeightForWidth())
        self.pb_S5_VClose.setSizePolicy(sizePolicy2)

        self.gridLayout_28.addWidget(self.pb_S5_VClose, 1, 1, 1, 1)


        self.gridLayout_43.addLayout(self.gridLayout_28, 0, 0, 1, 1)

        self.pb_move_s5 = QPushButton(self.groupBox_26)
        self.pb_move_s5.setObjectName(u"pb_move_s5")

        self.gridLayout_43.addWidget(self.pb_move_s5, 1, 0, 1, 1)


        self.gridLayout_59.addLayout(self.gridLayout_43, 1, 0, 1, 2)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_184 = QLabel(self.groupBox_26)
        self.label_184.setObjectName(u"label_184")
        sizePolicy2.setHeightForWidth(self.label_184.sizePolicy().hasHeightForWidth())
        self.label_184.setSizePolicy(sizePolicy2)

        self.gridLayout_22.addWidget(self.label_184, 1, 0, 1, 1)

        self.label_126 = QLabel(self.groupBox_26)
        self.label_126.setObjectName(u"label_126")
        sizePolicy2.setHeightForWidth(self.label_126.sizePolicy().hasHeightForWidth())
        self.label_126.setSizePolicy(sizePolicy2)

        self.gridLayout_22.addWidget(self.label_126, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_26)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.gridLayout_22.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_27.addLayout(self.gridLayout_22, 0, 0, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_182 = QLabel(self.groupBox_26)
        self.label_182.setObjectName(u"label_182")
        sizePolicy2.setHeightForWidth(self.label_182.sizePolicy().hasHeightForWidth())
        self.label_182.setSizePolicy(sizePolicy2)
        self.label_182.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_182, 0, 0, 1, 1)

        self.db_s5_x_set = QDoubleSpinBox(self.groupBox_26)
        self.db_s5_x_set.setObjectName(u"db_s5_x_set")
        self.db_s5_x_set.setDecimals(3)
        self.db_s5_x_set.setValue(0.100000000000000)

        self.gridLayout_23.addWidget(self.db_s5_x_set, 1, 0, 1, 1)

        self.db_s5_x = QDoubleSpinBox(self.groupBox_26)
        self.db_s5_x.setObjectName(u"db_s5_x")
        sizePolicy2.setHeightForWidth(self.db_s5_x.sizePolicy().hasHeightForWidth())
        self.db_s5_x.setSizePolicy(sizePolicy2)
        self.db_s5_x.setReadOnly(True)
        self.db_s5_x.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_s5_x.setDecimals(3)
        self.db_s5_x.setMinimum(-0.100000000000000)
        self.db_s5_x.setMaximum(4.000000000000000)
        self.db_s5_x.setValue(1.000000000000000)

        self.gridLayout_23.addWidget(self.db_s5_x, 2, 0, 1, 1)


        self.gridLayout_27.addLayout(self.gridLayout_23, 0, 1, 1, 1)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_185 = QLabel(self.groupBox_26)
        self.label_185.setObjectName(u"label_185")
        sizePolicy2.setHeightForWidth(self.label_185.sizePolicy().hasHeightForWidth())
        self.label_185.setSizePolicy(sizePolicy2)
        self.label_185.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.label_185, 0, 0, 1, 1)

        self.db_s5_y_set = QDoubleSpinBox(self.groupBox_26)
        self.db_s5_y_set.setObjectName(u"db_s5_y_set")
        self.db_s5_y_set.setDecimals(3)
        self.db_s5_y_set.setValue(0.100000000000000)

        self.gridLayout_26.addWidget(self.db_s5_y_set, 1, 0, 1, 1)

        self.db_s5_y = QDoubleSpinBox(self.groupBox_26)
        self.db_s5_y.setObjectName(u"db_s5_y")
        sizePolicy2.setHeightForWidth(self.db_s5_y.sizePolicy().hasHeightForWidth())
        self.db_s5_y.setSizePolicy(sizePolicy2)
        self.db_s5_y.setReadOnly(True)
        self.db_s5_y.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_s5_y.setDecimals(3)
        self.db_s5_y.setMinimum(-0.100000000000000)
        self.db_s5_y.setMaximum(4.000000000000000)
        self.db_s5_y.setValue(1.000000000000000)

        self.gridLayout_26.addWidget(self.db_s5_y, 2, 0, 1, 1)


        self.gridLayout_27.addLayout(self.gridLayout_26, 0, 2, 1, 1)


        self.gridLayout_59.addLayout(self.gridLayout_27, 1, 2, 1, 2)

        self.label_60 = QLabel(self.groupBox_26)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_59.addWidget(self.label_60, 2, 0, 1, 1)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_199 = QLabel(self.groupBox_26)
        self.label_199.setObjectName(u"label_199")
        sizePolicy2.setHeightForWidth(self.label_199.sizePolicy().hasHeightForWidth())
        self.label_199.setSizePolicy(sizePolicy2)

        self.verticalLayout_29.addWidget(self.label_199)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pb_s5_hcen_move_neg = QPushButton(self.groupBox_26)
        self.pb_s5_hcen_move_neg.setObjectName(u"pb_s5_hcen_move_neg")
        sizePolicy2.setHeightForWidth(self.pb_s5_hcen_move_neg.sizePolicy().hasHeightForWidth())
        self.pb_s5_hcen_move_neg.setSizePolicy(sizePolicy2)

        self.horizontalLayout_29.addWidget(self.pb_s5_hcen_move_neg)

        self.db_s5_hcen_move = QDoubleSpinBox(self.groupBox_26)
        self.db_s5_hcen_move.setObjectName(u"db_s5_hcen_move")
        self.db_s5_hcen_move.setDecimals(3)
        self.db_s5_hcen_move.setValue(0.500000000000000)

        self.horizontalLayout_29.addWidget(self.db_s5_hcen_move)

        self.pb_s5_hcen_move_positive = QPushButton(self.groupBox_26)
        self.pb_s5_hcen_move_positive.setObjectName(u"pb_s5_hcen_move_positive")
        sizePolicy2.setHeightForWidth(self.pb_s5_hcen_move_positive.sizePolicy().hasHeightForWidth())
        self.pb_s5_hcen_move_positive.setSizePolicy(sizePolicy2)

        self.horizontalLayout_29.addWidget(self.pb_s5_hcen_move_positive)


        self.verticalLayout_29.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.pb_s5_vcen_move_neg = QPushButton(self.groupBox_26)
        self.pb_s5_vcen_move_neg.setObjectName(u"pb_s5_vcen_move_neg")
        sizePolicy2.setHeightForWidth(self.pb_s5_vcen_move_neg.sizePolicy().hasHeightForWidth())
        self.pb_s5_vcen_move_neg.setSizePolicy(sizePolicy2)

        self.horizontalLayout_30.addWidget(self.pb_s5_vcen_move_neg)

        self.db_s5_vcen_move = QDoubleSpinBox(self.groupBox_26)
        self.db_s5_vcen_move.setObjectName(u"db_s5_vcen_move")
        self.db_s5_vcen_move.setDecimals(3)
        self.db_s5_vcen_move.setValue(0.500000000000000)

        self.horizontalLayout_30.addWidget(self.db_s5_vcen_move)

        self.pb_s5_vcen_move_positive = QPushButton(self.groupBox_26)
        self.pb_s5_vcen_move_positive.setObjectName(u"pb_s5_vcen_move_positive")
        sizePolicy2.setHeightForWidth(self.pb_s5_vcen_move_positive.sizePolicy().hasHeightForWidth())
        self.pb_s5_vcen_move_positive.setSizePolicy(sizePolicy2)

        self.horizontalLayout_30.addWidget(self.pb_s5_vcen_move_positive)


        self.verticalLayout_29.addLayout(self.horizontalLayout_30)


        self.gridLayout_59.addLayout(self.verticalLayout_29, 2, 2, 1, 1)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_195 = QLabel(self.groupBox_26)
        self.label_195.setObjectName(u"label_195")
        sizePolicy2.setHeightForWidth(self.label_195.sizePolicy().hasHeightForWidth())
        self.label_195.setSizePolicy(sizePolicy2)

        self.verticalLayout_28.addWidget(self.label_195)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_197 = QLabel(self.groupBox_26)
        self.label_197.setObjectName(u"label_197")
        sizePolicy2.setHeightForWidth(self.label_197.sizePolicy().hasHeightForWidth())
        self.label_197.setSizePolicy(sizePolicy2)
        self.label_197.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_197)

        self.db_s5_hcen_rbv = QDoubleSpinBox(self.groupBox_26)
        self.db_s5_hcen_rbv.setObjectName(u"db_s5_hcen_rbv")
        sizePolicy2.setHeightForWidth(self.db_s5_hcen_rbv.sizePolicy().hasHeightForWidth())
        self.db_s5_hcen_rbv.setSizePolicy(sizePolicy2)
        self.db_s5_hcen_rbv.setReadOnly(True)
        self.db_s5_hcen_rbv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_s5_hcen_rbv.setDecimals(3)
        self.db_s5_hcen_rbv.setMinimum(-0.100000000000000)
        self.db_s5_hcen_rbv.setMaximum(4.000000000000000)
        self.db_s5_hcen_rbv.setValue(0.050000000000000)

        self.horizontalLayout_27.addWidget(self.db_s5_hcen_rbv)


        self.verticalLayout_28.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_198 = QLabel(self.groupBox_26)
        self.label_198.setObjectName(u"label_198")
        sizePolicy2.setHeightForWidth(self.label_198.sizePolicy().hasHeightForWidth())
        self.label_198.setSizePolicy(sizePolicy2)
        self.label_198.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_198)

        self.db_s5_vcen_rbv = QDoubleSpinBox(self.groupBox_26)
        self.db_s5_vcen_rbv.setObjectName(u"db_s5_vcen_rbv")
        sizePolicy2.setHeightForWidth(self.db_s5_vcen_rbv.sizePolicy().hasHeightForWidth())
        self.db_s5_vcen_rbv.setSizePolicy(sizePolicy2)
        self.db_s5_vcen_rbv.setReadOnly(True)
        self.db_s5_vcen_rbv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_s5_vcen_rbv.setDecimals(3)
        self.db_s5_vcen_rbv.setMinimum(-0.100000000000000)
        self.db_s5_vcen_rbv.setMaximum(4.000000000000000)
        self.db_s5_vcen_rbv.setValue(0.050000000000000)

        self.horizontalLayout_28.addWidget(self.db_s5_vcen_rbv)


        self.verticalLayout_28.addLayout(self.horizontalLayout_28)


        self.gridLayout_59.addLayout(self.verticalLayout_28, 2, 3, 1, 1)


        self.gridLayout_81.addWidget(self.groupBox_26, 1, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.tab_11)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_70 = QGridLayout(self.groupBox_12)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.label_59 = QLabel(self.groupBox_12)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_70.addWidget(self.label_59, 2, 0, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_58 = QLabel(self.groupBox_12)
        self.label_58.setObjectName(u"label_58")

        self.verticalLayout_25.addWidget(self.label_58)

        self.pb_peakBeamXY = QPushButton(self.groupBox_12)
        self.pb_peakBeamXY.setObjectName(u"pb_peakBeamXY")
        sizePolicy.setHeightForWidth(self.pb_peakBeamXY.sizePolicy().hasHeightForWidth())
        self.pb_peakBeamXY.setSizePolicy(sizePolicy)

        self.verticalLayout_25.addWidget(self.pb_peakBeamXY)

        self.pb_recover_from_beamdump = QPushButton(self.groupBox_12)
        self.pb_recover_from_beamdump.setObjectName(u"pb_recover_from_beamdump")
        sizePolicy.setHeightForWidth(self.pb_recover_from_beamdump.sizePolicy().hasHeightForWidth())
        self.pb_recover_from_beamdump.setSizePolicy(sizePolicy)

        self.verticalLayout_25.addWidget(self.pb_recover_from_beamdump)


        self.gridLayout_70.addLayout(self.verticalLayout_25, 0, 0, 1, 1)

        self.pb_enable_run = QPushButton(self.groupBox_12)
        self.pb_enable_run.setObjectName(u"pb_enable_run")

        self.gridLayout_70.addWidget(self.pb_enable_run, 1, 0, 1, 1)


        self.gridLayout_81.addWidget(self.groupBox_12, 2, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.tab_11)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_32 = QGridLayout(self.groupBox_19)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_134 = QLabel(self.groupBox_19)
        self.label_134.setObjectName(u"label_134")
        sizePolicy2.setHeightForWidth(self.label_134.sizePolicy().hasHeightForWidth())
        self.label_134.setSizePolicy(sizePolicy2)
        self.label_134.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_32.addWidget(self.label_134, 0, 0, 1, 1)

        self.gridLayout_78 = QGridLayout()
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.gridLayout_75 = QGridLayout()
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.pb_SSA2_HClose = QPushButton(self.groupBox_19)
        self.pb_SSA2_HClose.setObjectName(u"pb_SSA2_HClose")
        sizePolicy2.setHeightForWidth(self.pb_SSA2_HClose.sizePolicy().hasHeightForWidth())
        self.pb_SSA2_HClose.setSizePolicy(sizePolicy2)

        self.gridLayout_75.addWidget(self.pb_SSA2_HClose, 1, 0, 1, 1)

        self.pb_SSA2_VClose = QPushButton(self.groupBox_19)
        self.pb_SSA2_VClose.setObjectName(u"pb_SSA2_VClose")
        sizePolicy2.setHeightForWidth(self.pb_SSA2_VClose.sizePolicy().hasHeightForWidth())
        self.pb_SSA2_VClose.setSizePolicy(sizePolicy2)

        self.gridLayout_75.addWidget(self.pb_SSA2_VClose, 1, 1, 1, 1)

        self.pb_SSA2_Open = QPushButton(self.groupBox_19)
        self.pb_SSA2_Open.setObjectName(u"pb_SSA2_Open")
        sizePolicy2.setHeightForWidth(self.pb_SSA2_Open.sizePolicy().hasHeightForWidth())
        self.pb_SSA2_Open.setSizePolicy(sizePolicy2)

        self.gridLayout_75.addWidget(self.pb_SSA2_Open, 0, 0, 1, 1)

        self.pb_SSA2_Close = QPushButton(self.groupBox_19)
        self.pb_SSA2_Close.setObjectName(u"pb_SSA2_Close")
        sizePolicy.setHeightForWidth(self.pb_SSA2_Close.sizePolicy().hasHeightForWidth())
        self.pb_SSA2_Close.setSizePolicy(sizePolicy)

        self.gridLayout_75.addWidget(self.pb_SSA2_Close, 0, 1, 1, 1)


        self.gridLayout_78.addLayout(self.gridLayout_75, 0, 0, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_78, 1, 0, 2, 2)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_180 = QLabel(self.groupBox_19)
        self.label_180.setObjectName(u"label_180")
        sizePolicy2.setHeightForWidth(self.label_180.sizePolicy().hasHeightForWidth())
        self.label_180.setSizePolicy(sizePolicy2)
        self.label_180.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_180, 0, 0, 1, 1)

        self.db_ssa2_x_set = QDoubleSpinBox(self.groupBox_19)
        self.db_ssa2_x_set.setObjectName(u"db_ssa2_x_set")
        self.db_ssa2_x_set.setDecimals(3)
        self.db_ssa2_x_set.setValue(0.500000000000000)

        self.gridLayout_29.addWidget(self.db_ssa2_x_set, 1, 0, 1, 1)

        self.db_ssa2_x = QDoubleSpinBox(self.groupBox_19)
        self.db_ssa2_x.setObjectName(u"db_ssa2_x")
        sizePolicy2.setHeightForWidth(self.db_ssa2_x.sizePolicy().hasHeightForWidth())
        self.db_ssa2_x.setSizePolicy(sizePolicy2)
        self.db_ssa2_x.setReadOnly(True)
        self.db_ssa2_x.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_ssa2_x.setDecimals(3)
        self.db_ssa2_x.setMinimum(-0.100000000000000)
        self.db_ssa2_x.setMaximum(4.000000000000000)
        self.db_ssa2_x.setValue(0.050000000000000)

        self.gridLayout_29.addWidget(self.db_ssa2_x, 2, 0, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_29, 0, 1, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_183 = QLabel(self.groupBox_19)
        self.label_183.setObjectName(u"label_183")
        sizePolicy2.setHeightForWidth(self.label_183.sizePolicy().hasHeightForWidth())
        self.label_183.setSizePolicy(sizePolicy2)

        self.gridLayout_14.addWidget(self.label_183, 2, 0, 1, 1)

        self.label_125 = QLabel(self.groupBox_19)
        self.label_125.setObjectName(u"label_125")
        sizePolicy2.setHeightForWidth(self.label_125.sizePolicy().hasHeightForWidth())
        self.label_125.setSizePolicy(sizePolicy2)

        self.gridLayout_14.addWidget(self.label_125, 3, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_19)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.gridLayout_14.addWidget(self.label_10, 1, 0, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_181 = QLabel(self.groupBox_19)
        self.label_181.setObjectName(u"label_181")
        sizePolicy2.setHeightForWidth(self.label_181.sizePolicy().hasHeightForWidth())
        self.label_181.setSizePolicy(sizePolicy2)
        self.label_181.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.label_181, 0, 0, 1, 1)

        self.db_ssa2_y_set = QDoubleSpinBox(self.groupBox_19)
        self.db_ssa2_y_set.setObjectName(u"db_ssa2_y_set")
        self.db_ssa2_y_set.setDecimals(3)
        self.db_ssa2_y_set.setValue(0.500000000000000)

        self.gridLayout_30.addWidget(self.db_ssa2_y_set, 1, 0, 1, 1)

        self.db_ssa2_y = QDoubleSpinBox(self.groupBox_19)
        self.db_ssa2_y.setObjectName(u"db_ssa2_y")
        sizePolicy2.setHeightForWidth(self.db_ssa2_y.sizePolicy().hasHeightForWidth())
        self.db_ssa2_y.setSizePolicy(sizePolicy2)
        self.db_ssa2_y.setReadOnly(True)
        self.db_ssa2_y.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_ssa2_y.setDecimals(3)
        self.db_ssa2_y.setMinimum(-0.100000000000000)
        self.db_ssa2_y.setMaximum(4.000000000000000)
        self.db_ssa2_y.setValue(0.050000000000000)

        self.gridLayout_30.addWidget(self.db_ssa2_y, 2, 0, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_30, 0, 2, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_31, 1, 2, 1, 2)

        self.pb_move_ssa2 = QPushButton(self.groupBox_19)
        self.pb_move_ssa2.setObjectName(u"pb_move_ssa2")

        self.gridLayout_32.addWidget(self.pb_move_ssa2, 2, 2, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_127 = QLabel(self.groupBox_19)
        self.label_127.setObjectName(u"label_127")
        sizePolicy2.setHeightForWidth(self.label_127.sizePolicy().hasHeightForWidth())
        self.label_127.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.label_127)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_186 = QLabel(self.groupBox_19)
        self.label_186.setObjectName(u"label_186")
        sizePolicy2.setHeightForWidth(self.label_186.sizePolicy().hasHeightForWidth())
        self.label_186.setSizePolicy(sizePolicy2)
        self.label_186.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_186)

        self.db_ssa2_hcen_rbv = QDoubleSpinBox(self.groupBox_19)
        self.db_ssa2_hcen_rbv.setObjectName(u"db_ssa2_hcen_rbv")
        sizePolicy2.setHeightForWidth(self.db_ssa2_hcen_rbv.sizePolicy().hasHeightForWidth())
        self.db_ssa2_hcen_rbv.setSizePolicy(sizePolicy2)
        self.db_ssa2_hcen_rbv.setReadOnly(True)
        self.db_ssa2_hcen_rbv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_ssa2_hcen_rbv.setDecimals(3)
        self.db_ssa2_hcen_rbv.setMinimum(-0.100000000000000)
        self.db_ssa2_hcen_rbv.setMaximum(4.000000000000000)
        self.db_ssa2_hcen_rbv.setValue(0.050000000000000)

        self.horizontalLayout_18.addWidget(self.db_ssa2_hcen_rbv)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_187 = QLabel(self.groupBox_19)
        self.label_187.setObjectName(u"label_187")
        sizePolicy2.setHeightForWidth(self.label_187.sizePolicy().hasHeightForWidth())
        self.label_187.setSizePolicy(sizePolicy2)
        self.label_187.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_187)

        self.db_ssa2_vcen_rbv = QDoubleSpinBox(self.groupBox_19)
        self.db_ssa2_vcen_rbv.setObjectName(u"db_ssa2_vcen_rbv")
        sizePolicy2.setHeightForWidth(self.db_ssa2_vcen_rbv.sizePolicy().hasHeightForWidth())
        self.db_ssa2_vcen_rbv.setSizePolicy(sizePolicy2)
        self.db_ssa2_vcen_rbv.setReadOnly(True)
        self.db_ssa2_vcen_rbv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_ssa2_vcen_rbv.setDecimals(3)
        self.db_ssa2_vcen_rbv.setMinimum(-0.100000000000000)
        self.db_ssa2_vcen_rbv.setMaximum(4.000000000000000)
        self.db_ssa2_vcen_rbv.setValue(0.050000000000000)

        self.horizontalLayout_24.addWidget(self.db_ssa2_vcen_rbv)


        self.verticalLayout_2.addLayout(self.horizontalLayout_24)


        self.gridLayout_32.addLayout(self.verticalLayout_2, 3, 1, 1, 2)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_128 = QLabel(self.groupBox_19)
        self.label_128.setObjectName(u"label_128")
        sizePolicy2.setHeightForWidth(self.label_128.sizePolicy().hasHeightForWidth())
        self.label_128.setSizePolicy(sizePolicy2)

        self.verticalLayout_27.addWidget(self.label_128)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pb_ssa2_hcen_move_neg = QPushButton(self.groupBox_19)
        self.pb_ssa2_hcen_move_neg.setObjectName(u"pb_ssa2_hcen_move_neg")
        sizePolicy2.setHeightForWidth(self.pb_ssa2_hcen_move_neg.sizePolicy().hasHeightForWidth())
        self.pb_ssa2_hcen_move_neg.setSizePolicy(sizePolicy2)

        self.horizontalLayout_25.addWidget(self.pb_ssa2_hcen_move_neg)

        self.db_ssa2_hcen_move = QDoubleSpinBox(self.groupBox_19)
        self.db_ssa2_hcen_move.setObjectName(u"db_ssa2_hcen_move")
        self.db_ssa2_hcen_move.setDecimals(3)
        self.db_ssa2_hcen_move.setValue(0.500000000000000)

        self.horizontalLayout_25.addWidget(self.db_ssa2_hcen_move)

        self.pb_ssa2_hcen_move_positive = QPushButton(self.groupBox_19)
        self.pb_ssa2_hcen_move_positive.setObjectName(u"pb_ssa2_hcen_move_positive")
        sizePolicy2.setHeightForWidth(self.pb_ssa2_hcen_move_positive.sizePolicy().hasHeightForWidth())
        self.pb_ssa2_hcen_move_positive.setSizePolicy(sizePolicy2)

        self.horizontalLayout_25.addWidget(self.pb_ssa2_hcen_move_positive)


        self.verticalLayout_27.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pb_ssa2_vcen_move_neg = QPushButton(self.groupBox_19)
        self.pb_ssa2_vcen_move_neg.setObjectName(u"pb_ssa2_vcen_move_neg")
        sizePolicy2.setHeightForWidth(self.pb_ssa2_vcen_move_neg.sizePolicy().hasHeightForWidth())
        self.pb_ssa2_vcen_move_neg.setSizePolicy(sizePolicy2)

        self.horizontalLayout_26.addWidget(self.pb_ssa2_vcen_move_neg)

        self.db_ssa2_vcen_move = QDoubleSpinBox(self.groupBox_19)
        self.db_ssa2_vcen_move.setObjectName(u"db_ssa2_vcen_move")
        self.db_ssa2_vcen_move.setDecimals(3)
        self.db_ssa2_vcen_move.setValue(0.500000000000000)

        self.horizontalLayout_26.addWidget(self.db_ssa2_vcen_move)

        self.pb_ssa2_vcen_move_positive = QPushButton(self.groupBox_19)
        self.pb_ssa2_vcen_move_positive.setObjectName(u"pb_ssa2_vcen_move_positive")
        sizePolicy2.setHeightForWidth(self.pb_ssa2_vcen_move_positive.sizePolicy().hasHeightForWidth())
        self.pb_ssa2_vcen_move_positive.setSizePolicy(sizePolicy2)

        self.horizontalLayout_26.addWidget(self.pb_ssa2_vcen_move_positive)


        self.verticalLayout_27.addLayout(self.horizontalLayout_26)


        self.gridLayout_32.addLayout(self.verticalLayout_27, 3, 3, 1, 1)

        self.pb_center_ssa2 = QPushButton(self.groupBox_19)
        self.pb_center_ssa2.setObjectName(u"pb_center_ssa2")

        self.gridLayout_32.addWidget(self.pb_center_ssa2, 4, 1, 1, 3)


        self.gridLayout_81.addWidget(self.groupBox_19, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_11, "")

        self.gridLayout_115.addWidget(self.tabWidget_2, 1, 0, 1, 2)

        self.HXN_GUI_tabs.addTab(self.alignment_tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_58 = QGridLayout(self.tab_3)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.pte_log = QPlainTextEdit(self.tab_3)
        self.pte_log.setObjectName(u"pte_log")

        self.gridLayout_58.addWidget(self.pte_log, 0, 0, 1, 1)

        self.HXN_GUI_tabs.addTab(self.tab_3, "")
        self.energy = QWidget()
        self.energy.setObjectName(u"energy")
        self.gridLayout_107 = QGridLayout(self.energy)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.gridLayout_86 = QGridLayout()
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.groupBox_23 = QGroupBox(self.energy)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy2.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy2)
        self.groupBox_23.setStyleSheet(u"")
        self.groupBox_23.setFlat(False)
        self.groupBox_23.setCheckable(False)
        self.gridLayout_71 = QGridLayout(self.groupBox_23)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_80 = QGridLayout()
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.gridLayout_76 = QGridLayout()
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.label_72 = QLabel(self.groupBox_23)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_76.addWidget(self.label_72, 0, 0, 1, 1)

        self.label_75 = QLabel(self.groupBox_23)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_76.addWidget(self.label_75, 1, 0, 1, 1)

        self.gridLayout_74 = QGridLayout()
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.pb_CAM6_OUT = QPushButton(self.groupBox_23)
        self.pb_CAM6_OUT.setObjectName(u"pb_CAM6_OUT")
        sizePolicy.setHeightForWidth(self.pb_CAM6_OUT.sizePolicy().hasHeightForWidth())
        self.pb_CAM6_OUT.setSizePolicy(sizePolicy)

        self.gridLayout_74.addWidget(self.pb_CAM6_OUT, 2, 1, 1, 1)

        self.pb_FS_OUT = QPushButton(self.groupBox_23)
        self.pb_FS_OUT.setObjectName(u"pb_FS_OUT")
        sizePolicy.setHeightForWidth(self.pb_FS_OUT.sizePolicy().hasHeightForWidth())
        self.pb_FS_OUT.setSizePolicy(sizePolicy)

        self.gridLayout_74.addWidget(self.pb_FS_OUT, 0, 1, 1, 1)

        self.pb_FS_IN = QPushButton(self.groupBox_23)
        self.pb_FS_IN.setObjectName(u"pb_FS_IN")
        sizePolicy.setHeightForWidth(self.pb_FS_IN.sizePolicy().hasHeightForWidth())
        self.pb_FS_IN.setSizePolicy(sizePolicy)

        self.gridLayout_74.addWidget(self.pb_FS_IN, 0, 0, 1, 1)

        self.pb_CAM6_IN = QPushButton(self.groupBox_23)
        self.pb_CAM6_IN.setObjectName(u"pb_CAM6_IN")
        sizePolicy.setHeightForWidth(self.pb_CAM6_IN.sizePolicy().hasHeightForWidth())
        self.pb_CAM6_IN.setSizePolicy(sizePolicy)

        self.gridLayout_74.addWidget(self.pb_CAM6_IN, 2, 0, 1, 1)


        self.gridLayout_76.addLayout(self.gridLayout_74, 0, 1, 2, 1)

        self.pb_CAM6_LASER = QPushButton(self.groupBox_23)
        self.pb_CAM6_LASER.setObjectName(u"pb_CAM6_LASER")

        self.gridLayout_76.addWidget(self.pb_CAM6_LASER, 2, 1, 1, 1)


        self.gridLayout_80.addLayout(self.gridLayout_76, 1, 0, 1, 1)


        self.gridLayout_71.addLayout(self.gridLayout_80, 1, 0, 1, 2)

        self.label_133 = QLabel(self.groupBox_23)
        self.label_133.setObjectName(u"label_133")
        sizePolicy2.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy2)

        self.gridLayout_71.addWidget(self.label_133, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.db_fs = QDoubleSpinBox(self.groupBox_23)
        self.db_fs.setObjectName(u"db_fs")
        sizePolicy.setHeightForWidth(self.db_fs.sizePolicy().hasHeightForWidth())
        self.db_fs.setSizePolicy(sizePolicy)
        self.db_fs.setReadOnly(True)
        self.db_fs.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_fs.setDecimals(1)
        self.db_fs.setMinimum(-100.000000000000000)
        self.db_fs.setMaximum(100.000000000000000)
        self.db_fs.setValue(1.000000000000000)

        self.verticalLayout_5.addWidget(self.db_fs)

        self.db_cam6 = QDoubleSpinBox(self.groupBox_23)
        self.db_cam6.setObjectName(u"db_cam6")
        sizePolicy.setHeightForWidth(self.db_cam6.sizePolicy().hasHeightForWidth())
        self.db_cam6.setSizePolicy(sizePolicy)
        self.db_cam6.setReadOnly(True)
        self.db_cam6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_cam6.setDecimals(1)
        self.db_cam6.setMinimum(-100.000000000000000)
        self.db_cam6.setMaximum(100.000000000000000)
        self.db_cam6.setValue(1.000000000000000)

        self.verticalLayout_5.addWidget(self.db_cam6)


        self.gridLayout_71.addLayout(self.verticalLayout_5, 1, 3, 1, 1)


        self.gridLayout_86.addWidget(self.groupBox_23, 0, 0, 1, 1)

        self.groupBox_33 = QGroupBox(self.energy)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.pushButton_2 = QPushButton(self.groupBox_33)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(8, 33, 210, 59))
        self.label_153 = QLabel(self.groupBox_33)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setGeometry(QRect(8, 8, 16, 19))

        self.gridLayout_86.addWidget(self.groupBox_33, 1, 0, 1, 1)


        self.gridLayout_107.addLayout(self.gridLayout_86, 0, 0, 1, 1)

        self.groupBox_32 = QGroupBox(self.energy)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.gridLayout_99 = QGridLayout(self.groupBox_32)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.label_46 = QLabel(self.groupBox_32)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_99.addWidget(self.label_46, 0, 0, 1, 1)

        self.label_81 = QLabel(self.groupBox_32)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_99.addWidget(self.label_81, 1, 0, 1, 1)

        self.dsb_target_e = QDoubleSpinBox(self.groupBox_32)
        self.dsb_target_e.setObjectName(u"dsb_target_e")
        self.dsb_target_e.setStyleSheet(u"font: 14pt \"Cantarell\";")
        self.dsb_target_e.setDecimals(2)
        self.dsb_target_e.setMinimum(5.000000000000000)
        self.dsb_target_e.setMaximum(25.000000000000000)
        self.dsb_target_e.setSingleStep(0.500000000000000)
        self.dsb_target_e.setValue(12.000000000000000)

        self.gridLayout_99.addWidget(self.dsb_target_e, 1, 1, 1, 1)

        self.groupBox_31 = QGroupBox(self.groupBox_32)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.gridLayout_114 = QGridLayout(self.groupBox_31)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_114.addItem(self.verticalSpacer_19, 0, 0, 1, 1)

        self.gridLayout_113 = QGridLayout()
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.label_150 = QLabel(self.groupBox_31)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_113.addWidget(self.label_150, 3, 0, 1, 1)

        self.cb_target_coating = QComboBox(self.groupBox_31)
        self.cb_target_coating.addItem("")
        self.cb_target_coating.addItem("")
        self.cb_target_coating.addItem("")
        self.cb_target_coating.addItem("")
        self.cb_target_coating.setObjectName(u"cb_target_coating")

        self.gridLayout_113.addWidget(self.cb_target_coating, 2, 1, 1, 1)

        self.dsb_target_roll = QDoubleSpinBox(self.groupBox_31)
        self.dsb_target_roll.setObjectName(u"dsb_target_roll")
        self.dsb_target_roll.setDecimals(4)
        self.dsb_target_roll.setMinimum(-9.000000000000000)
        self.dsb_target_roll.setMaximum(9.000000000000000)
        self.dsb_target_roll.setSingleStep(0.100000000000000)
        self.dsb_target_roll.setValue(0.200000000000000)

        self.gridLayout_113.addWidget(self.dsb_target_roll, 0, 1, 1, 1)

        self.sb_calc_harmonic = QSpinBox(self.groupBox_31)
        self.sb_calc_harmonic.setObjectName(u"sb_calc_harmonic")
        self.sb_calc_harmonic.setMinimum(-1)
        self.sb_calc_harmonic.setSingleStep(2)
        self.sb_calc_harmonic.setValue(-1)

        self.gridLayout_113.addWidget(self.sb_calc_harmonic, 3, 1, 1, 1)

        self.label_146 = QLabel(self.groupBox_31)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_113.addWidget(self.label_146, 2, 0, 1, 1)

        self.label_154 = QLabel(self.groupBox_31)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_113.addWidget(self.label_154, 0, 0, 1, 1)

        self.label_155 = QLabel(self.groupBox_31)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_113.addWidget(self.label_155, 1, 0, 1, 1)

        self.dsb_hfm_target_pitch = QDoubleSpinBox(self.groupBox_31)
        self.dsb_hfm_target_pitch.setObjectName(u"dsb_hfm_target_pitch")
        self.dsb_hfm_target_pitch.setDecimals(4)
        self.dsb_hfm_target_pitch.setMinimum(-9.000000000000000)
        self.dsb_hfm_target_pitch.setMaximum(9.000000000000000)
        self.dsb_hfm_target_pitch.setSingleStep(0.100000000000000)
        self.dsb_hfm_target_pitch.setValue(1.200000000000000)

        self.gridLayout_113.addWidget(self.dsb_hfm_target_pitch, 1, 1, 1, 1)


        self.gridLayout_114.addLayout(self.gridLayout_113, 3, 0, 1, 1)

        self.gridLayout_112 = QGridLayout()
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.label_149 = QLabel(self.groupBox_31)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_112.addWidget(self.label_149, 0, 0, 1, 1)

        self.dsb_target_ugap = QDoubleSpinBox(self.groupBox_31)
        self.dsb_target_ugap.setObjectName(u"dsb_target_ugap")
        self.dsb_target_ugap.setDecimals(1)
        self.dsb_target_ugap.setMinimum(4000.000000000000000)
        self.dsb_target_ugap.setMaximum(25000.000000000000000)
        self.dsb_target_ugap.setSingleStep(5.000000000000000)
        self.dsb_target_ugap.setValue(5920.000000000000000)

        self.gridLayout_112.addWidget(self.dsb_target_ugap, 0, 1, 1, 1)


        self.gridLayout_114.addLayout(self.gridLayout_112, 1, 0, 1, 1)

        self.gridLayout_109 = QGridLayout()
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.label_132 = QLabel(self.groupBox_31)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_109.addWidget(self.label_132, 0, 0, 1, 1)

        self.dsb_target_pitch = QDoubleSpinBox(self.groupBox_31)
        self.dsb_target_pitch.setObjectName(u"dsb_target_pitch")
        self.dsb_target_pitch.setDecimals(4)
        self.dsb_target_pitch.setMinimum(-5.000000000000000)
        self.dsb_target_pitch.setMaximum(5.000000000000000)
        self.dsb_target_pitch.setSingleStep(0.005000000000000)
        self.dsb_target_pitch.setValue(0.960500000000000)

        self.gridLayout_109.addWidget(self.dsb_target_pitch, 0, 1, 1, 1)


        self.gridLayout_114.addLayout(self.gridLayout_109, 2, 0, 1, 1)


        self.gridLayout_99.addWidget(self.groupBox_31, 1, 2, 5, 1)

        self.label_148 = QLabel(self.groupBox_32)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_99.addWidget(self.label_148, 2, 0, 1, 1)

        self.sb_harmonic = QSpinBox(self.groupBox_32)
        self.sb_harmonic.setObjectName(u"sb_harmonic")
        self.sb_harmonic.setMinimum(-1)
        self.sb_harmonic.setSingleStep(2)
        self.sb_harmonic.setValue(-1)

        self.gridLayout_99.addWidget(self.sb_harmonic, 2, 1, 1, 1)

        self.cb_change_energy_only = QCheckBox(self.groupBox_32)
        self.cb_change_energy_only.setObjectName(u"cb_change_energy_only")
        self.cb_change_energy_only.setChecked(False)

        self.gridLayout_99.addWidget(self.cb_change_energy_only, 3, 1, 1, 1)

        self.pb_move_energy = QPushButton(self.groupBox_32)
        self.pb_move_energy.setObjectName(u"pb_move_energy")
        self.pb_move_energy.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.pb_move_energy.sizePolicy().hasHeightForWidth())
        self.pb_move_energy.setSizePolicy(sizePolicy9)

        self.gridLayout_99.addWidget(self.pb_move_energy, 4, 0, 1, 2)

        self.groupBox4 = QGroupBox(self.groupBox_32)
        self.groupBox4.setObjectName(u"groupBox4")
        self.gridLayout_96 = QGridLayout(self.groupBox4)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.label_70 = QLabel(self.groupBox4)
        self.label_70.setObjectName(u"label_70")
        sizePolicy1.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy1)
        self.label_70.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_96.addWidget(self.label_70, 1, 0, 1, 1)

        self.pb_energy_change_w_sid = QPushButton(self.groupBox4)
        self.pb_energy_change_w_sid.setObjectName(u"pb_energy_change_w_sid")

        self.gridLayout_96.addWidget(self.pb_energy_change_w_sid, 1, 2, 1, 1)

        self.sb_energy_sid = QSpinBox(self.groupBox4)
        self.sb_energy_sid.setObjectName(u"sb_energy_sid")
        self.sb_energy_sid.setMinimum(-9999999)
        self.sb_energy_sid.setMaximum(9999999)
        self.sb_energy_sid.setSingleStep(10)
        self.sb_energy_sid.setValue(0)

        self.gridLayout_96.addWidget(self.sb_energy_sid, 1, 1, 1, 1)


        self.gridLayout_99.addWidget(self.groupBox4, 6, 0, 1, 2)

        self.gridLayout_106 = QGridLayout()
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.label_178 = QLabel(self.groupBox_32)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_106.addWidget(self.label_178, 1, 1, 1, 1)

        self.dsb_ZPZ1TargetPos_energy = QDoubleSpinBox(self.groupBox_32)
        self.dsb_ZPZ1TargetPos_energy.setObjectName(u"dsb_ZPZ1TargetPos_energy")
        sizePolicy2.setHeightForWidth(self.dsb_ZPZ1TargetPos_energy.sizePolicy().hasHeightForWidth())
        self.dsb_ZPZ1TargetPos_energy.setSizePolicy(sizePolicy2)
        self.dsb_ZPZ1TargetPos_energy.setDecimals(4)
        self.dsb_ZPZ1TargetPos_energy.setMinimum(-100.000000000000000)
        self.dsb_ZPZ1TargetPos_energy.setMaximum(20.000000000000000)
        self.dsb_ZPZ1TargetPos_energy.setValue(-15.000000000000000)

        self.gridLayout_106.addWidget(self.dsb_ZPZ1TargetPos_energy, 1, 2, 1, 1)

        self.pb_movezpz1_energy = QPushButton(self.groupBox_32)
        self.pb_movezpz1_energy.setObjectName(u"pb_movezpz1_energy")

        self.gridLayout_106.addWidget(self.pb_movezpz1_energy, 2, 2, 1, 1)


        self.gridLayout_99.addLayout(self.gridLayout_106, 6, 2, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox_32)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_116 = QGridLayout(self.groupBox_9)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.sb_max_iter = QSpinBox(self.groupBox_9)
        self.sb_max_iter.setObjectName(u"sb_max_iter")
        self.sb_max_iter.setMinimum(1)

        self.gridLayout_116.addWidget(self.sb_max_iter, 2, 1, 1, 1)

        self.label_151 = QLabel(self.groupBox_9)
        self.label_151.setObjectName(u"label_151")

        self.gridLayout_116.addWidget(self.label_151, 2, 0, 1, 1)

        self.cb_beam_at_ssa2 = QCheckBox(self.groupBox_9)
        self.cb_beam_at_ssa2.setObjectName(u"cb_beam_at_ssa2")
        self.cb_beam_at_ssa2.setChecked(False)

        self.gridLayout_116.addWidget(self.cb_beam_at_ssa2, 1, 0, 1, 2)

        self.label_152 = QLabel(self.groupBox_9)
        self.label_152.setObjectName(u"label_152")

        self.gridLayout_116.addWidget(self.label_152, 0, 0, 1, 1)


        self.gridLayout_99.addWidget(self.groupBox_9, 5, 0, 1, 2)


        self.gridLayout_107.addWidget(self.groupBox_32, 0, 1, 1, 1)

        self.gb_calib_foil = QGroupBox(self.energy)
        self.gb_calib_foil.setObjectName(u"gb_calib_foil")

        self.gridLayout_107.addWidget(self.gb_calib_foil, 1, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 795, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_107.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.HXN_GUI_tabs.addTab(self.energy, "")
        self.beamline_contacts_tab = QWidget()
        self.beamline_contacts_tab.setObjectName(u"beamline_contacts_tab")
        self.gridLayout_77 = QGridLayout(self.beamline_contacts_tab)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.tw_hxn_contact = QTableWidget(self.beamline_contacts_tab)
        if (self.tw_hxn_contact.columnCount() < 3):
            self.tw_hxn_contact.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_hxn_contact.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_hxn_contact.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_hxn_contact.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tw_hxn_contact.rowCount() < 5):
            self.tw_hxn_contact.setRowCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_hxn_contact.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_hxn_contact.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_hxn_contact.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_hxn_contact.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_hxn_contact.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(2, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(3, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(4, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(4, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tw_hxn_contact.setItem(4, 2, __qtablewidgetitem21)
        self.tw_hxn_contact.setObjectName(u"tw_hxn_contact")
        self.tw_hxn_contact.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.tw_hxn_contact.sizePolicy().hasHeightForWidth())
        self.tw_hxn_contact.setSizePolicy(sizePolicy6)
        self.tw_hxn_contact.setMinimumSize(QSize(500, 500))
        self.tw_hxn_contact.setAcceptDrops(False)
        self.tw_hxn_contact.setLayoutDirection(Qt.LeftToRight)
        self.tw_hxn_contact.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_hxn_contact.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_hxn_contact.horizontalHeader().setDefaultSectionSize(200)

        self.gridLayout_77.addWidget(self.tw_hxn_contact, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(571, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_77.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 853, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_77.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.HXN_GUI_tabs.addTab(self.beamline_contacts_tab, "")

        self.gridLayout_53.addWidget(self.HXN_GUI_tabs, 3, 1, 1, 1)


        self.gridLayout_98.addLayout(self.gridLayout_53, 2, 0, 1, 1)

        window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1334, 30))
        self.menuHelp_2 = QMenu(self.menubar)
        self.menuHelp_2.setObjectName(u"menuHelp_2")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(window)
        self.statusbar.setObjectName(u"statusbar")
        window.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.cb_dets, self.cb_motor1)
        QWidget.setTabOrder(self.cb_motor1, self.cb_motor2)
        QWidget.setTabOrder(self.cb_motor2, self.x_start)
        QWidget.setTabOrder(self.x_start, self.x_end)
        QWidget.setTabOrder(self.x_end, self.x_step)
        QWidget.setTabOrder(self.x_step, self.y_start)
        QWidget.setTabOrder(self.y_start, self.y_end)
        QWidget.setTabOrder(self.y_end, self.y_step)
        QWidget.setTabOrder(self.y_step, self.dwell)
        QWidget.setTabOrder(self.dwell, self.pb_open_b_shutter)
        QWidget.setTabOrder(self.pb_open_b_shutter, self.le_image_path)
        QWidget.setTabOrder(self.le_image_path, self.pb_close_b_shutter)
        QWidget.setTabOrder(self.pb_close_b_shutter, self.pb_open_c_shutter)
        QWidget.setTabOrder(self.pb_open_c_shutter, self.pb_close_c_shutter)
        QWidget.setTabOrder(self.pb_close_c_shutter, self.pb_scan_copy)
        QWidget.setTabOrder(self.pb_scan_copy, self.pb_batchscan_copy)
        QWidget.setTabOrder(self.pb_batchscan_copy, self.pb_cam6IN)
        QWidget.setTabOrder(self.pb_cam6IN, self.pb_cam6OUT)
        QWidget.setTabOrder(self.pb_cam6OUT, self.pb_vortexIN)
        QWidget.setTabOrder(self.pb_vortexIN, self.pb_vortexOUT)
        QWidget.setTabOrder(self.pb_vortexOUT, self.pb_dexela_IN)
        QWidget.setTabOrder(self.pb_dexela_IN, self.pb_dexela_OUT)
        QWidget.setTabOrder(self.pb_dexela_OUT, self.pb_cam11IN)
        QWidget.setTabOrder(self.pb_cam11IN, self.pb_telescope)
        QWidget.setTabOrder(self.pb_telescope, self.pb_merlinIN)
        QWidget.setTabOrder(self.pb_merlinIN, self.pb_merlinOUT)
        QWidget.setTabOrder(self.pb_merlinOUT, self.sp_dexela_xpixel)
        QWidget.setTabOrder(self.sp_dexela_xpixel, self.sp_dexela_ypixel)
        QWidget.setTabOrder(self.sp_dexela_ypixel, self.pb_pos_to_angle)
        QWidget.setTabOrder(self.pb_pos_to_angle, self.sp_diff_det_calc_x)
        QWidget.setTabOrder(self.sp_diff_det_calc_x, self.sp_diff_det_calc_y)
        QWidget.setTabOrder(self.sp_diff_det_calc_y, self.sp_diff_det_calc_2theta)
        QWidget.setTabOrder(self.sp_diff_det_calc_2theta, self.sp_diff_det_r)
        QWidget.setTabOrder(self.sp_diff_det_r, self.pb_move_diff)
        QWidget.setTabOrder(self.pb_move_diff, self.pb_abort_diff)
        QWidget.setTabOrder(self.pb_abort_diff, self.pb_copy_pos2angle)
        QWidget.setTabOrder(self.pb_copy_pos2angle, self.pb_move_dsx_neg)
        QWidget.setTabOrder(self.pb_move_dsx_neg, self.db_move_dsx)
        QWidget.setTabOrder(self.db_move_dsx, self.pb_move_dsx_pos)
        QWidget.setTabOrder(self.pb_move_dsx_pos, self.pb_move_dsy_neg)
        QWidget.setTabOrder(self.pb_move_dsy_neg, self.db_move_dsy)
        QWidget.setTabOrder(self.db_move_dsy, self.pb_move_dsy_pos)
        QWidget.setTabOrder(self.pb_move_dsy_pos, self.pb_move_dsz_neg)
        QWidget.setTabOrder(self.pb_move_dsz_neg, self.db_move_dsz)
        QWidget.setTabOrder(self.db_move_dsz, self.pb_move_dsz_pos)
        QWidget.setTabOrder(self.pb_move_dsz_pos, self.pb_move_dth_pos_neg)
        QWidget.setTabOrder(self.pb_move_dth_pos_neg, self.db_move_dsth)
        QWidget.setTabOrder(self.db_move_dsth, self.pb_move_dth_pos)
        QWidget.setTabOrder(self.pb_move_dth_pos, self.pb_move_sbz_neg)
        QWidget.setTabOrder(self.pb_move_sbz_neg, self.db_move_sbz)
        QWidget.setTabOrder(self.db_move_sbz, self.pb_move_sbz_pos)
        QWidget.setTabOrder(self.pb_move_sbz_pos, self.pb_move_smarx_neg)
        QWidget.setTabOrder(self.pb_move_smarx_neg, self.db_move_smarx)
        QWidget.setTabOrder(self.db_move_smarx, self.pb_move_smarx_pos)
        QWidget.setTabOrder(self.pb_move_smarx_pos, self.pb_move_smary_neg)
        QWidget.setTabOrder(self.pb_move_smary_neg, self.db_move_smary)
        QWidget.setTabOrder(self.db_move_smary, self.pb_move_smary_pos)
        QWidget.setTabOrder(self.pb_move_smary_pos, self.pb_move_smarz_neg)
        QWidget.setTabOrder(self.pb_move_smarz_neg, self.db_move_smarz)
        QWidget.setTabOrder(self.db_move_smarz, self.pb_move_smarz_pos)
        QWidget.setTabOrder(self.pb_move_smarz_pos, self.pb_move_zpsth_pos_neg)
        QWidget.setTabOrder(self.pb_move_zpsth_pos_neg, self.db_move_zpsth)
        QWidget.setTabOrder(self.db_move_zpsth, self.pb_move_zpsth_pos)
        QWidget.setTabOrder(self.pb_move_zpsth_pos, self.pb_move_zpz_neg)
        QWidget.setTabOrder(self.pb_move_zpz_neg, self.db_move_zpz)
        QWidget.setTabOrder(self.db_move_zpz, self.pb_move_zpz_pos)
        QWidget.setTabOrder(self.pb_move_zpz_pos, self.pb_recover_scan_pos_zp)
        QWidget.setTabOrder(self.pb_recover_scan_pos_zp, self.cb_sid_moveZPZ)
        QWidget.setTabOrder(self.cb_sid_moveZPZ, self.pb_show_scan_pos_zp)
        QWidget.setTabOrder(self.pb_show_scan_pos_zp, self.pb_print_scan_meta_zp)
        QWidget.setTabOrder(self.pb_print_scan_meta_zp, self.pb_save_pos_zp)
        QWidget.setTabOrder(self.pb_save_pos_zp, self.pb_move_pos_zp)
        QWidget.setTabOrder(self.pb_move_pos_zp, self.pb_copy_curr_pos_zp)
        QWidget.setTabOrder(self.pb_copy_curr_pos_zp, self.zp_sample_roi_list_widget)
        QWidget.setTabOrder(self.zp_sample_roi_list_widget, self.pb_roiList_export_zp)
        QWidget.setTabOrder(self.pb_roiList_export_zp, self.pb_roiList_import_zp)
        QWidget.setTabOrder(self.pb_roiList_import_zp, self.pb_roiList_clear_zp)
        QWidget.setTabOrder(self.pb_roiList_clear_zp, self.pb_roiList_clear_sel_zp)
        QWidget.setTabOrder(self.pb_roiList_clear_sel_zp, self.db_smarx)
        QWidget.setTabOrder(self.db_smarx, self.start)
        QWidget.setTabOrder(self.start, self.db_smary)
        QWidget.setTabOrder(self.db_smary, self.db_smarz)
        QWidget.setTabOrder(self.db_smarz, self.pb_3030)
        QWidget.setTabOrder(self.pb_3030, self.db_zpz1)
        QWidget.setTabOrder(self.db_zpz1, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.rb_2d)
        QWidget.setTabOrder(self.rb_2d, self.le_sid_position_zp)
        QWidget.setTabOrder(self.le_sid_position_zp, self.pb_22)
        QWidget.setTabOrder(self.pb_22, self.pb_66)
        QWidget.setTabOrder(self.pb_66, self.pb_2020)
        QWidget.setTabOrder(self.pb_2020, self.pb_zp_stop_all_sample)
        QWidget.setTabOrder(self.pb_zp_stop_all_sample, self.text_scan_plan)
        QWidget.setTabOrder(self.text_scan_plan, self.le_experimenters)
        QWidget.setTabOrder(self.le_experimenters, self.db_zpsth)
        QWidget.setTabOrder(self.db_zpsth, self.rb_1d)
        QWidget.setTabOrder(self.rb_1d, self.lcd_monoE)
        QWidget.setTabOrder(self.lcd_monoE, self.le_pdf_name)
        QWidget.setTabOrder(self.le_pdf_name, self.textEdit_2)
        QWidget.setTabOrder(self.textEdit_2, self.cb_elem_13)
        QWidget.setTabOrder(self.cb_elem_13, self.db_dsy)
        QWidget.setTabOrder(self.db_dsy, self.cb_elem_14)
        QWidget.setTabOrder(self.cb_elem_14, self.db_dsth)
        QWidget.setTabOrder(self.db_dsth, self.db_dsx)
        QWidget.setTabOrder(self.db_dsx, self.lcd_ic3)
        QWidget.setTabOrder(self.lcd_ic3, self.cb_elem_16)
        QWidget.setTabOrder(self.cb_elem_16, self.db_dsz)
        QWidget.setTabOrder(self.db_dsz, self.pb_insert_user_image)
        QWidget.setTabOrder(self.pb_insert_user_image, self.db_sbz)
        QWidget.setTabOrder(self.db_sbz, self.le_username)
        QWidget.setTabOrder(self.le_username, self.cb_elem_12)
        QWidget.setTabOrder(self.cb_elem_12, self.cb_elem_15)
        QWidget.setTabOrder(self.cb_elem_15, self.lcd_scanNumber)
        QWidget.setTabOrder(self.lcd_scanNumber, self.le_sample_name)
        QWidget.setTabOrder(self.le_sample_name, self.pb_mll_stop_all_sample)
        QWidget.setTabOrder(self.pb_mll_stop_all_sample, self.pb_move_pos_mll)
        QWidget.setTabOrder(self.pb_move_pos_mll, self.pb_save_pos_mll)
        QWidget.setTabOrder(self.pb_save_pos_mll, self.pb_copy_curr_pos_mll)
        QWidget.setTabOrder(self.pb_copy_curr_pos_mll, self.mll_sample_roi_list_widget)
        QWidget.setTabOrder(self.mll_sample_roi_list_widget, self.pb_roiList_clear_mll)
        QWidget.setTabOrder(self.pb_roiList_clear_mll, self.pb_roiList_export_mll)
        QWidget.setTabOrder(self.pb_roiList_export_mll, self.pb_roiList_import_mll)
        QWidget.setTabOrder(self.pb_roiList_import_mll, self.pb_roiList_clear_sel_mll)
        QWidget.setTabOrder(self.pb_roiList_clear_sel_mll, self.le_sid_position_mll)
        QWidget.setTabOrder(self.le_sid_position_mll, self.pb_recover_scan_pos_mll)
        QWidget.setTabOrder(self.pb_recover_scan_pos_mll, self.cb_sid_move_base_mll)
        QWidget.setTabOrder(self.cb_sid_move_base_mll, self.pb_print_scan_meta_mll)
        QWidget.setTabOrder(self.pb_print_scan_meta_mll, self.pb_show_scan_pos_mll)
        QWidget.setTabOrder(self.pb_show_scan_pos_mll, self.tabWidget_18)
        QWidget.setTabOrder(self.tabWidget_18, self.cb_elem_2)
        QWidget.setTabOrder(self.cb_elem_2, self.cb_elem_3)
        QWidget.setTabOrder(self.cb_elem_3, self.cb_elem_4)
        QWidget.setTabOrder(self.cb_elem_4, self.cb_elem_5)
        QWidget.setTabOrder(self.cb_elem_5, self.cb_elem_6)
        QWidget.setTabOrder(self.cb_elem_6, self.cb_elem_7)
        QWidget.setTabOrder(self.cb_elem_7, self.cb_elem_8)
        QWidget.setTabOrder(self.cb_elem_8, self.cb_elem_9)
        QWidget.setTabOrder(self.cb_elem_9, self.cb_elem_10)
        QWidget.setTabOrder(self.cb_elem_10, self.cb_elem_11)
        QWidget.setTabOrder(self.cb_elem_11, self.pb_stop_fluor)
        QWidget.setTabOrder(self.pb_stop_fluor, self.pb_stop_dexela)
        QWidget.setTabOrder(self.pb_stop_dexela, self.pb_stop_cam11)
        QWidget.setTabOrder(self.pb_stop_cam11, self.pb_stop_merlin)
        QWidget.setTabOrder(self.pb_stop_merlin, self.pb_update_xrf_elems)
        QWidget.setTabOrder(self.pb_update_xrf_elems, self.pb_export_xrf_elem_list)
        QWidget.setTabOrder(self.pb_export_xrf_elem_list, self.sb_live_elem_num)
        QWidget.setTabOrder(self.sb_live_elem_num, self.le_line_elem)
        QWidget.setTabOrder(self.le_line_elem, self.pb_import_xrf_elem_list)
        QWidget.setTabOrder(self.pb_import_xrf_elem_list, self.le_roi_elems)
        QWidget.setTabOrder(self.le_roi_elems, self.le_live_elems)
        QWidget.setTabOrder(self.le_live_elems, self.cb_elem_1)
        QWidget.setTabOrder(self.cb_elem_1, self.db_fs_det)
        QWidget.setTabOrder(self.db_fs_det, self.db_cam06x)
        QWidget.setTabOrder(self.db_cam06x, self.db_dexela)
        QWidget.setTabOrder(self.db_dexela, self.db_diffx)
        QWidget.setTabOrder(self.db_diffx, self.dsb_flur_in_pos)
        QWidget.setTabOrder(self.dsb_flur_in_pos, self.pb_cam11_disable_flatfield)
        QWidget.setTabOrder(self.pb_cam11_disable_flatfield, self.pb_cam11_flatfield)
        QWidget.setTabOrder(self.pb_cam11_flatfield, self.cb_dets_for_ff_corr)
        QWidget.setTabOrder(self.cb_dets_for_ff_corr, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.cb_det_names_for_pos)
        QWidget.setTabOrder(self.cb_det_names_for_pos, self.pb_update_dets_pos)
        QWidget.setTabOrder(self.pb_update_dets_pos, self.pb_merlin_filterIN)
        QWidget.setTabOrder(self.pb_merlin_filterIN, self.pb_merlin_filterOUT)
        QWidget.setTabOrder(self.pb_merlin_filterOUT, self.pb_light_OFF)
        QWidget.setTabOrder(self.pb_light_OFF, self.pb_light_ON)
        QWidget.setTabOrder(self.pb_light_ON, self.cb_plot_elem)
        QWidget.setTabOrder(self.cb_plot_elem, self.le_plot_sd)
        QWidget.setTabOrder(self.le_plot_sd, self.pb_erf_fit)
        QWidget.setTabOrder(self.pb_erf_fit, self.cb_erf_linear_flag)
        QWidget.setTabOrder(self.cb_erf_linear_flag, self.dsb_line_center_thre)
        QWidget.setTabOrder(self.dsb_line_center_thre, self.pb_plot_line_center)
        QWidget.setTabOrder(self.pb_plot_line_center, self.pb_plot)
        QWidget.setTabOrder(self.pb_plot, self.pb_close_all_plot)
        QWidget.setTabOrder(self.pb_close_all_plot, self.pb_open_mll_tomo_widget)
        QWidget.setTabOrder(self.pb_open_mll_tomo_widget, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.pb_start_pressure_live_plot)
        QWidget.setTabOrder(self.pb_start_pressure_live_plot, self.pressure_plot_canvas)
        QWidget.setTabOrder(self.pressure_plot_canvas, self.pb_stop_pressure_live_plot)
        QWidget.setTabOrder(self.pb_stop_pressure_live_plot, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.sample_ex_tabs)
        QWidget.setTabOrder(self.sample_ex_tabs, self.dsb_target_p)
        QWidget.setTabOrder(self.dsb_target_p, self.cb_sample_ex_cam11_in)
        QWidget.setTabOrder(self.cb_sample_ex_cam11_in, self.pb_start_pump)
        QWidget.setTabOrder(self.pb_start_pump, self.cb_he_backfill_bool)
        QWidget.setTabOrder(self.cb_he_backfill_bool, self.pb_start_vent)
        QWidget.setTabOrder(self.pb_start_vent, self.cb_sample_ex_det_out)
        QWidget.setTabOrder(self.cb_sample_ex_det_out, self.pb_open_fast_pumps)
        QWidget.setTabOrder(self.pb_open_fast_pumps, self.pb_stop_vent)
        QWidget.setTabOrder(self.pb_stop_vent, self.pb_auto_he_fill)
        QWidget.setTabOrder(self.pb_auto_he_fill, self.pb_stop_pump)
        QWidget.setTabOrder(self.pb_stop_pump, self.pb_open_he_valve)
        QWidget.setTabOrder(self.pb_open_he_valve, self.pb_close_he_valve)
        QWidget.setTabOrder(self.pb_close_he_valve, self.rb_he_backfill_fail)
        QWidget.setTabOrder(self.rb_he_backfill_fail, self.rb_fast_vent)
        QWidget.setTabOrder(self.rb_fast_vent, self.rb_pumpB_slow)
        QWidget.setTabOrder(self.rb_pumpB_slow, self.rb_pumpA_slow)
        QWidget.setTabOrder(self.rb_pumpA_slow, self.lcdPressure)
        QWidget.setTabOrder(self.lcdPressure, self.tabWidget_3)
        QWidget.setTabOrder(self.tabWidget_3, self.pb_zpbsy_out)
        QWidget.setTabOrder(self.pb_zpbsy_out, self.pb_osa_in)
        QWidget.setTabOrder(self.pb_osa_in, self.pb_osa_out)
        QWidget.setTabOrder(self.pb_osa_out, self.pb_zpbsy_in)
        QWidget.setTabOrder(self.pb_zpbsy_in, self.pb_zp_cam11_view)
        QWidget.setTabOrder(self.pb_zp_cam11_view, self.pb_zp_nanobeam)
        QWidget.setTabOrder(self.pb_zp_nanobeam, self.sb_ZPZ1RelativeStart)
        QWidget.setTabOrder(self.sb_ZPZ1RelativeStart, self.sb_ZPZ1RelativeEnd)
        QWidget.setTabOrder(self.sb_ZPZ1RelativeEnd, self.sb_ZPZ1Steps)
        QWidget.setTabOrder(self.sb_ZPZ1Steps, self.cb_foucsScanMotor)
        QWidget.setTabOrder(self.cb_foucsScanMotor, self.sb_FocusScanMtrStart)
        QWidget.setTabOrder(self.sb_FocusScanMtrStart, self.sb_FocusScanMtrEnd)
        QWidget.setTabOrder(self.sb_FocusScanMtrEnd, self.sb_FocusScanMtrStep)
        QWidget.setTabOrder(self.sb_FocusScanMtrStep, self.dsb_FocusScanDwell)
        QWidget.setTabOrder(self.dsb_FocusScanDwell, self.dsb_ZPZ1TargetPos)
        QWidget.setTabOrder(self.dsb_ZPZ1TargetPos, self.cb_linearFlag_zpFocus)
        QWidget.setTabOrder(self.cb_linearFlag_zpFocus, self.cb_zp_focus_elem)
        QWidget.setTabOrder(self.cb_zp_focus_elem, self.sb_zp_rot_angle_end)
        QWidget.setTabOrder(self.sb_zp_rot_angle_end, self.sb_zp_rot_angle_num)
        QWidget.setTabOrder(self.sb_zp_rot_angle_num, self.cb_zp_rot_elem)
        QWidget.setTabOrder(self.cb_zp_rot_elem, self.sb_zp_rot_scan_start)
        QWidget.setTabOrder(self.sb_zp_rot_scan_start, self.sb_zp_rot_scan_end)
        QWidget.setTabOrder(self.sb_zp_rot_scan_end, self.sb_zp_rot_scan_num)
        QWidget.setTabOrder(self.sb_zp_rot_scan_num, self.pb_zp_rot_align_start)
        QWidget.setTabOrder(self.pb_zp_rot_align_start, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.dsb_rot_align_zpsth)
        QWidget.setTabOrder(self.dsb_rot_align_zpsth, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.dsb_rot_align_smarx)
        QWidget.setTabOrder(self.dsb_rot_align_smarx, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.dsb_rot_align_smarz)
        QWidget.setTabOrder(self.dsb_rot_align_smarz, self.sb_mll_rot_angle_start)
        QWidget.setTabOrder(self.sb_mll_rot_angle_start, self.sb_mll_rot_angle_end)
        QWidget.setTabOrder(self.sb_mll_rot_angle_end, self.sb_mll_rot_angle_num)
        QWidget.setTabOrder(self.sb_mll_rot_angle_num, self.cb_mll_rot_elem)
        QWidget.setTabOrder(self.cb_mll_rot_elem, self.dsb_rot_align_dsth)
        QWidget.setTabOrder(self.dsb_rot_align_dsth, self.dsb_rot_align_dsx)
        QWidget.setTabOrder(self.dsb_rot_align_dsx, self.dsb_rot_align_dsz)
        QWidget.setTabOrder(self.dsb_rot_align_dsz, self.cb_mll_foucs_mtr)
        QWidget.setTabOrder(self.cb_mll_foucs_mtr, self.dsb_mll_foucs_mtr_start)
        QWidget.setTabOrder(self.dsb_mll_foucs_mtr_start, self.dsb_mll_foucs_mtr_end)
        QWidget.setTabOrder(self.dsb_mll_foucs_mtr_end, self.dsb_mll_foucs_mtr_steps)
        QWidget.setTabOrder(self.dsb_mll_foucs_mtr_steps, self.dsb_mll_foucs_mtr_exp_time)
        QWidget.setTabOrder(self.dsb_mll_foucs_mtr_exp_time, self.cb_mll_focus_elem)
        QWidget.setTabOrder(self.cb_mll_focus_elem, self.cb_linearflag_mll_focus)
        QWidget.setTabOrder(self.cb_linearflag_mll_focus, self.cb_mll_z_motor_move)
        QWidget.setTabOrder(self.cb_mll_z_motor_move, self.dsb_mll_z_target_pos)
        QWidget.setTabOrder(self.dsb_mll_z_target_pos, self.cb_mll_z_motor)
        QWidget.setTabOrder(self.cb_mll_z_motor, self.sb_mll_z_start)
        QWidget.setTabOrder(self.sb_mll_z_start, self.sb_mll_z_end)
        QWidget.setTabOrder(self.sb_mll_z_end, self.sb_mll_z_steps)
        QWidget.setTabOrder(self.sb_mll_z_steps, self.pb_mll_nanobeam)
        QWidget.setTabOrder(self.pb_mll_nanobeam, self.pb_mll_lens_in)
        QWidget.setTabOrder(self.pb_mll_lens_in, self.pb_mll_osa_out)
        QWidget.setTabOrder(self.pb_mll_osa_out, self.pb_mll_lens_out)
        QWidget.setTabOrder(self.pb_mll_lens_out, self.pb_mll_cam11_view)
        QWidget.setTabOrder(self.pb_mll_cam11_view, self.pb_mll_osa_in)
        QWidget.setTabOrder(self.pb_mll_osa_in, self.pb_mll_bs_out)
        QWidget.setTabOrder(self.pb_mll_bs_out, self.pb_mll_bs_in)
        QWidget.setTabOrder(self.pb_mll_bs_in, self.pb_mll_sample_out)
        QWidget.setTabOrder(self.pb_mll_sample_out, self.pb_mll_sample_in)
        QWidget.setTabOrder(self.pb_mll_sample_in, self.pb_stop_mll_motion)
        QWidget.setTabOrder(self.pb_stop_mll_motion, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.pb_SSA2_HClose)
        QWidget.setTabOrder(self.pb_SSA2_HClose, self.pb_SSA2_VClose)
        QWidget.setTabOrder(self.pb_SSA2_VClose, self.pb_SSA2_Open)
        QWidget.setTabOrder(self.pb_SSA2_Open, self.pb_SSA2_Close)
        QWidget.setTabOrder(self.pb_SSA2_Close, self.pb_move_ssa2)
        QWidget.setTabOrder(self.pb_move_ssa2, self.db_ssa2_x_set)
        QWidget.setTabOrder(self.db_ssa2_x_set, self.db_ssa2_x)
        QWidget.setTabOrder(self.db_ssa2_x, self.db_ssa2_y_set)
        QWidget.setTabOrder(self.db_ssa2_y_set, self.db_ssa2_y)
        QWidget.setTabOrder(self.db_ssa2_y, self.db_s5_x_set)
        QWidget.setTabOrder(self.db_s5_x_set, self.db_s5_x)
        QWidget.setTabOrder(self.db_s5_x, self.db_s5_y_set)
        QWidget.setTabOrder(self.db_s5_y_set, self.db_s5_y)
        QWidget.setTabOrder(self.db_s5_y, self.pb_S5_VClose)
        QWidget.setTabOrder(self.pb_S5_VClose, self.pb_S5_Open)
        QWidget.setTabOrder(self.pb_S5_Open, self.pb_S5_HClose)
        QWidget.setTabOrder(self.pb_S5_HClose, self.pb_move_s5)
        QWidget.setTabOrder(self.pb_move_s5, self.pb_S5_Close)
        QWidget.setTabOrder(self.pb_S5_Close, self.pb_peakBeamXY)
        QWidget.setTabOrder(self.pb_peakBeamXY, self.pb_recover_from_beamdump)
        QWidget.setTabOrder(self.pb_recover_from_beamdump, self.pb_enable_run)
        QWidget.setTabOrder(self.pb_enable_run, self.pb_CAM6_IN)
        QWidget.setTabOrder(self.pb_CAM6_IN, self.pb_CAM6_OUT)
        QWidget.setTabOrder(self.pb_CAM6_OUT, self.pb_FS_IN)
        QWidget.setTabOrder(self.pb_FS_IN, self.pb_FS_OUT)
        QWidget.setTabOrder(self.pb_FS_OUT, self.db_fs)
        QWidget.setTabOrder(self.db_fs, self.db_cam6)
        QWidget.setTabOrder(self.db_cam6, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.dsb_target_ugap)
        QWidget.setTabOrder(self.dsb_target_ugap, self.dsb_target_pitch)
        QWidget.setTabOrder(self.dsb_target_pitch, self.cb_target_coating)
        QWidget.setTabOrder(self.cb_target_coating, self.dsb_target_roll)
        QWidget.setTabOrder(self.dsb_target_roll, self.sb_calc_harmonic)
        QWidget.setTabOrder(self.sb_calc_harmonic, self.dsb_hfm_target_pitch)
        QWidget.setTabOrder(self.dsb_hfm_target_pitch, self.sb_max_iter)
        QWidget.setTabOrder(self.sb_max_iter, self.cb_beam_at_ssa2)
        QWidget.setTabOrder(self.cb_beam_at_ssa2, self.dsb_target_e)
        QWidget.setTabOrder(self.dsb_target_e, self.pte_log)
        QWidget.setTabOrder(self.pte_log, self.tw_hxn_contact)

        self.menubar.addAction(self.menuHelp_2.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.actionRestart)
        self.menuOptions.addAction(self.actionExit)

        self.retranslateUi(window)

        self.HXN_GUI_tabs.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_18.setCurrentIndex(0)
        self.sample_ex_tabs.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"HXN GUI", None))
#if QT_CONFIG(statustip)
        window.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.actionScreenshot_tool.setText(QCoreApplication.translate("window", u"Screenshot tool", None))
        self.actionWeb_Browser.setText(QCoreApplication.translate("window", u"Web Browser", None))
        self.actionImagej.setText(QCoreApplication.translate("window", u"Open Imagej", None))
        self.actionImage_Correlation_tool.setText(QCoreApplication.translate("window", u"Image Correlation tool", None))
        self.actionOpen_a_Batch_File.setText(QCoreApplication.translate("window", u"Load a Batch File", None))
        self.actionSave_Batch_File.setText(QCoreApplication.translate("window", u"Save Batch File", None))
        self.actionClose_Application.setText(QCoreApplication.translate("window", u"Close Application", None))
        self.actionRestart.setText(QCoreApplication.translate("window", u"Restart", None))
        self.actionExit.setText(QCoreApplication.translate("window", u"Exit", None))
        self.pbar_flyscan.setFormat("")
        self.label_scanStatus.setText(QCoreApplication.translate("window", u"Idle", None))
        self.label_14.setText(QCoreApplication.translate("window", u"HXN 3-ID", None))
        self.db_flytube_p.setSuffix(QCoreApplication.translate("window", u" Torr", None))
        self.label_138.setText(QCoreApplication.translate("window", u"Flytube Pressure:", None))
        self.label_79.setText(QCoreApplication.translate("window", u"Scan ID:", None))
        self.label_122.setText(QCoreApplication.translate("window", u"IC3:", None))
        self.lcd_monoE.setSuffix(QCoreApplication.translate("window", u" keV", None))
        self.label_123.setText(QCoreApplication.translate("window", u"  Energy:  ", None))
        self.pb_open_b_shutter.setText(QCoreApplication.translate("window", u"\n"
"Open B Shutter\n"
"", None))
        self.pb_close_b_shutter.setText(QCoreApplication.translate("window", u"\n"
"Close B Shutter\n"
"", None))
        self.pb_open_c_shutter.setText(QCoreApplication.translate("window", u"\n"
"Open Fast Shutter (C)\n"
"", None))
        self.pb_close_c_shutter.setText(QCoreApplication.translate("window", u"\n"
"Close Fast Shutter (C)\n"
"", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("window", u"Set XRF Elements for Plotting", None))
#if QT_CONFIG(tooltip)
        self.pb_update_xrf_elems.setToolTip(QCoreApplication.translate("window", u"Click to update changes to the data collection. This will reload the program", None))
#endif // QT_CONFIG(tooltip)
        self.pb_update_xrf_elems.setText(QCoreApplication.translate("window", u"\n"
"Apply Element Selection                   \n"
"                                          ", None))
        self.pb_import_xrf_elem_list.setText(QCoreApplication.translate("window", u"\n"
"Import List\n"
"", None))
        self.pb_export_xrf_elem_list.setText(QCoreApplication.translate("window", u"\n"
"Export List\n"
"", None))
        self.le_roi_elems.setPlaceholderText(QCoreApplication.translate("window", u"limit =16", None))
        self.label_16.setText(QCoreApplication.translate("window", u"Elements of Interest (limit =16)   ", None))
        self.label_19.setText(QCoreApplication.translate("window", u"Live Image Elements (first", None))
        self.le_live_elems.setPlaceholderText(QCoreApplication.translate("window", u"4 or 6 recommened (must be in the elements of interest list)", None))
        self.label_25.setText(QCoreApplication.translate("window", u")", None))
        self.le_line_elem.setPlaceholderText(QCoreApplication.translate("window", u"only one (must be in the elements of interest list)", None))
        self.label_20.setText(QCoreApplication.translate("window", u"Line Plot Element (limit =1)         ", None))
        self.xrf_elem_cb_widget.setTitle(QCoreApplication.translate("window", u"Select Elements", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("window", u"1", None))
        self.label_24.setText(QCoreApplication.translate("window", u"2", None))
        self.label_38.setText(QCoreApplication.translate("window", u"3", None))
        self.label_33.setText(QCoreApplication.translate("window", u"4", None))
        self.label_35.setText(QCoreApplication.translate("window", u"5", None))
        self.label_30.setText(QCoreApplication.translate("window", u"6", None))
        self.label_36.setText(QCoreApplication.translate("window", u"7", None))
        self.label_31.setText(QCoreApplication.translate("window", u"8", None))
        self.label_37.setText(QCoreApplication.translate("window", u"9", None))
        self.label_34.setText(QCoreApplication.translate("window", u"10", None))
        self.label_29.setText(QCoreApplication.translate("window", u"11", None))
        self.label_28.setText(QCoreApplication.translate("window", u"12", None))
        self.label_26.setText(QCoreApplication.translate("window", u"13", None))
        self.label_39.setText(QCoreApplication.translate("window", u"14", None))
        self.label_40.setText(QCoreApplication.translate("window", u"15", None))
        self.label_41.setText(QCoreApplication.translate("window", u"16", None))
        self.label_21.setText("")
        self.textEdit_2.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt;\">Please note that this list is only for creating plots during data aquistion. Complete XRF spectrum is saved for all data collected. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><b"
                        "r /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt;\">If you make any changes to the list click &quot;Apply Element Selection &quot;. The program will restart to load those changes.</span></p></body></html>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("window", u"Create Directory", None))
        self.label_66.setText(QCoreApplication.translate("window", u"Proposal Number ", None))
        self.pb_create_user.setText(QCoreApplication.translate("window", u"\n"
"Create PDF and User Directory\n"
"", None))
        self.label_13.setText(QCoreApplication.translate("window", u"Sample Name    ", None))
        self.le_sample_name.setPlaceholderText(QCoreApplication.translate("window", u"Precious", None))
        self.label_69.setText(QCoreApplication.translate("window", u"PDF Filename", None))
        self.le_pdf_name.setText(QCoreApplication.translate("window", u"elog", None))
        self.pb_insert_user_image.setText(QCoreApplication.translate("window", u" Insert An image   ", None))
        self.label_12.setText(QCoreApplication.translate("window", u"Experimenters     ", None))
        self.le_experimenters.setPlaceholderText(QCoreApplication.translate("window", u"HX,NU,SER", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("window", u"Techniques", None))
        self.cb_technique_diff.setText(QCoreApplication.translate("window", u"Nanodiffraction", None))
        self.cb_technique_xanes.setText(QCoreApplication.translate("window", u"Nano-XANES", None))
        self.cb_technique_xrf.setText(QCoreApplication.translate("window", u"XRF", None))
        self.cb_technique_ptycho.setText(QCoreApplication.translate("window", u"Ptycho", None))
        self.label_50.setText("")
        self.label_11.setText(QCoreApplication.translate("window", u"PI Name             ", None))
#if QT_CONFIG(tooltip)
        self.le_username.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_username.setPlaceholderText(QCoreApplication.translate("window", u"Professor", None))
        self.pb_create_new_pdf_log.setText(QCoreApplication.translate("window", u"\n"
"Create PDF log\n"
"", None))
        self.label_15.setText("")
        self.pb_get_proposal_info.setText(QCoreApplication.translate("window", u"Get Proposal Info", None))
        self.pb_move_data_to_globus.setText(QCoreApplication.translate("window", u"\n"
"Move Data to Globus \n"
"", None))
        self.HXN_GUI_tabs.setTabText(self.HXN_GUI_tabs.indexOf(self.tab_4), QCoreApplication.translate("window", u"User Setup", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("window", u"FlyScans", None))
        self.label_17.setText(QCoreApplication.translate("window", u"Detectors", None))
#if QT_CONFIG(tooltip)
        self.cb_dets.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("window", u"Motors", None))
#if QT_CONFIG(tooltip)
        self.cb_motor1.setToolTip(QCoreApplication.translate("window", u"first motor to scan in 2D and Line scan motor", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cb_motor2.setToolTip(QCoreApplication.translate("window", u"second motor in 2D", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("window", u"Start", None))
#if QT_CONFIG(tooltip)
        self.x_start.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.x_start.setSuffix(QCoreApplication.translate("window", u"um", None))
#if QT_CONFIG(tooltip)
        self.y_start.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.y_start.setSuffix(QCoreApplication.translate("window", u"um", None))
        self.label_18.setText(QCoreApplication.translate("window", u"End", None))
#if QT_CONFIG(tooltip)
        self.x_end.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.y_end.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("window", u"Steps", None))
#if QT_CONFIG(tooltip)
        self.x_step.setToolTip(QCoreApplication.translate("window", u"first motor steps", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.y_step.setToolTip(QCoreApplication.translate("window", u"second motor steps", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("window", u"Dwell Time", None))
#if QT_CONFIG(tooltip)
        self.dwell.setToolTip(QCoreApplication.translate("window", u"exposure time per point", None))
#endif // QT_CONFIG(tooltip)
        self.dwell.setPrefix("")
#if QT_CONFIG(tooltip)
        self.rb_1d.setToolTip(QCoreApplication.translate("window", u"select for line scan", None))
#endif // QT_CONFIG(tooltip)
        self.rb_1d.setText(QCoreApplication.translate("window", u"Fly1D", None))
#if QT_CONFIG(tooltip)
        self.rb_2d.setToolTip(QCoreApplication.translate("window", u"select for 2D scan", None))
#endif // QT_CONFIG(tooltip)
        self.rb_2d.setText(QCoreApplication.translate("window", u"Fly2D", None))
#if QT_CONFIG(tooltip)
        self.groupBox_2.setToolTip(QCoreApplication.translate("window", u"Quickly fill the selected parameters above", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("window", u" Quick Fill", None))
        self.pb_3030.setText(QCoreApplication.translate("window", u"  28umx28um, 30:30 steps, 0.005 sec", None))
        self.pb_66.setText(QCoreApplication.translate("window", u" 6umx6um, 100:100 steps, 0.005 sec", None))
        self.pb_2020.setText(QCoreApplication.translate("window", u" 20umx20um, 100:100 steps, 0.005 sec", None))
        self.pb_22.setText(QCoreApplication.translate("window", u" 2umx2um, 100:100 steps, 0.005 sec", None))
        self.label_136.setText("")
        self.pb_abort_fly.setText(QCoreApplication.translate("window", u"Abort", None))
#if QT_CONFIG(tooltip)
        self.pb_batchscan_copy.setToolTip(QCoreApplication.translate("window", u"yield from will be added to the front", None))
#endif // QT_CONFIG(tooltip)
        self.pb_batchscan_copy.setText(QCoreApplication.translate("window", u"    Copy For Batch   ", None))
#if QT_CONFIG(tooltip)
        self.pb_scan_copy.setToolTip(QCoreApplication.translate("window", u"paste the scan to a terminal for scan", None))
#endif // QT_CONFIG(tooltip)
        self.pb_scan_copy.setText(QCoreApplication.translate("window", u"Copy Plan", None))
        self.label_scan_info_calc.setText(QCoreApplication.translate("window", u"Scan Info", None))
        self.label_53.setText("")
#if QT_CONFIG(tooltip)
        self.start.setToolTip(QCoreApplication.translate("window", u"excetute the scan plan", None))
#endif // QT_CONFIG(tooltip)
        self.start.setText(QCoreApplication.translate("window", u"RUN", None))
        self.toolBox_10.setItemText(self.toolBox_10.indexOf(self.toolBox_10Page1), QCoreApplication.translate("window", u"Scan", None))
        self.pb_flyplan_to_qserver.setText(QCoreApplication.translate("window", u"    Send to Queue    ", None))
        self.label_52.setText(QCoreApplication.translate("window", u"Label:", None))
        self.le_qplan_name.setText(QCoreApplication.translate("window", u"queue_plan1", None))
        self.cb_queue_use_curr_pos.setText(QCoreApplication.translate("window", u"Use Current Position", None))
        self.gb_queue_server_plan.setTitle(QCoreApplication.translate("window", u"Manual ROI", None))
#if QT_CONFIG(tooltip)
        self.dsb_zpssz_manual_roi.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_zpssz_manual_roi.setSuffix(QCoreApplication.translate("window", u" um", None))
#if QT_CONFIG(tooltip)
        self.dsb_zpssy_manual_roi.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_zpssy_manual_roi.setSuffix(QCoreApplication.translate("window", u" um", None))
#if QT_CONFIG(tooltip)
        self.dsb_zpsth_manual_roi.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_zpsth_manual_roi.setSuffix(QCoreApplication.translate("window", u" deg", None))
#if QT_CONFIG(tooltip)
        self.dsb_smary_manual_roi.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_smary_manual_roi.setSuffix(QCoreApplication.translate("window", u" um", None))
#if QT_CONFIG(tooltip)
        self.dsb_smarx_manual_roi.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_smarx_manual_roi.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pb_get_current_position.setText(QCoreApplication.translate("window", u"\n"
"Get curr pos\n"
"", None))
        self.label_196.setText(QCoreApplication.translate("window", u"zpssx", None))
#if QT_CONFIG(tooltip)
        self.dsb_zpz1_manual_roi.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_zpz1_manual_roi.setSuffix(QCoreApplication.translate("window", u" mm", None))
#if QT_CONFIG(tooltip)
        self.dsb_zpssx_manual_roi.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_zpssx_manual_roi.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_209.setText(QCoreApplication.translate("window", u"smarz", None))
#if QT_CONFIG(tooltip)
        self.rb_mll_manual_roi.setToolTip(QCoreApplication.translate("window", u"select for 2D scan", None))
#endif // QT_CONFIG(tooltip)
        self.rb_mll_manual_roi.setText(QCoreApplication.translate("window", u"MLL", None))
        self.label_206.setText("")
        self.label_193.setText(QCoreApplication.translate("window", u"zpssy", None))
        self.label_210.setText(QCoreApplication.translate("window", u"zpsth", None))
        self.label_208.setText(QCoreApplication.translate("window", u"smary", None))
        self.label_207.setText(QCoreApplication.translate("window", u"smarx", None))
        self.label_211.setText(QCoreApplication.translate("window", u"zpz1", None))
#if QT_CONFIG(tooltip)
        self.dsb_smarz_manual_roi.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_smarz_manual_roi.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_194.setText(QCoreApplication.translate("window", u"zpssz", None))
        self.rb_zp_manual_roi.setText(QCoreApplication.translate("window", u"ZP", None))
        self.toolBox_10.setItemText(self.toolBox_10.indexOf(self.page), QCoreApplication.translate("window", u"QueueServer", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("window", u"Sample Stage Controls", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("window", u"Save Positions", None))
        self.label_163.setText(QCoreApplication.translate("window", u"Recover Pos. Using Scan ID", None))
        self.label_164.setText(QCoreApplication.translate("window", u"Scan ID", None))
        self.pb_recover_scan_pos_zp.setText(QCoreApplication.translate("window", u"\n"
"Move to Scan Pos\n"
"", None))
        self.cb_sid_moveZPZ.setText(QCoreApplication.translate("window", u"Move ZP Focus", None))
        self.pb_show_scan_pos_zp.setText(QCoreApplication.translate("window", u"\n"
"Show Scan Pos\n"
"", None))
        self.pb_print_scan_meta_zp.setText(QCoreApplication.translate("window", u"\n"
"Show Meta Data\n"
"", None))
        self.pb_save_pos_zp.setText(QCoreApplication.translate("window", u"Save Current Position", None))
        self.pb_move_pos_zp.setText(QCoreApplication.translate("window", u"Move to Selected", None))
#if QT_CONFIG(tooltip)
        self.pb_copy_curr_pos_zp.setToolTip(QCoreApplication.translate("window", u"motor values to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.pb_copy_curr_pos_zp.setText(QCoreApplication.translate("window", u"Copy Curr. Pos. to Clipboard", None))
        self.pb_roiList_export_zp.setText(QCoreApplication.translate("window", u"  Export List  ", None))
        self.pb_roiList_import_zp.setText(QCoreApplication.translate("window", u"   Import List   ", None))
        self.pb_roiList_clear_zp.setText(QCoreApplication.translate("window", u"Clear All", None))
        self.pb_roiList_clear_sel_zp.setText(QCoreApplication.translate("window", u"Clear Selected", None))
        self.label_45.setText("")
        self.groupBox_36.setTitle(QCoreApplication.translate("window", u"Navigation", None))
        self.db_smarx.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.db_move_smarz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pb_move_zpsth_pos_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.db_smary.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_78.setText(QCoreApplication.translate("window", u"Zone Plate Z  ", None))
        self.db_smarz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pb_move_smary_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.db_zpz1.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_158.setText(QCoreApplication.translate("window", u"Readback", None))
        self.label_159.setText(QCoreApplication.translate("window", u"Sample Angle  ", None))
        self.db_move_zpz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pb_move_smarx_pos.setText(QCoreApplication.translate("window", u"  +  ", None))
        self.pb_move_smarz_pos.setText(QCoreApplication.translate("window", u"+", None))
        self.db_move_zpsth.setSuffix(QCoreApplication.translate("window", u" deg", None))
        self.pb_move_zpz_pos.setText(QCoreApplication.translate("window", u"+", None))
        self.pb_move_smarz_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.pb_move_zpsth_pos.setText(QCoreApplication.translate("window", u"+", None))
        self.db_move_smary.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pb_move_smary_pos.setText(QCoreApplication.translate("window", u"+", None))
        self.pb_zp_stop_all_sample.setText(QCoreApplication.translate("window", u"\n"
"Stop All Sample Motion\n"
"", None))
        self.pb_move_zpz_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.label_42.setText(QCoreApplication.translate("window", u"smarZ", None))
        self.label_129.setText(QCoreApplication.translate("window", u"Move by", None))
        self.label_160.setText(QCoreApplication.translate("window", u"smarX", None))
        self.pb_move_smarx_neg.setText(QCoreApplication.translate("window", u"   -   ", None))
        self.db_zpsth.setSuffix(QCoreApplication.translate("window", u" deg", None))
        self.label_161.setText(QCoreApplication.translate("window", u"Motor", None))
        self.db_move_smarx.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_162.setText(QCoreApplication.translate("window", u"smarY", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("window", u"Zone Plate Module", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("window", u"Navigation", None))
        self.label_167.setText("")
        self.pb_move_dsz_pos.setText(QCoreApplication.translate("window", u"+", None))
        self.pb_move_dth_pos.setText(QCoreApplication.translate("window", u"+", None))
        self.label_43.setText(QCoreApplication.translate("window", u"DSZ", None))
        self.pb_move_dsy_pos.setText(QCoreApplication.translate("window", u"+", None))
        self.label_82.setText(QCoreApplication.translate("window", u"SBZ", None))
        self.db_move_dsx.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.db_dsy.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_131.setText(QCoreApplication.translate("window", u"Move by", None))
        self.pb_move_dsx_pos.setText(QCoreApplication.translate("window", u"  +  ", None))
        self.db_dsth.setSuffix(QCoreApplication.translate("window", u" deg", None))
        self.label_168.setText(QCoreApplication.translate("window", u"Readback", None))
        self.label_169.setText(QCoreApplication.translate("window", u"Sample Angle  ", None))
        self.db_dsx.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.db_move_dsz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.db_move_dsy.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_170.setText(QCoreApplication.translate("window", u"DSX", None))
        self.db_move_sbz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.db_dsz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.db_move_dsth.setSuffix(QCoreApplication.translate("window", u" deg", None))
        self.db_sbz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_171.setText(QCoreApplication.translate("window", u"Motor", None))
        self.label_172.setText(QCoreApplication.translate("window", u"DSY", None))
        self.pb_move_sbz_pos.setText(QCoreApplication.translate("window", u"+", None))
        self.pb_move_dsx_neg.setText(QCoreApplication.translate("window", u"   -   ", None))
        self.pb_move_dsy_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.pb_move_dsz_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.pb_move_dth_pos_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.pb_move_sbz_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.pb_mll_stop_all_sample.setText(QCoreApplication.translate("window", u"\n"
"Stop All Sample Motion\n"
"", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("window", u"Save Positions", None))
        self.pb_move_pos_mll.setText(QCoreApplication.translate("window", u"Move to Selected", None))
        self.pb_save_pos_mll.setText(QCoreApplication.translate("window", u"Save Current Position", None))
#if QT_CONFIG(tooltip)
        self.pb_copy_curr_pos_mll.setToolTip(QCoreApplication.translate("window", u"motor values to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.pb_copy_curr_pos_mll.setText(QCoreApplication.translate("window", u"Copy Curr. Pos. to Clipboard", None))
        self.pb_roiList_clear_mll.setText(QCoreApplication.translate("window", u"Clear All", None))
        self.pb_roiList_export_mll.setText(QCoreApplication.translate("window", u"  Export List  ", None))
        self.pb_roiList_import_mll.setText(QCoreApplication.translate("window", u"   Import List   ", None))
        self.pb_roiList_clear_sel_mll.setText(QCoreApplication.translate("window", u"Clear Selected", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("window", u"Positions fromScan ID", None))
        self.label_166.setText(QCoreApplication.translate("window", u"Scan ID", None))
        self.pb_recover_scan_pos_mll.setText(QCoreApplication.translate("window", u"\n"
"Move to Scan Pos\n"
"", None))
        self.cb_sid_move_base_mll.setText(QCoreApplication.translate("window", u"Move Sbz", None))
        self.pb_print_scan_meta_mll.setText(QCoreApplication.translate("window", u"\n"
"Show Meta Data\n"
"", None))
        self.pb_show_scan_pos_mll.setText(QCoreApplication.translate("window", u"\n"
"Show Scan Pos\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("window", u"MLL Module", None))
        self.label_6.setText("")
        self.label_130.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("window", u"Abort Motion", None))
        self.pb_stop_fluor.setText(QCoreApplication.translate("window", u"               Stop Fluor.             ", None))
        self.label_55.setText("")
        self.pb_stop_dexela.setText(QCoreApplication.translate("window", u"Stop Dexela", None))
        self.pb_stop_cam11.setText(QCoreApplication.translate("window", u"Stop CAM11", None))
        self.pb_stop_merlin.setText(QCoreApplication.translate("window", u"Stop Merlin/Eiger", None))
        self.groupBox1.setTitle(QCoreApplication.translate("window", u"CAM/DET IN and OUT", None))
        self.label_68.setText("")
        self.pb_cam6IN.setText(QCoreApplication.translate("window", u"  CAM6 IN  ", None))
        self.pb_vortexIN.setText(QCoreApplication.translate("window", u"XRF Det IN", None))
        self.pb_dexela_IN.setText(QCoreApplication.translate("window", u"   Dexela IN    ", None))
        self.pb_cam11IN.setText(QCoreApplication.translate("window", u"  CAM 11 IN   ", None))
        self.pb_merlinIN.setText(QCoreApplication.translate("window", u" Merlin IN  ", None))
        self.pb_vortexOUT.setText(QCoreApplication.translate("window", u"XRF Det OUT", None))
        self.pb_dexela_OUT.setText(QCoreApplication.translate("window", u"Dexela OUT", None))
        self.pb_telescope.setText(QCoreApplication.translate("window", u"   Telescope IN ", None))
        self.pb_cam6OUT.setText(QCoreApplication.translate("window", u"  CAM6 OUT  ", None))
        self.pb_merlinOUT.setText(QCoreApplication.translate("window", u"Merlin OUT", None))
        self.db_fs_det.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.db_cam06x.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_57.setText("")
        self.db_dexela.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.db_diffx.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.pb_eiger_in.setText(QCoreApplication.translate("window", u"Eiger IN", None))
        self.pb_laser_in.setText(QCoreApplication.translate("window", u"Laser IN", None))
        self.label_74.setText(QCoreApplication.translate("window", u"XRF Det IN Pos. = ", None))
        self.dsb_flur_in_pos.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("window", u"Diff Stage Motion", None))
        self.label_67.setText("")
        self.sp_dexela_xpixel.setPrefix(QCoreApplication.translate("window", u"x = ", None))
        self.sp_dexela_ypixel.setPrefix(QCoreApplication.translate("window", u"y = ", None))
        self.pb_pos_to_angle.setText(QCoreApplication.translate("window", u" Calculate Diff.Pos.", None))
        self.label_65.setText(QCoreApplication.translate("window", u"Enter Dexela XY Pixels", None))
        self.pb_read_dexela_ROI1.setText(QCoreApplication.translate("window", u"Read Dexela ROI1 (top-right corner)", None))
        self.pb_reset_dexela_ROI1.setText(QCoreApplication.translate("window", u"Reset ROI1", None))
        self.sp_diff_det_calc_x.setPrefix(QCoreApplication.translate("window", u"gamma = ", None))
        self.sp_diff_det_calc_x.setSuffix(QCoreApplication.translate("window", u" deg", None))
        self.sp_diff_det_calc_y.setPrefix(QCoreApplication.translate("window", u"delta = ", None))
        self.sp_diff_det_calc_y.setSuffix(QCoreApplication.translate("window", u" deg", None))
        self.sp_diff_det_calc_2theta.setPrefix(QCoreApplication.translate("window", u"2theta = ", None))
        self.sp_diff_det_calc_2theta.setSuffix(QCoreApplication.translate("window", u" deg", None))
        self.sp_diff_det_r.setPrefix(QCoreApplication.translate("window", u"r = ", None))
        self.sp_diff_det_r.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_73.setText(QCoreApplication.translate("window", u"diff_z", None))
        self.dsb_move_diff_z_rel_value.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.pb_move_diff_z.setText(QCoreApplication.translate("window", u"Move ", None))
        self.pb_move_diff.setText(QCoreApplication.translate("window", u"Move Diff. Stage", None))
        self.pb_abort_diff.setText(QCoreApplication.translate("window", u"Abort Diff. Motion", None))
        self.pb_copy_pos2angle.setText(QCoreApplication.translate("window", u"Copy Results", None))
        self.cb_mll_theta_for_diff.setText(QCoreApplication.translate("window", u"MLL User", None))
        self.tabWidget_18.setTabText(self.tabWidget_18.indexOf(self.tabWidget_18Page1), QCoreApplication.translate("window", u"Detector Motion", None))
        self.label_54.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("window", u"Flatfield Corrections", None))
        self.label_63.setText(QCoreApplication.translate("window", u"Chosse Detector", None))
        self.pb_cam11_disable_flatfield.setText(QCoreApplication.translate("window", u"  Disable CAM11 FlatField  ", None))
        self.pb_cam11_flatfield.setText(QCoreApplication.translate("window", u"  Save+Enable CAM11 FlatField  ", None))
        self.label_62.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("window", u"  Save+Enable FlatField  ", None))
        self.pushButton_16.setText(QCoreApplication.translate("window", u" Disable FlatField  ", None))
        self.label_27.setText(QCoreApplication.translate("window", u"Update Detector Position", None))
        self.pb_update_dets_pos.setText(QCoreApplication.translate("window", u"Update Position", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("window", u"Misc.", None))
        self.pb_merlin_filterIN.setText(QCoreApplication.translate("window", u"Merlin Filter IN", None))
        self.pb_merlin_filterOUT.setText(QCoreApplication.translate("window", u"Merlin Filter OUT", None))
        self.pb_light_OFF.setText(QCoreApplication.translate("window", u"Microscope Light OFF", None))
        self.pb_light_ON.setText(QCoreApplication.translate("window", u"Microscope Light ON", None))
        self.label_64.setText("")
        self.pb_eiger_filter_a_in.setText(QCoreApplication.translate("window", u"Eiger Filter-A IN", None))
        self.pb_eiger_filter_a_out.setText(QCoreApplication.translate("window", u"Eiger Filter-A OUT", None))
        self.pb_eiger_filter_b_in.setText(QCoreApplication.translate("window", u"Eiger Filter-B IN", None))
        self.pb_eiger_filter_b_out.setText(QCoreApplication.translate("window", u"Eiger Filter-B OUT", None))
        self.pb_eiger_filter_c_in.setText(QCoreApplication.translate("window", u"Eiger Filter-C IN", None))
        self.pb_eiger_filter_c_out.setText(QCoreApplication.translate("window", u"Eiger Filter-C OUT", None))
        self.tabWidget_18.setTabText(self.tabWidget_18.indexOf(self.tab_12), QCoreApplication.translate("window", u"Detector Controls", None))
        self.groupBox2.setTitle(QCoreApplication.translate("window", u"Plotting", None))
        self.label_51.setText("")
        self.label_48.setText(QCoreApplication.translate("window", u"    Elem:", None))
        self.label_47.setText(QCoreApplication.translate("window", u"Scan ID:", None))
        self.le_plot_sd.setText(QCoreApplication.translate("window", u"-1", None))
        self.pb_plot_last.setText(QCoreApplication.translate("window", u"Last Scan", None))
        self.pb_erf_fit.setText(QCoreApplication.translate("window", u" \n"
"ERF Fit\n"
"", None))
        self.cb_erf_linear_flag.setText(QCoreApplication.translate("window", u"Linear Flag      ", None))
        self.label_49.setText(QCoreApplication.translate("window", u"Threshold", None))
        self.pb_plot_line_center.setText(QCoreApplication.translate("window", u" \n"
" Return Line Center \n"
" ", None))
        self.pb_plot.setText(QCoreApplication.translate("window", u"  \n"
"Plot\n"
"", None))
        self.pb_close_all_plot.setText(QCoreApplication.translate("window", u"\n"
"  Close All Plots \n"
"", None))
        self.HXN_GUI_tabs.setTabText(self.HXN_GUI_tabs.indexOf(self.scan_tab), QCoreApplication.translate("window", u"Data Aquisition", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("window", u"Mosaic Scan", None))
#if QT_CONFIG(tooltip)
        self.cb_det_list_mosaic.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_177.setText(QCoreApplication.translate("window", u"Y Range", None))
        self.label_179.setText(QCoreApplication.translate("window", u"Det list", None))
#if QT_CONFIG(tooltip)
        self.sb_yrange_mosaic.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sb_xrange_mosaic.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.sb_xrange_mosaic.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_189.setText(QCoreApplication.translate("window", u"Overlap ", None))
#if QT_CONFIG(tooltip)
        self.dsb_dwell.setToolTip(QCoreApplication.translate("window", u"exposure time per point", None))
#endif // QT_CONFIG(tooltip)
        self.dsb_dwell.setPrefix("")
        self.dsb_overlap_mosaic.setSuffix(QCoreApplication.translate("window", u" %", None))
#if QT_CONFIG(tooltip)
        self.sb_stepsize_mosaic.setToolTip(QCoreApplication.translate("window", u"first motor steps", None))
#endif // QT_CONFIG(tooltip)
        self.sb_stepsize_mosaic.setSuffix(QCoreApplication.translate("window", u" nm", None))
        self.sb_stepsize_mosaic.setPrefix("")
        self.label_190.setText(QCoreApplication.translate("window", u"X Range", None))
        self.label_188.setText(QCoreApplication.translate("window", u"Dwell Time", None))
        self.label_191.setText(QCoreApplication.translate("window", u"Step size", None))
#if QT_CONFIG(tooltip)
        self.rb_mosaic_mll.setToolTip(QCoreApplication.translate("window", u"select for 2D scan", None))
#endif // QT_CONFIG(tooltip)
        self.rb_mosaic_mll.setText(QCoreApplication.translate("window", u"MLL", None))
        self.rb_mosaic_zp.setText(QCoreApplication.translate("window", u"ZP", None))
        self.le_mosaic_plan_name.setText(QCoreApplication.translate("window", u"Mosaic_scan#1", None))
        self.label_192.setText(QCoreApplication.translate("window", u"Plan name", None))
        self.pb_send_mosaic_to_queue.setText(QCoreApplication.translate("window", u"\n"
" Send to Queue \n"
"", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("window", u"MLL", None))
        self.pb_open_mll_tomo_widget.setText(QCoreApplication.translate("window", u"\n"
"MLL Tomo Widget\n"
"", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("window", u" \n"
"MLL-XANES Widget\n"
"", None))
        self.pushButton_15.setText(QCoreApplication.translate("window", u"\n"
"MLL Diff Widget\n"
"", None))
        self.groupBox3.setTitle(QCoreApplication.translate("window", u"ZP", None))
        self.pushButton_5.setText(QCoreApplication.translate("window", u"\n"
"ZP Tomo Widget\n"
"", None))
        self.pushButton_6.setText(QCoreApplication.translate("window", u"\n"
"ZP-XANES Widget\n"
"", None))
        self.label_3.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("window", u"\n"
"ZP Diff Widget\n"
"", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("window", u"Step scans", None))
#if QT_CONFIG(tooltip)
        self.x_step_end.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.x_step_2.setToolTip(QCoreApplication.translate("window", u"first motor steps", None))
#endif // QT_CONFIG(tooltip)
        self.label_95.setText(QCoreApplication.translate("window", u"End", None))
        self.label_92.setText(QCoreApplication.translate("window", u"Detectors", None))
#if QT_CONFIG(tooltip)
        self.dwell_2.setToolTip(QCoreApplication.translate("window", u"exposure time per point", None))
#endif // QT_CONFIG(tooltip)
        self.dwell_2.setPrefix("")
        self.label_165.setText(QCoreApplication.translate("window", u"Dwell Time", None))
#if QT_CONFIG(tooltip)
        self.rb_step_1d.setToolTip(QCoreApplication.translate("window", u"select for line scan", None))
#endif // QT_CONFIG(tooltip)
        self.rb_step_1d.setText(QCoreApplication.translate("window", u"Line scan", None))
#if QT_CONFIG(tooltip)
        self.rb_step_2d.setToolTip(QCoreApplication.translate("window", u"select for 2D scan", None))
#endif // QT_CONFIG(tooltip)
        self.rb_step_2d.setText(QCoreApplication.translate("window", u"2D Scan", None))
#if QT_CONFIG(tooltip)
        self.y_step_end.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.label_93.setText(QCoreApplication.translate("window", u"Motors", None))
#if QT_CONFIG(tooltip)
        self.cb_step_dets.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.y_step_start.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.y_step_start.setSuffix(QCoreApplication.translate("window", u"um", None))
#if QT_CONFIG(tooltip)
        self.y_step_2.setToolTip(QCoreApplication.translate("window", u"second motor steps", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cb_step_motor1.setToolTip(QCoreApplication.translate("window", u"first motor to scan in 2D and Line scan motor", None))
#endif // QT_CONFIG(tooltip)
        self.label_94.setText(QCoreApplication.translate("window", u"Start", None))
        self.label_96.setText(QCoreApplication.translate("window", u"Steps", None))
#if QT_CONFIG(tooltip)
        self.cb_step_motor2.setToolTip(QCoreApplication.translate("window", u"second motor in 2D", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.x_step_start.setToolTip(QCoreApplication.translate("window", u"scan range entry", None))
#endif // QT_CONFIG(tooltip)
        self.x_step_start.setSuffix(QCoreApplication.translate("window", u"um", None))
        self.pushButton_4.setText(QCoreApplication.translate("window", u"\n"
" RUN \n"
"", None))
        self.HXN_GUI_tabs.setTabText(self.HXN_GUI_tabs.indexOf(self.tab_2), QCoreApplication.translate("window", u"Advanced Scans/Queue", None))
        self.pb_start_pressure_live_plot.setText(QCoreApplication.translate("window", u"Start Plot", None))
        self.pb_stop_pressure_live_plot.setText(QCoreApplication.translate("window", u"Stop Plot", None))
        self.textEdit.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt;\">Read Me</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt;\">- Please don't close the window while pumping/venting/He-backfill. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt;\">- If the window crashes contact beamline staff to manually turn off/on the motors/valve controls. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-"
                        "size:12pt;\">- Make sure the helium valve is ON before backfilling with Helium</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt;\">- If the pressure value is not changing as expeted for more than 10 minutes, contact beamline staff. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:emp"
                        "ty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:12pt;\"><br /></p></body></html>", None))
        self.groupBox_22.setTitle("")
        self.label_71.setText(QCoreApplication.translate("window", u"Target P = ", None))
        self.cb_sample_ex_cam11_in.setText(QCoreApplication.translate("window", u"Move to cam11", None))
#if QT_CONFIG(tooltip)
        self.pb_start_pump.setToolTip(QCoreApplication.translate("window", u"Starts the pumping protocol. Status of all the valves will be checked ", None))
#endif // QT_CONFIG(tooltip)
        self.pb_start_pump.setText(QCoreApplication.translate("window", u"     \n"
"EVAC   \n"
" (Sample IN)", None))
        self.cb_he_backfill_bool.setText(QCoreApplication.translate("window", u"He BackFill", None))
        self.groupBox_29.setTitle("")
#if QT_CONFIG(tooltip)
        self.pb_start_vent.setToolTip(QCoreApplication.translate("window", u"Status of all the motors and valves will be checked", None))
#endif // QT_CONFIG(tooltip)
        self.pb_start_vent.setText(QCoreApplication.translate("window", u"       \n"
" VENT   \n"
"                   (Sample OUT)                  ", None))
        self.cb_sample_ex_det_out.setText(QCoreApplication.translate("window", u"Move Dets Out", None))
        self.sample_ex_tabs.setTabText(self.sample_ex_tabs.indexOf(self.tab_6), QCoreApplication.translate("window", u"Auto", None))
        self.pb_open_fast_pumps.setText(QCoreApplication.translate("window", u"  \n"
"  Force Open Fast Pumps  \n"
"", None))
        self.pb_stop_vent.setText(QCoreApplication.translate("window", u"\n"
"Stop Venting\n"
"", None))
        self.pb_auto_he_fill.setText(QCoreApplication.translate("window", u" \n"
"   Start  Auto He Back Fill   \n"
"      ", None))
        self.pb_stop_pump.setText(QCoreApplication.translate("window", u"  \n"
"Stop Pumping   \n"
"", None))
        self.pb_open_he_valve.setText(QCoreApplication.translate("window", u"\n"
"Open He Valve\n"
"", None))
        self.pb_close_he_valve.setText(QCoreApplication.translate("window", u"\n"
"Close He Valve\n"
"", None))
        self.sample_ex_tabs.setTabText(self.sample_ex_tabs.indexOf(self.tab_7), QCoreApplication.translate("window", u"Manual Controls", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("window", u"Status", None))
        self.label_44.setText("")
        self.groupBox_28.setTitle(QCoreApplication.translate("window", u"Vents", None))
        self.rb_he_backfill_fail.setText(QCoreApplication.translate("window", u"He Backfill Failed?", None))
        self.rb_fast_vent.setText(QCoreApplication.translate("window", u"                                     Vent Open?", None))
        self.label_145.setText("")
        self.groupBox_30.setTitle(QCoreApplication.translate("window", u"Pumps", None))
        self.label_147.setText("")
        self.rb_pumpB_slow.setText(QCoreApplication.translate("window", u"     B   ", None))
        self.rb_pumpA_slow.setText(QCoreApplication.translate("window", u"     A   ", None))
        self.label_144.setText("")
        self.lb_sample_change_action.setText(QCoreApplication.translate("window", u"Process Update", None))
        self.label_119.setText(QCoreApplication.translate("window", u"Current Pressure = ", None))
        self.lcdPressure.setSuffix(QCoreApplication.translate("window", u" mm Hg", None))
        self.prb_sample_exchange.setFormat(QCoreApplication.translate("window", u"%p%", None))
        self.HXN_GUI_tabs.setTabText(self.HXN_GUI_tabs.indexOf(self.sample_exchange_tab), QCoreApplication.translate("window", u"Sample Exchange", None))
        self.label_141.setText("")
        self.label_143.setText("")
        self.groupBox_21.setTitle("")
        self.pb_zpbsy_out.setText(QCoreApplication.translate("window", u"\n"
"Beam Stop OUT (Y-100)\n"
"", None))
        self.pb_osa_in.setText(QCoreApplication.translate("window", u"OSA IN (Y+2700)", None))
        self.pb_osa_out.setText(QCoreApplication.translate("window", u"\n"
"OSA OUT (Y-2700)\n"
"", None))
        self.pb_zpbsy_in.setText(QCoreApplication.translate("window", u"\n"
"Beam Stop IN (Y+100)\n"
"", None))
        self.pb_zp_cam11_view.setText(QCoreApplication.translate("window", u"\n"
"ZP to CAM 11 View\n"
"", None))
        self.pb_zp_nanobeam.setText(QCoreApplication.translate("window", u"\n"
"ZP to Nanobeam\n"
"", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("window", u"Zone Plate Z Focus", None))
        self.label_135.setText("")
        self.label_76.setText(QCoreApplication.translate("window", u"Zone Plate Z", None))
#if QT_CONFIG(tooltip)
        self.label_100.setToolTip(QCoreApplication.translate("window", u"relative start pos", None))
#endif // QT_CONFIG(tooltip)
        self.label_100.setText(QCoreApplication.translate("window", u"ZPZ Start", None))
        self.sb_ZPZ1RelativeStart.setSuffix(QCoreApplication.translate("window", u" um", None))
#if QT_CONFIG(tooltip)
        self.label_102.setToolTip(QCoreApplication.translate("window", u"relative end pos", None))
#endif // QT_CONFIG(tooltip)
        self.label_102.setText(QCoreApplication.translate("window", u"ZPZ End", None))
        self.sb_ZPZ1RelativeEnd.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_106.setText(QCoreApplication.translate("window", u"No. of Steps", None))
        self.sb_ZPZ1Steps.setSuffix("")
        self.label_77.setText(QCoreApplication.translate("window", u"FlyScan Param.", None))
        self.cb_foucsScanMotor.setItemText(0, QCoreApplication.translate("window", u"zpssx", None))
        self.cb_foucsScanMotor.setItemText(1, QCoreApplication.translate("window", u"zpssy", None))
        self.cb_foucsScanMotor.setItemText(2, QCoreApplication.translate("window", u"zpssz", None))

        self.label_99.setText(QCoreApplication.translate("window", u"Start", None))
        self.label_101.setText(QCoreApplication.translate("window", u"End", None))
        self.label_105.setText(QCoreApplication.translate("window", u"No. of Steps", None))
        self.sb_FocusScanMtrStep.setSuffix("")
        self.label_118.setText(QCoreApplication.translate("window", u"Dwell Time", None))
        self.label_56.setText(QCoreApplication.translate("window", u"New Focus Position = ", None))
        self.dsb_ZPZ1TargetPos.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_97.setText(QCoreApplication.translate("window", u"     Elem:  ", None))
        self.cb_linearFlag_zpFocus.setText(QCoreApplication.translate("window", u"Linear Flag", None))
        self.pb_MoveZPZ1AbsPos.setText(QCoreApplication.translate("window", u"\n"
"Move to New Focus\n"
"", None))
        self.pb_ZPZFocusScanStart.setText(QCoreApplication.translate("window", u"\n"
"Start Focus Series\n"
"", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("window", u"ZP_Rot.Center", None))
        self.label_156.setText("")
        self.label_108.setText(QCoreApplication.translate("window", u"Start", None))
        self.sb_zp_rot_scan_start.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_109.setText(QCoreApplication.translate("window", u"End", None))
        self.sb_zp_rot_scan_end.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_110.setText(QCoreApplication.translate("window", u"No. of Steps", None))
        self.sb_zp_rot_scan_num.setSuffix("")
        self.label_157.setText(QCoreApplication.translate("window", u"Dwell Time", None))
        self.pb_zp_rot_align_start.setText(QCoreApplication.translate("window", u"\n"
"Start\n"
"", None))
        self.label_103.setText(QCoreApplication.translate("window", u"Theta Start", None))
        self.sb_zp_rot_angle_start.setSuffix("")
        self.label_104.setText(QCoreApplication.translate("window", u"Theta End", None))
        self.sb_zp_rot_angle_end.setSuffix("")
        self.label_107.setText(QCoreApplication.translate("window", u"No. of Steps", None))
        self.sb_zp_rot_angle_num.setSuffix("")
        self.label_98.setText(QCoreApplication.translate("window", u"Elem:", None))
        self.pushButton_10.setText(QCoreApplication.translate("window", u"\n"
"Move smarZ by\n"
"", None))
        self.dsb_rot_align_smarz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pushButton_9.setText(QCoreApplication.translate("window", u"  \n"
"Move smarX by  \n"
"  ", None))
        self.dsb_rot_align_smarx.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pushButton_11.setText(QCoreApplication.translate("window", u"\n"
"Rotate to\n"
"", None))
        self.dsb_rot_align_zpsth.setSuffix("")
        self.pb_apply_zp_rot_align_corr.setText(QCoreApplication.translate("window", u"\n"
" Apply Rot. Align. Correction \n"
"", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("window", u"Zone Plate ", None))
        self.groupBox_35.setTitle("")
        self.pb_mll_osa_out.setText(QCoreApplication.translate("window", u"\n"
"OSA OUT (+X)\n"
"", None))
        self.pb_mll_lens_out.setText(QCoreApplication.translate("window", u"\n"
"Lenses OUT\n"
"", None))
        self.pb_mll_bs_out.setText(QCoreApplication.translate("window", u"\n"
"Beam Stops OUT\n"
"", None))
#if QT_CONFIG(tooltip)
        self.pb_mll_sample_out.setToolTip(QCoreApplication.translate("window", u"moves sbz, sbx, vmll_vz and vmll_hz", None))
#endif // QT_CONFIG(tooltip)
        self.pb_mll_sample_out.setText(QCoreApplication.translate("window", u"\n"
"MLL Sample OUT\n"
"", None))
        self.pb_mll_bs_in.setText(QCoreApplication.translate("window", u"\n"
"Beam Stops IN\n"
"", None))
        self.pb_mll_cam11_view.setText(QCoreApplication.translate("window", u"\n"
"MLL to CAM 11 View\n"
"", None))
        self.pb_mll_osa_in.setText(QCoreApplication.translate("window", u"OSA IN (-X)", None))
        self.pb_mll_nanobeam.setText(QCoreApplication.translate("window", u"\n"
"MLL to Nanobeam\n"
"", None))
        self.pb_mll_lens_in.setText(QCoreApplication.translate("window", u"\n"
"Lenses IN\n"
"", None))
#if QT_CONFIG(tooltip)
        self.pb_mll_sample_in.setToolTip(QCoreApplication.translate("window", u"moves sbx, vmll_vz and vmll_hz", None))
#endif // QT_CONFIG(tooltip)
        self.pb_mll_sample_in.setText(QCoreApplication.translate("window", u"\n"
"MLL Sample IN\n"
"", None))
        self.pb_mlls_to_upstream.setText(QCoreApplication.translate("window", u"\n"
"MLLs to Upstream\n"
"", None))
        self.pb_mlls_to_downstream.setText(QCoreApplication.translate("window", u"\n"
"MLLs to Downstream\n"
"", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("window", u"MLL Focusing ", None))
        self.label_121.setText(QCoreApplication.translate("window", u"Elem:", None))
        self.cb_linearflag_mll_focus.setText(QCoreApplication.translate("window", u"Linear Flag", None))
        self.cb_mll_z_motor_move.setItemText(0, QCoreApplication.translate("window", u"sbz", None))
        self.cb_mll_z_motor_move.setItemText(1, QCoreApplication.translate("window", u"hz", None))
        self.cb_mll_z_motor_move.setItemText(2, QCoreApplication.translate("window", u"vz", None))

        self.label_4.setText(QCoreApplication.translate("window", u"to", None))
        self.dsb_mll_z_target_pos.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_83.setText(QCoreApplication.translate("window", u"FlyScan Param.", None))
        self.cb_mll_foucs_mtr.setItemText(0, QCoreApplication.translate("window", u"dssx", None))
        self.cb_mll_foucs_mtr.setItemText(1, QCoreApplication.translate("window", u"dssy", None))
        self.cb_mll_foucs_mtr.setItemText(2, QCoreApplication.translate("window", u"dssz", None))

        self.cb_mll_foucs_mtr.setCurrentText(QCoreApplication.translate("window", u"dssx", None))
        self.label_111.setText(QCoreApplication.translate("window", u"Start", None))
        self.dsb_mll_foucs_mtr_start.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_113.setText(QCoreApplication.translate("window", u"End", None))
        self.dsb_mll_foucs_mtr_end.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_114.setText(QCoreApplication.translate("window", u"No. of Steps", None))
        self.dsb_mll_foucs_mtr_steps.setSuffix("")
        self.label_120.setText(QCoreApplication.translate("window", u"Dwell Time", None))
        self.label_84.setText(QCoreApplication.translate("window", u"Focus Series with:", None))
        self.cb_mll_z_motor.setItemText(0, QCoreApplication.translate("window", u"sbz", None))
        self.cb_mll_z_motor.setItemText(1, QCoreApplication.translate("window", u"hz", None))
        self.cb_mll_z_motor.setItemText(2, QCoreApplication.translate("window", u"vz", None))

        self.pb_mll_z_focus_start.setText(QCoreApplication.translate("window", u"\n"
"Start Focus Series\n"
"", None))
#if QT_CONFIG(tooltip)
        self.label_116.setToolTip(QCoreApplication.translate("window", u"relative end pos", None))
#endif // QT_CONFIG(tooltip)
        self.label_116.setText(QCoreApplication.translate("window", u"Z End", None))
        self.sb_mll_z_end.setSuffix(QCoreApplication.translate("window", u" um", None))
#if QT_CONFIG(tooltip)
        self.label_115.setToolTip(QCoreApplication.translate("window", u"relative start pos", None))
#endif // QT_CONFIG(tooltip)
        self.label_115.setText(QCoreApplication.translate("window", u"Z Start", None))
        self.sb_mll_z_start.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_117.setText(QCoreApplication.translate("window", u"No. of Steps", None))
        self.sb_mll_z_steps.setSuffix("")
        self.pb_mll_z_focus_move.setText(QCoreApplication.translate("window", u"      Move    ", None))
        self.label_61.setText("")
        self.label_137.setText("")
        self.pb_stop_mll_motion.setText(QCoreApplication.translate("window", u"\n"
"Stop All MLL Motion\n"
"(hmll, vmll,osa,bs,sample stage)\n"
"", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("window", u"MLL_Rot.Center Alignment", None))
        self.label_80.setText("")
        self.label_176.setText(QCoreApplication.translate("window", u"Threshold:", None))
        self.label_87.setText(QCoreApplication.translate("window", u"Angle Range", None))
        self.label_175.setText(QCoreApplication.translate("window", u"Elem:", None))
        self.label_124.setText(QCoreApplication.translate("window", u"Theta Start", None))
        self.sb_mll_rot_angle_start.setSuffix("")
        self.label_173.setText(QCoreApplication.translate("window", u"Theta End", None))
        self.sb_mll_rot_angle_end.setSuffix("")
        self.label_174.setText(QCoreApplication.translate("window", u"No. of Steps", None))
        self.sb_mll_rot_angle_num.setSuffix("")
        self.label_85.setText(QCoreApplication.translate("window", u"FlyScan Param.", None))
        self.label_112.setText(QCoreApplication.translate("window", u"Start", None))
        self.sb_mll_rot_scan_start_2.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_139.setText(QCoreApplication.translate("window", u"End", None))
        self.sb_mll_rot_scan_end_2.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_140.setText(QCoreApplication.translate("window", u"No. of Steps", None))
        self.sb_mll_rot_scan_num.setSuffix("")
        self.label_142.setText(QCoreApplication.translate("window", u"Dwell Time", None))
        self.label_91.setText(QCoreApplication.translate("window", u"sbx", None))
        self.dsb_rot_align_sbx.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pb_rot_align_sbx_move.setText(QCoreApplication.translate("window", u"\n"
"Move\n"
"", None))
        self.label_88.setText(QCoreApplication.translate("window", u"dsth", None))
        self.dsb_rot_align_dsth.setSuffix(QCoreApplication.translate("window", u" deg", None))
        self.pb_rot_align_dsth_move.setText(QCoreApplication.translate("window", u"\n"
"Move\n"
"", None))
        self.label_90.setText(QCoreApplication.translate("window", u"dsz", None))
        self.dsb_rot_align_dsz.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pb_rot_align_dsz_move.setText(QCoreApplication.translate("window", u"\n"
"Move\n"
"", None))
        self.label_86.setText(QCoreApplication.translate("window", u"Correction", None))
        self.label_89.setText(QCoreApplication.translate("window", u"dsx", None))
        self.dsb_rot_align_dsx.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.pb_rot_align_dsx_move.setText(QCoreApplication.translate("window", u"\n"
"Move\n"
"", None))
        self.pb_rot_align_all_move.setText(QCoreApplication.translate("window", u"\n"
"Apply All Corrections \n"
"", None))
        self.pb_mll_rot_align_start.setText(QCoreApplication.translate("window", u"\n"
"Start\n"
"", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("window", u"MLL", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("window", u"S5 (mm)", None))
        self.label_7.setText(QCoreApplication.translate("window", u"Preset positions", None))
        self.pb_S5_Open.setText(QCoreApplication.translate("window", u"   \n"
"  Fully Open\n"
"", None))
        self.pb_S5_Close.setText(QCoreApplication.translate("window", u"  \n"
"  0.3x0.3  \n"
" ", None))
        self.pb_S5_HClose.setText(QCoreApplication.translate("window", u"\n"
"  0.1 x 0.3 \n"
"", None))
        self.pb_S5_VClose.setText(QCoreApplication.translate("window", u"\n"
" 0.3 x 0.1\n"
"", None))
        self.pb_move_s5.setText(QCoreApplication.translate("window", u"\n"
"Move \n"
"", None))
        self.label_184.setText(QCoreApplication.translate("window", u"        SET ", None))
        self.label_126.setText(QCoreApplication.translate("window", u"        RBV", None))
        self.label_8.setText("")
        self.label_182.setText(QCoreApplication.translate("window", u"HGap", None))
        self.db_s5_x_set.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.db_s5_x.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_185.setText(QCoreApplication.translate("window", u"VGap", None))
        self.db_s5_y_set.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.db_s5_y.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_60.setText("")
        self.label_199.setText(QCoreApplication.translate("window", u"Move Relative", None))
        self.pb_s5_hcen_move_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.db_s5_hcen_move.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.pb_s5_hcen_move_positive.setText(QCoreApplication.translate("window", u"  +  ", None))
        self.pb_s5_vcen_move_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.db_s5_vcen_move.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.pb_s5_vcen_move_positive.setText(QCoreApplication.translate("window", u"  +  ", None))
        self.label_195.setText(QCoreApplication.translate("window", u"          RBV", None))
        self.label_197.setText(QCoreApplication.translate("window", u"Hcen", None))
        self.db_s5_hcen_rbv.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_198.setText(QCoreApplication.translate("window", u"Vcen ", None))
        self.db_s5_vcen_rbv.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("window", u"Troubleshooting", None))
        self.label_59.setText("")
        self.label_58.setText("")
        self.pb_peakBeamXY.setText(QCoreApplication.translate("window", u"    Peak the flux    ", None))
        self.pb_recover_from_beamdump.setText(QCoreApplication.translate("window", u"Recover from a beamdump", None))
        self.pb_enable_run.setText(QCoreApplication.translate("window", u"Enable RUN Button", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("window", u"SSA2 (mm)", None))
        self.label_134.setText(QCoreApplication.translate("window", u"\n"
"Preset Positions", None))
        self.pb_SSA2_HClose.setText(QCoreApplication.translate("window", u"\n"
"  0.1x2.1  \n"
"", None))
        self.pb_SSA2_VClose.setText(QCoreApplication.translate("window", u"\n"
"2.1x.1 \n"
"", None))
        self.pb_SSA2_Open.setText(QCoreApplication.translate("window", u"\n"
"     Fully Open\n"
"       ", None))
        self.pb_SSA2_Close.setText(QCoreApplication.translate("window", u"    0.05x0.03    ", None))
        self.label_180.setText(QCoreApplication.translate("window", u"HGap", None))
        self.db_ssa2_x_set.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.db_ssa2_x.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_183.setText(QCoreApplication.translate("window", u"          SET", None))
        self.label_125.setText(QCoreApplication.translate("window", u"          RBV", None))
        self.label_10.setText("")
        self.label_181.setText(QCoreApplication.translate("window", u"VGap", None))
        self.db_ssa2_y_set.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.db_ssa2_y.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.pb_move_ssa2.setText(QCoreApplication.translate("window", u"\n"
"Move   \n"
"", None))
        self.label_127.setText(QCoreApplication.translate("window", u"          RBV", None))
        self.label_186.setText(QCoreApplication.translate("window", u"Hcen", None))
        self.db_ssa2_hcen_rbv.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_187.setText(QCoreApplication.translate("window", u"Vcen ", None))
        self.db_ssa2_vcen_rbv.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.label_128.setText(QCoreApplication.translate("window", u"Move Relative", None))
        self.pb_ssa2_hcen_move_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.db_ssa2_hcen_move.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.pb_ssa2_hcen_move_positive.setText(QCoreApplication.translate("window", u"  +  ", None))
        self.pb_ssa2_vcen_move_neg.setText(QCoreApplication.translate("window", u"-", None))
        self.db_ssa2_vcen_move.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.pb_ssa2_vcen_move_positive.setText(QCoreApplication.translate("window", u"  +  ", None))
        self.pb_center_ssa2.setText(QCoreApplication.translate("window", u"Center SSA2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("window", u"Slits", None))
        self.HXN_GUI_tabs.setTabText(self.HXN_GUI_tabs.indexOf(self.alignment_tab), QCoreApplication.translate("window", u"Alignment", None))
        self.HXN_GUI_tabs.setTabText(self.HXN_GUI_tabs.indexOf(self.tab_3), QCoreApplication.translate("window", u"Log", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("window", u"Upstream Cameras", None))
        self.label_72.setText(QCoreApplication.translate("window", u"     Front End Fluor. Screen     ", None))
        self.label_75.setText(QCoreApplication.translate("window", u"    CAM 06    ", None))
        self.pb_CAM6_OUT.setText(QCoreApplication.translate("window", u"    OUT   ", None))
        self.pb_FS_OUT.setText(QCoreApplication.translate("window", u"    OUT   ", None))
        self.pb_FS_IN.setText(QCoreApplication.translate("window", u" \n"
"    IN     \n"
"", None))
        self.pb_CAM6_IN.setText(QCoreApplication.translate("window", u"   \n"
"  IN    \n"
"", None))
        self.pb_CAM6_LASER.setText(QCoreApplication.translate("window", u"Laser engage position", None))
        self.label_133.setText("")
        self.db_fs.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.db_cam6.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("window", u"Feedbacks", None))
        self.pushButton_2.setText(QCoreApplication.translate("window", u"\n"
" Engage Mirror Feedbacks \n"
"", None))
        self.label_153.setText("")
        self.groupBox_32.setTitle(QCoreApplication.translate("window", u"Set Energy", None))
        self.label_46.setText("")
        self.label_81.setText(QCoreApplication.translate("window", u"  Target Energy: ", None))
        self.dsb_target_e.setSuffix(QCoreApplication.translate("window", u" keV", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("window", u"Estimated Positions", None))
        self.label_150.setText(QCoreApplication.translate("window", u"Harmonic", None))
        self.cb_target_coating.setItemText(0, QCoreApplication.translate("window", u"Cr", None))
        self.cb_target_coating.setItemText(1, QCoreApplication.translate("window", u"Pt", None))
        self.cb_target_coating.setItemText(2, QCoreApplication.translate("window", u"Si", None))
        self.cb_target_coating.setItemText(3, QCoreApplication.translate("window", u"Rh", None))

        self.dsb_target_roll.setSuffix(QCoreApplication.translate("window", u" mrad", None))
        self.label_146.setText(QCoreApplication.translate("window", u"Mirror Coating", None))
        self.label_154.setText(QCoreApplication.translate("window", u"DCM Roll", None))
        self.label_155.setText(QCoreApplication.translate("window", u"HFM Pitch", None))
        self.dsb_hfm_target_pitch.setSuffix(QCoreApplication.translate("window", u" mrad", None))
        self.label_149.setText(QCoreApplication.translate("window", u"Gap", None))
        self.dsb_target_ugap.setSuffix(QCoreApplication.translate("window", u" um", None))
        self.label_132.setText(QCoreApplication.translate("window", u"DCM  Pitch  ", None))
        self.dsb_target_pitch.setSuffix(QCoreApplication.translate("window", u"  mrad", None))
        self.label_148.setText(QCoreApplication.translate("window", u"      Harmonic: ", None))
#if QT_CONFIG(tooltip)
        self.cb_change_energy_only.setToolTip(QCoreApplication.translate("window", u"does not mover mirrors or pitch, ugap and bragg only", None))
#endif // QT_CONFIG(tooltip)
        self.cb_change_energy_only.setText(QCoreApplication.translate("window", u"Change energy only", None))
        self.pb_move_energy.setText(QCoreApplication.translate("window", u"\n"
" Move   \n"
"", None))
        self.label_70.setText(QCoreApplication.translate("window", u"Move Energy with Sid = ", None))
        self.pb_energy_change_w_sid.setText(QCoreApplication.translate("window", u"\n"
" Move \n"
"", None))
        self.label_178.setText(QCoreApplication.translate("window", u"Zone Plate Focus ", None))
        self.dsb_ZPZ1TargetPos_energy.setSuffix(QCoreApplication.translate("window", u" mm", None))
        self.pb_movezpz1_energy.setText(QCoreApplication.translate("window", u"Move ZPZ1", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("window", u"Optmize", None))
        self.label_151.setText(QCoreApplication.translate("window", u"Max. Iter.", None))
        self.cb_beam_at_ssa2.setText(QCoreApplication.translate("window", u"Find beam at SSA2", None))
        self.label_152.setText("")
        self.gb_calib_foil.setTitle(QCoreApplication.translate("window", u"Calibration Foils", None))
        self.HXN_GUI_tabs.setTabText(self.HXN_GUI_tabs.indexOf(self.energy), QCoreApplication.translate("window", u"Energy Change", None))
        ___qtablewidgetitem = self.tw_hxn_contact.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("window", u"Email", None))
        ___qtablewidgetitem1 = self.tw_hxn_contact.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("window", u"Cell", None))
        ___qtablewidgetitem2 = self.tw_hxn_contact.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("window", u"Ext.", None))
        ___qtablewidgetitem3 = self.tw_hxn_contact.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("window", u"Hanfei Yan", None))
        ___qtablewidgetitem4 = self.tw_hxn_contact.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("window", u"Takenori shimamura", None))
        ___qtablewidgetitem5 = self.tw_hxn_contact.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("window", u"Xiaojing Huang", None))
        ___qtablewidgetitem6 = self.tw_hxn_contact.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("window", u"Randy Smith", None))
        ___qtablewidgetitem7 = self.tw_hxn_contact.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("window", u"Ajith Pattammattel", None))

        __sortingEnabled = self.tw_hxn_contact.isSortingEnabled()
        self.tw_hxn_contact.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tw_hxn_contact.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("window", u"hyan@bnl.gov", None))
        ___qtablewidgetitem9 = self.tw_hxn_contact.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("window", u"631-871-2035", None))
        ___qtablewidgetitem10 = self.tw_hxn_contact.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("window", u"7097", None))
        ___qtablewidgetitem11 = self.tw_hxn_contact.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("window", u"tshimamur1@bnl.gov", None))
        ___qtablewidgetitem12 = self.tw_hxn_contact.item(1, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("window", u"934-222-4282", None))
        ___qtablewidgetitem13 = self.tw_hxn_contact.item(2, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("window", u"xjhuang@bnl.gov", None))
        ___qtablewidgetitem14 = self.tw_hxn_contact.item(2, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("window", u"631-355-0360", None))
        ___qtablewidgetitem15 = self.tw_hxn_contact.item(2, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("window", u"8726", None))
        ___qtablewidgetitem16 = self.tw_hxn_contact.item(3, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("window", u"rsmith@bnl.gov", None))
        ___qtablewidgetitem17 = self.tw_hxn_contact.item(3, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("window", u"631-924-2675", None))
        ___qtablewidgetitem18 = self.tw_hxn_contact.item(3, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("window", u"8033", None))
        ___qtablewidgetitem19 = self.tw_hxn_contact.item(4, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("window", u"pattammattel@bnl.gov", None))
        ___qtablewidgetitem20 = self.tw_hxn_contact.item(4, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("window", u"860-713-4321", None))
        ___qtablewidgetitem21 = self.tw_hxn_contact.item(4, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("window", u"6082", None))
        self.tw_hxn_contact.setSortingEnabled(__sortingEnabled)

        self.HXN_GUI_tabs.setTabText(self.HXN_GUI_tabs.indexOf(self.beamline_contacts_tab), QCoreApplication.translate("window", u"Beamline Contacts", None))
        self.menuHelp_2.setTitle(QCoreApplication.translate("window", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("window", u"Options", None))
    # retranslateUi

