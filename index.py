import tkinter
from tkinter import *
import math
import re

window = Tk()
window.geometry("500x600")
window.title("Calculator")
window.config(bg='white')

def resultsFunc():
    
    userInput = operationEntry.get()

    #* incase of malformed operation like "11 11 + 100" or division by 0
    try:
        allowed_chars = set('0123456789+-*/(). m٪²√Π÷')
        if not all(char in allowed_chars or char == "x" for char in userInput):
            print("Error: Invalid characters in expression")
            return

        if "m" in userInput:   #* modulo
            userInput = userInput.replace("m", "%")

        if "٪" in userInput:   #* percentage
            userInput = re.sub(r'(\d+)٪', r'(\1/100)', userInput)

        if "x²" in userInput:  #* square
            userInput = userInput.replace("x²", "**2")

        if "x" in userInput:   #* multiplication
            userInput = userInput.replace("x", "*")

        if "√" in userInput:   #* square root
            userInput = re.sub(r'√(\d+)', r'math.sqrt(\1)', userInput)

        if "Π" in userInput:   #* pi
            userInput = re.sub(r'(\d+)Π', r'(\1*math.pi)', userInput)
            userInput = userInput.replace("Π", "math.pi")
            
        if "÷" in userInput:   #* division
            userInput = userInput.replace("÷", "/")

        result = eval(userInput)

        resultPrompt.config(state=NORMAL)
        resultPrompt.delete(0, END)
        resultPrompt.insert(0, result)
        resultPrompt.config(state=DISABLED)

        operationEntry.delete(0, END)
        operationEntry.insert(0, result)

        print(f"OPERATION: {userInput} = {result}")

    except:
        resultPrompt.config(state=NORMAL)
        resultPrompt.delete(0, END)
        resultPrompt.insert(0, "ERROR")
        resultPrompt.config(state=DISABLED)
        
        print("OPERATION ERROR!")
    
def deleteFunc():
    operationEntry.delete(0, END)
    
def backspaceFunc():
    operationEntry.delete(len(operationEntry.get())-1, END)

"""
    * hmmmmm...
    * one function for each operator or num, passed in parameter..
    * if statement?
    * clear input then redisplay new input?


    * get current input 
    *       -> add new character 
    *           -> place it in a new variable ..
    *               -> clear the current operation in input then display the new input? 
"""
def addCharacterFunc(expression):
    print(f"expression: {expression}")

    match expression:
        
        #! ROW 1
        case "(":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "("
            operationEntry.insert(0, replaceCurrentValue)
        case ")":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + ")"
            operationEntry.insert(0, replaceCurrentValue)
        case "mod":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "m"
            operationEntry.insert(0, replaceCurrentValue)
        case "Π":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "Π"
            operationEntry.insert(0, replaceCurrentValue)
            
            
        #! ROW 2
        case "7":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "7"
            operationEntry.insert(0, replaceCurrentValue)
        case "8":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "8"
            operationEntry.insert(0, replaceCurrentValue)
        case "9":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "9"
            operationEntry.insert(0, replaceCurrentValue)
        case "÷":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "÷"
            operationEntry.insert(0, replaceCurrentValue)
        case "√":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "√"
            operationEntry.insert(0, replaceCurrentValue)
            
            
        #! ROW 3
        case "4":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "4"
            operationEntry.insert(0, replaceCurrentValue)
        case "5":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "5"
            operationEntry.insert(0, replaceCurrentValue)
        case "6":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "6"
            operationEntry.insert(0, replaceCurrentValue)
        case "x":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "x"
            operationEntry.insert(0, replaceCurrentValue)
        case "x²":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "x²"
            operationEntry.insert(0, replaceCurrentValue)
            
            
        #! ROW 4
        case "1":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "1"
            operationEntry.insert(0, replaceCurrentValue)
        case "2":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "2"
            operationEntry.insert(0, replaceCurrentValue)
        case "3":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "3"
            operationEntry.insert(0, replaceCurrentValue)
        
        case "-":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "-"
            operationEntry.insert(0, replaceCurrentValue)
            
            
        #! ROW 5
        case "0":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "0"
            operationEntry.insert(0, replaceCurrentValue)
        case ".":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "."
            operationEntry.insert(0, replaceCurrentValue)
        case "percentage":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "٪"
            operationEntry.insert(0, replaceCurrentValue)
        
        case "+":
            getInput = operationEntry.get()
            operationEntry.delete(0, END)
            replaceCurrentValue = getInput + "+"
            operationEntry.insert(0, replaceCurrentValue)
    
    print(getInput)
    
    
