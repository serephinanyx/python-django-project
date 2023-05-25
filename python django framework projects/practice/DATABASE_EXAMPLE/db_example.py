import tkinter

import pymysql
from tkinter import Button, Entry, Label, StringVar ,Tk

mydb=pymysql.connect(host="localhost",user="root",password="",database="python_ex1")



cur=mydb.cursor()

cur.execute("create table if not exists student (id int primary key AUTO_INCREMENT,name varchar(20), subject varchar(20))")

mydb.commit()




screen=Tk()
screen.geometry("500x500")

var_ename=StringVar()
var_sub=StringVar()
var_id=tkinter.IntVar()
def insertData():
    query="insert into student (name,subject) values('%s','%s')"
    values=(var_ename.get(),var_sub.get())


    cur.execute(query%values)
    print("data inserted!!!")
    mydb.commit()

def deleteData():
    query="delete from student where id = %s"
    values=(var_id.get())
    cur.execute(query,values)
    mydb.commit()
    print("data deleted!!!")

lbl_name=Label(screen,text="Enter Name :")
lbl_name.place(x=10,y=10)

ename=Entry(screen,textvariable=var_ename)
ename.place(x=150,y=20)

lbl_sub=Label(screen,text="Enter Subject :")
lbl_sub.place(x=10,y=60)

ename=Entry(screen,textvariable=var_sub)
ename.place(x=150,y=60)



btn=Button(screen,text="submit",width=6,height=2,font=("arial",12,"bold"),command=insertData)
btn.place(x=150,y=100)

lbl_id=Label(screen,text="Enter id to delete:")
lbl_id.place(x=10,y=200)
idbox=Entry(screen,textvariable=var_id)
idbox.place(x=120,y=200)


btn=Button(screen,text="delete",width=6,height=2,font=("arial",12,"bold"),command=deleteData)
btn.place(x=180,y=195)


screen.mainloop()