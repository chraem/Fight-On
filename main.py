
import sys
from PySide2.QtWidgets import (QMainWindow, QApplication)
from PySide2.QtCore import Qt

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
        
        

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainScreen()
    sys.exit(application.exec_())