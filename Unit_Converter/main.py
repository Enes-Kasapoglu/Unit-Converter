from tkinter import *
import converter
import math

def window():
    window = Tk()
    window.title("Birim Çevirici")
    window.resizable(False,False)
    window.config(bg="#282A36")
    window.geometry("1010x700")
    
    bgC = "#282a36"
    
    choice_Text = Label(text="Çevirmek istediğiniz birimi seçiniz",bg=bgC,fg="#fff")
    choice_Text.pack()
    choice_Text.place(x=10,y=15)
    
    category_Text = Label(text="Kategoriler",bg=bgC,fg="#fff")
    category_Text.pack()
    category_Text.place(x=10,y=50)
    
    hrLine = Label(text="----------------------",bg=bgC,fg="#fff")
    hrLine.pack()
    hrLine.place(x=10,y=65)
    
    category_Text_Sicaklik = Label(text="Sıcaklık",bg=bgC,fg="#fff")
    category_Text_Sicaklik.pack()
    category_Text_Sicaklik.place(x=10,y=85)
    
    degtofahbtn = Button(text="Derece - Fahrenheit\n\n*C - F",bg="#488bff",fg="#fff",command=converter.degtofah)
    degtofahbtn.pack()
    degtofahbtn.place(x=10,y=115,width=150,height=200)
    
    fahtodeg = Button(text="Fahrenheit - Derece\n\nF - *C",bg="#488bff",fg="#fff",command=converter.fahtodeg)
    fahtodeg.pack()
    fahtodeg.place(x=190,y=115,width=150,height=200)
   
    degtokel = Button(text="Derece - Kelvin\n\n*C - K",bg="#488bff",fg="#fff",command=converter.degtokel)
    degtokel.pack()
    degtokel.place(x=370,y=115,width=150,height=200)
    
    fahtodeg = Button(text="Kelvin - Derece\n\nK - *C",bg="#488bff",fg="#fff",command=converter.keltodeg)
    fahtodeg.pack()
    fahtodeg.place(x=550,y=115,width=150,height=200)
    
    
    #-------------------
    
    
    category_Text_Sicaklik = Label(text="Uzunluk",bg=bgC,fg="#fff")
    category_Text_Sicaklik.pack()
    category_Text_Sicaklik.place(x=10,y=390)
    
    mltocm = Button(text="Milimetre - Santimetre\n\nmm - cm",bg="#cc181e",fg="#fff",command=converter.mmtocm)
    mltocm.pack()
    mltocm.place(x=10,y=425,width=170,height=200)
    
    cmtoml = Button(text="Santimetre - Milimetre\n\ncm - mm",bg="#cc181e",fg="#fff",command=converter.cmtomm)
    cmtoml.pack()
    cmtoml.place(x=190,y=425,width=170,height=200)
   
    cmtom = Button(text="Santimetre - Metre\n\ncm - M",bg="#cc181e",fg="#fff",command=converter.cmtoM)
    cmtom.pack()
    cmtom.place(x=370,y=425,width=150,height=200)
    
    mtocm = Button(text="Metre - Santimetre\n\nM - cm",bg="#cc181e",fg="#fff",command=converter.Mtocm)
    mtocm.pack()
    mtocm.place(x=530,y=425,width=150,height=200)
    
    mtokm = Button(text="Metre - Kilometre\n\nM - Km",bg="#cc181e",fg="#fff",command=converter.MtoKm)
    mtokm.pack()
    mtokm.place(x=690,y=425,width=150,height=200)
    
    kmtom = Button(text="Kilometre - Metre\n\nKm - M",bg="#cc181e",fg="#fff",command=converter.KmtoM)
    kmtom.pack()
    kmtom.place(x=850,y=425,width=150,height=200)
    
    
    mainloop()

window()

