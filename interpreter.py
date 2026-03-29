environment = {}
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import tkinter as tk
from tkinter import filedialog

def interpret(line):
    words = line.split()
    if not words:
        return

    if words[0] == "set":
        if words[3] == "button_press":
            prompt = line.split("button_press", 1)[1].strip().strip('"')
            environment[words[1]] = input(prompt)
        else:
            value = line.split("to", 1)[1].strip().strip('"')
            environment[words[1]] = value
    elif words[0] == "say":
        say_value = line.split("say", 1)[1].strip()
        if say_value.startswith('"'):
            print(say_value.strip('"'))
        elif say_value in environment:
            print(environment[say_value])
        else:
            print(f"Error! '{say_value}' has not been set!")
    elif words[0] == "--":
        return
    
def evaluate_condition(words):
    left = environment.get(words[1], words[1])
    right = environment.get(words[3], words[3].rstrip(':').strip('"'))
    op = words[2]
    if op in ("is", "=="):
        return left == right
    elif op == "!=":
        return left != right
    elif op == ">":
        return left > right
    elif op == "<":
        return left < right
    elif op == ">=":
        return left >= right
    elif op == "<=":
        return left <= right
    return False

def run(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    inside_if = False
    condition_true = False
    any_true = False
 
    for line in lines:
        words = line.split()
        if not words:
            continue
 
        if words[0] == "if":
            inside_if = True
            any_true = False
            condition_true = evaluate_condition(words)
            if condition_true:
                any_true = True
 
        elif words[0] == "otherwise":
            if inside_if and not any_true:
                condition_true = evaluate_condition(words)
                if condition_true:
                    any_true = True
            else:
                condition_true = False
 
        elif words[0] == "else:":
            if inside_if and not any_true:
                condition_true = True
                any_true = True
            else:
                condition_true = False
 
        elif line.startswith("\t") and inside_if:
            if condition_true:
                interpret(line)
 
        else:
            inside_if = False
            condition_true = False
            any_true = False
            interpret(line)

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