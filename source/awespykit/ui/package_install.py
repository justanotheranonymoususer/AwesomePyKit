# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package_install.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_package_install(object):
    def setupUi(self, package_install):
        package_install.setObjectName("package_install")
        package_install.setWindowModality(QtCore.Qt.WindowModal)
        package_install.resize(393, 416)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        package_install.setFont(font)
        package_install.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(package_install)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.uiLabel_target_environment = QtWidgets.QLabel(self.centralwidget)
        self.uiLabel_target_environment.setFrameShape(QtWidgets.QFrame.Box)
        self.uiLabel_target_environment.setObjectName("uiLabel_target_environment")
        self.horizontalLayout.addWidget(self.uiLabel_target_environment)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.uiHorizontalLayout_package_name = QtWidgets.QHBoxLayout()
        self.uiHorizontalLayout_package_name.setSpacing(8)
        self.uiHorizontalLayout_package_name.setObjectName("uiHorizontalLayout_package_name")
        self.pte_package_names_old = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pte_package_names_old.setObjectName("pte_package_names_old")
        self.uiHorizontalLayout_package_name.addWidget(self.pte_package_names_old)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_including_pre = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_including_pre.setObjectName("cb_including_pre")
        self.verticalLayout_2.addWidget(self.cb_including_pre)
        self.cb_install_for_user = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_install_for_user.setObjectName("cb_install_for_user")
        self.verticalLayout_2.addWidget(self.cb_install_for_user)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.pb_load_from_text = QtWidgets.QPushButton(self.centralwidget)
        self.pb_load_from_text.setObjectName("pb_load_from_text")
        self.verticalLayout_2.addWidget(self.pb_load_from_text)
        self.pb_save_as_text = QtWidgets.QPushButton(self.centralwidget)
        self.pb_save_as_text.setObjectName("pb_save_as_text")
        self.verticalLayout_2.addWidget(self.pb_save_as_text)
        self.pb_do_install = QtWidgets.QPushButton(self.centralwidget)
        self.pb_do_install.setMinimumSize(QtCore.QSize(0, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pb_do_install.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pb_do_install.setFont(font)
        self.pb_do_install.setObjectName("pb_do_install")
        self.verticalLayout_2.addWidget(self.pb_do_install)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(6, 1)
        self.uiHorizontalLayout_package_name.addLayout(self.verticalLayout_2)
        self.uiHorizontalLayout_package_name.setStretch(0, 1)
        self.verticalLayout_3.addLayout(self.uiHorizontalLayout_package_name)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_use_index_url = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_use_index_url.setObjectName("cb_use_index_url")
        self.verticalLayout.addWidget(self.cb_use_index_url)
        self.le_use_index_url = QtWidgets.QLineEdit(self.centralwidget)
        self.le_use_index_url.setObjectName("le_use_index_url")
        self.verticalLayout.addWidget(self.le_use_index_url)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        package_install.setCentralWidget(self.centralwidget)

        self.retranslateUi(package_install)
        QtCore.QMetaObject.connectSlotsByName(package_install)

    def retranslateUi(self, package_install):
        _translate = QtCore.QCoreApplication.translate
        package_install.setWindowTitle(_translate("package_install", "安装"))
        self.label_3.setToolTip(_translate("package_install", "当前即将安装的包的目标环境。"))
        self.label_3.setText(_translate("package_install", "目标环境："))
        self.label.setText(_translate("package_install", "要安装的包名称（每行一个）："))
        self.cb_including_pre.setToolTip(_translate("package_install", "从网络安装时是否查找包括预发行版和开发版在内的版本。\n"
"如果预发行版或开发版是最新版本，则安装预发行版或开发版。"))
        self.cb_including_pre.setText(_translate("package_install", "包括预发行版和开发版"))
        self.cb_install_for_user.setToolTip(_translate("package_install", "将包安装到系统当前登录的用户的用户目录内。"))
        self.cb_install_for_user.setText(_translate("package_install", "仅为系统当前用户安装"))
        self.pb_load_from_text.setToolTip(_translate("package_install", "从文本文件载入名称及版本等内容。\n"
"例如从常见的requirements.txt文件载入。"))
        self.pb_load_from_text.setText(_translate("package_install", "从文件加载名称"))
        self.pb_save_as_text.setToolTip(_translate("package_install", "将文本框内的内容保存至文本文件。"))
        self.pb_save_as_text.setText(_translate("package_install", "名称保存至文件"))
        self.pb_do_install.setText(_translate("package_install", "开始安装"))
        self.cb_use_index_url.setText(_translate("package_install", "临时使用其他镜像源："))
        self.label_2.setText(_translate("package_install", "名称后支持跟随以下符号限定要安装的版本：\n"
"\"==\"、\">=\"、\"<=\"、\">\"、\"<\"、\",\"\n"
"每行一个名称，名称和限定符中不允许出现空格。\n"
"例如：fastpip>=0.6.2,<0.10.0\n"
"支持将whl文件拖入文本框内以从本地文件安装该包，whl文件需为正确版本。"))
