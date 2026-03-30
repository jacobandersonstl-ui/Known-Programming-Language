environment = {}
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import tkinter as tk
from tkinter import filedialog
import sys
from lexer import tokenize, Token, KEYWORD, IDENTIFIER, STRING, NUMBER, OPERATOR
from parser import Parser, SetNode, SayNode, IfNode, InputNode, OtherwiseNode, ElseNode, WhileNode

def execute(node):
    if isinstance(node, SetNode):
        environment[node.name] = node.value
    elif isinstance(node, SayNode):
        value = environment.get(node.value, node.value)
        print(value)
    elif isinstance(node, InputNode):
        environment[node.name] = input(node.prompt)

def interpret(line):
    tokens = tokenize(line.strip())
    if not tokens:
        return
    parser = Parser(tokens)
    node = parser.parse()
    if node:
        execute(node)
    
def evaluate_condition_node(node):
    left_raw, op, right_raw = node.condition
    left = environment.get(left_raw, left_raw)
    right = environment.get(right_raw, right_raw)
    if op in ("is", "=="):
        return left == right
    elif op == "!=":
        return left != right
    elif op == ">":
        return float(left) > float(right)
    elif op == "<":
        return float(left) < float(right)
    elif op == ">=":
        return float(left) >= float(right)
    elif op == "<=":
        return float(left) <= float(right)
    return False

def get_indent_level(line):
    return len(line) - len(line.lstrip("\t"))

def run(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    inside_if = False
    if_indent = 0
    condition_true = False
    any_true = False

 
    for line in lines:
        tokens = tokenize(line.strip())
        if not tokens:
            continue

        parser = Parser(tokens)
        node = parser.parse()
 
        if isinstance(node, IfNode):
            inside_if = True
            if_indent = get_indent_level(line)
            any_true = False
            condition_true = evaluate_condition_node(node)
            if condition_true:
                any_true = True
        
        elif isinstance(node, OtherwiseNode):
            if inside_if and not any_true:
                condition_true = evaluate_condition_node(node)
                if condition_true:
                    any_true = True
            else:
                condition_true = False

        elif isinstance(node, ElseNode):
            if inside_if and not any_true:
                condition_true = True
                any_true = True
            else:
                condition_true = False
        
        elif inside_if:
            indent = get_indent_level(line)

            if indent > if_indent:
                if condition_true:
                    interpret(line)
            
            else:
                inside_if = False
                condition_true = False
                any_true = False
                if not isinstance(node, (IfNode, OtherwiseNode, ElseNode)):
                    execute(node)

        else:
            execute(node)

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    filepath = filedialog.askopenfilename(
        title="Select a .KnLAN file",
        filetypes=[("Known Language files", "*.KnLAN"), ("All files", "*.*")]
    )
    root.destroy()
    return filepath

filepath = open_file_dialog()
if filepath:
    run(filepath)
input("\nPress Enter to Close")

#Known Programming Language Interpreter - Copyright Jacob Anderson, 2025
