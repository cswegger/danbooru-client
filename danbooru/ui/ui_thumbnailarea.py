#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from thumbnailarea.ui on Sat Jul 16 10:43:31 2011
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ThumbnailArea(object):
    def setupUi(self, ThumbnailArea):
        ThumbnailArea.setObjectName(_fromUtf8("ThumbnailArea"))
        ThumbnailArea.resize(570, 502)
        ThumbnailArea.setWindowTitle(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(ThumbnailArea)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.thumbnailTabWidget = KTabWidget(ThumbnailArea)
        self.thumbnailTabWidget.setObjectName(_fromUtf8("thumbnailTabWidget"))
        self.gridLayout.addWidget(self.thumbnailTabWidget, 0, 0, 1, 2)
        self.spacerItem = QtGui.QSpacerItem(370, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(self.spacerItem, 1, 0, 1, 1)
        self.nextPageButton = KPushButton(ThumbnailArea)
        self.nextPageButton.setObjectName(_fromUtf8("nextPageButton"))
        self.gridLayout.addWidget(self.nextPageButton, 1, 1, 1, 1)

        self.retranslateUi(ThumbnailArea)
        QtCore.QMetaObject.connectSlotsByName(ThumbnailArea)

    def retranslateUi(self, ThumbnailArea):
        self.nextPageButton.setText(kdecore.i18n(_fromUtf8("Add Page")))

from PyKDE4.kdeui import KPushButton, KTabWidget
