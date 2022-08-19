from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()


#------------ funcçoes -----------------------------------
def calcula_resistor():
    if entrada_de_v.get() == str or entrada_de_v.get() == "" or entrada_de_i.get() == str or entrada_de_i.get() == "":
        messagemErro()
    else:
        tensao = float(entrada_de_v.get())
        corrente = float(entrada_de_i.get())
        saidaR.set(f"O valor calculado é {round(tensao / corrente, 3)} ohms")  #saida recebe o resultado

def messagemErro():
    menssagem = Tk()
    menssagem.geometry("250x20+300+300")
    menssagem.configure(background="yellow")
    menssagem.title("Warning")
    t = Label(menssagem, text="Entre com um numero !!!", bg="yellow", fg="red")
    t.pack()
    menssagem.bind("<Button-1>", fechaWarning)

def fechaWarning(menssagem):
    print("fecha")

    

#------------ Configurando Janela ------------------------
root.geometry("300x200+300+300")
root.configure(background="lightgreen")
root.title("Calculadora OHMs")
root.wm_iconbitmap("resistor.ico")


#------------ Inserindo label ---------------------------
saidaR = StringVar()     #para a variavel "saida" ser exibida no label tem que usar esta instrução
entra_i = Label(root, text="Digite o valor de I", bg="lightgreen")
entra_v = Label(root, text="Digite o valor de V", bg="lightgreen")
resultadoR = Label(root, textvariable=saidaR, bg="lightgreen")

entra_i.grid(column=0, row=0, padx=5, pady=5)
entra_v.grid(column=0, row=1, padx=6, pady=5)
resultadoR.grid(column=0, row=2, columnspan=2, padx=0, pady=5)

#-------------- Inserido cx entrada --------------------
entrada_de_i = Entry(root, width=6)
entrada_de_v = Entry(root, width=6)

entrada_de_i.grid(column=1, row=0, padx=5, pady=5)
entrada_de_v.grid(column=1, row=1, padx=5, pady=5)

#-------------- Inseridno botoes ----------------------
calc_r = ttk.Button(root, text="Calcular", width=8, command=calcula_resistor)
bt_limpar = ttk.Button(root, text="limpar", width=6)

calc_r.grid(column=2, row=1, padx=5, pady=5)
bt_limpar.grid()

root.mainloop()