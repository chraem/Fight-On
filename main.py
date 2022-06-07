
import sys
import re
import json
from fight_on import fightOn, fightOn_lexer, fightOn_parser

from PySide2.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem)
from PySide2.QtCore import Qt
#from PySide2.QtGui import QTable

from assets.ui_FightOn import Ui_MainWindow
    
class MainScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        
        # Initializes UI state
        self.UI.lineNumberArea_PTE.insertPlainText("1")
        self.UI.lineNumberArea_PTE.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.UI.lineNumberArea_PTE.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.UI.lineNumberArea_PTE.verticalScrollBar().setDisabled(True)
        
        # Changes in UI state
        self.UI.codeEditor_PTE.verticalScrollBar().valueChanged.connect(self.numberScroll)
        self.UI.codeEditor_PTE.blockCountChanged.connect(self.numberLine)
        
        # Button press
        self.UI.run_Btn.clicked.connect(self.analyzer)
        self.show()
        
    def numberScroll(self):
        self.UI.lineNumberArea_PTE.verticalScrollBar().setValue(self.UI.codeEditor_PTE.verticalScrollBar().value())
        
    def numberLine(self):
        number_of_text_block = self.UI.codeEditor_PTE.blockCount()
        self.UI.lineNumberArea_PTE.clear()
        self.UI.lineNumberArea_PTE.insertPlainText("1")
        i = 1
        while(i < number_of_text_block):
            i += 1
            self.UI.lineNumberArea_PTE.insertPlainText("\n" + str(i))
            
        self.UI.lineNumberArea_PTE.ensureCursorVisible()
                
    def analyzer(self):
        self.UI.lexicalError_Tbl.setRowCount(0)
        self.UI.lexical_Tbl.setRowCount(0)
        
        lexicalError, lexicalToken = fightOn_lexer.tokenize(self.removeComments() + " _")
        
        for row in range(len(lexicalError)):
                for col in range(3):
                    if("_" in lexicalError[row][col]):
                        del lexicalError[row]
        
        self.printAnalysis(lexicalError, lexicalToken)
        
        if len(lexicalError) == 0:
            fightOn_parser.fightOn_parser(lexicalToken)
        
    def removeComments(self):
        with open("reservedWordsAndSymbols.json", "r") as f:
            jsonFile = json.load(f)
            
        wholeSourceCode = self.UI.codeEditor_PTE.toPlainText()
        
        commentRegex = re.compile(jsonFile["comment"])
        commentlessSourceCode = commentRegex.sub("", wholeSourceCode)
        
        return commentlessSourceCode

            
    def printAnalysis(self, lexicalError, lexicalToken):
        if lexicalToken:
            self.UI.lexical_Tbl.setRowCount(len(lexicalToken))
            self.UI.lexical_Tbl.setColumnCount(len(lexicalToken[0]))

            for row in range(len(lexicalToken)):
                for col in range(3):
                    self.UI.lexical_Tbl.setItem(row, col, QTableWidgetItem(lexicalToken[row][col]))
        else: 
            self.UI.lexical_Tbl.setRowCount(0)
        
        if lexicalError:
            self.UI.lexicalError_Tbl.setRowCount(len(lexicalError))
            self.UI.lexicalError_Tbl.setColumnCount(len(lexicalError[0]))
            
            for row in range(len(lexicalError)):
                for col in range(3):
                    if(lexicalError[row][col] == []):
                        pass
                    else:
                        self.UI.lexicalError_Tbl.setItem(row, col, QTableWidgetItem(lexicalError[row][col]))
        else: 
            self.UI.lexicalError_Tbl.setRowCount(0)
                    
if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainScreen()
    sys.exit(application.exec_())