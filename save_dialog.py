# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 148)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 351, 57))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mQgsFileWidget = QgsFileWidget(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mQgsFileWidget.sizePolicy().hasHeightForWidth())
        self.mQgsFileWidget.setSizePolicy(sizePolicy)
        self.mQgsFileWidget.setStorageMode(QgsFileWidget.SaveFile)
        self.mQgsFileWidget.setObjectName("mQgsFileWidget")
        self.gridLayout_2.addWidget(self.mQgsFileWidget, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 2, 0, 1, 1)
        self.mQgsProjectionSelectionWidget = QgsProjectionSelectionWidget(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mQgsProjectionSelectionWidget.sizePolicy().hasHeightForWidth())
        self.mQgsProjectionSelectionWidget.setSizePolicy(sizePolicy)
        self.mQgsProjectionSelectionWidget.setObjectName("mQgsProjectionSelectionWidget")
        self.gridLayout_2.addWidget(self.mQgsProjectionSelectionWidget, 2, 1, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 90, 195, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_ok = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 0, 0, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "選擇輸出檔名："))
        self.label_1.setText(_translate("Dialog", "選擇座標系統："))
        self.btn_ok.setText(_translate("Dialog", "確定"))
        self.btn_cancel.setText(_translate("Dialog", "重置"))
from qgsfilewidget import QgsFileWidget
from qgsprojectionselectionwidget import QgsProjectionSelectionWidget
