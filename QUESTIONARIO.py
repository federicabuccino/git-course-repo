
# coding: utf-8

# In[5]:

import tkinter as tk 
import tkinter.ttk as ttk

class Quest(ttk.Frame):
    def __init__(self, master, question_list):
        ttk.Frame.__init__(self, master)
        title = ttk.Label(self, text="QUESTIONARIO")
        istruzioni=ttk.Label(self, text='Osserva il comportamento quotidiano di tuo figlio, scegli i valori in una scala da 1 a 5, dove: 1=frequenza minima 5=frequenza massima')
        title.pack()
        istruzioni.pack()

        self.questions = Questions(self, question_list)
        self.questions.pack()

        risultati = ttk.Button(self, text="Fine", command=self.risultati)
        risultati.pack()

    def risultati(self):
        b=[]
        for q, a in self.questions.q_and_a:
            b.append("{}: {}".format(q,a.get()))
            
        root = tk.Tk()        

        label = {}
        i = 0
        for lista in b:
            lb = tk.Label(root, text=lista)
            lb.grid(row=i, column=1)
            label[lista] = lb
            i += 1

        root.mainloop()                
        quit()

class Questions(ttk.Frame):
    
    def __init__(self, master, question_list):
        ttk.Frame.__init__(self, master)

        self.q_and_a = []
        for row, question in enumerate(question_list):
            var = tk.IntVar(value = -1) #-1 indica che la domanda non ha avuto risposta
            q_label = ttk.Label(self, text=question)
            q_label.grid(row=row, column = 0)
            for i in range(1,6):
                button = tk.Radiobutton(self, variable = var, value = i,text=i)
                button.grid(row = row, column = i)
            self.q_and_a.append((question, var))
            
#inserimento delle domande in un'unica lista
questionlist = ["Atteggiamenti stereotipati, ripetitivi", "Senso di angoscia alla vista di estranei", 
                "Comprensione di semplici istruzioni verbali", "Riconoscimento delle proprie/altrui emozioni",
                "Stati emotivi incontrollati/incontrollabili", "Attività ludiche con coetanei",
                "Repulsione verso particolari forme, colori"]

root = tk.Tk()
root.title('Questionario')
window = Quest(root, questionlist)
window.pack()
root.mainloop()


# In[ ]:




# In[ ]:



