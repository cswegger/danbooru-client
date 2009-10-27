#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Copyright 2009 Luca Beltrame <einar@heavensinferno.net>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License, under 
#   version 2 of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the
#   Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

'''
File: thumbnailview.py
Author: Luca Beltrame
Description: Main widget to display and download thumbnails
'''

from PyQt4.QtCore import QSize, pyqtSignal, Qt
from PyQt4.QtGui import (QLabel, QWidget, QTableWidget, QVBoxLayout,
                         QHeaderView, QPixmap)

from PyKDE4.kdecore import KUrl
from PyKDE4.kdeui import KUrlLabel

import actiondialog

#TODO: Switch to model/view

class ThumbnailViewItem(QWidget):

    def __init__(self, image=None, url=None, data=None):

        super(ThumbnailViewItem, self).__init__()

        self.label = KUrlLabel()

        self.data = data
        label_text = self.label_text()
        self.label.setUrl(url)

        if image is not None:
            self.label.setPixmap(image)

        self.label.setUseTips(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTipText(KUrl(self.data.full_url).fileName())

        self.__text_label = QLabel()

        self.layout = QVBoxLayout(self)
        self.layout.addStretch()
        self.layout.addWidget(self.label)

        if label_text is not None:
            self.__text_label.setText(label_text)
            # self.layout.addStretch()
            self.layout.addWidget(self.__text_label)

        self.layout.setSpacing(6) # Ugly hack!

    def label_text(self):

        if self.data is not None:
            height = self.data.height
            width = self.data.width
            size = self.data.size / float (1024000)

            width = "Width: %d pixels" % width
            size = "Size: %1.2f Mb" % size
            height = "Height: %d pixels" % height

            text = "\n".join((width, height, size))
        else:
            text = None

        return text


class ThumbnailView(QTableWidget):

    thumbnailDownloaded = pyqtSignal() # To notify changes

    def __init__(self, api_data, preferences, columns=5, parent=None):

        super(ThumbnailView, self).__init__(parent)
        self.setColumnCount(columns)
        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.verticalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.setShowGrid(False)

        self.__max_columns = columns
        self.__column_index = 0
        self.__row_index = 0
        self.__preferences = preferences

        self.api_data = api_data

        self.itemClicked.connect(self.retrieve_url)
        self.api_data.dataDownloaded.connect(self.process_thumbnails)

    def retrieve_url(self, item):

        row = self.currentRow()
        column = self.currentColumn()

        widget = self.cellWidget(row, column)
        pixmap = widget.label.pixmap()

        dialog = actiondialog.ActionDialog(item, pixmap=pixmap,
                                           preferences=self.__preferences,
                                           parent=self)

        if not dialog.exec_():
            return

    def create_image_item(self, pixmap=None, item=None):

        pixmap = QPixmap() if not pixmap else pixmap

        if pixmap.isNull():
            return

        if item is None:
            return

        full_img_url = item.full_url
        item = ThumbnailViewItem(image=pixmap, url=full_img_url,
                                 data=item)
        return item

    def insert_items(self, thumbnail_item):

        if self.__column_index >= self.__max_columns:
            self.__row_index += 1
            self.__column_index = 0

        self.setCellWidget(self.__row_index, self.__column_index, thumbnail_item)
        self.__column_index += 1
        self.resizeRowsToContents()
        self.resizeColumnsToContents()
        thumbnail_item.label.leftClickedUrl.connect(self.retrieve_url)

        self.thumbnailDownloaded.emit()

    def setup_rows(self, item_no):

        result = item_no // self.__max_columns
        self.setRowCount(result+1)

    def process_thumbnails(self, url, pixmap):

        # Empty data is worthless: skip!
        if url.isEmpty() or pixmap.isNull():
            return

        item_url = unicode(url.prettyUrl())
        name = url.fileName()
        post_data = self.api_data.data[item_url]

        item = self.create_image_item(pixmap, post_data)
        self.insert_items(item)

    def display_thumbnails(self):

        self.setup_rows(len(self.api_data.data))

        for item in self.api_data.data:

            self.api_data.get_image(item.thumbnail_url)
