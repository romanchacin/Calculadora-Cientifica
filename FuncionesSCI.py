import numpy as np
import math
import sympy as sp
from tkinter import *
import re


trigonometria = ["sin","asin","cos","acos","tan","atan"]
angulos = ["DEG","RAD","° ' " + '""']
logaritmosYexponenciales = ["^","x√","LOG","LN"]
factoriales = ["!","mPn","mCn"]
constantes = ["pi","e"]
todos = ["sin","asin","cos","acos","tan","atan","DEG","RADIAN","° ' " + '""',"^","x√","LOG","LN","!","mPn","mCn","pi","e"]
todosConParentesis = ["sin","asin","cos","acos","tan","atan","^","x√","LOG","LN","mPn","mCn"]
numerosOsimbolos = ["1","2","3","4","5","6","7","8","9","0",".","+","-","*","/","(",")"]
finalesTodos = ["n","s","G","N","°","'",'"',"^","√","G","N","!","P","C","i","e"]
operadores = ["+","-","*","/","(",")","."]
numeros = ["1","2","3","4","5","6","7","8","9","0"]

global estadoGMS
#radianOgrado = "radianes"

def operacionTrigonomentrica(operacion,numero):
    if operacion == "sin":
        resultado = math.sin(math.radians(numero))
    elif operacion == "arcsin":
        resultado = math.asin(math.radians(numero))
    elif operacion == "cos":
        resultado = math.cos(math.radians(numero))
    elif operacion == "arccos":
        resultado = math.acos(math.radians(numero))
    elif operacion == "tan":
        resultado = math.tan(math.radians(numero))
    elif operacion == "arctan":
        resultado = math.atan(math.radians(numero))
    return resultado


def eliminarSiEsGMS(expresion):
    expresion = expresion.get()
    resultadoEnGMS = False
    for i in expresion:
        if i == "°":
            resultadoEnGMS = True
            break
    if resultadoEnGMS:
        expresion.delete(0,END)
        expresion.insert(0,"")
    return resultadoEnGMS

def numero_a_GMS(numero):
    try:
        numero = float(numero)
        grados = int(numero)
        minutos = int((numero - grados) * 60)
        segundos = round((numero - grados - minutos / 60) * 3600, 2)
        resultado = str(grados) + "°" + str(minutos) + "'" + str(segundos) + '"'
        return resultado
    except:
        print(Exception)

def GMS_a_numero(expresion):
    try:
        grados = float(expresion[:expresion.find("°")])   
        minutos = float(expresion[expresion.find("°"):expresion.find("'")])
        segundos = float(expresion[expresion.find("'"):expresion.find('"')])
        resultado = grados + minutos / 60 + segundos / 3600
        return resultado
    except:
        print(Exception)


def calcular(entry,botonRAD):
    global n

#try:

    entry.config(state="normal")
    contenido = entry.get()
    estaEnRADoDEG = modoRADoDEG(botonRAD)
    print(estaEnRADoDEG)
    trigonometria = ["sin","asin","cos","acos","tan","atan"]
    if estaEnRADoDEG == "grados":
        
        contenido = math.radians(contenido)
        resultado = math.evalf(contenido)
        resultado = math.degrees(float(resultado))
        print(resultado)

    else:
        resultado = sp.sympify(contenido)  # Convierte la expresión en una expresión simbólica (no numérica)
        resultado = resultado.evalf()  # Evalúa la expresión numéricamente

    if abs(resultado - round(resultado)) < 1e-10:
        resultado = int(resultado)
    else:
        resultado = round(resultado, 4)

    print(esGMS)
    if esGMS:#estaEnGMS:
        resultado = numero_a_GMS(resultado)

    entry.delete(0, END)
    entry.insert(0, resultado)
    entry.config(state="readonly")
    n = len(str(resultado))
#except Exception as e:
    #print(e)
    entry.delete(0, END)
    entry.insert(0, "Error")

esGMS = False
def cambiar_modo(botonPresionado,botonCambioColor,entry,radianOgrado):
    global esGMS
    #global radianOgrado
    #x = "° ' " + '""'
    state_entry = entry.get()
    texto_boton = botonPresionado.cget("text")
    match texto_boton:
        case "DEG":           
            #state_entry.np.degrees()
            botonPresionado.config(bg="#BDC51B")
            botonCambioColor.config(bg="#2FF574")
            radianOgrado = "grados"
        case "RAD":
            #state_entry.np.radians()
            botonPresionado.config(bg="#BDC51B")
            botonCambioColor.config(bg="#2FF574")
            radianOgrado = "radianes"
        case _:
            pass
    return radianOgrado

def modoRADoDEG(botonRAD):
    global radianOgrado

    #state_entry = entry.get()
    if botonRAD.cget("bg") == "#2FF574":
        radianOgrado = "grados"
    else:
        radianOgrado = "radianes"
    return radianOgrado

# def cambiarGMS(boton):
#     global esGMS
#     print(esGMS)
#     if esGMS == False:
#         esGMS = True
#         boton.config(bg="#BDC51B")
#     else:
#         boton.config(bg="#2FF574")
#         esGMS = False

def cambiarGMS(boton):
    global esGMS
    if esGMS:
        esGMS = False
        boton.config(bg="#2FF574")
        print(esGMS)
    else:
        boton.config(bg="#BDC51B")
        esGMS = True
        print(esGMS)
    return esGMS

n = 0

def borrarTodo(entry):
    global n
    entry.delete(0,END)
    n = 0

def boton(entrySCI,boton):
    entrySCI.config(state="normal") 
    entrySCI_state = entrySCI.get() 
    print(entrySCI_state)
    if len(entrySCI_state) != 0:
        eliminarSiEsGMS(entrySCI)

    global n
    global esGMS
    global radianOgrado
    operador = boton.cget("text")   
    entrySCI_state = entrySCI.get()

    if operador in todosConParentesis:
        entrySCI_new_state = entrySCI_state + operador + "("
        borrarTodo(entrySCI)
        entrySCI.insert(0,entrySCI_new_state)
        n = len(entrySCI_new_state)
        entrySCI.config(state="readonly")
    elif (operador in numeros) or (operador in operadores) or (operador == "!"):
        entrySCI.insert(n,(operador))
        n += 1
        entrySCI.config(state="readonly")
    elif operador in angulos:     #angulos = ["DEG","RAD","° ' " + '""']
        match operador:
            case "DEG":
                radianOgrado = "grados"
            case "RAD":
                radianOgrado = "radianes"
            case _:
                estadoGMS = not estadoGMS
    else:
        match operador:
            case "=":             
                try:
                    calcular(entrySCI,radianOgrado)   #(entrySCI,esGMS,radianOgrado)
                except Exception as e:
                    print(e)
                    borrarTodo(entrySCI)
                    entrySCI.insert(0,"Error")
                    entrySCI.config(state="readonly")
            case "DEL":
                if entrySCI_state != 0:
                    entry_new_state = entrySCI_state[:-1]
                    borrarTodo(entrySCI)
                    entrySCI.insert(0,entry_new_state)
                    n = len(entry_new_state) 
                    entrySCI.config(state="readonly")
                else:
                    borrarTodo(entrySCI)
                    entrySCI.insert(0,"Error")
                    entrySCI.config(state="readonly")
            case "AC":
                borrarTodo(entrySCI)
                entrySCI.config(state="readonly")
            case _:
                pass