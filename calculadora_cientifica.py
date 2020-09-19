from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Calculadora cientifica")
root.configure(background = "white")
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

vistaTexto = Entry(calc, font = ('Kozuka Mincho Pr6N',20,'bold'), bg = "white", bd = 30, width = 28, justify = RIGHT)
vistaTexto.grid(row = 0, column = 0, columnspan = 4, pady = 1)
vistaTexto.insert(0,"0")

teclas_numericas = "789456123"
i = 0
boton = []
for j in range(2,5):
    for k in range(3):
        boton.append(Button(calc, width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bg = "lightgray", bd = 4, text = teclas_numericas[i]))
        boton[i].grid(row = j, column = k, pady = 1)
        i += 1
###
boton_limpiar = Button(calc, text = chr(67), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "silver").grid(row = 1, column = 0, pady = 1)
boton_limpiar_todo = Button(calc, text = chr(67) + chr(69), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "silver").grid(row = 1, column = 1, pady = 1)

boton_raiz = Button(calc, text = chr(67), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "silver").grid(row = 1, column = 0, pady = 1)
boton_agregar = Button(calc, text = chr(67) + chr(69), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "silver").grid(row = 1, column = 1, pady = 1)
### Menu superior ####

def Salida():
    Salida = tkinter.messagebox.askyesno("Calculadora cientifica","Confirma si quieres salir")
    if Salida > 0:
        root.destroy()
        return

def Cientifica():
    root.resizable(width = False, height = False)
    root.geometry("944x568+0+0")

def Basica():
    root.resizable(width = False, height = False)
    root.geometry("480x568+0+0")


barra_menu = Menu(calc)

menu_principal = Menu(barra_menu, tearoff =0)
barra_menu.add_cascade(label = "Archivo", menu=menu_principal)
menu_principal.add_command(label = "Básica", command = Basica)
menu_principal.add_command(label = "Cientifica", command = Cientifica)
menu_principal.add_separator()
menu_principal.add_command(label = "Salir", command = Salida)

menu_editar = Menu(barra_menu, tearoff =0)
barra_menu.add_cascade(label = "Editar", menu=menu_editar)
menu_editar.add_command(label = "Cortar")
menu_editar.add_command(label = "Copiar")
menu_editar.add_separator()
menu_editar.add_command(label = "Pegar")

menu_ayuda = Menu(barra_menu, tearoff =0)
barra_menu.add_cascade(label = "Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label = "Ver ayuda")

root.config(menu=barra_menu)
root.mainloop()
