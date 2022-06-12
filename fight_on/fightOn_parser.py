from fight_on.fightOn import translate
from lark import Lark

def fightOn_parser(lexicalToken):
    Tokens = []
    
    for token_ in lexicalToken:
        Tokens.append(token_[1].replace(" ", ""))
    
    tokens = " ".join(Tokens)
    
    tokens = translate(tokens)
    
    with open("fight_on\cfg_lark.txt", "r") as file:
        cfgLark = file.read()
    
    cfg = Lark(r"{}".format(cfgLark), start = "program")
    parseTree = cfg.parse(tokens).pretty()
    
    return parseTree