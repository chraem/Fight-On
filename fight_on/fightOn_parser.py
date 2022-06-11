from lark import Lark

def fightOn_parser(lexicalToken):
    Tokens = []
    
    for token in lexicalToken:
        Tokens.append(token[1].replace(" ", ""))
    
    tokens = " ".join(Tokens)
    
    with open("fight_on\cfg_lark.txt", "r") as file:
        cfgLark = file.read()
    
    cfg = Lark(r"{}".format(cfgLark), start = "program")
    parseTree = cfg.parse(tokens)
    
    return parseTree.pretty()