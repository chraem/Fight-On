
import sys
import re
import json
from fight_on import fightOn

from PySide2.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem)
from PySide2.QtCore import Qt
#from PySide2.QtGui import QTable

from assets.ui_FightOn import Ui_MainWindow

with open("reservedWordsAndSymbols.json", "r") as f:
    jsonFile = json.load(f)
    
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
        self.UI.run_Btn.clicked.connect(self.lexicalAnalyzer)
        
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
                
    def lexicalAnalyzer(self):
        commentlessSourceCode = self.removeComments()
        self.tokenize(commentlessSourceCode + " ")
        
    def removeComments(self):
        wholeSourceCode = self.UI.codeEditor_PTE.toPlainText()
        
        commentRegex = re.compile(jsonFile["comment"])
        commentlessSourceCode = commentRegex.sub("", wholeSourceCode)
        
        return commentlessSourceCode
    
    def tokenize(self, sourceCode):
        clockLength = 10            # before decimal point
        hoverLength = 5             # after decimal point
        identifierMaxLength = 16
        lineNumber = 1
        index = 0
        currentLexeme = ""
        sourceCodeLength = len(sourceCode)
        lexicalError = []
        lexicalToken = []
        
        while(index < sourceCodeLength):
            if(sourceCode[index] == "\n"):
                lineNumber += 1
    
            if(sourceCode[index] == " " or sourceCode[index] == "\t" or sourceCode[index] == "\n"):
                index += 1
                continue
            
            # Checking for numbers
            if(sourceCode[index].isdecimal()):                
                while(index < sourceCodeLength and sourceCode[index].isdecimal()):
                    currentLexeme += sourceCode[index]
                    index += 1
                
                # For floating values Part 1
                if(sourceCode[index] == "."):
                    currentLexeme = currentLexeme.lstrip("0")
                    
                    currentLexeme += sourceCode[index]
                    index += 1
                    
                    if(currentLexeme == ""):
                        currentLexeme = "0"
                        
                    if(len(currentLexeme) > clockLength):
                        lexicalError.append([str(lineNumber), "L1", "Maximum length exceeded"])
                        lexicalToken.append([str(lineNumber), "L1",  currentLexeme])
                    
                    # For floating values Part 2
                    while(index < sourceCodeLength and sourceCode[index].isdecimal()):
                        currentLexeme += sourceCode[index]
                        index += 1
                
                    if(currentLexeme[len(currentLexeme)-1] == "." and fightOn.checkContent("numbersWS", sourceCode[index])):
                        lexicalError.append([str(lineNumber), "L2", "Missing decimal numbers"])
                        lexicalToken.append([str(lineNumber), "L2", currentLexeme])
                        currentLexeme = ""
                    
                    elif(currentLexeme[len(currentLexeme)-1] == "." and (fightOn.checkContent("numbersWS", sourceCode[index]) == False)):
                        lexicalError.append([str(lineNumber), "L3", "Missing decimal numbers"])
                        lexicalToken.append([str(lineNumber), "L3", currentLexeme])
                        currentLexeme = ""
                        
                    elif(fightOn.checkDelim("LD", "hoverlit", sourceCode[index])):
                        if(len(currentLexeme.split(".")[1]) > hoverLength):
                            lexicalError.append([str(lineNumber), "L4", "Maximum decimal number exceeded"])
                            lexicalToken.append([str(lineNumber), "L4", currentLexeme])
                        else:
                            lexicalToken.append([str(lineNumber), "Hover Literal", currentLexeme])
                            currentLexeme = ""
                  
                    else:
                        lexicalError.append([str(lineNumber), "L5", "Unexpected delimiter: "  + sourceCode[index]])
                        lexicalToken.append([str(lineNumber), "L5", currentLexeme])
                        currentLexeme = ""
                
                elif(fightOn.checkDelim("LD", "clocklit", sourceCode[index]) 
                     and fightOn.checkPattern("(\.[\d]+)", currentLexeme) == False):
                    currentLexeme = currentLexeme.lstrip("0")
                    
                    if(currentLexeme == ""):
                        currentLexeme = "0"
                    
                    if(len(currentLexeme) > clockLength):
                        lexicalError.append([str(lineNumber), "L6", "Clock literal exceeded the maximum length"])
                        lexicalToken.append([str(lineNumber), "L6", currentLexeme])
                        currentLexeme = ""
                    else:
                        lexicalToken.append([str(lineNumber), "Clock Literal", currentLexeme])
                        currentLexeme = ""
                
                else:
                    lexicalError.append([str(lineNumber), "L7", "Unexpected delimiter: "  + sourceCode[index]])
                    lexicalToken.append([str(lineNumber), "L7", currentLexeme + sourceCode[index]])
                    currentLexeme = ""
            
            elif(sourceCode[index] == "."):
                currentLexeme += sourceCode[index]
                index += 1
                
                while(index < sourceCodeLength and sourceCode[index].isdecimal()):
                    currentLexeme += sourceCode[index]
                    index += 1
                
                if(currentLexeme[0] == "." and fightOn.checkPattern("(\.[\d]+)", currentLexeme)):
                    lexicalError.append([str(lineNumber), "L8", "Missing whole numbers"])
                    lexicalToken.append([str(lineNumber), "L8", currentLexeme])
                    currentLexeme = ""
            
            # For String and Char Literals
            elif(sourceCode[index] == "'"):
                currentLexeme += sourceCode[index]
                index += 1
                
                while(index < sourceCodeLength ):
                    currentLexeme += sourceCode[index]
                    index += 1
                    
                    if(currentLexeme[0] == currentLexeme[len(currentLexeme)-1]):
                        break
                      
                if(currentLexeme[0] != currentLexeme[len(currentLexeme)-1] ):
                    print("currentLexeme(rune): ",currentLexeme[0])
                    print("currentLexeme(rune): ",currentLexeme[len(currentLexeme)-2])
                    lexicalError.append([str(lineNumber), "L9", "Missing ' (Single quotation)"])
                    lexicalToken.append([str(lineNumber), "L9", currentLexeme])
                    currentLexeme = ""
                    
                elif(currentLexeme[0] == "'"):
                    if(len(currentLexeme) > 3 + ( 1 if currentLexeme[1] == "\\" else 0)):
                        print(currentLexeme)
                        print(len(currentLexeme))
                        lexicalError.append([str(lineNumber), "L10", "Rune literal exceeded its maximum length"])
                        lexicalToken.append([str(lineNumber), "L10", currentLexeme])
                        currentLexeme = ""
                        
                    elif(currentLexeme[1] == "\\"):
                        if(fightOn.checkContent("esc_seq", currentLexeme[2]) == False):
                            lexicalError.append([str(lineNumber), "L11", "Unrecognized escaped character: \\" + currentLexeme[2]])
                            lexicalToken.append([str(lineNumber), "L11", currentLexeme])
                            currentLexeme = ""
                            
                    elif(fightOn.checkDelim("LD", "runelit", sourceCode[index])):
                        lexicalToken.append([str(lineNumber), "Rune Literal", currentLexeme])
                        currentLexeme = ""
                    else:
                        lexicalError.append([str(lineNumber), "L12", "Unexpected delimiter: " + sourceCode[index]])
                        lexicalToken.append([str(lineNumber), "L12", currentLexeme])
                        currentLexeme = ""
                    
                else:
                    lexicalError.append(str(lineNumber), "L13", "Unexpected delimiter: " + sourceCode[index])
                    lexicalToken.append(str(lineNumber), "L13", currentLexeme)
                    currentLexeme = ""
            
            elif(sourceCode[index] == "\""):
                currentLexeme += sourceCode[index]
                index += 1
                    
                while(index < sourceCodeLength and sourceCode[index] != "\n"):
                    currentLexeme += sourceCode[index]
                    index += 1
                    
                    if(currentLexeme[0] == currentLexeme[len(currentLexeme)-1]):
                        currentLexeme += sourceCode[index]
                        index += 1
                        break
           
                if(currentLexeme[0] != currentLexeme[len(currentLexeme)-2]):
                    lexicalError.append([str(lineNumber), "L14", "Missing \" (Double quotation)"])
                    lexicalToken.append([str(lineNumber), "L14", currentLexeme])
                    currentLexeme = ""
                
                elif("\\" in currentLexeme):
                    errorMessagge = fightOn.checkStringContent(currentLexeme)
                    
                    if(errorMessagge != ""):
                        lexicalError.append([str(lineNumber), "L15", errorMessagge])
                        lexicalToken.append([str(lineNumber), "L15", currentLexeme])
                        currentLexeme = ""
                    else:
                        lexicalToken.append([str(lineNumber), "Rope Literal", currentLexeme])
                        currentLexeme = ""
                
                elif(fightOn.checkDelim("LD", "ropelit", sourceCode[index]) and len(currentLexeme) > 2):
                    lexicalToken.append([str(lineNumber), "Rope Literal", currentLexeme])
                    currentLexeme = ""

                else:
                    lexicalError.append([str(lineNumber), "L16", "Unexpected delimiter: " + sourceCode[index]])
                    lexicalToken.append([str(lineNumber), "L16", currentLexeme])
                    currentLexeme = ""
            
            # Reserved Symbol    
            elif(fightOn.checkKeys("RSD", sourceCode[index])):
                currentLexeme += sourceCode[index]
                index += 1
                
                while(index < sourceCodeLength):
                    if(fightOn.checkKeys("RSD", currentLexeme + sourceCode[index])):
                        currentLexeme += sourceCode[index]
                        index += 1
                        
                    elif(fightOn.checkKeys("RSD", currentLexeme)):
                        lexicalToken.append([str(lineNumber), currentLexeme, currentLexeme])
                        currentLexeme = ""
                        break
                        
                    elif(fightOn.checkDelim("RSD", currentLexeme, sourceCode[index])):
                        lexicalError.append([str(lineNumber), "L19", "Unexpected delimiter: " + sourceCode[index]])
                        lexicalToken.append([str(lineNumber), "L19", currentLexeme])
                        currentLexeme = ""
                            
                    else:
                        lexicalError.append([str(lineNumber), "L17", "Unexpected delimiter: " + currentLexeme[len(currentLexeme) - 1]])
                        lexicalToken.append([str(lineNumber), "L17", currentLexeme])
                        currentLexeme = ""
                        break
            
            # Identifiers
            elif(fightOn.checkContent("letters", sourceCode[index])):
                currentLexeme += sourceCode[index]
                index += 1
                
                while(index < sourceCodeLength):
                    if(fightOn.checkKeys("RWD", currentLexeme)):
                        if(fightOn.checkContent("alphanumeric", sourceCode[index])):
                            currentLexeme += sourceCode[index]
                            index += 1
                            continue
                        
                        elif(fightOn.checkDelim("LD", "identifier", sourceCode[index])):
                            lexicalToken.append([str(lineNumber), currentLexeme, currentLexeme])
                            currentLexeme = ""
                            break
                        
                        else:
                            lexicalError.append([str(lineNumber), "L18", "Unexpected delimiter: " + sourceCode[index]])
                            lexicalToken.append([str(lineNumber), "L18", currentLexeme])
                            currentLexeme = ""
                    
                    elif(fightOn.checkContent("alphanumeric", sourceCode[index]) == False):
                        break                        
                    
                    else:
                        
                        currentLexeme += sourceCode[index]
                        index += 1
                        
                
                if(currentLexeme == ""):
                    continue
                
                elif(fightOn.checkDelim("LD", "identifier", sourceCode[index]) == False):
                        lexicalError.append([str(lineNumber), "L19", "Unexpected delimiter: " + sourceCode[index]])
                        lexicalToken.append([str(lineNumber), "L19", currentLexeme])
                        currentLexeme = ""
                
                elif(len(currentLexeme.strip(" ")) > identifierMaxLength):
                    lexicalError.append([str(lineNumber), "L20", currentLexeme + ", an identifier, exceeded its maximum length"])
                    lexicalToken.append([str(lineNumber), "L20", currentLexeme])
                    currentLexeme = ""
                
                else:
                    lexicalToken.append([ str(lineNumber), "Identifier",currentLexeme])
                    currentLexeme = ""
                        
            else:
                currentLexeme += sourceCode[index]
                lexicalError.append([str(lineNumber), "L21", "Can't define: " + currentLexeme])
                index+=1
            
            self.printLexicalAnalysis(lexicalError, lexicalToken)
            
    def printLexicalAnalysis(self, lexicalError, lexicalToken):
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
                    self.UI.lexicalError_Tbl.setItem(row, col, QTableWidgetItem(lexicalError[row][col]))
            
        else: 
            self.UI.lexicalError_Tbl.setRowCount(0)
        
            
            
        

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainScreen()
    sys.exit(application.exec_())