#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from ../ui_src/actiondialog.ui on Tue Apr 27 00:07:01 2010
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_ActionDialog(object):
    def setupUi(self, ActionDialog):
        ActionDialog.setObjectName("ActionDialog")
        ActionDialog.resize(436, 282)
        ActionDialog.setWindowTitle("")
        self.gridLayout = QtGui.QGridLayout(ActionDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pictureLabel = QtGui.QLabel(ActionDialog)
        self.pictureLabel.setText("")
        self.pictureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureLabel.setObjectName("pictureLabel")
        self.gridLayout.addWidget(self.pictureLabel, 1, 0, 1, 2)
        self.actionSelectLabel = QtGui.QLabel(ActionDialog)
        self.actionSelectLabel.setObjectName("actionSelectLabel")
        self.gridLayout.addWidget(self.actionSelectLabel, 4, 0, 1, 1)
        self.actionSelectComboBox = KComboBox(ActionDialog)
        self.actionSelectComboBox.setObjectName("actionSelectComboBox")
        self.actionSelectComboBox.addItem("")
        self.actionSelectComboBox.addItem("")
        self.gridLayout.addWidget(self.actionSelectComboBox, 4, 1, 1, 1)
        self.captionLabel = QtGui.QLabel(ActionDialog)
        self.captionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.captionLabel.setObjectName("captionLabel")
        self.gridLayout.addWidget(self.captionLabel, 0, 0, 1, 2)
        self.tagList = QtGui.QListWidget(ActionDialog)
        self.tagList.setObjectName("tagList")
        self.gridLayout.addWidget(self.tagList, 1, 2, 1, 1)
        self.label = QtGui.QLabel(ActionDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.linkLabel = QtGui.QLabel(ActionDialog)
        self.linkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.linkLabel.setObjectName("linkLabel")
        self.gridLayout.addWidget(self.linkLabel, 3, 2, 1, 1)
        self.actionSelectLabel.setBuddy(self.actionSelectComboBox)

        self.retranslateUi(ActionDialog)
        QtCore.QMetaObject.connectSlotsByName(ActionDialog)

    def retranslateUi(self, ActionDialog):
        self.actionSelectLabel.setText(kdecore.i18n("Actions "))
        self.actionSelectComboBox.setItemText(0, kdecore.i18n("Display image"))
        self.actionSelectComboBox.setItemText(1, kdecore.i18n("Download image"))
        self.captionLabel.setText(kdecore.i18n("Selected image"))
        self.label.setText(kdecore.i18n("Tags:"))
        self.linkLabel.setText(kdecore.i18n("Direct image link"))

from PyKDE4.kdeui import KComboBox
