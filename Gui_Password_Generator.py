# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:08:55 2019

@author: nicol
"""

from tkinter import *
import tkinter
import string
import random
class Generator:
    def entry(self):
        self.Expression=self.e.get()
        
    def password(self,passw):
        self.entry()
        try:
           size=8 
           self.p=[random.choice(string.ascii_letters)]+[random.choice(string.digits)]+[random.choice(string.punctuation)]+[random.choice(string.ascii_uppercase)]+[random.choice(string.ascii_lowercase)]
 
           passw=''.join(random.choice(self.p) for i in range(self.size))
           self.e.insert(END,passw)
        except TypeError:
            self.e.delete(0,END)
            self.e.insert(0,"Oops Something Went Wrong")
    def passs(self):
         self.p=[random.choice(string.ascii_letters)]+[random.choice(string.digits)]+[random.choice(string.punctuation)]+[random.choice(string.ascii_uppercase)]+[random.choice(string.ascii_lowercase)]
         self.ps=''.join(random.choice(self.p) for i in range(8))
      #   self.password=self.e.get()
         self.e.insert(0,self.ps)
    def Clearall(self):
        self.e.delete(0,END)
    def Clear(self):
        self.text=self.e.get()[:-1]
        self.e.delete(0,END)
        self.e.insert(0,self.text)
    def actions(self,argi):
        self.e.insert(END,argi)
    def __init__(self,master):
        master.title("Password Generator")
        master.geometry()
        self.e=Entry(master)
        self.e.grid(row=1,column=0,columnspan=17,ipady=2)
        self.e.focus_set()
        #Buttons
        Button(master,text="Generate",width=11,height=2,bg="grey",fg="black",command=lambda:self.passs()).grid(row=2,column=1)
        Button(master,text="Clear",width=11,height=2,bg="grey",fg="black",command=lambda:self.Clearall()).grid(row=2,column=1,columnspan=6)
      #  -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
        Label(master,text="GUI BASED PASSWORD GENERATOR",bg="black",fg="grey",width=80,height=7).grid(row=0,column=0,columnspan=4,pady=3)
if __name__=='__main__':
    root=tkinter.Tk()
    root.configure(background="grey")
    obj=Generator(root)
    root.mainloop()#Main loop is used to keep the Gui on the screen