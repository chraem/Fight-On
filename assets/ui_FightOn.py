# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FightOnbVmwRP.ui'
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
        MainWindow.resize(943, 678)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.gridLayout_4.setObjectName(u"gridLayout_4")
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
        self.lexical_Tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lexical_Tbl.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lexical_Tbl.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lexical_Tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.lexical_Tbl, 0, 0, 1, 1)

        self.rightTabWidget.addTab(self.Lexical, "")
        self.Syntax = QWidget()
        self.Syntax.setObjectName(u"Syntax")
        self.gridLayout_5 = QGridLayout(self.Syntax)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.syntax_Tbl = QTableWidget(self.Syntax)
        if (self.syntax_Tbl.columnCount() < 3):
            self.syntax_Tbl.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.syntax_Tbl.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.syntax_Tbl.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.syntax_Tbl.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.syntax_Tbl.setObjectName(u"syntax_Tbl")
        self.syntax_Tbl.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(51, 69, 83);")
        self.syntax_Tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.syntax_Tbl.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.syntax_Tbl.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.syntax_Tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_5.addWidget(self.syntax_Tbl, 0, 0, 1, 1)

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
        self.botTabWidget = QTabWidget(self.bot_Frame)
        self.botTabWidget.setObjectName(u"botTabWidget")
        self.botTabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: none;")
        self.botTabWidget.setDocumentMode(False)
        self.LexicalError = QWidget()
        self.LexicalError.setObjectName(u"LexicalError")
        self.gridLayout_8 = QGridLayout(self.LexicalError)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lexicalError_Tbl = QTableWidget(self.LexicalError)
        if (self.lexicalError_Tbl.columnCount() < 2):
            self.lexicalError_Tbl.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.lexicalError_Tbl.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.lexicalError_Tbl.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.lexicalError_Tbl.setObjectName(u"lexicalError_Tbl")
        self.lexicalError_Tbl.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(51, 69, 83);")
        self.lexicalError_Tbl.setFrameShape(QFrame.NoFrame)
        self.lexicalError_Tbl.setFrameShadow(QFrame.Plain)
        self.lexicalError_Tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lexicalError_Tbl.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lexicalError_Tbl.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lexicalError_Tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_8.addWidget(self.lexicalError_Tbl, 0, 0, 1, 1)

        self.botTabWidget.addTab(self.LexicalError, "")
        self.SyntaxError = QWidget()
        self.SyntaxError.setObjectName(u"SyntaxError")
        self.gridLayout_9 = QGridLayout(self.SyntaxError)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.syntaxError_Tbl = QTableWidget(self.SyntaxError)
        if (self.syntaxError_Tbl.columnCount() < 3):
            self.syntaxError_Tbl.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.syntaxError_Tbl.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.syntaxError_Tbl.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.syntaxError_Tbl.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.syntaxError_Tbl.setObjectName(u"syntaxError_Tbl")
        self.syntaxError_Tbl.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(51, 69, 83);")
        self.syntaxError_Tbl.setFrameShape(QFrame.NoFrame)
        self.syntaxError_Tbl.setFrameShadow(QFrame.Plain)
        self.syntaxError_Tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.syntaxError_Tbl.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.syntaxError_Tbl.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.syntaxError_Tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_9.addWidget(self.syntaxError_Tbl, 0, 0, 1, 1)

        self.botTabWidget.addTab(self.SyntaxError, "")

        self.verticalLayout_2.addWidget(self.botTabWidget)


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
        self.fileName_Lbl.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.fileName_Lbl)


        self.gridLayout.addWidget(self.top_Frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.rightTabWidget.setCurrentIndex(0)
        self.botTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fight On", None))
        self.codeEditor_PTE.setPlainText("")
        ___qtablewidgetitem = self.lexical_Tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem1 = self.lexical_Tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Lexeme", None));
        ___qtablewidgetitem2 = self.lexical_Tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Token", None));
        self.rightTabWidget.setTabText(self.rightTabWidget.indexOf(self.Lexical), QCoreApplication.translate("MainWindow", u"Lexical", None))
        ___qtablewidgetitem3 = self.syntax_Tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem4 = self.syntax_Tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Production", None));
        ___qtablewidgetitem5 = self.syntax_Tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Set", None));
        self.rightTabWidget.setTabText(self.rightTabWidget.indexOf(self.Syntax), QCoreApplication.translate("MainWindow", u"Syntax", None))
        ___qtablewidgetitem6 = self.lexicalError_Tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem7 = self.lexicalError_Tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        self.botTabWidget.setTabText(self.botTabWidget.indexOf(self.LexicalError), QCoreApplication.translate("MainWindow", u"Lexical Error", None))
        ___qtablewidgetitem8 = self.syntaxError_Tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem9 = self.syntaxError_Tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Production", None));
        ___qtablewidgetitem10 = self.syntaxError_Tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        self.botTabWidget.setTabText(self.botTabWidget.indexOf(self.SyntaxError), QCoreApplication.translate("MainWindow", u"SyntaxError", None))
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

