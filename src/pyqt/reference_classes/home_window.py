# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(1366, 697)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HomeWindow.sizePolicy().hasHeightForWidth())
        HomeWindow.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(HomeWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.save_template_btn = QtWidgets.QPushButton(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_template_btn.sizePolicy().hasHeightForWidth())
        self.save_template_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.save_template_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-zapisz-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_template_btn.setIcon(icon)
        self.save_template_btn.setIconSize(QtCore.QSize(30, 30))
        self.save_template_btn.setObjectName("save_template_btn")
        self.gridLayout.addWidget(self.save_template_btn, 4, 8, 1, 1)
        self.next_btn = QtWidgets.QPushButton(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy)
        self.next_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-następny-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon1)
        self.next_btn.setIconSize(QtCore.QSize(40, 40))
        self.next_btn.setObjectName("next_btn")
        self.gridLayout.addWidget(self.next_btn, 0, 2, 1, 1)
        self.total_num_label = QtWidgets.QLabel(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_num_label.sizePolicy().hasHeightForWidth())
        self.total_num_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.total_num_label.setFont(font)
        self.total_num_label.setObjectName("total_num_label")
        self.gridLayout.addWidget(self.total_num_label, 3, 7, 1, 1)
        self.listView = QtWidgets.QListView(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listView.setFont(font)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listView.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 2, 0, 3, 4)
        self.add_product_btn = QtWidgets.QPushButton(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_product_btn.sizePolicy().hasHeightForWidth())
        self.add_product_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.add_product_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-plus-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_product_btn.setIcon(icon2)
        self.add_product_btn.setIconSize(QtCore.QSize(30, 30))
        self.add_product_btn.setObjectName("add_product_btn")
        self.gridLayout.addWidget(self.add_product_btn, 4, 7, 1, 1)
        self.last_btn = QtWidgets.QPushButton(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.last_btn.sizePolicy().hasHeightForWidth())
        self.last_btn.setSizePolicy(sizePolicy)
        self.last_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-ostatni-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.last_btn.setIcon(icon3)
        self.last_btn.setIconSize(QtCore.QSize(40, 40))
        self.last_btn.setObjectName("last_btn")
        self.gridLayout.addWidget(self.last_btn, 0, 3, 1, 1)
        self.beginning_btn = QtWidgets.QPushButton(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beginning_btn.sizePolicy().hasHeightForWidth())
        self.beginning_btn.setSizePolicy(sizePolicy)
        self.beginning_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-pierwszy-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.beginning_btn.setIcon(icon4)
        self.beginning_btn.setIconSize(QtCore.QSize(40, 40))
        self.beginning_btn.setObjectName("beginning_btn")
        self.gridLayout.addWidget(self.beginning_btn, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 9, 1, 1)
        self.prev_btn = QtWidgets.QPushButton(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_btn.sizePolicy().hasHeightForWidth())
        self.prev_btn.setSizePolicy(sizePolicy)
        self.prev_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-poprzedni-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev_btn.setIcon(icon5)
        self.prev_btn.setIconSize(QtCore.QSize(40, 40))
        self.prev_btn.setObjectName("prev_btn")
        self.gridLayout.addWidget(self.prev_btn, 0, 1, 1, 1)
        self.total_words_label = QtWidgets.QLabel(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_words_label.sizePolicy().hasHeightForWidth())
        self.total_words_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.total_words_label.setFont(font)
        self.total_words_label.setObjectName("total_words_label")
        self.gridLayout.addWidget(self.total_words_label, 3, 8, 1, 3)
        self.dateEdit = QtWidgets.QDateEdit(HomeWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2019, 12, 29))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 10, 1, 1)
        self.tableView = QtWidgets.QTableView(HomeWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.tableView.setFont(font)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableView.setSortingEnabled(False)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 7, 1, 4)
        self.customer_completer = QtWidgets.QLineEdit(HomeWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.customer_completer.setFont(font)
        self.customer_completer.setText("")
        self.customer_completer.setObjectName("customer_completer")
        self.gridLayout.addWidget(self.customer_completer, 1, 0, 1, 4)
        self.customer_label = QtWidgets.QLabel(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_label.sizePolicy().hasHeightForWidth())
        self.customer_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.customer_label.setFont(font)
        self.customer_label.setTextFormat(QtCore.Qt.AutoText)
        self.customer_label.setObjectName("customer_label")
        self.gridLayout.addWidget(self.customer_label, 1, 7, 1, 3)
        self.print_btn = QtWidgets.QPushButton(HomeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.print_btn.sizePolicy().hasHeightForWidth())
        self.print_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.print_btn.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/nowyPrzedrostek/images/icons8-drukuj-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_btn.setIcon(icon6)
        self.print_btn.setIconSize(QtCore.QSize(30, 30))
        self.print_btn.setObjectName("print_btn")
        self.gridLayout.addWidget(self.print_btn, 0, 8, 1, 1)

        self.retranslateUi(HomeWindow)
        self.beginning_btn.clicked.connect(HomeWindow._select_first)
        self.prev_btn.clicked.connect(HomeWindow._select_prev)
        self.next_btn.clicked.connect(HomeWindow._select_next)
        self.last_btn.clicked.connect(HomeWindow._select_last)
        self.add_product_btn.clicked.connect(HomeWindow._add_product)
        self.save_template_btn.clicked.connect(HomeWindow._save_template)
        self.print_btn.clicked.connect(HomeWindow._print_invoice)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "Form"))
        self.save_template_btn.setText(_translate("HomeWindow", "Zapisz jako wzorzec"))
        self.total_num_label.setText(_translate("HomeWindow", "Łącznie"))
        self.add_product_btn.setText(_translate("HomeWindow", "Dodaj produkt"))
        self.label_2.setText(_translate("HomeWindow", "Data"))
        self.total_words_label.setText(_translate("HomeWindow", "TextLabel"))
        self.customer_completer.setPlaceholderText(_translate("HomeWindow", "Wyszukaj..."))
        self.customer_label.setText(_translate("HomeWindow", "Wybrany kontrahent:"))
        self.print_btn.setText(_translate("HomeWindow", "Drukuj"))

import resources_rc
