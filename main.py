import sys
import re
import os
from assets.ui_FightOn import Ui_MainWindow
from fight_on import fightOn_lexer, fightOn_parser
from PySide2.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem, QFileDialog)
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QFont
    
class MainScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        # Initializes UI state
        self.setWindowIcon(QIcon(r"assets\FightOnLogo.png"))
        self.UI.lineNumberArea_PTE.insertPlainText("1")
        self.UI.rightTabWidget.setCurrentWidget(self.UI.Lexical)
        self.UI.lineNumberArea_PTE.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.UI.lineNumberArea_PTE.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.UI.lineNumberArea_PTE.verticalScrollBar().setDisabled(True)
        
        # Changes in UI state
        self.UI.codeEditor_PTE.verticalScrollBar().valueChanged.connect(self.numberScroll)
        self.UI.codeEditor_PTE.blockCountChanged.connect(self.numberLine)
        
        # Button press
        self.UI.newFile_Btn.clicked.connect(self.clearAll)
        self.UI.saveFile_Btn.clicked.connect(self.saveFile)
        self.UI.openFile_Btn.clicked.connect(self.openFile)
        self.UI.run_Btn.clicked.connect(self.analyzer)
        self.show()
    
    def saveFile(self):
        fileDir = self.UI.fileName_Lbl.text()
        
        if(fileDir == ""):
            fileDir, _ = QFileDialog.getSaveFileName(self, caption="Save File", dir=os.path.expanduser("~/Desktop"),
                                                     filter="Text Document (*.txt)")
            if fileDir:
                with open(fileDir, "w") as savedFile:
                    savedFile.write(self.UI.codeEditor_PTE.toPlainText())
            self.UI.fileName_Lbl.setText(fileDir)
        else:
            with open(fileDir, "w") as savedFile:
                savedFile.write(self.UI.codeEditor_PTE.toPlainText())
    
    def openFile(self):
        
        fileDir, _ = QFileDialog.getOpenFileName(self, caption="Open File", dir=os.path.expanduser("~/Desktop"), 
                                               filter="Text Document (*.txt)")
        
        if fileDir:
            with open(fileDir, "r") as openedFile:
                fileContent = openedFile.read()
            
            self.UI.codeEditor_PTE.setPlainText(fileContent)
            self.UI.fileName_Lbl.setText(fileDir)
        
    def clearAll(self):
        self.UI.codeEditor_PTE.setPlainText(""),
        self.UI.error_Tbl.setRowCount(0),
        self.UI.lexical_Tbl.setRowCount(0),
        self.UI.syntax_PTE.setPlainText("")
        self.UI.fileName_Lbl.setText("")
        
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
        self.UI.error_Tbl.setRowCount(0)
        self.UI.lexical_Tbl.setRowCount(0)
        self.UI.syntax_PTE.clear()
        
        lexicalError, lexicalToken = fightOn_lexer.tokenize(self.removeComments() + "  ")
        
        if (self.UI.codeEditor_PTE.toPlainText() and (len(lexicalError) == 0 and lexicalToken != 0)):
            try:
                self.UI.syntax_PTE.insertPlainText(str(fightOn_parser.fightOn_parser(lexicalToken)))
            except Exception as syntaxError:
                errorType = re.findall("'.+'", str(type(syntaxError)))
                errorType = errorType[0].replace("lark.exceptions.", "").replace("'", "")
                
                syntaxError = str(syntaxError)
        
                errorMessage = re.findall("(.+\n *\^)", syntaxError)
                
                try:
                    expectedToken = syntaxError[syntaxError.index("Expected"):]
                    self.UI.syntax_PTE.insertPlainText(errorMessage[0] + "\n" + expectedToken)
                except:
                    pass
                
                print("syntaxError", syntaxError)
                print("errorType", errorType)
                print("errorMessage", errorMessage)
                                
                lexicalError.append(["", errorType, syntaxError.split("\n")[0]])    
        else:
            self.UI.syntax_PTE.insertPlainText("SYNTAX ANALYSIS CAN ONLY BE GENERATED IS LEXICAL ANALYSIS PASSED.")
            
        self.printAnalysis(lexicalError, lexicalToken)
        
    def removeComments(self):          
        wholeSourceCode = self.UI.codeEditor_PTE.toPlainText()
        
        commentRegex = re.compile("(<\/.+\/>)|(\\$.+)|(\\$)")
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
            self.UI.error_Tbl.setRowCount(len(lexicalError))
            self.UI.error_Tbl.setColumnCount(len(lexicalError[0]))
            
            for row in range(len(lexicalError)):
                for col in range(3):
                    if(lexicalError[row][col] == []):
                        pass
                    else:
                        self.UI.error_Tbl.setItem(row, col, QTableWidgetItem(lexicalError[row][col]))
        else: 
            self.UI.error_Tbl.setRowCount(0)
                    
if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainScreen()
    sys.exit(application.exec_())