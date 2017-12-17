
    
from tkinter import *


def verbo():
    resultado['text'] = ' Coloque os dados acima para calcular suas chances'
    resultado['fg'] = 'red'
    resultado['font']='40'
    member =  int(pf1.get())
    income =  float(rf1.get())
    semester =  float(cs1.get())
    montly = float(cm1.get())
    calculando = income / member
    calculando1 = (600 / calculando)*100
    
    if calculando1 > 60:
        resultado['text'] = 'Parabéns, você tem chances de 100% de financiamento'
        resultado['fg'] = 'green'
        resultado['font']='10,bold'
    elif calculando1 > 40:
        resultado['text']= 'Parabéns, você tem chances de 75% de financiamento'
        resultado['fg'] = 'green'
        resultado['font']='10,bold'
    elif calculando1 > 20:
        resultado['text']= 'Parabéns, você tem chances de 50% de financiamento'
        resultado['fg'] = 'green'
        resultado['font']='10,bold'
    else:
        resultado['text'] = 'Infelizmente, sua renda é muito superior para este fim.'
        resultado['fg'] = 'red'
        resultado['font']='10,bold'
#~~~~~~~~~~interface~~~~~~~~~~#
root = Tk()
root.configure(bg = '#9FB6CD')
root.title('FIES')
root.geometry('500x300')
root.resizable(width=False, height=False)

#~~~~~~~~~~Pessoas na familia~~~~~~~~~~~~~~#
#label
pf = Label(root, text='NÚMERO DE PESSOAS NA FAMILIA',bg ='#9FB6CD',font=('weight=bold'))
pf.place(x = 30 , y = 15)
#dialogue box
pf1 = Entry()
pf1.place(x = 310, y = 16)
#~~~~~~~~~~Renda familiar~~~~~~~~~~#
#label
rf = Label(root, text='RENDA PER CAPITA',bg ='#9FB6CD',font=('weight=bold'))
rf.place(x = 30 , y = 50)
#dialogue box
rf1 = Entry()
rf1.place(x = 310, y = 52)
#~~~~~~~~~~Semestre do Curso~~~~~~~~~~#
#label
cs = Label(root, text='VALOR DO CURSO/SEMESTRE',bg ='#9FB6CD',font=('weight=bold'))
cs.place(x = 30 , y = 85)
#dialogue box
cs1 = Entry()
cs1.place(x = 310, y = 87)
#~~~~~~~~~~mensalidade do curso~~~~~~~~~~#
#label
cm = Label(root, text='VALOR DO CURSO/MENSAL',bg ='#9FB6CD',font=('weight=bold'))
cm.place(x = 30 , y = 120)
#dialogue box
cm1 = Entry()
cm1.place(x = 310, y = 122)
#~~~~~~~~~~~Botão Calcular~~~~~~~~~~#
calculo = Button(root,text='CALCULAR',command = verbo)
calculo.place(x = 190, y = 170)

#~~~~~~~~~~resultado~~~~~~~~~~#

resultado = Label(root,bg = '#9FB6CD')
resultado.place (x = 50 , y = 260)


root.mainloop()
