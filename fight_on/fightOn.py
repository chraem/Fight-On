from lib2to3.pgen2.token import MINEQUAL, RBRACE
import re
import json
from token import PLUSEQUAL

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
    
def translate(validTokens):   
    validTokens = validTokens.replace("+=", "PLUSEQUAL")
    validTokens = validTokens.replace("-=", "MINEQUAL") 
    validTokens = validTokens.replace("*=", "MULTEQUAL")
    validTokens = validTokens.replace("/=", "DIVEQUAL") 
    validTokens = validTokens.replace("%=", "MODSEQUAL")
    validTokens = validTokens.replace("==", "EQEQUAL") 
    validTokens = validTokens.replace("!=", "NOTEQUAL")
    validTokens = validTokens.replace("++", "INCREMENT")
    validTokens = validTokens.replace("--", "DECREMENT")
    validTokens = validTokens.replace("<=", "LTEQUAL")
    validTokens = validTokens.replace(">=", "GTEQUAL")
    
    return validTokens
    
def revert(cfgSyntax):
    cfgSyntax = cfgSyntax.replace("PLUSEQUAL", "+=")
    cfgSyntax = cfgSyntax.replace("MINEQUAL", "-=") 
    cfgSyntax = cfgSyntax.replace("MULTEQUAL", "*=")
    cfgSyntax = cfgSyntax.replace("DIVEQUAL", "/=") 
    cfgSyntax = cfgSyntax.replace("MODSEQUAL", "%=")
    cfgSyntax = cfgSyntax.replace("EQEQUAL", "==") 
    cfgSyntax = cfgSyntax.replace("NOTEQUAL", "!=")
    cfgSyntax = cfgSyntax.replace("INCREMENT", "++")
    cfgSyntax = cfgSyntax.replace("DECREMENT", "--")
    cfgSyntax = cfgSyntax.replace("LTEQUAL", "<=")
    cfgSyntax = cfgSyntax.replace("GTEQUAL", ">=")
    cfgSyntax = cfgSyntax.replace("MULTIPLY", "STAR")
    cfgSyntax = cfgSyntax.replace("DIVIDE", "SLASH")
    cfgSyntax = cfgSyntax.replace("MODULO", "PERCENT")
    
    return cfgSyntax
    