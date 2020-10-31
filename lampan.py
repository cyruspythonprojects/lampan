import tkinter as tk 
from tkinter import * 
from tkinter import messagebox as mb 
  
class lampaObj():
    
    def __init__(self,lampa):
        self.lampa = False    

    def askLampa(self):
        if self.lampa == True:
            return "släcka"
        elif self.lampa == False:
            return "tända"
        
    def evalLampa(self):
        if self.lampa == True:
            return "tänd"
        elif self.lampa == False:
            return "släckt"
    
    def changeLampa(self, lampa):
        if self.lampa == False:
            b.configure(fg="black",bg="yellow")
            self.lampa = True
        elif self.lampa == True:
            b.configure(fg="white",bg="black")
            self.lampa = False

    def getLampa(self):
        return self.lampa
    
    def setLampa(self, value):
        self.lampa = value

lamp = lampaObj(False)

def call(lamp): 
    res = mb.askquestion("Lampan är " + lamp.evalLampa(), "Vill du " + lamp.askLampa() + "?") 
    if res == 'yes': 
        lamp.changeLampa(lamp.getLampa)
        l.configure(text="Lampan är " + lamp.evalLampa() + ".")
    else : 
        if lamp.getLampa() == True:
            mb.showinfo("Status","Lampan förblir tänd.")
        elif lamp.getLampa() == False:
            mb.showinfo("Status","Lampan förblir släckt.")
  
# Driver's code 
root = tk.Tk() 
canvas = tk.Canvas(root, width = 0, height = 0) 

b = Button(root, text ='Lampa', command = lambda: call(lamp), bg="black",fg="white") 
l = Label(root, text = "Lampan är " + lamp.evalLampa() + ".")

canvas.create_window(0,0,window = b) 

b.pack()
l.pack()

root.mainloop() 