#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from ui/connectdialog.ui on Sat Oct 10 16:11:24 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_connectForm(object):
    def setupUi(self, connectForm):
        connectForm.setObjectName("connectForm")
        connectForm.resize(350, 95)
        self.formLayout = QtGui.QFormLayout(connectForm)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.urlLabel = QtGui.QLabel(connectForm)
        self.urlLabel.setObjectName("urlLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.urlLabel)
        self.urlBox = KHistoryComboBox(connectForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlBox.sizePolicy().hasHeightForWidth())
        self.urlBox.setSizePolicy(sizePolicy)
        self.urlBox.setAutoCompletion(True)
        self.urlBox.setObjectName("urlBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.urlBox)
        self.userLabel = QtGui.QLabel(connectForm)
        self.userLabel.setObjectName("userLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.userLabel)
        self.userLineEdit = KLineEdit(connectForm)
        self.userLineEdit.setObjectName("userLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.userLineEdit)
        self.passwordLabel = QtGui.QLabel(connectForm)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.passwordLabel)
        self.passwdLineEdit = KLineEdit(connectForm)
        self.passwdLineEdit.setPasswordMode(True)
        self.passwdLineEdit.setObjectName("passwdLineEdit")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.passwdLineEdit)

        self.retranslateUi(connectForm)
        QtCore.QMetaObject.connectSlotsByName(connectForm)

    def retranslateUi(self, connectForm):
        self.urlLabel.setText(kdecore.i18n("Danbooru URL"))
        self.userLabel.setText(kdecore.i18n("Username"))
        self.userLineEdit.setClickMessage(kdecore.i18n("Danbooru username (optional)"))
        self.passwordLabel.setText(kdecore.i18n("Password"))
        self.passwdLineEdit.setClickMessage(kdecore.i18n("Danbooru password (optional)"))

from PyKDE4.kdeui import KLineEdit, KHistoryComboBox
