from tkinter import *
import Funciones1
import Interfaz1 
import FuncionesSCI

#global trigonometria, logaritmosYexponenciales, factoriales, constantes


trigonometria = {}
logaritmosYexponenciales = {}
factoriales = {}
constantes = {}

global esGMS

def InterfazSCI(frame):
    global esGMS
    frame.destroy()  
    rootSCI = Tk()
    rootSCI.title("SCIENCE")
    rootSCI.geometry("390x370")
    #rootSCI.pack(fill="both", expand="False")

    esGMS = False
    n = 0
    global radianOgrado
    radianOgrado = "radianes"

    frame1 = Frame(rootSCI, bg="#19873E")
    frame1.pack(fill="both",expand="True")

    texto = Entry(frame1, font=("Arial", 18))
    texto.config(state="disabled")
    texto.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

    # ultimo = texto[-1]

    botonDEL = Button(frame1, text="DEL", width=5, height=2, bg="red", command=lambda: FuncionesSCI.boton(texto,botonDEL))  #texto,ultimo
    botonDEL.grid(row=0, column=5, padx=5, pady=5, sticky="nsew")

    botonAC = Button(frame1, text="AC", width=5, height=2, bg="red", command=lambda: FuncionesSCI.boton(texto, botonAC))
    botonAC.grid(row=0, column=6, padx=5, pady=5, sticky="nsew")

    #boton7 = Button(frame1, text="7", width=5, height=2, command=lambda: FuncionesSCI.click_numero(7, texto))
    boton7 = Button(frame1, text="7", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton7))
    boton7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    boton8 = Button(frame1, text="8", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton8))
    boton8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    boton9 = Button(frame1, text="9", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton9))
    boton9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

    botonPOTENCIA = Button(frame1, text="^", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonPOTENCIA))
    botonPOTENCIA.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

    botonRAIZ = Button(frame1, text="x√", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonRAIZ))
    botonRAIZ.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

    botonSIN = Button(frame1, text="sin", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonSIN))
    botonSIN.grid(row=1, column=5, padx=5, pady=5, sticky="nsew")

    botonASIN = Button(frame1, text="asin", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonASIN))
    botonASIN.grid(row=1, column=6, padx=5, pady=5, sticky="nsew")

    boton4 = Button(frame1, text="4", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton4))
    boton4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    boton5 = Button(frame1, text="5", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton5))
    boton5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

    boton6 = Button(frame1, text="6", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton6))
    boton6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

    botonMAS = Button(frame1, text="+", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonMAS))
    botonMAS.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

    botonMENOS = Button(frame1, text="-", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonMENOS))
    botonMENOS.grid(row=2, column=4, padx=5, pady=5, sticky="nsew")
   
    botonCOS = Button(frame1, text="cos", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonCOS))
    botonCOS.grid(row=2, column=5, padx=5, pady=5, sticky="nsew")

    botonACOS = Button(frame1, text="acos", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonACOS))
    botonACOS.grid(row=2, column=6, padx=5, pady=5, sticky="nsew")

    boton1 = Button(frame1, text="1", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton1))
    boton1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

    boton2 = Button(frame1, text="2", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton2))
    boton2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

    boton3 = Button(frame1, text="3", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton3))
    boton3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

    botonX = Button(frame1, text="*", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonX))
    botonX.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

    botonDIV = Button(frame1, text="/", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonDIV))
    botonDIV.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

    botonTAN = Button(frame1, text="tan", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonTAN))
    botonTAN.grid(row=3, column=5, padx=5, pady=5, sticky="nsew")

    botonATAN = Button(frame1, text="atan", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonATAN))
    botonATAN.grid(row=3, column=6, padx=5, pady=5, sticky="nsew")

    boton0 = Button(frame1, text="0", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, boton0))
    boton0.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

    botonCOMA = Button(frame1, text=".", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonCOMA))
    botonCOMA.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

    botonPAR1 = Button(frame1, text="(", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonPAR1))
    botonPAR1.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

    botonPAR2 = Button(frame1, text=")", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonPAR2))
    botonPAR2.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

    global botonRADIANES
    botonGRADOS = Button(frame1, text="DEG", width=5, height=2, command=lambda: FuncionesSCI.cambiar_modo(botonGRADOS,botonRADIANES,texto,radianOgrado))       #FuncionesSCI.boton(texto, botonGRADOS))
    botonGRADOS.grid(row=4, column=5, padx=5, pady=5, sticky="nsew")    #cambiar_modo(botonPresionado,botonCambioColor, entry)

    botonRADIANES = Button(frame1, text="RAD", width=5, height=2, command=lambda: FuncionesSCI.cambiar_modo(botonRADIANES,botonGRADOS,texto,radianOgrado))   #FuncionesSCI.boton(texto, botonRADIANES))
    botonRADIANES.grid(row=4, column=6, padx=5, pady=5, sticky="nsew")

    botonIGUAL = Button(frame1, text="=", width=5, height=2, command=lambda: FuncionesSCI.calcular(texto,botonRADIANES))   #botonIGUAL))
    botonIGUAL.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

    x = "° ' " + '""'
    botonGMS = Button(frame1, text=x, width=5, height=2, command=lambda: FuncionesSCI.cambiarGMS(botonGMS))#FuncionesSCI.boton(texto, botonGMS))
    botonGMS.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    botonFACTORIAL = Button(frame1, text="!", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonFACTORIAL))
    botonFACTORIAL.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

    botonPERMUTACION = Button(frame1, text="mPn", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonPERMUTACION))
    botonPERMUTACION.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

    botonCOMBINACION = Button(frame1, text="mCn", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonCOMBINACION))
    botonCOMBINACION.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

    botonANS = Button(frame1, text="ANS", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonANS))
    botonANS.grid(row=5, column=4, padx=5, pady=5, sticky="nsew")

    botonLOG = Button(frame1, text="LOG", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonANS))
    botonLOG.grid(row=5, column=5, padx=5, pady=5, sticky="nsew")

    botonLN = Button(frame1, text="LN", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonLN))
    botonLN.grid(row=5, column=6, padx=5, pady=5, sticky="nsew")
    
    botonNORMAL = Button(frame1, text="Normal", width=5, height=2, bg="#6FC6F1", command=lambda: Interfaz1.Interfaz1(rootSCI))  #texto,botonNORMALrootSCI
    botonNORMAL.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

    botonMATRIX = Button(frame1, text="MATRIX", width=5, height=2, bg="#D6FA33")
    botonMATRIX.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

    botonGRAPH = Button(frame1, text="GRAPH", width=5, height=2, bg="#F95F2F")
    botonGRAPH.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

    botonSTC = Button(frame1, text="STC", width=5, height=2, bg="#1CC0F1")
    botonSTC.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

    botonEQN = Button(frame1, text="EQN", width=5, height=2, bg="#D795F1")
    botonEQN.grid(row=6, column=4, padx=5, pady=5, sticky="nsew")

    botonPI = Button(frame1, text="π", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonPI))
    botonPI.grid(row=6, column=5, padx=5, pady=5, sticky="nsew")

    botonEULER = Button(frame1, text="e", width=5, height=2, command=lambda: FuncionesSCI.boton(texto, botonEULER))
    botonEULER.grid(row=6, column=6, padx=5, pady=5, sticky="nsew")

    BotonesInterfaz2 = [botonPOTENCIA, botonRAIZ, botonSIN, botonASIN, botonCOS, botonACOS, 
    botonTAN, botonATAN, botonGRADOS, botonRADIANES, botonGMS, botonFACTORIAL, botonPERMUTACION, botonCOMBINACION, 
    botonANS, botonLOG, botonLN, botonPI, botonEULER]

    for i in BotonesInterfaz2:
        i.config(bg="#2FF574")
    botonRADIANES.config(bg="#BDC51B")
    #trigonometria = [botonSIN, botonARCSIN, botonCOS, botonARCCOS, botonTAN, botonARCTAN, botonGRADOS, botonRADIANES, botonGMS]
    #logaritmosYexponenciales = [botonPOTENCIA, botonRAIZ,botonLOG, botonLN]
    #factoriales = [botonFACTORIAL, botonPERMUTACION, botonCOMBINACION]
    #constantes = [botonPI, botonEULER]

    # global trigonometria, logaritmosYexponenciales, factoriales, constantes
    # trigonometria = {botonSIN: "sin", botonARCSIN: "arcsin", botonCOS: "cos", botonARCCOS: "arccos", botonTAN: "tan", botonARCTAN: "arctan", botonGRADOS: "DEG", botonRADIANES: "RADIAN", botonGMS: "° ' " + '""'}
    # logaritmosYexponenciales = {botonPOTENCIA: "^", botonRAIZ: "x√", botonLOG: "LOG", botonLN: "LN"}
    # factoriales = {botonFACTORIAL: "!", botonPERMUTACION: "mPn", botonCOMBINACION: "mCn"}
    # constantes = {botonPI: "pi", botonEULER: "e"}

    rootSCI.mainloop()

    #rootSCI.mainloop()

#funciones = [trigonometria,logaritmosYexponenciales,factoriales,constantes]


