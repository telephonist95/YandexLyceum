# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 414)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 50, 441, 281))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.sortEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sortEdit.setObjectName("sortEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sortEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.roastEdit = QtWidgets.QComboBox(self.formLayoutWidget)
        self.roastEdit.setObjectName("roastEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roastEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.grindingEdit = QtWidgets.QComboBox(self.formLayoutWidget)
        self.grindingEdit.setObjectName("grindingEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.grindingEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.descriptionEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.descriptionEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.priceEdit = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.priceEdit.setMaximum(1000000)
        self.priceEdit.setObjectName("priceEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.priceEdit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.sizeEdit = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.sizeEdit.setMaximum(1000000)
        self.sizeEdit.setObjectName("sizeEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sizeEdit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Сорт"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Помолка"))
        self.label_4.setText(_translate("Form", "Описание"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Объём"))
        self.pushButton.setText(_translate("Form", "Подтвердить"))
