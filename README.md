# Known Language Documentation
**File extension:** `.KnLAN`  
**Run with:** `known_transpiler yourscript.convo`

---

## Output

```
say "Hello, world!"
say myVariable
```
Prints text or a variable to the terminal.

---

## Comments

```
-- This is a comment, it won't run
```

---

## Variables

```
set x to 5
set name to "Jacob"
set result to x + 10
set active to true
set active to false
```

---

## Global Variables
Used inside functions to access variables defined outside them.

```
make global x, y, health
```

---

## Math & Shortcuts

Standard symbols for math:

| Operation | Example |
|---|---|
| Add | `set x to x + 5` |
| Subtract | `set x to x - 5` |
| Multiply | `set x to x * 5` |
| Divide | `set x to x / 5` |

Shortcut add/subtract:

```
add 2 to x
take 1 from health
```

---

## Booleans

```
set running to True
set done to False
```

Check if True or False in conditions:

```
if running is true:
    say "still going"

if done is false:
    say "not done yet"
```

---

## User Input

```
set name to button_press "What is your name? "
set name to uppercase of name
```

`uppercase of` strips whitespace and makes the value all caps. Useful for comparing inputs.

---

## Conditionals

```
if x > 5:
    say "big number"
else if x == 5:
    say "exactly 5"
else:
    say "small number"
```

Comparison symbols:

| Symbol | Meaning |
|---|---|
| `==` | equals |
| `!=` | not equals |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal |
| `<=` | less than or equal |

---

## Loops

```
repeat 5 times:
    say "hello"

while x < 10:
    add 1 to x
```

---

## Functions

```
make_a_function_called greet:
    say "Hello!"

call greet
```

---

## Stop

```
stop
```
Exits the program immediately.

---

## Full Example Script

```
-- Simple text adventure

set health to 100
set name to "unknown"

make_a_function_called setup:
    make global health, name
    set name to button_press "What is your name? "
    say "Welcome, "
    say name

make_a_function_called game_loop:
    make global health
    set running to true
    while running is true:
        set move to button_press "Go N, S, E, or W? "
        set move to uppercase of move
        if move == "N":
            say "You go north."
            take 1 from health
        else if move == "S":
            say "You go south."
            take 1 from health
        else:
            say "Invalid move."
        if health <= 0:
            say "You died."
            stop

call setup
call game_loop
```

---

## Quick Reference Card

| Known Programming Language | Python |
|---|---|
| `say "hello"` | `print("hello")` |
| `-- comment` | `# comment` |
| `set x to 5` | `x = 5` |
| `set x to true` | `x = True` |
| `add 2 to x` | `x += 2` |
| `take 1 from x` | `x -= 1` |
| `make global x, y` | `global x, y` |
| `set x to button_press "prompt"` | `x = input("prompt")` |
| `set x to uppercase of y` | `x = y.strip().upper()` |
| `x is True` | `x` |
| `x is False` | `not x` |
| `if x > 5:` | `if x > 5:` |
| `else if x == 5:` | `elif x == 5:` |
| `else:` | `else:` |
| `while x < 10:` | `while x < 10:` |
| `repeat 5 times:` | `for _i in range(5):` |
| `make_a_function_called name:` | `def name():` |
| `call name` | `name()` |
| `stop` | `quit()` |

---

*Known Programming Language - Starveil Game Studios*

IMPORTANT!! As of adding this file, only 'say', 'set', comments, and if/otherwise/else statements exist in the actual language.
