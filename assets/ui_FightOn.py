# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FightOngmXMFw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(943, 605)
        icon = QIcon()
        icon.addFile(u"FightOnLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: 11pt \"assets\\MonoSpatial.ttf\";")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bg_Frame = QFrame(self.centralwidget)
        self.bg_Frame.setObjectName(u"bg_Frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg_Frame.sizePolicy().hasHeightForWidth())
        self.bg_Frame.setSizePolicy(sizePolicy)
        self.bg_Frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bg_Frame.setFrameShape(QFrame.NoFrame)
        self.bg_Frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.bg_Frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.mid_Frame = QFrame(self.bg_Frame)
        self.mid_Frame.setObjectName(u"mid_Frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mid_Frame.sizePolicy().hasHeightForWidth())
        self.mid_Frame.setSizePolicy(sizePolicy1)
        self.mid_Frame.setStyleSheet(u"background-color:rgb(234, 234, 234);")
        self.mid_Frame.setFrameShape(QFrame.NoFrame)
        self.mid_Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.mid_Frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.codeEditor_Frame = QFrame(self.mid_Frame)
        self.codeEditor_Frame.setObjectName(u"codeEditor_Frame")
        self.codeEditor_Frame.setStyleSheet(u"")
        self.codeEditor_Frame.setFrameShape(QFrame.NoFrame)
        self.codeEditor_Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.codeEditor_Frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineNumberArea_PTE = QPlainTextEdit(self.codeEditor_Frame)
        self.lineNumberArea_PTE.setObjectName(u"lineNumberArea_PTE")
        sizePolicy.setHeightForWidth(self.lineNumberArea_PTE.sizePolicy().hasHeightForWidth())
        self.lineNumberArea_PTE.setSizePolicy(sizePolicy)
        self.lineNumberArea_PTE.setMinimumSize(QSize(40, 0))
        self.lineNumberArea_PTE.setMaximumSize(QSize(50, 16777215))
        self.lineNumberArea_PTE.setStyleSheet(u"background-color:rgb(234, 234, 234);\n"
"border: 1px solid rgb(51, 69, 83);\n"
"border-right: none;")
        self.lineNumberArea_PTE.setFrameShape(QFrame.NoFrame)
        self.lineNumberArea_PTE.setFrameShadow(QFrame.Plain)
        self.lineNumberArea_PTE.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lineNumberArea_PTE.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lineNumberArea_PTE.setReadOnly(True)
        self.lineNumberArea_PTE.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.lineNumberArea_PTE)

        self.codeEditor_PTE = QPlainTextEdit(self.codeEditor_Frame)
        self.codeEditor_PTE.setObjectName(u"codeEditor_PTE")
        self.codeEditor_PTE.setMinimumSize(QSize(478, 393))
        self.codeEditor_PTE.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(51, 69, 83);")
        self.codeEditor_PTE.setFrameShape(QFrame.NoFrame)
        self.codeEditor_PTE.setFrameShadow(QFrame.Plain)
        self.codeEditor_PTE.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.codeEditor_PTE.setBackgroundVisible(False)

        self.horizontalLayout_3.addWidget(self.codeEditor_PTE)


        self.horizontalLayout_2.addWidget(self.codeEditor_Frame)

        self.tokens_Frame = QFrame(self.mid_Frame)
        self.tokens_Frame.setObjectName(u"tokens_Frame")
        self.tokens_Frame.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border: 1px solid rgb(51, 69, 83);")
        self.tokens_Frame.setFrameShape(QFrame.NoFrame)
        self.tokens_Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.tokens_Frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.rightTabWidget = QTabWidget(self.tokens_Frame)
        self.rightTabWidget.setObjectName(u"rightTabWidget")
        self.rightTabWidget.setMinimumSize(QSize(343, 373))
        self.rightTabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: none;")
        self.rightTabWidget.setTabPosition(QTabWidget.North)
        self.rightTabWidget.setTabShape(QTabWidget.Rounded)
        self.rightTabWidget.setTabBarAutoHide(False)
        self.Lexical = QWidget()
        self.Lexical.setObjectName(u"Lexical")
        self.gridLayout_4 = QGridLayout(self.Lexical)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.lexical_Tbl = QTableWidget(self.Lexical)
        if (self.lexical_Tbl.columnCount() < 3):
            self.lexical_Tbl.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.lexical_Tbl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.lexical_Tbl.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.lexical_Tbl.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.lexical_Tbl.setObjectName(u"lexical_Tbl")
        self.lexical_Tbl.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(51, 69, 83);")
        self.lexical_Tbl.setFrameShape(QFrame.NoFrame)
        self.lexical_Tbl.setFrameShadow(QFrame.Plain)
        self.lexical_Tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lexical_Tbl.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lexical_Tbl.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lexical_Tbl.horizontalHeader().setStretchLastSection(True)
        self.lexical_Tbl.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.lexical_Tbl, 0, 0, 1, 1)

        self.rightTabWidget.addTab(self.Lexical, "")
        self.Syntax = QWidget()
        self.Syntax.setObjectName(u"Syntax")
        self.gridLayout_5 = QGridLayout(self.Syntax)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.syntax_PTE = QPlainTextEdit(self.Syntax)
        self.syntax_PTE.setObjectName(u"syntax_PTE")
        self.syntax_PTE.setStyleSheet(u"border: 1px solid rgb(51, 69, 83);")
        self.syntax_PTE.setFrameShape(QFrame.NoFrame)
        self.syntax_PTE.setFrameShadow(QFrame.Plain)
        self.syntax_PTE.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_5.addWidget(self.syntax_PTE, 0, 0, 1, 1)

        self.rightTabWidget.addTab(self.Syntax, "")

        self.horizontalLayout_4.addWidget(self.rightTabWidget)


        self.horizontalLayout_2.addWidget(self.tokens_Frame)


        self.verticalLayout.addWidget(self.mid_Frame)

        self.bot_Frame = QFrame(self.bg_Frame)
        self.bot_Frame.setObjectName(u"bot_Frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bot_Frame.sizePolicy().hasHeightForWidth())
        self.bot_Frame.setSizePolicy(sizePolicy2)
        self.bot_Frame.setMinimumSize(QSize(0, 150))
        self.bot_Frame.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.bot_Frame.setFrameShape(QFrame.NoFrame)
        self.bot_Frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.bot_Frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.error_Tbl = QTableWidget(self.bot_Frame)
        if (self.error_Tbl.columnCount() < 3):
            self.error_Tbl.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.error_Tbl.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.error_Tbl.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.error_Tbl.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.error_Tbl.setObjectName(u"error_Tbl")
        self.error_Tbl.setMouseTracking(False)
        self.error_Tbl.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(51, 69, 83);")
        self.error_Tbl.setFrameShape(QFrame.NoFrame)
        self.error_Tbl.setFrameShadow(QFrame.Plain)
        self.error_Tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.error_Tbl.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.error_Tbl.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.error_Tbl.setSortingEnabled(True)
        self.error_Tbl.setWordWrap(True)
        self.error_Tbl.horizontalHeader().setStretchLastSection(True)
        self.error_Tbl.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.error_Tbl)


        self.verticalLayout.addWidget(self.bot_Frame)


        self.gridLayout.addWidget(self.bg_Frame, 1, 0, 1, 1)

        self.top_Frame = QFrame(self.centralwidget)
        self.top_Frame.setObjectName(u"top_Frame")
        sizePolicy2.setHeightForWidth(self.top_Frame.sizePolicy().hasHeightForWidth())
        self.top_Frame.setSizePolicy(sizePolicy2)
        self.top_Frame.setMinimumSize(QSize(0, 50))
        self.top_Frame.setStyleSheet(u"background-color:rgb(234, 234, 234);")
        self.top_Frame.setFrameShape(QFrame.NoFrame)
        self.top_Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.top_Frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.newFile_Btn = QPushButton(self.top_Frame)
        self.newFile_Btn.setObjectName(u"newFile_Btn")
        self.newFile_Btn.setMinimumSize(QSize(75, 29))
        self.newFile_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newFile_Btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(51, 69, 83);\n"
