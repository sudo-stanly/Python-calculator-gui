# Date         : September 2, 2025
# Project Name : Calculator GUI

## Table of Contents
- [Overview](#overview)
- [Problem ](#problem)
- [Solution](#solution)
- [Features](#features)
- [Program ](#explained)

---

## Overview
This project is a **Graphical User Interface (GUI) Calculator** built using **Python’s Tkinter library**.  
It evaluates a variety of mathematical operations — from simple arithmetic to more advanced ones like square roots, powers, modulo, and even π (pi).  

---

## Problem
Math is everywhere, but not everyone enjoys fumbling with command-line tools or doing it by hand.  
A good calculator should:  
- Be **intuitive** to use.  
- Support both **basic** and **extra** operations.  
- Provide **quick, accurate results**.  
- Have a **clean and friendly interface**.  

---

## Solution
The solution is a **Tkinter-based calculator** that:  
- Provides buttons for digits, operations, and special functions.  
- Ensures safe evaluation of input (filtering invalid characters).  
- Handles errors gracefully (no scary crashes, just “Error” when input is invalid).  
- Mimics the feel of a physical calculator with extra digital perks.  

In short: *math, but with less pain and more clicky buttons.*  

---

## Features
- **Basic operations**: Addition, subtraction, multiplication, division.  
- **Advanced operations**: Square, square root, modulo, percentage, pi.  
- **Utility**: Clear (C), Backspace (⌫).  
- **Error handling**: Displays an error instead of breaking.  

---

## Program
Before the whole logic operation, i designed the calculator with frame as a container for all of the
widgets, rows for buttons and entries from the user. I added a function to the result button "=", for the other buttons i match cased instead of one by one functionalities, and used lamba in order for me to pass an argument to the add character function expression and match cased it. for me to be able to add new characters i used the delete entry and inserted the string that i contained in a variable before deleting the whole entry. i simply did a simple eval and allowed character checking first before the progress, as progress went on modulo, percentage, pi, square, and root symbols became a challenge, i searched for solutions online and formula and got myself more progressed and imported more math logics and re import, i tried different approaches before i was able to finalize, i tried with find, index methods and for loops and got to the point i used if the value is in the input to change each symbols to a proper operation and get properly evaluated.