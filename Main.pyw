# NOTE : Please change the image path before writing this code on your System.
# First of all, Download & save all image in one Folder. Then, one by one copy the path of image and then paste it in this code.
# Match all images according to "Demo_Structure.jpg" File Which is already Provided in this repo.

from tkinter import *

menu = Tk()
menu.title('Billing System')
menu.geometry("700x1000")

Label(menu,text="PRISM BAR",font=("comic sans MS", 33, "bold","underline")).place(x=99,y=35)
sum=0.0
def calculation():
    try:
        a1 = int(a.get())
    except:
        a1 = 0
    try:
        b1 = int(b.get())
    except:
        b1=0
    try:
        c1 = int(c.get())
    except:
        c1=0
    try:
        d1 = int(d.get())
    except:
        d1=0
    try:
        e1 = int(e.get())
    except:
        e1=0
    try:
        f1 = int(f.get())
    except:
        f1=0
    
    sum = (a1*100)+(b1*20)+(c1*80)+(d1*10)+(e1*15)+(f1*40)

    Label(menu,text="ITEMS",font="times 13 bold underline").place(x=50,y=530)
    Label(menu,text="QUANTITY",font="times 13 bold underline").place(x=380,y=530)
    
    Label(menu,text="Red Bull               -                "+str(a1),font="Courier 12",bg="LightBlue").place(x=50,y=570)
    Label(menu,text="Sting                 -                 "+str(b1),font="Courier 12",bg="LightBlue").place(x=50,y=590)
    Label(menu,text="Maaza                  -                "+str(c1),font="Courier 12",bg="LightBlue").place(x=50,y=610)
    Label(menu,text="Smoodh                 -                "+str(d1),font="Courier 12",bg="LightBlue").place(x=50,y=630)
    Label(menu,text="Appy Fizz              -                "+str(e1),font="Courier 12",bg="LightBlue").place(x=50,y=650)
    Label(menu,text="Thumbs Up              -                "+str(f1),font="Courier 12",bg="LightBlue").place(x=50,y=670)

    Label(menu,text="----------------------------------------------------------------------------------",bg="LightBlue").place(x=50,y=695)
    Label(menu,text="Total Amount                       Rs. "+str(sum),font="Courier 12",bg="cyan").place(x=50,y=710)

#menu....
Label(menu,text="MENU",font="times 30 bold").place(x=530,y=80)

Label(menu,text="Red Bull         Rs 100",font="times 15",bg="Silver").place(x=500,y=130)

Label(menu,text="Sting               Rs 20  ",font="times 15",bg="Silver").place(x=500,y=160)

Label(menu,text="Maaza             Rs 80  ",font="times 15",bg="Silver").place(x=500,y=190)

Label(menu,text="Smoodh           Rs 10 ",font="times 15",bg="Silver").place(x=500,y=220)

Label(menu,text="Appy Fizz        Rs 15 ",font="times 15",bg="Silver").place(x=500,y=250)

Label(menu,text="Thumbs Up      Rs 40 ",font="times 15",bg="Silver").place(x=500,y=280)


#input item taken by user..

Label(menu,text="RED BULL",font="arial 14").place(x=50,y=130)
a = Entry(menu)
a.place(x=50,y=170)
i1=PhotoImage(file='C:\\Users\\professor prasam\\Desktop\\jaypee\\GUI_Python\\images for bar_project\\red_bull.png')
Label(menu,image=i1).place(x=180,y=130)

Label(menu,text="STING",font="arial 14").place(x=280,y=130)
b = Entry(menu)
b.place(x=280,y=170)
i2=PhotoImage(file='C:\\Users\\professor prasam\\Desktop\\jaypee\\GUI_Python\\images for bar_project\\string.png')
Label(menu,image=i2).place(x=410,y=120)

Label(menu,text="MAAZA",font="arial 14").place(x=50,y=260)
c = Entry(menu)
c.place(x=50,y=300)
i3=PhotoImage(file='C:\\Users\\professor prasam\\Desktop\\jaypee\\GUI_Python\\images for bar_project\\maza.png')
Label(menu,image=i3).place(x=180,y=250)

Label(menu,text="SMOODH",font="arial 14").place(x=280,y=260)
d = Entry(menu)
d.place(x=280,y=300)
i4=PhotoImage(file='C:\\Users\\professor prasam\\Desktop\\jaypee\\GUI_Python\\images for bar_project\\smoodh.png')
Label(menu,image=i4).place(x=410,y=240)

Label(menu,text="APPY FIZZ",font="arial 14").place(x=50,y=390)
e = Entry(menu)
e.place(x=50,y=430)
i5=PhotoImage(file='C:\\Users\\professor prasam\\Desktop\\jaypee\\GUI_Python\\images for bar_project\\fizz.png')
Label(menu,image=i5).place(x=180,y=360)

Label(menu,text="THUMBS UP",font="arial 14").place(x=280,y=390)
f = Entry(menu)
f.place(x=280,y=430)
i6=PhotoImage(file='C:\\Users\\professor prasam\\Desktop\\jaypee\\GUI_Python\\images for bar_project\\thumbsup.png')
Label(menu,image=i6).place(x=410,y=380)

#image of coca cola for creation
i7=PhotoImage(file='C:\\Users\\professor prasam\\Desktop\\jaypee\\GUI_Python\\images for bar_project\\coca.png')
Label(menu,image=i7).place(x=500,y=400)

#logo of P
i8=PhotoImage(file='C:\\Users\\professor prasam\\Desktop\\jaypee\\GUI_Python\\images for bar_project\\P1.png')
Label(menu,image=i8).place(x=0,y=0)

#Button...
Button(menu,text="DONE",width=20,command=calculation,activebackground="pink",activeforeground="white").place(x=162,y=480)
menu.mainloop()


