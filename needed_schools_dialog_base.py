# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'additional_schools_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_additionalSchoolsDialog(object):
    def setupUi(self, additionalSchoolsDialog):
        additionalSchoolsDialog.setObjectName("additionalSchoolsDialog")
        additionalSchoolsDialog.resize(641, 300)
        self.label_cityLayer = QtWidgets.QLabel(additionalSchoolsDialog)
        self.label_cityLayer.setGeometry(QtCore.QRect(10, 10, 101, 20))
        self.label_cityLayer.setObjectName("label_cityLayer")
        self.comboBox_cityLayer = QtWidgets.QComboBox(additionalSchoolsDialog)
        self.comboBox_cityLayer.setGeometry(QtCore.QRect(120, 10, 380, 25))
        self.comboBox_cityLayer.setObjectName("comboBox_cityLayer")
        self.label_schoolsLayer = QtWidgets.QLabel(additionalSchoolsDialog)
        self.label_schoolsLayer.setGeometry(QtCore.QRect(10, 90, 101, 20))
        self.label_schoolsLayer.setObjectName("label_schoolsLayer")
        self.comboBox_schoolsLayer = QtWidgets.QComboBox(additionalSchoolsDialog)
        self.comboBox_schoolsLayer.setGeometry(QtCore.QRect(120, 90, 380, 25))
        self.comboBox_schoolsLayer.setObjectName("comboBox_schoolsLayer")
        self.label_population = QtWidgets.QLabel(additionalSchoolsDialog)
        self.label_population.setGeometry(QtCore.QRect(10, 50, 101, 20))
        self.label_population.setObjectName("label_population")
        self.comboBox_populationField = QtWidgets.QComboBox(additionalSchoolsDialog)
        self.comboBox_populationField.setGeometry(QtCore.QRect(120, 50, 380, 25))
        self.comboBox_populationField.setObjectName("comboBox_populationField")
        self.label_peoplePerSchool = QtWidgets.QLabel(additionalSchoolsDialog)
        self.label_peoplePerSchool.setGeometry(QtCore.QRect(10, 130, 101, 20))
        self.label_peoplePerSchool.setObjectName("label_peoplePerSchool")
        self.spinBox_peoplePerSchool = QtWidgets.QSpinBox(additionalSchoolsDialog)
        self.spinBox_peoplePerSchool.setGeometry(QtCore.QRect(120, 130, 100, 25))
        self.spinBox_peoplePerSchool.setMinimum(1)
        self.spinBox_peoplePerSchool.setMaximum(100000)
        self.spinBox_peoplePerSchool.setProperty("value", 2000)
        self.spinBox_peoplePerSchool.setObjectName("spinBox_peoplePerSchool")
        self.button_execute = QtWidgets.QPushButton(additionalSchoolsDialog)
        self.button_execute.setGeometry(QtCore.QRect(10, 180, 100, 30))
        self.button_execute.setObjectName("button_execute")

        self.retranslateUi(additionalSchoolsDialog)
        QtCore.QMetaObject.connectSlotsByName(additionalSchoolsDialog)

    def retranslateUi(self, additionalSchoolsDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_cityLayer.setText(_translate("additionalSchoolsDialog", "City Layer"))
        self.label_schoolsLayer.setText(_translate("additionalSchoolsDialog", "Schools Layer"))
        self.label_population.setText(_translate("additionalSchoolsDialog", "Population Field"))
        self.label_peoplePerSchool.setText(_translate("additionalSchoolsDialog", "People Per School"))
        self.button_execute.setText(_translate("additionalSchoolsDialog", "Compute"))
