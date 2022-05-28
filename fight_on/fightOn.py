import json
import re

with open("reservedWordsAndSymbols.json", "r") as f:
    json_file = json.load(f)

def checkDelim(type, delimName, currentChar):
    delimiterName = json_file[type][delimName]
    delimiters = json_file["RegDef"][str(delimiterName)]
    
    # print("Passed Lexeme:", currentChar)
    # print("Delimiters", delimiters)
  
    if currentChar in delimiters:
        return True
    else:
        return False
    
def checkContent(delimName, currentChar):
    acceptableContent = json_file["RegDef"][str(delimName)]
    
    #print("Current Lexeme:", currentChar)
    #print("Delimiters", acceptableContent)
  
    if currentChar in acceptableContent:
        return True
    else:
        return False
    
def checkPattern( pattern, currentLexeme):
    if re.match(pattern, currentLexeme):
        return True
    else:
        return False
    
def checkStringContent(string):    
    for i in range(len(string)):
        if(i == len(string)):
            break
        elif(string[len(string)-3] == "\\"):
            return "Missing \" (Double quotation)"
        elif(string[i] == "\\" and checkContent("esc_seq", string[i+1]) == True):
            return ""
        elif(string[i] == "\\" and checkContent("esc_seq", string[i+1]) == False):
            return "Unrecognized escaped character: \\" + string[i+1]  
        else:
            continue
        
def checkKeys(delimName, currentLexeme):
    reservedSymbols = json_file[delimName]
    
    if(currentLexeme in reservedSymbols.keys()):
        return True
    else:
        return False
    