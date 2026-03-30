KEYWORD = "KEYWORD"
IDENTIFIER = "IDENTIFIER"
STRING = "STRING"
NUMBER = "NUMBER"
OPERATOR = "OPERATOR"

class Token:
    def __init__(self, michaeljackson, spiderman):
        self.type = michaeljackson
        self.value = spiderman

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def tokenize(line):
    KEYWORDS = ["set","say", "if", "otherwise", "else", "while", "repeat", "call", "stop", "make", "add", "take", "button_press", "to", "is"]

    tokens = []
    i = 0
    while i < len(line):
        if line[i] == " ":
            i += 1
        
        elif line[i] == '"':
            j = i + 1
            while j < len(line) and line[j] != '"':
                j += i
            tokens.append(Token(STRING, line[i+1:j].strip('"')))
            i = j + 1
        
        else:
            j = i
            while j < len(line) and line[j] not in (' ', '"'):
                j += 1
            word = line[i:j].rstrip(':')
            if not word:
                i += 1
                continue
            if word in KEYWORDS:
                tokens.append(Token(KEYWORD, word))
            elif word.isdigit():
                tokens.append(Token(NUMBER, int(word)))
            elif word:
                tokens.append(Token(IDENTIFIER, word))
            
            i = j

    return tokens
