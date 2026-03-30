from lexer import tokenize

class SetNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"SetNode({self.name}, {self.value})"
    
class SayNode:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"SayNode({self.value})"
    
class IfNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"IfNode ({self.condition}, {self.body})"
    
class InputNode:
    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt
    def __repr__(self):
        return f"InputNode({self.name}, {self.prompt})"
    
class OtherwiseNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"OtherwiseNode({self.condition}, {self.body})"
    
class ElseNode:
    def __init__(self, body):
        self.body = body
    def __repr__(self):
        return f"ElseNode({self.body})"
    
class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"WhileNode({self.condition}, {self.body})"
    
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def consume(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token
    
    def parse(self):
        if not self.tokens:
            return None
        first = self.peek()
        if first.value == "set":
            return self.parse_set()
        elif first.value == "say":
            return self.parse_say()
        elif first.value == "if":
            return self.parse_if()
        elif first.value == "otherwise":
            return self.parse_otherwise()
        elif first.value == "else":
            return self.parse_else()
        elif first.value == "while":
            return self.parse_while()
        return None
    
    def parse_set(self):
        self.consume()
        name = self.consume().value
        self.consume()

        next_token = self.peek()
        if next_token and next_token.value == "button_press":
            self.consume()
            prompt = self.consume().value
            return SetNode(name, prompt)
        else:
            value = self.consume().value
            return SetNode(name, value)
        
    def parse_say(self):
        self.consume()
        value = self.consume().value
        return SayNode(value)
    
    def parse_if(self):
        self.consume()
        left = self.consume().value
        op = self.consume().value
        right = self.consume().value
        condition = (left, op, right)
        body = []
        return IfNode(condition, body)
    
    def parse_otherwise(self):
        self.consume()
        left = self.consume().value
        op = self.consume().value
        right = self.consume().value
        condition = (left, op, right)
        body = []
        return OtherwiseNode(condition, body)
    
    def parse_else(self):
        self.consume()
        body = []
        return ElseNode(body)

    def parse_while(self):
        self.consume()
        left = self.consume().value
        op = self.consume().value
        right = self.consume().value
        condition = (left, op, right)
        body = []
        return WhileNode(condition, body)