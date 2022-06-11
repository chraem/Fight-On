import re
import json

with open("reservedWordsAndSymbols.json", "r") as f:
    json_file = json.load(f)

def checkDelim(type, delimName, currentChar):
    delimiterName = json_file[type][delimName]
    delimiters = json_file["RegDef"][str(delimiterName)]
    
    if currentChar in delimiters:
        return True
    else:
        return False
    
def checkContent(delimName, currentChar):
    acceptableContent = json_file["RegDef"][str(delimName)]
    
    if currentChar in acceptableContent:
        return True
    else:
        return False
    
def checkPattern( pattern, currentLexeme):
    if re.match(pattern, currentLexeme):
        return True
    else:
        return False
        
def checkKeys(delimName, currentLexeme):
    reservedSymbols = json_file[delimName]
    
    if(currentLexeme in reservedSymbols.keys()):
        return True
    else:
        return False
    