parentContainer = Frame(
    window,
    width=500,
    height=600,
    bg='#FFFFFF',
    highlightthickness=0, #outline,
    highlightbackground="#cccccc",
    highlightcolor="#cccccc"
)
parentContainer.pack(padx=20, pady=20)
parentContainer.pack_propagate(False)


spaceContainer = Frame(
    parentContainer,
    width=500,
    height=200,
    bg='#F7F4F3',
)
spaceContainer.pack()
spaceContainer.pack_propagate(False)


resultEntry = Frame(
    parentContainer, 
    width=30,
    height=32
)
resultEntry.pack(fill="x", padx=0, pady=0,) 
resultEntry.pack_propagate(False)

resultPrompt = Entry(resultEntry)
resultPrompt = Entry(resultEntry, bg="#F7F4F3", relief="flat", bd=0, highlightthickness=0, font=("Courier New", 30))
resultPrompt.insert(0,'...') #! replace with a variable later  
resultPrompt.pack(fill="x", expand=True, padx=0, pady=0)
resultPrompt.config(state=DISABLED, disabledbackground="#F7F4F3")


spaceContainer2 = Frame(
    parentContainer,
    width=500,
    height=10,
    bg='white',
)
spaceContainer2.pack()
spaceContainer2.pack_propagate(False)


operationEntry = Entry(parentContainer, bg="white",relief="flat",bd=2,highlightthickness=1,font=("Courier New", 18),justify="left", )
operationEntry.insert(0, "") #! sample operation (12 + 93)
operationEntry.pack(fill="x", padx=0, pady=0)


spaceContainer3 = Frame(
    parentContainer,
    width=500,
    height=15,
    bg='white',
)
spaceContainer3.pack()
spaceContainer3.pack_propagate(False)


#! Row 1
row1 = Frame(parentContainer, bg="white")
row1.pack(fill="x", padx=0, pady=0)

cBtn = Button(row1, text="C",   width=8, height=2,  font=("Courier New", 10, "bold"))
cBtn.pack(side=LEFT, padx=2)
cBtn.config(bg="#F3F3F3")
cBtn.config(activebackground="#DFDFDF", command=deleteFunc)

lprBtn = Button(row1, text="(",   width=8, height=2,  font=("Courier New", 10))
lprBtn.pack(side=LEFT, padx=2)
lprBtn.config(bg="#F3F3F3")
lprBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("("))

rprBtn = Button(row1, text=")",   width=8, height=2,  font=("Courier New", 10))
rprBtn.pack(side=LEFT, padx=2)
rprBtn.config(bg="#F3F3F3")
rprBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc(")"))

modBtn = Button(row1, text="mod",   width=8, height=2,  font=("Courier New", 10))
modBtn.pack(side=LEFT, padx=2)
modBtn.config(bg="#F3F3F3")
modBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("mod"))

pieBtn = Button(row1, text="Π",   width=8, height=2,  font=("Courier New", 10))
pieBtn.pack(side=LEFT, padx=2)
pieBtn.config(bg="#F3F3F3")
pieBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("Π"))

#! Row 2
row2 = Frame(parentContainer, bg="white")
row2.pack(fill="x", padx=0, pady=3)

numBtn_7 = Button(row2, text="7",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_7.pack(side=LEFT, padx=2)
numBtn_7.config(bg="#D4D4D4")
numBtn_7.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("7"))

numBtn_8 = Button(row2, text="8",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_8.pack(side=LEFT, padx=2)
numBtn_8.config(bg="#D4D4D4")
numBtn_8.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("8"))

numBtn_9 = Button(row2, text="9",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_9.pack(side=LEFT, padx=2)
numBtn_9.config(bg="#D4D4D4")
numBtn_9.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("9"))

