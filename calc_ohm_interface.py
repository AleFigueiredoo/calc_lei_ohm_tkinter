from tkinter import *
from tkinter import ttk


root = Tk()

#------------ funcçoes -----------------------------------


def calcula_resistor():
    #verifica se foi digitado um numero , se sim faz a operção, se não da msg de erro
    if entrada_de_v_resistor.get() == str or entrada_de_v_resistor.get() == "" or entrada_de_i_resistor.get() == str or entrada_de_i_resistor.get() == "":
        saidaR.set("Entre com um numero!!!!")
    else:
        tensao = float(entrada_de_v_resistor.get())
        corrente = float(entrada_de_i_resistor.get())
        saidaR.set(f"O valor calculado é {round(tensao / corrente, 3)} ohms")  #saida recebe o resultado com .set
        entrada_de_i_resistor.delete(0, END)     #limpa a caixa de entrada do valor depois de executar a operação
        entrada_de_v_resistor.delete(0, END)

def calcula_corrente():
    if entrada_de_v_corrente.get() == str or entrada_de_v_corrente.get() == "" or entrada_de_r_corrente.get() == str or entrada_de_r_corrente.get() == "":
        saidaI.set("Entre com um numero!!!!")
    else:
        tensao = float(entrada_de_v_corrente.get())
        resistor = float(entrada_de_r_corrente.get())
        saidaI.set(f"O valor calculado é {round(tensao / resistor, 3)} ampêres")  # saida recebe o resultado com .set
        entrada_de_r_corrente.delete(0, END)  # limpa a caixa de entrada do valor depois de executar a operação
        entrada_de_v_corrente.delete(0, END)

def calcula_tensao():
    if entrada_de_r_tensao.get() == str or entrada_de_r_tensao.get() == "" or entrada_de_i_tensao.get() == str or entrada_de_i_tensao.get() == "":
        saidaV.set("Entre com um numero!!!!")
    else:
        corrente = float(entrada_de_i_tensao.get())
        resistor = float(entrada_de_r_tensao.get())
        saidaV.set(f"O valor calculado é {round(resistor * corrente, 3)} volts")  # saida recebe o resultado com .set
        entrada_de_i_tensao.delete(0, END)  # limpa a caixa de entrada do valor depois de executar a operação
        entrada_de_r_tensao.delete(0, END)

#------------ Configurando Janela principal ------------------------
root.geometry("305x300+300+300")
root.configure(background="lightgreen")
root.title("Calculadora OHMs")
root.wm_iconbitmap("resistor.ico")


#----------------- criando container -------------------------------------------------------
calculo_resistor = Frame(root, width=300, height=100, bg="lightgreen", highlightbackground="green", highlightthickness=1)
calculo_resistor.place(x=0, y=0)  # aqui depende do tamanho da janela principal. 'root'

calculo_corrente = Frame(root, width=300, height=100, bg="lightgreen", highlightbackground="green", highlightthickness=1)
calculo_corrente.place(x=0, y=100)

calculo_tensao = Frame(root, width=300, height=100, bg="lightgreen", highlightbackground="green", highlightthickness=1)
calculo_tensao.place(x=0, y=200)


'''----------------------------------- Frame do calculo de resistor -------------------------------------------------'''
#------------ Inserindo label ---------------------------
entra_i_resistor = Label(calculo_resistor, text="Digite o valor de I", font='Times, 9', bg="lightgreen", borderwidth=2, relief="groove")  #, font="arial, 9"
entra_i_resistor.grid(column=0, row=0, padx=15, pady=5)

entra_v_resistor = Label(calculo_resistor, text="Digite o valor de V", font='Times, 9', bg="lightgreen", borderwidth=2, relief="groove")
entra_v_resistor.grid(column=0, row=1, padx=6, pady=5)

