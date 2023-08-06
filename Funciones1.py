from tkinter import *
from numpy import *
n = 0

def borrarTodo(entry):
    global n
    entry.delete(0,END)
    n = 0


def boton(entry, boton):
    entry.config(state="normal")
    global n
    caracter = boton.cget("text")
    operadores = ["+","-","*","/","(",")","."]
    entry_state = entry.get()

    if entry_state == "Error":
        borrarTodo(entry)
        n = 0
        entry.config(state="readonly")

    if caracter in operadores:
        if entry_state != 0:
            entry_new_state = entry_state + caracter
            borrarTodo(entry)
            entry.insert(0,entry_new_state)
            n = len(entry_new_state)
            entry.config(state="readonly")
        else:
            entry.insert(0,"Error")
            entry.config(state="readonly")
    else:
        match caracter:
            case "DEL":
                if entry_state != 0:
                    entry_new_state = entry_state[:-1]
                    borrarTodo(entry)
                    entry.insert(0,entry_new_state)
                    n = len(entry_new_state) 
                    entry.config(state="readonly")
                else:
                    borrarTodo(entry)
                    entry.insert(0,"Error")
                    entry.config(state="readonly")
            case "AC":
                borrarTodo(entry)
                entry.config(state="readonly")
            case "=":
                try:
                    x = eval(entry_state)
                    x = round(x,6)
                    borrarTodo(entry)
                    entry.insert(0,x)
                    a = str(x)
                    n = int(len(a))
                    entry.config(state="readonly")
                except:
                    borrarTodo(entry)
                    entry.insert(0,"Error")
                    entry.config(state="readonly")
            case _:
                entry.insert(n,(caracter))
                n += 1
                entry.config(state="readonly")
