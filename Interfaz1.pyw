from tkinter import *

root = Tk()
root.title("Interfaz 1")
root.geometry("400x300")

frame1 = Frame(root, bg="blue")
frame1.pack(fill="both", expand="True")

texto = Entry(frame1, font=("Arial", 18))
texto.grid(row=0, column=0, columnspan=7, padx=5, pady=5)


boton7 = Button(frame1, text="7", width=5, height=2)
boton7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

boton8 = Button(frame1, text="8", width=5, height=2)
boton8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

boton9 = Button(frame1, text="9", width=5, height=2)
boton9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

boton4 = Button(frame1, text="4", width=5, height=2)
boton4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

boton5 = Button(frame1, text="5", width=5, height=2)
boton5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

boton6 = Button(frame1, text="6", width=5, height=2)
boton6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

boton1 = Button(frame1, text="1", width=5, height=2)
boton1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

boton2 = Button(frame1, text="2", width=5, height=2)
boton2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

boton3 = Button(frame1, text="3", width=5, height=2)
boton3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

boton0 = Button(frame1, text="0", width=5, height=2)
boton0.grid(row=4, column=0, columnspan=3,padx=5, pady=5, sticky="nsew")

botonDEL = Button(frame1, text="DEL", width=5, height=2)
botonDEL.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

botonAC = Button(frame1, text="AC", width=5, height=2)
botonAC.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

botonX = Button(frame1, text="X", width=5, height=2)
botonX.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

botonDIV = Button(frame1, text="/", width=5, height=2)
botonDIV.grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

botonMAS = Button(frame1, text="+", width=5, height=2)
botonMAS.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

botonMENOS = Button(frame1, text="-", width=5, height=2)
botonMENOS.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

botonIGUAL = Button(frame1, text="=", width=5, height=2)
botonIGUAL.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

botonANS = Button(frame1, text="ANS", width=5, height=2)
botonANS.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")


root.mainloop()
