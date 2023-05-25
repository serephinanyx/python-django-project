

from itertools import count
import tkinter

screen=tkinter.Tk()
screen.geometry("500x500")
screen.configure(bg="pink")

#tkinter variable
var_num1=tkinter.StringVar()
count=0


def myfun():
    global count
    count+=1
    print("your reviews is:",count)
def myfun1():
     global count
     count-=1
     print("your reviews:",count)
       
print("your reviews",var_num1.get())



#label=title
lbl=tkinter.Label(screen,text="Welcome to Reviews ",font=("arial",24,"bold"),bg="grey")
lbl.place(x=80,y=10)




#button1
btn=tkinter.Button(screen,text="like",font=("arial",10,"bold"),fg="black",bg="grey",command=myfun)
btn.place(x=100,y=140)
#button2
btn2=tkinter.Button(screen,text="dislike",font=("arial",10,"bold"),fg="black",bg="grey",command=myfun1)
btn2.place(x=320,y=140)

#label2
lbl_name1=tkinter.Label(screen,text="your reviews",font=("arial",15,"bold"),fg="blue",bg="grey")
lbl_name1.place(x=200,y=230)


screen.mainloop()

