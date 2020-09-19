from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Calculadora cientifica")
root.configure(background = "powder blue")
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

barra_menu = Menu(calc)

menu_principal = Menu(barra_menu, tearoff =0)
barra_menu.add_cascade(label = "Archivo", menu=menu_principal)
menu_principal.add_command(label = "Básica")
menu_principal.add_command(label = "Cientifica")
menu_principal.add_separator()
menu_principal.add_command(label = "Salir")

menu_editar = Menu(barra_menu, tearoff =0)
barra_menu.add_cascade(label = "Editar", menu=menu_principal)
menu_editar.add_command(label = "Cortar")
menu_editar.add_command(label = "Copiar")
menu_editar.add_separator()
menu_editar.add_command(label = "Pegar")

root.config(menu=barra_menu)
root.mainloop()
