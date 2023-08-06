from tkinter import *
import Funciones1
import InterfazSCI


def Interfaz1(rootN):
    root = Tk()
    root.title("Interfaz 1")
    root.geometry("275x300")
    #root.pack(fill="both", expand="False")
    try:
        rootN.destroy()
    except:
        pass
    n = 0
    estadoGMS = False
    radianOgrado = "radianes"
    frame1 = Frame(root, bg="#6FC6F1")
    frame1.pack(fill="both", expand="True")  #frame1.pack(fill="both", expand="False")

    texto = Entry(frame1, font=("Arial", 18))
    texto.config(state="disabled")
    texto.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

    #boton7 = Button(frame1, text="7", width=5, height=2, command=lambda: Funciones1.click_numero(7, texto))
    boton7 = Button(frame1, text="7", width=5, height=2, command=lambda: Funciones1.boton(texto, boton7))
    boton7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    boton8 = Button(frame1, text="8", width=5, height=2, command=lambda: Funciones1.boton(texto, boton8))
    boton8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    boton9 = Button(frame1, text="9", width=5, height=2, command=lambda: Funciones1.boton(texto, boton9))
    boton9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

    boton4 = Button(frame1, text="4", width=5, height=2, command=lambda: Funciones1.boton(texto, boton4))
    boton4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    boton5 = Button(frame1, text="5", width=5, height=2, command=lambda: Funciones1.boton(texto, boton5))
    boton5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

    boton6 = Button(frame1, text="6", width=5, height=2, command=lambda: Funciones1.boton(texto, boton6))
    boton6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

    boton1 = Button(frame1, text="1", width=5, height=2, command=lambda: Funciones1.boton(texto, boton1))
    boton1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

    boton2 = Button(frame1, text="2", width=5, height=2, command=lambda: Funciones1.boton(texto, boton2))
    boton2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

    boton3 = Button(frame1, text="3", width=5, height=2, command=lambda: Funciones1.boton(texto, boton3))
    boton3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

    boton0 = Button(frame1, text="0", width=5, height=2, command=lambda: Funciones1.boton(texto, boton0))
    boton0.grid(row=4, column=0,padx=5, pady=5, sticky="nsew")

    botonDEL = Button(frame1, text="DEL", width=5, height=2, bg="red", command=lambda: Funciones1.boton(texto, botonDEL))
    botonDEL.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

    botonAC = Button(frame1, text="AC", width=5, height=2, bg="red", command=lambda: Funciones1.boton(texto, botonAC))
    botonAC.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

    botonMAS = Button(frame1, text="+", width=5, height=2, command=lambda: Funciones1.boton(texto, botonMAS))
    botonMAS.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

    botonMENOS = Button(frame1, text="-", width=5, height=2, command=lambda: Funciones1.boton(texto, botonMENOS))
    botonMENOS.grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

    botonX = Button(frame1, text="*", width=5, height=2, command=lambda: Funciones1.boton(texto, botonX))
    botonX.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

    botonDIV = Button(frame1, text="/", width=5, height=2, command=lambda: Funciones1.boton(texto, botonDIV))
    botonDIV.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

    botonCOMA = Button(frame1, text=".", width=5, height=2, command=lambda: Funciones1.boton(texto, botonCOMA))
    botonCOMA.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

    botonPAR1 = Button(frame1, text="(", width=5, height=2, command=lambda: Funciones1.boton(texto, botonPAR1))
    botonPAR1.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

    botonPAR2 = Button(frame1, text=")", width=5, height=2, command=lambda: Funciones1.boton(texto, botonPAR2))
    botonPAR2.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

    botonIGUAL = Button(frame1, text="=", width=5, height=2, command=lambda: Funciones1.boton(texto, botonIGUAL))
    botonIGUAL.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")


    botonSCI = Button(frame1, text="SCI", width=5, height=2, bg="#19873E", command=lambda: InterfazSCI.InterfazSCI(root))  ##2FF574
    botonSCI.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    botonMATRIX = Button(frame1, text="MATRIX", width=5, height=2, bg="#D6FA33")
    botonMATRIX.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

    botonGRAPH = Button(frame1, text="GRAPH", width=5, height=2, bg="#F95F2F")
    botonGRAPH.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

    botonGRAPH = Button(frame1, text="STC", width=5, height=2, bg="#1CC0F1")
    botonGRAPH.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

    botonGRAPH = Button(frame1, text="EQN", width=5, height=2, bg="#D795F1")
    botonGRAPH.grid(row=5, column=4, padx=5, pady=5, sticky="nsew")


    root.mainloop()
