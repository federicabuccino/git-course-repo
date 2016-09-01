
# coding: utf-8

# In[1]:

#INTERFACCIA
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
#import numpy as np

finestra=Tk()
finestra.geometry('800x300')


def password():
    l1=Label(text='Inserisci la password: ').pack()
    pw=Entry()
    def getpw():
        b=pw.get()
        if b!='giulia':
            l2=Label(text='Password errata!').pack()
            password()
        else:
            l3=Label(text='Password corretta!').pack()
            schermatamedico()
    submit = Button(text ="Invia", command = getpw)
    pw.pack()
    submit.pack()
def password1():
    l1=Label(text='Inserisci la password: ').pack()
    pw=Entry()
    def getpw():
        b=pw.get()
        if b!='federica':
            l2=Label(text='Password errata!').pack()
            password1()
        else:
            l3=Label(text='Password corretta!').pack()
            schermatagenitore()
    submit = Button(text ="Invia", command = getpw)
    pw.pack()
    submit.pack()

def schermatamedico():
    finestra=Tk()
    finestra.geometry('300x300')
    finestra.title('Neuropsichiatra infantile')
    #menu
    barra_menu=Menu(finestra)
    #menu file
    menu_file=Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='File',menu=menu_file)
    ###################
        
    menu_file.add_command(label='Visualizza questionario')
    def visualizza():
        doc=filedialog.askopenfile()
        Label(finestra, text=doc, fg='blue').pack()
       
    menu_file.add_command(label='Visualizza dati GSR', command=visualizza)
    
    menu_file.add_command(label='Visualizza dati EarClip', command=visualizza)
    
    def uscita():
        risp=messagebox.askyesno(title='Uscita', message='Vuoi davvero uscire?')
        if risp==True:
            finestra.destroy()
            
    menu_file.add_command(label='Esci',command=uscita)
    
    #menu contatti
    menu_contatti=Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Contatti',menu=menu_contatti)
    def numero():
        messagebox.showinfo(title='Recapiti', message='Casa: +39 0270126473        Ufficio : +39 3356120333')
        
    menu_contatti.add_command(label='Psicologa dott.ssa Silvani', command=numero)
    menu_contatti.add_command(label='Paziente Calboni', command=numero)
    
    #menu info
    menu_info=Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Info',menu=menu_info)
    def informaz():
        messagebox.showinfo(title='Info', message="In questa sezione è possibile visualizzare i dati relativi all'utilizzo del GSR e dell'EarClip da parte del paziente, consultare gli esiti del questionario e ottenere i recapiti telefonici dei familiari del paziente e dello psicologo")
    menu_info.add_command(label='Info', command=informaz)
    finestra.config(menu=barra_menu)

    
def QQ():
    import QUESTIONARIO as Q
    import tkinter.ttk as ttk
    import tkinter as tk
    #inserimento delle domande in un'unica lista
    questionlist = ["Atteggiamenti stereotipati, ripetitivi", "Senso di angoscia alla vista di estranei", 
                    "Comprensione di semplici istruzioni verbali", "Riconoscimento delle proprie/altrui emozioni",
                    "Stati emotivi incontrollati/incontrollabili", "Attività ludiche con coetanei",
                    "Repulsione verso particolari forme, colori"]

    root = tk.Tk()
    window = Q.Quest(root, questionlist)
    window.pack()
    root.mainloop()
    

def schermatagenitore():
    
    finestra=Tk()
    finestra.geometry('300x300')
    finestra.title('Genitore')
    #menu
    barra_menu=Menu(finestra)
    #menu file
    menu_file=Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='File',menu=menu_file)
    ###################
    menu_file.add_command(label='Compila questionario', command=QQ)
    def apri():
        GSR=filedialog.askopenfile()
        Label(finestra, text=GSR, fg='blue').pack()
        
    

    menu_file.add_command(label='Invia dati GSR', command=apri)
    
    menu_file.add_command(label='Invia dati EarClip',command=apri)
    
    def uscita():
        risp=messagebox.askyesno(title='Uscita', message='Vuoi davvero uscire?')
        if risp==True:
            finestra.destroy()
            
    menu_file.add_command(label='Esci',command=uscita)
    
    #menu contatti
    menu_contatti=Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Contatti',menu=menu_contatti)
    def numero():
        messagebox.showinfo(title='Recapiti', message='Studio: +39 0432541689        Emergenze: +39 3356120333')
        
    menu_contatti.add_command(label='Neuropsichiatra infantile Dott. Filini', command=numero)
    menu_contatti.add_command(label='Psicologa Dott.ssa Silvani', command=numero)
    
    #menu info
    menu_info=Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Info',menu=menu_info)
    def informaz():
        messagebox.showinfo(title='Info', message="In questa sezione è possibile inviare i dati relativi all'utilizzo del GSR e dell'EarClip, compilare l'apposito questionario e consultare i recapiti telefonici del neuropsichiatra e dello psicologo")
    menu_info.add_command(label='Info', command=informaz)
    finestra.config(menu=barra_menu)

    
   
    

finestra.title('Pathochromo')
testo=Label(text='Pathochromo... Benvenuto!', bg='lightblue', font=('Calibri',40)).pack()
b1=Button(text='Neuropsichiatra infantile',command=password).pack()
b2=Button(text='Genitore',command=password1).pack()

finestra.mainloop()


# In[ ]:



