# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/look_and_feel.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Look(object):
    def setupUi(self, Look):
        Look.setObjectName("Look")
        Look.resize(588, 406)
        Look.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Look)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Look)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.style_sheet = QtWidgets.QComboBox(self.groupBox)
        self.style_sheet.setObjectName("style_sheet")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.style_sheet)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.look_and_feel = QtWidgets.QComboBox(self.groupBox)
        self.look_and_feel.setObjectName("look_and_feel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.look_and_feel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Look)
        QtCore.QMetaObject.connectSlotsByName(Look)

    def retranslateUi(self, Look):
        _translate = QtCore.QCoreApplication.translate
        Look.setWindowTitle(_translate("Look", "Aparência do sistema"))
        self.groupBox.setTitle(_translate("Look", "Configurações"))
        self.label.setText(_translate("Look", "Cores"))
        self.label_2.setText(_translate("Look", "Estilo"))

