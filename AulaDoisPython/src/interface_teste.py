from tkinter import *
from tkinter import messagebox

menu_inicial = Tk()
menu_inicial.title("☆*: .｡. o(≧▽≦)o .｡.:*☆")
menu_inicial.geometry("500x500+580+200")
menu_inicial.resizable(width=False, height=False)
menu_inicial ['bg'] = "pink"
menu_inicial.iconbitmap("pngegg.ico")

def hello():
    # Gerando uma string com "POYO" repetido 100 vezes
    poyo_text = "POYO " * 10000  # Cria "POYO" 100 vezes separadas por um espaço

    # Atualiza o label para exibir o texto
    label_exit.config(text=poyo_text)


def quit():
    resposta = messagebox.askyesno("Quit", "Poyo?")
    if resposta:
        menu_inicial.destroy()

label1 = Label(menu_inicial, text="Mate deus.", fg="red", font="ComicSans", bg="pink")
label1.pack()

botao = Button(menu_inicial, text="POYO", bg="Green", fg="pink",
               command=hello)
botao.pack()

btsair= Button(menu_inicial, text="Sair", bg="Green", fg="pink", command=quit)
btsair.pack()

label_exit = Label(menu_inicial, text="", fg="red", font=("Arial", 10), bg="pink", wraplength=480)
label_exit.pack()

menu_inicial.mainloop()
