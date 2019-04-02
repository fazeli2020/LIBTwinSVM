# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI-LIBTwinSVM.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# icons_rc should be imported as follows
from . import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 615)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_win = QtWidgets.QWidget(MainWindow)
        self.main_win.setObjectName("main_win")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_win)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabs = QtWidgets.QTabWidget(self.main_win)
        self.tabs.setEnabled(True)
        self.tabs.setObjectName("tabs")
        self.data_tab = QtWidgets.QWidget()
        self.data_tab.setObjectName("data_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.data_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.data_tab_frame = QtWidgets.QFrame(self.data_tab)
        self.data_tab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_tab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_tab_frame.setObjectName("data_tab_frame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.data_tab_frame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem, 4, 1, 1, 1)
        self.feature_box = QtWidgets.QGroupBox(self.data_tab_frame)
        self.feature_box.setObjectName("feature_box")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.feature_box)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.feature_table = QtWidgets.QTableWidget(self.feature_box)
        self.feature_table.setObjectName("feature_table")
        self.feature_table.setColumnCount(2)
        self.feature_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(1, item)
        self.gridLayout_13.addWidget(self.feature_table, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.feature_box, 4, 0, 1, 1)
        self.import_box = QtWidgets.QGroupBox(self.data_tab_frame)
        self.import_box.setObjectName("import_box")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.import_box)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.header_ha_lay = QtWidgets.QHBoxLayout()
        self.header_ha_lay.setObjectName("header_ha_lay")
        self.header_check = QtWidgets.QCheckBox(self.import_box)
        self.header_check.setChecked(True)
        self.header_check.setObjectName("header_check")
        self.header_ha_lay.addWidget(self.header_check)
        self.sep_label = QtWidgets.QLabel(self.import_box)
        self.sep_label.setObjectName("sep_label")
        self.header_ha_lay.addWidget(self.sep_label)
        self.sep_char_box = QtWidgets.QLineEdit(self.import_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_char_box.sizePolicy().hasHeightForWidth())
        self.sep_char_box.setSizePolicy(sizePolicy)
        self.sep_char_box.setMaximumSize(QtCore.QSize(32, 16777215))
        self.sep_char_box.setMaxLength(1)
        self.sep_char_box.setObjectName("sep_char_box")
        self.header_ha_lay.addWidget(self.sep_char_box)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_ha_lay.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_ha_lay.addItem(spacerItem2)
        self.gridLayout_11.addLayout(self.header_ha_lay, 1, 0, 1, 1)
        self.path_hz_lay = QtWidgets.QHBoxLayout()
        self.path_hz_lay.setObjectName("path_hz_lay")
        self.path_label = QtWidgets.QLabel(self.import_box)
        self.path_label.setObjectName("path_label")
        self.path_hz_lay.addWidget(self.path_label)
        self.path_box = QtWidgets.QLineEdit(self.import_box)
        self.path_box.setObjectName("path_box")
        self.path_hz_lay.addWidget(self.path_box)
        self.open_btn = QtWidgets.QPushButton(self.import_box)
        self.open_btn.setObjectName("open_btn")
        self.path_hz_lay.addWidget(self.open_btn)
        self.gridLayout_11.addLayout(self.path_hz_lay, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.import_box, 0, 0, 1, 2)
        self.info_box = QtWidgets.QGroupBox(self.data_tab_frame)
        self.info_box.setObjectName("info_box")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.info_box)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.feature_label = QtWidgets.QLabel(self.info_box)
        self.feature_label.setObjectName("feature_label")
        self.gridLayout_12.addWidget(self.feature_label, 0, 2, 1, 1)
        self.no_features = QtWidgets.QLabel(self.info_box)
        self.no_features.setObjectName("no_features")
        self.gridLayout_12.addWidget(self.no_features, 0, 3, 1, 1)
        self.class_label = QtWidgets.QLabel(self.info_box)
        self.class_label.setObjectName("class_label")
        self.gridLayout_12.addWidget(self.class_label, 0, 4, 1, 1)
        self.no_classes = QtWidgets.QLabel(self.info_box)
        self.no_classes.setObjectName("no_classes")
        self.gridLayout_12.addWidget(self.no_classes, 0, 5, 1, 1)
        self.samples_label = QtWidgets.QLabel(self.info_box)
        self.samples_label.setObjectName("samples_label")
        self.gridLayout_12.addWidget(self.samples_label, 0, 0, 1, 1)
        self.no_samples = QtWidgets.QLabel(self.info_box)
        self.no_samples.setObjectName("no_samples")
        self.gridLayout_12.addWidget(self.no_samples, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.info_box, 3, 0, 1, 2)
        self.read_box = QtWidgets.QGroupBox(self.data_tab_frame)
        self.read_box.setEnabled(False)
        self.read_box.setObjectName("read_box")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.read_box)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.read_hz_lay = QtWidgets.QHBoxLayout()
        self.read_hz_lay.setObjectName("read_hz_lay")
        self.normalize_box = QtWidgets.QCheckBox(self.read_box)
        self.normalize_box.setEnabled(False)
        self.normalize_box.setObjectName("normalize_box")
        self.read_hz_lay.addWidget(self.normalize_box)
        self.shuffle_box = QtWidgets.QCheckBox(self.read_box)
        self.shuffle_box.setEnabled(False)
        self.shuffle_box.setObjectName("shuffle_box")
        self.read_hz_lay.addWidget(self.shuffle_box)
        self.gridLayout_14.addLayout(self.read_hz_lay, 0, 0, 1, 1)
        self.load_btn = QtWidgets.QPushButton(self.read_box)
        self.load_btn.setEnabled(False)
        self.load_btn.setObjectName("load_btn")
        self.gridLayout_14.addWidget(self.load_btn, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.read_box, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.data_tab_frame, 0, 0, 1, 1)
        self.tabs.addTab(self.data_tab, "")
        self.classify_tab = QtWidgets.QWidget()
        self.classify_tab.setEnabled(False)
        self.classify_tab.setObjectName("classify_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.classify_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.classigy_tab_frame = QtWidgets.QFrame(self.classify_tab)
        self.classigy_tab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.classigy_tab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.classigy_tab_frame.setObjectName("classigy_tab_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.classigy_tab_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.eval_box = QtWidgets.QGroupBox(self.classigy_tab_frame)
        self.eval_box.setObjectName("eval_box")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.eval_box)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cv_rbtn = QtWidgets.QRadioButton(self.eval_box)
        self.cv_rbtn.setChecked(True)
        self.cv_rbtn.setObjectName("cv_rbtn")
        self.gridLayout_6.addWidget(self.cv_rbtn, 0, 0, 1, 1)
        self.tt_split_rbtn = QtWidgets.QRadioButton(self.eval_box)
        self.tt_split_rbtn.setObjectName("tt_split_rbtn")
        self.gridLayout_6.addWidget(self.tt_split_rbtn, 2, 0, 1, 1)
        self.fold_hz_lay = QtWidgets.QHBoxLayout()
        self.fold_hz_lay.setObjectName("fold_hz_lay")
        self.folds_label = QtWidgets.QLabel(self.eval_box)
        self.folds_label.setObjectName("folds_label")
        self.fold_hz_lay.addWidget(self.folds_label)
        self.cv_folds = QtWidgets.QSpinBox(self.eval_box)
        self.cv_folds.setMinimum(1)
        self.cv_folds.setMaximum(10)
        self.cv_folds.setProperty("value", 5)
        self.cv_folds.setObjectName("cv_folds")
        self.fold_hz_lay.addWidget(self.cv_folds)
        self.gridLayout_6.addLayout(self.fold_hz_lay, 1, 0, 1, 1)
        self.tt_percent_hz_lay = QtWidgets.QHBoxLayout()
        self.tt_percent_hz_lay.setObjectName("tt_percent_hz_lay")
        self.tt_percent_label = QtWidgets.QLabel(self.eval_box)
        self.tt_percent_label.setObjectName("tt_percent_label")
        self.tt_percent_hz_lay.addWidget(self.tt_percent_label)
        self.tt_percentage = QtWidgets.QSpinBox(self.eval_box)
        self.tt_percentage.setMinimum(1)
        self.tt_percentage.setMaximum(99)
        self.tt_percentage.setProperty("value", 70)
        self.tt_percentage.setObjectName("tt_percentage")
        self.tt_percent_hz_lay.addWidget(self.tt_percentage)
        self.gridLayout_6.addLayout(self.tt_percent_hz_lay, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.eval_box, 0, 2, 1, 1)
        self.classifiers_box = QtWidgets.QGroupBox(self.classigy_tab_frame)
        self.classifiers_box.setObjectName("classifiers_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.classifiers_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.STSVM_rbtn = QtWidgets.QRadioButton(self.classifiers_box)
        self.STSVM_rbtn.setChecked(True)
        self.STSVM_rbtn.setObjectName("STSVM_rbtn")
        self.gridLayout_2.addWidget(self.STSVM_rbtn, 0, 0, 1, 1)
        self.LSTSVM_rbtn = QtWidgets.QRadioButton(self.classifiers_box)
        self.LSTSVM_rbtn.setObjectName("LSTSVM_rbtn")
        self.gridLayout_2.addWidget(self.LSTSVM_rbtn, 1, 0, 1, 1)
        self.mc_box = QtWidgets.QGroupBox(self.classifiers_box)
        self.mc_box.setEnabled(False)
        self.mc_box.setObjectName("mc_box")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.mc_box)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.mc_hz_lay = QtWidgets.QHBoxLayout()
        self.mc_hz_lay.setObjectName("mc_hz_lay")
        self.ova_rbtn = QtWidgets.QRadioButton(self.mc_box)
        self.ova_rbtn.setObjectName("ova_rbtn")
        self.mc_hz_lay.addWidget(self.ova_rbtn)
        self.ovo_rbtn = QtWidgets.QRadioButton(self.mc_box)
        self.ovo_rbtn.setObjectName("ovo_rbtn")
        self.mc_hz_lay.addWidget(self.ovo_rbtn)
        self.gridLayout_16.addLayout(self.mc_hz_lay, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.mc_box, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.classifiers_box, 0, 0, 1, 1)
        self.kernel_box = QtWidgets.QGroupBox(self.classigy_tab_frame)
        self.kernel_box.setObjectName("kernel_box")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.kernel_box)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lin_kernel_rbtn = QtWidgets.QRadioButton(self.kernel_box)
        self.lin_kernel_rbtn.setChecked(True)
        self.lin_kernel_rbtn.setObjectName("lin_kernel_rbtn")
        self.gridLayout_7.addWidget(self.lin_kernel_rbtn, 0, 0, 1, 1)
        self.rbf_kernel_rbtn = QtWidgets.QRadioButton(self.kernel_box)
        self.rbf_kernel_rbtn.setObjectName("rbf_kernel_rbtn")
        self.gridLayout_7.addWidget(self.rbf_kernel_rbtn, 1, 0, 1, 1)
        self.rect_kernel_rbtn = QtWidgets.QRadioButton(self.kernel_box)
        self.rect_kernel_rbtn.setObjectName("rect_kernel_rbtn")
        self.gridLayout_7.addWidget(self.rect_kernel_rbtn, 2, 0, 1, 1)
        self.rect_hz_lay = QtWidgets.QHBoxLayout()
        self.rect_hz_lay.setObjectName("rect_hz_lay")
        self.percent_label = QtWidgets.QLabel(self.kernel_box)
        self.percent_label.setObjectName("percent_label")
        self.rect_hz_lay.addWidget(self.percent_label)
        self.rect_kernel_percent = QtWidgets.QSpinBox(self.kernel_box)
        self.rect_kernel_percent.setMinimum(5)
        self.rect_kernel_percent.setProperty("value", 75)
        self.rect_kernel_percent.setObjectName("rect_kernel_percent")
        self.rect_hz_lay.addWidget(self.rect_kernel_percent)
        self.gridLayout_7.addLayout(self.rect_hz_lay, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.kernel_box, 0, 1, 1, 1)
        self.hparam_box = QtWidgets.QGroupBox(self.classigy_tab_frame)
        self.hparam_box.setObjectName("hparam_box")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.hparam_box)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.c1_hz_lay = QtWidgets.QHBoxLayout()
        self.c1_hz_lay.setObjectName("c1_hz_lay")
        self.C1_label = QtWidgets.QLabel(self.hparam_box)
        self.C1_label.setObjectName("C1_label")
        self.c1_hz_lay.addWidget(self.C1_label)
        self.C1_lbound = QtWidgets.QSpinBox(self.hparam_box)
        self.C1_lbound.setMinimum(-10)
        self.C1_lbound.setMaximum(0)
        self.C1_lbound.setProperty("value", -5)
        self.C1_lbound.setObjectName("C1_lbound")
        self.c1_hz_lay.addWidget(self.C1_lbound)
        self.c1_to_label = QtWidgets.QLabel(self.hparam_box)
        self.c1_to_label.setObjectName("c1_to_label")
        self.c1_hz_lay.addWidget(self.c1_to_label)
        self.C1_ubound = QtWidgets.QSpinBox(self.hparam_box)
        self.C1_ubound.setMinimum(1)
        self.C1_ubound.setMaximum(10)
        self.C1_ubound.setProperty("value", 5)
        self.C1_ubound.setObjectName("C1_ubound")
        self.c1_hz_lay.addWidget(self.C1_ubound)
        self.gridLayout_8.addLayout(self.c1_hz_lay, 0, 0, 1, 1)
        self.c2_hz_lay = QtWidgets.QHBoxLayout()
        self.c2_hz_lay.setObjectName("c2_hz_lay")
        self.C2_label = QtWidgets.QLabel(self.hparam_box)
        self.C2_label.setObjectName("C2_label")
        self.c2_hz_lay.addWidget(self.C2_label)
        self.C2_lbound = QtWidgets.QSpinBox(self.hparam_box)
        self.C2_lbound.setMinimum(-10)
        self.C2_lbound.setMaximum(0)
        self.C2_lbound.setProperty("value", -5)
        self.C2_lbound.setObjectName("C2_lbound")
        self.c2_hz_lay.addWidget(self.C2_lbound)
        self.c2_to_label = QtWidgets.QLabel(self.hparam_box)
        self.c2_to_label.setObjectName("c2_to_label")
        self.c2_hz_lay.addWidget(self.c2_to_label)
        self.C2_ubound = QtWidgets.QSpinBox(self.hparam_box)
        self.C2_ubound.setMinimum(1)
        self.C2_ubound.setMaximum(10)
        self.C2_ubound.setProperty("value", 5)
        self.C2_ubound.setObjectName("C2_ubound")
        self.c2_hz_lay.addWidget(self.C2_ubound)
        self.gridLayout_8.addLayout(self.c2_hz_lay, 0, 1, 1, 1)
        self.u_hz_lay = QtWidgets.QHBoxLayout()
        self.u_hz_lay.setObjectName("u_hz_lay")
        self.u_label = QtWidgets.QLabel(self.hparam_box)
        self.u_label.setObjectName("u_label")
        self.u_hz_lay.addWidget(self.u_label)
        self.u_lbound = QtWidgets.QSpinBox(self.hparam_box)
        self.u_lbound.setMinimum(-20)
        self.u_lbound.setMaximum(0)
        self.u_lbound.setProperty("value", -5)
        self.u_lbound.setObjectName("u_lbound")
        self.u_hz_lay.addWidget(self.u_lbound)
        self.u_to_label = QtWidgets.QLabel(self.hparam_box)
        self.u_to_label.setObjectName("u_to_label")
        self.u_hz_lay.addWidget(self.u_to_label)
        self.u_ubound = QtWidgets.QSpinBox(self.hparam_box)
        self.u_ubound.setMinimum(1)
        self.u_ubound.setMaximum(10)
        self.u_ubound.setProperty("value", 5)
        self.u_ubound.setObjectName("u_ubound")
        self.u_hz_lay.addWidget(self.u_ubound)
        self.gridLayout_8.addLayout(self.u_hz_lay, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.hparam_box, 1, 0, 1, 1)
        self.gs_box = QtWidgets.QGroupBox(self.classigy_tab_frame)
        self.gs_box.setObjectName("gs_box")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gs_box)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.elapsed_time = QtWidgets.QLabel(self.gs_box)
        self.elapsed_time.setObjectName("elapsed_time")
        self.gridLayout_9.addWidget(self.elapsed_time, 0, 6, 1, 1)
        self.acc = QtWidgets.QLabel(self.gs_box)
        self.acc.setObjectName("acc")
        self.gridLayout_9.addWidget(self.acc, 0, 4, 1, 1)
        self.run_btn = QtWidgets.QPushButton(self.gs_box)
        self.run_btn.setObjectName("run_btn")
        self.gridLayout_9.addWidget(self.run_btn, 0, 0, 1, 1)
        self.acc_label = QtWidgets.QLabel(self.gs_box)
        self.acc_label.setObjectName("acc_label")
        self.gridLayout_9.addWidget(self.acc_label, 0, 3, 1, 1)
        self.gs_progress_bar = QtWidgets.QProgressBar(self.gs_box)
        self.gs_progress_bar.setProperty("value", 0)
        self.gs_progress_bar.setObjectName("gs_progress_bar")
        self.gridLayout_9.addWidget(self.gs_progress_bar, 1, 0, 1, 6)
        self.best_acc_label = QtWidgets.QLabel(self.gs_box)
        self.best_acc_label.setObjectName("best_acc_label")
        self.gridLayout_9.addWidget(self.best_acc_label, 0, 1, 1, 1)
        self.elapsed_t_label = QtWidgets.QLabel(self.gs_box)
        self.elapsed_t_label.setObjectName("elapsed_t_label")
        self.gridLayout_9.addWidget(self.elapsed_t_label, 0, 5, 1, 1)
        self.best_acc = QtWidgets.QLabel(self.gs_box)
        self.best_acc.setObjectName("best_acc")
        self.gridLayout_9.addWidget(self.best_acc, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.gs_box, 2, 0, 1, 3)
        self.gridLayout_3.addWidget(self.classigy_tab_frame, 1, 0, 2, 1)
        self.tabs.addTab(self.classify_tab, "")
        self.visualize_tab = QtWidgets.QWidget()
        self.visualize_tab.setObjectName("visualize_tab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.visualize_tab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.vis_tab_frame = QtWidgets.QFrame(self.visualize_tab)
        self.vis_tab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vis_tab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vis_tab_frame.setObjectName("vis_tab_frame")
        self.gridLayout_15.addWidget(self.vis_tab_frame, 0, 0, 1, 1)
        self.tabs.addTab(self.visualize_tab, "")
        self.gridLayout_4.addWidget(self.tabs, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.main_win)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 31))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Dataset = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icons/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Dataset.setIcon(icon)
        self.actionOpen_Dataset.setObjectName("actionOpen_Dataset")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_Results = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Results.setIcon(icon2)
        self.actionSave_Results.setObjectName("actionSave_Results")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionView_License = QtWidgets.QAction(MainWindow)
        self.actionView_License.setObjectName("actionView_License")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionView_License)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionOpen_Dataset)
        self.menuFile.addAction(self.actionSave_Results)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LIBTwinSVM"))
        self.feature_box.setTitle(_translate("MainWindow", "Features"))
        item = self.feature_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No"))
        item = self.feature_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.import_box.setTitle(_translate("MainWindow", "Import"))
        self.header_check.setText(_translate("MainWindow", "Header"))
        self.sep_label.setText(_translate("MainWindow", "Separator:"))
        self.sep_char_box.setText(_translate("MainWindow", ","))
        self.path_label.setText(_translate("MainWindow", "Path:"))
        self.open_btn.setText(_translate("MainWindow", "Open"))
        self.info_box.setTitle(_translate("MainWindow", "Info"))
        self.feature_label.setText(_translate("MainWindow", "Features:"))
        self.no_features.setText(_translate("MainWindow", "0"))
        self.class_label.setText(_translate("MainWindow", "Classes:"))
        self.no_classes.setText(_translate("MainWindow", "0"))
        self.samples_label.setText(_translate("MainWindow", "Samples:"))
        self.no_samples.setText(_translate("MainWindow", "0"))
        self.read_box.setTitle(_translate("MainWindow", "Read"))
        self.normalize_box.setText(_translate("MainWindow", "Normalize"))
        self.shuffle_box.setText(_translate("MainWindow", "Shuffle"))
        self.load_btn.setText(_translate("MainWindow", "Load"))
        self.tabs.setTabText(self.tabs.indexOf(self.data_tab), _translate("MainWindow", "Data"))
        self.eval_box.setTitle(_translate("MainWindow", "Evaluation"))
        self.cv_rbtn.setText(_translate("MainWindow", "Cross-validation"))
        self.tt_split_rbtn.setText(_translate("MainWindow", "Train/Test split"))
        self.folds_label.setText(_translate("MainWindow", "Folds:"))
        self.tt_percent_label.setText(_translate("MainWindow", "Percentage:"))
        self.classifiers_box.setTitle(_translate("MainWindow", "Classifiers"))
        self.STSVM_rbtn.setText(_translate("MainWindow", "Standard TwinSVM"))
        self.LSTSVM_rbtn.setText(_translate("MainWindow", "Least Squares TwinSVM"))
        self.mc_box.setTitle(_translate("MainWindow", "Multi-class scheme"))
        self.ova_rbtn.setText(_translate("MainWindow", "One-vs-All"))
        self.ovo_rbtn.setText(_translate("MainWindow", "One-vs-One"))
        self.kernel_box.setTitle(_translate("MainWindow", "Kernel"))
        self.lin_kernel_rbtn.setText(_translate("MainWindow", "Linear"))
        self.rbf_kernel_rbtn.setText(_translate("MainWindow", "RBF"))
        self.rect_kernel_rbtn.setText(_translate("MainWindow", "Rectangular"))
        self.percent_label.setText(_translate("MainWindow", "Percentage:"))
        self.hparam_box.setTitle(_translate("MainWindow", "Hyper-Parameters"))
        self.C1_label.setText(_translate("MainWindow", "C1:"))
        self.c1_to_label.setText(_translate("MainWindow", "to"))
        self.C2_label.setText(_translate("MainWindow", "C2:"))
        self.c2_to_label.setText(_translate("MainWindow", "to"))
        self.u_label.setText(_translate("MainWindow", "<html><head/><body><p>u:</p></body></html>"))
        self.u_to_label.setText(_translate("MainWindow", "to"))
        self.gs_box.setTitle(_translate("MainWindow", "Grid Search"))
        self.elapsed_time.setText(_translate("MainWindow", "00:00:00"))
        self.acc.setText(_translate("MainWindow", "0.0"))
        self.run_btn.setText(_translate("MainWindow", "Run!"))
        self.acc_label.setText(_translate("MainWindow", "Acc:"))
        self.best_acc_label.setText(_translate("MainWindow", "Best Acc:"))
        self.elapsed_t_label.setText(_translate("MainWindow", "Elapsed:"))
        self.best_acc.setText(_translate("MainWindow", "0.0"))
        self.tabs.setTabText(self.tabs.indexOf(self.classify_tab), _translate("MainWindow", "Classify"))
        self.tabs.setTabText(self.tabs.indexOf(self.visualize_tab), _translate("MainWindow", "Visualize"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Dataset.setText(_translate("MainWindow", "Open Dataset"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Click to exit the application."))
        self.actionSave_Results.setText(_translate("MainWindow", "Save Results"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionView_License.setText(_translate("MainWindow", "View License "))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

