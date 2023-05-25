"""
GUI: GRAPHIC USER INTERFACE
CLI: COMMAND LINE INTERFACE

"""


import tkinter
screen=tkinter.Tk()
screen.geometry("500x500")
screen.configure(bg="blue")

#tkinter variable
var_ename_id=tkinter.StringVar()        # it will accept value in string formate
var_num=tkinter.IntVar()


def myfun():
    print("WELCOME")
    print("value from entry=",var_ename_id.get())

   


#label=title
lbl=tkinter.Label(screen,text="Welcome to tkinter",font=("arial",26,"bold"),bg="grey")
lbl.place(x=80,y=10)


#label=heading name
lbl_name=tkinter.Label(screen,text="enter your name:",font=("arial",10,"bold"))
lbl_name.place(x=20,y=80)

#entry
e1=tkinter.Entry(screen, textvariable=var_ename_id)
e1.place(x=160,y=80)


#button
btn=tkinter.Button(screen,text="submit",font=("arial",10,"bold"),fg="black",command=myfun)
btn.place(x=300,y=80)





screen.mainloop()
