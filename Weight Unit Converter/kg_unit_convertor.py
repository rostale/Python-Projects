from tkinter import *


window=Tk()
window.title("KG Unit Convertor")
window['background']='#856ff8'

def clear_all():
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)
    t4.delete("1.0", END)
    t5.delete("1.0", END)
    t6.delete("1.0", END)
    t7.delete("1.0", END)
    e2.delete(0, 'end')



def from_kg():
    gram=float(e2_value.get())*1000
    pound=float(e2_value.get())*2.20462
    ounce=float(e2_value.get())*35.274
    Milligram=float(e2_value.get())*1000000
    Metric_Ton=float(e2_value.get())/1000
    Dekagram=float(e2_value.get())/100
    Hectogram=float(e2_value.get())/10
    t1.delete("1.0", END)
    t1.insert(END,gram)
    t2.delete("1.0", END)
    t2.insert(END,pound)
    t3.delete("1.0", END)
    t3.insert(END,ounce)
    t4.delete("1.0", END)
    t4.insert(END,Milligram)
    t5.delete("1.0", END)
    t5.insert(END,Metric_Ton)
    t6.delete("1.0", END)
    t6.insert(END,Dekagram)
    t7.delete("1.0", END)
    t7.insert(END,Hectogram)
 
e1=Label(window,text="Kg", bg='red', width=8)
e1.grid(row=1,column=1, ipadx=15)
 
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value, justify='center',width=10, font=('Helvetica',24))
e2.grid(row=0,column=1,padx=10, pady=(40,20))
 
b1=Button(window,text="Convert",command=from_kg, activebackground = 'green', cursor="exchange", width=20)
b1.grid(row=8,column=1,padx=10, pady=(40,20))
 
t1=Text(window,height=2,width=20, font=('Helvetica',18))
t1.grid(row=2,column=0,padx=10, pady=20)
e3=Label(window,text="Grams", bg='yellow')
e3.grid(row=3,column=0, ipadx=35)
 
t2=Text(window,height=2,width=20,font=('Helvetica',18))
t2.grid(row=2,column=1,padx=10, pady=20)
e4=Label(window,text="Pounds",bg='yellow')
e4.grid(row=3,column=1, ipadx=35)
 
t3=Text(window,height=2,width=20,font=('Helvetica',18))
t3.grid(row=2,column=2,padx=10, pady=20)
e5=Label(window,text="Ounces",bg='yellow')
e5.grid(row=3,column=2, ipadx=35)

t3=Text(window,height=2,width=20,font=('Helvetica',18))
t3.grid(row=2,column=2,padx=10, pady=20)
e5=Label(window,text="Ounces",bg='yellow')
e5.grid(row=3,column=2, ipadx=35)

t4=Text(window,height=2,width=20,font=('Helvetica',18))
t4.grid(row=4,column=0,padx=10, pady=20)
e6=Label(window,text="Milligram",bg='yellow')
e6.grid(row=5,column=0, ipadx=35)

t5=Text(window,height=2,width=20,font=('Helvetica',18))
t5.grid(row=4,column=1,padx=10, pady=20)
e7=Label(window,text="Metric Ton",bg='yellow')
e7.grid(row=5,column=1, ipadx=35)

t6=Text(window,height=2,width=20,font=('Helvetica',18))
t6.grid(row=4,column=2,padx=10, pady=20)
e8=Label(window,text="Dekagram",bg='yellow')
e8.grid(row=5,column=2, ipadx=35)

t7=Text(window,height=2,width=20,font=('Helvetica',18))
t7.grid(row=6,column=1,padx=10, pady=20)
e9=Label(window,text="Hectogram ",bg='yellow')
e9.grid(row=7,column=1, ipadx=35)

b2=Button(window, text="Reset",command=clear_all, width=20, activebackground = 'green', cursor="exchange")
b2.grid(row=8,column=2,padx=10, pady=(40,20))

window.mainloop()