# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Working\Eric\systemtest\updateErrorInfo.ui'
#
# Created: Sun Jul 13 20:01:02 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(697, 573)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 1, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 1, 3, 1, 1)
        self.textEdit_3 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_2.addWidget(self.textEdit_3, 2, 1, 1, 1)
        self.textEdit_4 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_2.addWidget(self.textEdit_4, 2, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 3, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setMaximum(99999999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 3)
        self.gridLayout_2.setRowStretch(2, 3)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_6.addWidget(self.tableView)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 3)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.spinBox, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.textEdit_2)
        Dialog.setTabOrder(self.textEdit_2, self.textEdit_3)
        Dialog.setTabOrder(self.textEdit_3, self.textEdit_4)
        Dialog.setTabOrder(self.textEdit_4, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.pushButton_4)
        Dialog.setTabOrder(self.pushButton_4, self.tableView)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "更新故障信息", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "更新故障信息", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "更新仪器故障", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "现象：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "具体故障现象：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "使用情况：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "故障编号：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "故障部位及原因：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "解决方法：", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "使用中", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "未使用", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "修改并刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "删除并刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "关闭", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
