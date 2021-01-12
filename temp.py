
from tkinter import *
def build_GUI():
    myWindow = Tk()
    myWindow.title("Temperature Converter")
    myWindow.geometry("700x700")


    Celcius= IntVar()
    Fahrenheit= IntVar()

    labelframe1 = LabelFrame(myWindow,text="Celsius To Fahrenheit", padx=40, pady=40)
    labelframe1.pack(fill="both")
    labelframe1.place(x=100,y=10)
    Celsius_entry=Entry(labelframe1)
    Celsius_entry.configure(state="disable")
    Celsius_entry.pack(side=LEFT)

    labelframe2 = LabelFrame(myWindow,text="Fahrenheit To Celsius", padx=40, pady=40)
    labelframe2.pack(fill="both")
    labelframe2.place(x=350,y=10)
    Fahrenheit_entry = Entry(labelframe2)
    Fahrenheit_entry.configure(state="disable")
    Fahrenheit_entry.pack(side=RIGHT)

    def Activ_Celsius():
        Celsius_entry.configure(state="normal")

    Convert_btn_CF=Button(text="Activate Celsius-Fahrenheit Conversion",command=Activ_Celsius)
    Convert_btn_CF.pack()
    Convert_btn_CF.place(x=120,y=150)

    def Activ_Fahrenheit():
        Fahrenheit_entry.configure(state="normal")

    Convert_btn_FC=Button(text="Activate Fahrenheit-Celsius Conversion",command= Activ_Fahrenheit)
    Convert_btn_FC.pack(side = RIGHT)
    Convert_btn_FC.place(x=380, y=150)

    def Conversion():
        if Celsius_entry:
            Celcius=float(Celsius_entry.get())
            Fahrenheit=float(Celcius*9/5)+32
            answer.insert(0, float(Fahrenheit))

    def Conversion2():
        if Fahrenheit_entry:
            Fahrenheit=float(Fahrenheit_entry.get())
            Celcius =float(Fahrenheit-32)*5/9
            answer.insert(0, float(Celcius))

#########################################################################################
#########################################################################################
#Have to look at this again#
    execute_btn1=Button(text="Celsius-Fahrenheit",command=Conversion)
    execute_btn1.pack(side=LEFT)
    execute_btn1.place(x=50, y=290)
    execute_btn2=Button(text="Fahrenheit-Celsius",command=Conversion2)
    execute_btn2.pack(side=LEFT)
    execute_btn2.place(x=50, y=230)
###########################################################################################
###########################################################################################

    answer=Entry(text="",background="lime")
    answer.pack()
    answer.place(x=280,y=230)


    def clear_all():
        Celsius_entry.delete(0, END)
        Fahrenheit_entry.delete(0, END)
        answer.delete(0, END)

    Clear_btn=Button(text="Clear",command=clear_all)
    Clear_btn.pack(side=RIGHT)
    Clear_btn.place(x=500,y=230)


    def exit_Func():
        myWindow.destroy()
    exit_btn=Button(text="Exit",command=exit_Func)
    exit_btn.pack(side=RIGHT)
    exit_btn.place(x=500,y=270)



    myWindow.mainloop()
build_GUI()
