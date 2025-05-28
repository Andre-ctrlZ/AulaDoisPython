from cProfile import label
from tkinter import  *

menu_inicial = Tk()
menu_inicial.title("Login")
menu_inicial.geometry("400x400+580+200")

label1=Label(menu_inicial, text="Usário", fg='red')
label1.grid(row=0, column=0, padx=5, pady=10, sticky=W)

label2= Label(menu_inicial, text="Senha", fg='red')
label2.grid(row=1, column=0, padx=5, pady=10, sticky=W)

txtUsario = Entry(menu_inicial)
txtUsario.grid(row=0, column=1, padx=0, pady=10, sticky=W)

txtSenha = Entry(menu_inicial)
txtSenha.grid(row=1, column=1, padx=0, pady=0, sticky=W)

botao = Button(menu_inicial, text="POYO", bg="Gray", fg="pink")
botao.grid(row=2, column=1, padx=40, pady=10, sticky=W)

menu_inicial.mainloop()