saidaR = StringVar()     #para a variavel "saida" ser exibida no label tem que usar esta instrução
resultadoR = Label(calculo_resistor, textvariable=saidaR, bg="lightgreen")
resultadoR.grid(column=0, row=2, columnspan=2, padx=0, pady=5)

#-------------- Inserido cx entrada --------------------
entrada_de_i_resistor = Entry(calculo_resistor, width=6)
entrada_de_i_resistor.grid(column=1, row=0, padx=5, pady=5)

entrada_de_v_resistor = Entry(calculo_resistor, width=6)
entrada_de_v_resistor.grid(column=1, row=1, padx=5, pady=5)

#-------------- Inseridno botoes ----------------------
bt_calc_resistor = ttk.Button(calculo_resistor, text="Calcular valor de R", width=17, command=calcula_resistor)
bt_calc_resistor.grid(column=2, row=1, padx=5, pady=5)

'''----------------------------------- Frame do calculo de corrente -------------------------------------------------'''
#------------ Inserindo label ---------------------------
entra_v_corrente = Label(calculo_corrente, text="Digite o valor de V", font='Times, 9', bg="lightgreen", borderwidth=2, relief="groove")  #, font="arial, 9"
entra_v_corrente.grid(column=0, row=0, padx=13, pady=5)

entra_r_corrente = Label(calculo_corrente, text="Digite o valor de R", font='Times, 9', bg="lightgreen", borderwidth=2, relief="groove")
entra_r_corrente.grid(column=0, row=1, padx=7, pady=5)

saidaI = StringVar()     #para a variavel "saida" ser exibida no label tem que usar esta instrução
resultadoI = Label(calculo_corrente, textvariable=saidaI, bg="lightgreen")
resultadoI.grid(column=0, row=2, columnspan=2, padx=0, pady=5)

#-------------- Inserido cx entrada --------------------
entrada_de_v_corrente = Entry(calculo_corrente, width=6)
entrada_de_v_corrente.grid(column=1, row=0, padx=5, pady=5)

entrada_de_r_corrente = Entry(calculo_corrente, width=6)
entrada_de_r_corrente.grid(column=1, row=1, padx=5, pady=5)

#-------------- Inseridno botoes ----------------------
bt_calc_corrente = ttk.Button(calculo_corrente, text="Calcular valor de I", width=17, command=calcula_corrente)
bt_calc_corrente.grid(column=2, row=1, padx=5, pady=5)

'''----------------------------------- Frame do calculo de tensão -------------------------------------------------'''
#------------ Inserindo label ---------------------------
entra_r_tensao = Label(calculo_tensao, text="Digite o valor de R", font='Times, 9', bg="lightgreen", borderwidth=2, relief="groove")
entra_r_tensao.grid(column=0, row=1, padx=12, pady=5)

entra_i_tensao = Label(calculo_tensao, text="Digite o valor de I", font='Times, 9', bg="lightgreen", borderwidth=2, relief="groove")  #, font="arial, 9"
entra_i_tensao.grid(column=0, row=0, padx=7, pady=5)

saidaV = StringVar()     #para a variavel "saida" ser exibida no label tem que usar esta instrução
resultadoV = Label(calculo_tensao, textvariable=saidaV, bg="lightgreen")
resultadoV.grid(column=0, row=2, columnspan=2, padx=0, pady=5)

#-------------- Inserido cx entrada --------------------
entrada_de_r_tensao = Entry(calculo_tensao, width=6)
entrada_de_r_tensao.grid(column=1, row=1, padx=5, pady=5)

entrada_de_i_tensao = Entry(calculo_tensao, width=6)
entrada_de_i_tensao.grid(column=1, row=0, padx=5, pady=5)

#-------------- Inseridno botoes ----------------------
bt_calc_tensao = ttk.Button(calculo_tensao, text="Calcular valor de V", width=17, command=calcula_tensao)
bt_calc_tensao.grid(column=2, row=1, padx=5, pady=5)



root.mainloop()