"	background-color:rgb(234, 234, 234);\n"
"	border: 1px solid rgb(51, 69, 83);\n"
"}")
        self.newFile_Btn.setFlat(True)

        self.horizontalLayout.addWidget(self.newFile_Btn)

        self.openFile_Btn = QPushButton(self.top_Frame)
        self.openFile_Btn.setObjectName(u"openFile_Btn")
        self.openFile_Btn.setMinimumSize(QSize(75, 29))
        self.openFile_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.openFile_Btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(51, 69, 83);\n"
"	background-color:rgb(234, 234, 234);\n"
"	border: 1px solid rgb(51, 69, 83);\n"
"}")
        self.openFile_Btn.setFlat(True)

        self.horizontalLayout.addWidget(self.openFile_Btn)

        self.saveFile_Btn = QPushButton(self.top_Frame)
        self.saveFile_Btn.setObjectName(u"saveFile_Btn")
        self.saveFile_Btn.setMinimumSize(QSize(75, 29))
        self.saveFile_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveFile_Btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(51, 69, 83);\n"
"	background-color:rgb(234, 234, 234);\n"
"	border: 1px solid rgb(51, 69, 83);\n"
"}")
        self.saveFile_Btn.setFlat(True)

        self.horizontalLayout.addWidget(self.saveFile_Btn)

        self.run_Btn = QPushButton(self.top_Frame)
        self.run_Btn.setObjectName(u"run_Btn")
        self.run_Btn.setMinimumSize(QSize(75, 29))
        self.run_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_Btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(51, 69, 83);\n"
"	background-color:rgb(234, 234, 234);\n"
"	border: 1px solid rgb(51, 69, 83);\n"
"}")
        self.run_Btn.setFlat(True)

        self.horizontalLayout.addWidget(self.run_Btn)

        self.horizontalSpacer = QSpacerItem(585, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.fileName_Lbl = QLabel(self.top_Frame)
        self.fileName_Lbl.setObjectName(u"fileName_Lbl")
        self.fileName_Lbl.setStyleSheet(u"")
        self.fileName_Lbl.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.fileName_Lbl)


        self.gridLayout.addWidget(self.top_Frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.rightTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fight On", None))
        self.codeEditor_PTE.setPlainText("")
        ___qtablewidgetitem = self.lexical_Tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem1 = self.lexical_Tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Token", None));
        ___qtablewidgetitem2 = self.lexical_Tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lexeme", None));
        self.rightTabWidget.setTabText(self.rightTabWidget.indexOf(self.Lexical), QCoreApplication.translate("MainWindow", u"Lexical", None))
        self.rightTabWidget.setTabText(self.rightTabWidget.indexOf(self.Syntax), QCoreApplication.translate("MainWindow", u"Syntax", None))
        ___qtablewidgetitem3 = self.error_Tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem4 = self.error_Tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        ___qtablewidgetitem5 = self.error_Tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.newFile_Btn.setText(QCoreApplication.translate("MainWindow", u"New File", None))
#if QT_CONFIG(shortcut)
        self.newFile_Btn.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.openFile_Btn.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
#if QT_CONFIG(shortcut)
        self.openFile_Btn.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.saveFile_Btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.saveFile_Btn.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.run_Btn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(shortcut)
        self.run_Btn.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.fileName_Lbl.setText("")
    # retranslateUi

