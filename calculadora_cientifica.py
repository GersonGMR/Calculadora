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
        boton.append(Button(calc, width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bg = "silver", bd = 4, text = teclas_numericas[i]))
        boton[i].grid(row = j, column = k, pady = 1)
        i += 1
### Botones de las funciones ###

boton_limpiar = Button(calc, text = "C", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 1, column = 0, pady = 1)
boton_limpiar_todo = Button(calc, text = "CE", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 1, column = 1, pady = 1)
boton_raiz = Button(calc, text = "√", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 1, column = 2, pady = 1)
boton_suma = Button(calc, text = "+", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 1, column = 3, pady = 1)
boton_resta = Button(calc, text = "-", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 2, column = 3, pady = 1)
boton_multiplicacion = Button(calc, text = "*", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 3, column = 3, pady = 1)
boton_division = Button(calc, text = chr(247), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 4, column = 3, pady = 1)

boton_cero = Button(calc, text = "0", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "silver").grid(row = 5, column = 0, pady = 1)
boton_punto = Button(calc, text = ".", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 5, column = 1, pady = 1)
boton_punto_medio = Button(calc, text = chr(177), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 5, column = 2, pady = 1)
boton_igual = Button(calc, text = "=", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 5, column = 3, pady = 1)

### Calculadora cientifica fila 1 ###

boton_pi = Button(calc, text = chr(960), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 1, column = 4, pady = 1)
boton_cos = Button(calc, text = "cos", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 1, column = 5, pady = 1)
boton_tan = Button(calc, text = "tan", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 1, column = 6, pady = 1)
boton_sen = Button(calc, text = "sin", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 1, column = 7, pady = 1)

### Calculadora cientifica fila 2 ###

boton_2pi = Button(calc, text = "2π", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 2, column = 4, pady = 1)
boton_cosh = Button(calc, text = "cosh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 2, column = 5, pady = 1)
boton_tanh = Button(calc, text = "tanh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 2, column = 6, pady = 1)
boton_senh = Button(calc, text = "sinh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 2, column = 7, pady = 1)

### Calculadora cientifica fila 3 ###

boton_log = Button(calc, text = "log", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 3, column = 4, pady = 1)
boton_exp = Button(calc, text = "Exp", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 3, column = 5, pady = 1)
boton_mod = Button(calc, text = "Mod", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 3, column = 6, pady = 1)
boton_e = Button(calc, text = "e", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 3, column = 7, pady = 1)

### Calculadora cientifica fila 4 ###

boton_log2 = Button(calc, text = "log2", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 4, column = 4, pady = 1)
boton_deg = Button(calc, text = "deg", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 4, column = 5, pady = 1)
boton_acosh = Button(calc, text = "acosh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 4, column = 6, pady = 1)
boton_asinh = Button(calc, text = "asinh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 4, column = 7, pady = 1)

### Calculadora cientifica fila 5 ###

boton_log10 = Button(calc, text = "log10", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 5, column = 4, pady = 1)
boton_log1p = Button(calc, text = "log1p", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 5, column = 5, pady = 1)
boton_expm1 = Button(calc, text = "expm1", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 5, column = 6, pady = 1)
boton_lgamma = Button(calc, text = "lgamma", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey").grid(row = 5, column = 7, pady = 1)

labelVista = Label(calc, text = "Calculadora cientifica", font = ("Kozuka Mincho Prn6N", 30, 'bold'), justify = CENTER)
labelVista.grid(row = 0, column = 4, columnspan = 4)
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
