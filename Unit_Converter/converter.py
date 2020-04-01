from tkinter import *
import math

def degtofah():
    root = Tk()
    root.title("Derece - Fahrenheit")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convertdegtofah():
        degree = float(entrydeg.get())
        fah = (degree*9/5)+32
        result["text"] = ("F: {0}".format(fah))
        
    convert_text = Label(root,text="Derece cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entrydeg = Entry(root)
    entrydeg.pack()
    entrydeg.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convertdegtofah)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",35))
    result.pack()
    result.place(x=10,y=100)
    mainloop()


def fahtodeg():
    root = Tk()
    root.title("Fahrenheit - Derece")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convertdegtofah():
        fah = float(entryfah.get())
        degree = (fah-32)*5/9
        result["text"] = ("*C: {0}".format(degree))
        
    convert_text = Label(root,text="Fahrenheit cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entryfah = Entry(root)
    entryfah.pack()
    entryfah.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convertdegtofah)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()


def degtokel():
    root = Tk()
    root.title("Derece - Kelvin")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convertdegtokel():
        degree = float(entrydeg.get())
        k = degree + 273.15
        result["text"] = ("K: {0}".format(k))
        
    convert_text = Label(root,text="Derece cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entrydeg = Entry(root)
    entrydeg.pack()
    entrydeg.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convertdegtokel)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()

def keltodeg():
    root = Tk()
    root.title("Kelvin - Derece")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convertkeltodeg():
        k = float(entrykel.get())
        degree = k-273.15
        result["text"] = ("*C: {0}".format(degree))
        
    convert_text = Label(root,text="Kelvin cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entrykel = Entry(root)
    entrykel.pack()
    entrykel.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convertkeltodeg)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()


#-----------------------------



def mmtocm():
    root = Tk()
    root.title("Milimetre - Santimetre")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convert():
        mm = int(entry.get())
        cm = mm/10.000
        result["text"] = ("cm: {0}".format(cm))
        
    convert_text = Label(root,text="Milimetre cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entry = Entry(root)
    entry.pack()
    entry.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convert)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()
    
    
    
def cmtomm():
    root = Tk()
    root.title("Santimetre - Milimetre")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convert():
        cm = int(entry.get())
        mm = cm*10.000
        result["text"] = ("mm: {0}".format(mm))
        
    convert_text = Label(root,text="Santimetre cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entry = Entry(root)
    entry.pack()
    entry.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convert)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()


def cmtoM():
    root = Tk()
    root.title("Santimetre - Metre")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convert():
        cm = int(entry.get())
        M = cm/100.00
        result["text"] = ("M: {0}".format(M))
        
    convert_text = Label(root,text="Santimetre cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entry = Entry(root)
    entry.pack()
    entry.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convert)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()


def Mtocm():
    root = Tk()
    root.title("Metre - Santimetre")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convert():
        m = int(entry.get())
        cm = m*100.00
        result["text"] = ("cm: {0}".format(cm))
        
    convert_text = Label(root,text="Metre cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entry = Entry(root)
    entry.pack()
    entry.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convert)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()
    
    
def MtoKm():
    root = Tk()
    root.title("Metre - Kilometre")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convert():
        m = int(entry.get())
        km = m/1000.0
        result["text"] = ("Km: {0}".format(km))
        
    convert_text = Label(root,text="Metre cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entry = Entry(root)
    entry.pack()
    entry.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convert)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()
    
def KmtoM():
    root = Tk()
    root.title("Kilometre - Metre")
    root.geometry("400x200")
    root.resizable(False,False)
    
    def convert():
        km = int(entry.get())
        m = km*1000.0
        result["text"] = ("M: {0}".format(m))
        
    convert_text = Label(root,text="Kilometre cinsinden çevirmek istediğiniz sayıyı giriniz. ")
    convert_text.pack()
    convert_text.place(x=10,y=10)
    
    entry = Entry(root)
    entry.pack()
    entry.place(x=10,y=35)
    
    entrybtn = Button(root,text="Çevir",bg="#21252e",fg="#fff",command=convert)
    entrybtn.pack()
    entrybtn.place(x=10,y=60,width=100)
    
    result = Label(root,text="",font=("Roboto",32))
    result.pack()
    result.place(x=10,y=100)
    mainloop()