import tkinter
import random
screen=tkinter.Tk()
screen.title("ROCK PAPER SCISSOR")
screen.geometry("500x500")

var_com_choice=tkinter.StringVar()
var_result_choice=tkinter.StringVar()
var_user_choice=tkinter.StringVar()
game_list=["ROCK","PAPER","SCISSOR"]
def myfun(msg):
    var_user_choice.set(msg)
    com=random.choice(game_list)
    var_com_choice.set(com)
    if msg==com :
        var_result_choice.set("TIE")
    else:
        if msg=="ROCK"and com=="PAPER" or msg=="SCISSOR"and com=="PAPER":
            var_result_choice.set("COMPUTER WON")
        elif msg=="PAPER"and com=="ROCK":
            var_result_choice.set("USER WON")

btn=tkinter.Button(screen,text="ROCK", font=("ariel",20,"bold"),bg="blue",fg="white",activebackground="black",activeforeground="white" ,command=lambda:myfun("ROCK"))
btn.place(x=10,y=10)

btn=tkinter.Button(screen,text="PAPER", font=("ariel",20,"bold"),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda:myfun("PAPER"))
btn.place(x=150,y=10)

btn=tkinter.Button(screen,text="SCISSOR", font=("ariel",20,"bold"),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda:myfun("SCISSOR"))
btn.place(x=300,y=10)

user=tkinter.Label(screen,text="USER",font=("ariel",14,"bold"))
user.place(x=10,y=150)
computer=tkinter.Label(screen,text="COMPUTER",font=("ariel",14,"bold"))
computer.place(x=10,y=200)
user=tkinter.Label(screen,textvariable=var_user_choice,font=("ariel",14,"bold"),bg="green",fg="black")
user.place(x=150,y=150)

computer=tkinter.Label(screen,textvariable=var_com_choice,font=("ariel",14,"bold"),bg="green",fg="black")
computer.place(x=150,y=200)
btn=tkinter.Button(screen,textvariable=var_result_choice, font=("ariel",20,"bold"),bg="blue",fg="white",activebackground="black",activeforeground="white",width="25")
btn.place(x=10,y=400)

screen.mainloop()