divBtn = Button(row2, text="÷",   width=8, height=2,  font=("Courier New", 10))
divBtn.pack(side=LEFT, padx=2)
divBtn.config(bg="#F3F3F3")
divBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("÷"))

rootBtn = Button(row2, text="√",   width=8, height=2,  font=("Courier New", 10))
rootBtn.pack(side=LEFT, padx=2)
rootBtn.config(bg="#F3F3F3")
rootBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("√"))


#! Row 3
row3 = Frame(parentContainer, bg="white")
row3.pack(fill="x", padx=0, pady=3)

numBtn_4 = Button(row3, text="4",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_4.pack(side=LEFT, padx=2)
numBtn_4.config(bg="#D4D4D4")
numBtn_4.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("4"))

numBtn_5 = Button(row3, text="5",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_5.pack(side=LEFT, padx=2)
numBtn_5.config(bg="#D4D4D4")
numBtn_5.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("5"))

numBtn_6 = Button(row3, text="6",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_6.pack(side=LEFT, padx=2)
numBtn_6.config(bg="#D4D4D4")
numBtn_6.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("6"))

multiplyBtn = Button(row3, text="x",   width=8, height=2,  font=("Courier New", 10))
multiplyBtn.pack(side=LEFT, padx=2)
multiplyBtn.config(bg="#F3F3F3")
multiplyBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("x"))

squareBtn = Button(row3, text="x²",   width=8, height=2,  font=("Courier New", 10))
squareBtn.pack(side=LEFT, padx=2)
squareBtn.config(bg="#F3F3F3")
squareBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("x²"))


#! Row 4
row4 = Frame(parentContainer, bg="white")
row4.pack(fill="x", padx=0, pady=3)

numBtn_1 = Button(row4, text="1",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_1.pack(side=LEFT, padx=2)
numBtn_1.config(bg="#D4D4D4")
numBtn_1.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("1"))

numBtn_2 = Button(row4, text="2",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_2.pack(side=LEFT, padx=2)
numBtn_2.config(bg="#D4D4D4")
numBtn_2.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("2"))

numBtn_3 = Button(row4, text="3",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_3.pack(side=LEFT, padx=2)
numBtn_3.config(bg="#D4D4D4")
numBtn_3.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("3"))

subtractBtn = Button(row4, text="-",   width=8, height=2,  font=("Courier New", 10))
subtractBtn.pack(side=LEFT, padx=2)
subtractBtn.config(bg="#F3F3F3")
subtractBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("-"))

backspaceBtn = Button(row4, text="⌫",   width=8, height=2,  font=("Courier New", 10))
backspaceBtn.pack(side=LEFT, padx=2)
backspaceBtn.config(bg="#F3F3F3")
backspaceBtn.config(activebackground="#DFDFDF", command=backspaceFunc)


#! Row 5
row5 = Frame(parentContainer, bg="white")
row5.pack(fill="x", padx=0, pady=3)

numBtn_0 = Button(row5, text="0",   width=8, height=2,  font=("Courier New", 10, "bold"))
numBtn_0.pack(side=LEFT, padx=2)
numBtn_0.config(bg="#D4D4D4")
numBtn_0.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("0"))

pointBtn = Button(row5, text=".",   width=8, height=2,  font=("Courier New", 10, "bold"))
pointBtn.pack(side=LEFT, padx=2)
pointBtn.config(bg="#D4D4D4")
pointBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("."))

percentageBtn = Button(row5, text="%",   width=8, height=2,  font=("Courier New", 10, "bold"))
percentageBtn.pack(side=LEFT, padx=2)
percentageBtn.config(bg="#D4D4D4")
percentageBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("percentage"))

additionBtn = Button(row5, text="+",   width=8, height=2,  font=("Courier New", 10))
additionBtn.pack(side=LEFT, padx=2)
additionBtn.config(bg="#F3F3F3")
additionBtn.config(activebackground="#DFDFDF", command=lambda: addCharacterFunc("+"))

resultBtn = Button(row5, text="=",   width=8, height=2,  font=("Courier New", 10), foreground="white")
resultBtn.pack(side=LEFT, padx=2)
resultBtn.config(bg="#F24333", activebackground="#C42A1C", activeforeground="white", command=resultsFunc)

window.mainloop()