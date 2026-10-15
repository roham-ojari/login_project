from tkinter import *
from tkinter import messagebox
import data

win = Tk()
win.resizable(0,0)
win.geometry("500x400+400+150")
win.config(bg="light blue")
win.title("LOGIN FORM")
db1 = data.database("D:/project 3/data.db")
##################################################################
def insert():
    fname = ent_fname.get()
    lname = ent_lname.get()
    email = ent_email.get()
    password = ent_password.get()
    
    if fname == "" or lname == "" or email == "" or password == "":
        messagebox.showerror("ERROR","FILL ALL THE BLANK")

    else:
        db1.insert_record(fname,lname,email,password)
        clear()
        



def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_password.delete(0,END)
    ent_fname.focus()



def search():
    email = ent_email.get().strip()
    password = ent_password.get().strip()
    a =  db1.search(email,password)
    if len(a) == 0:
         messagebox.showerror("ERROR","PLEASE SIGN UP")
    else:
        clear()
        roat = Tk()
        roat.resizable(0,0)
        roat.geometry("400x300")
        roat.config(bg="light blue")
        roat.mainloop()
        

        





##################################################################
lbl_fname = Label(win,text="NAME : ",font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_fname.place(x=60,y=30)

lbl_lname = Label(win,text="FAMILY : ",font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_lname.place(x=60,y=100)

lbl_email = Label(win,text="EMAIL : ",font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_email.place(x=60,y=170)

lbl_password = Label(win,text="PASSWORD : ",font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_password.place(x=60,y=240)

lbl_star1 = Label(win,text="*",font=("Comic Sans MS", 12, "bold"),fg="red",bg="light blue")
lbl_star1.place(x=45,y=170)

lbl_star2 = Label(win,text="*",font=("Comic Sans MS", 12, "bold"),fg="red",bg="light blue")
lbl_star2.place(x=45,y=240)


##################################################################

ent_fname = Entry(win,font=("Comic Sans MS", 12, "bold"),width=20)
ent_fname.place(x=180,y=30)

ent_lname = Entry(win,font=("Comic Sans MS", 12, "bold"),width=20)
ent_lname.place(x=180,y=100)

ent_email = Entry(win,font=("Comic Sans MS", 12, "bold"),width=20)
ent_email.place(x=180,y=170)

ent_password = Entry(win,font=("Comic Sans MS", 12, "bold"),width=20,show="*")
ent_password.place(x=180,y=240)


##################################################################
btn_sign_up = Button(win,text="SIGN UP",font=("Comic Sans MS", 12, "bold"),width=15,command=insert)
btn_sign_up.place(x=50,y=330)

btn_sign_in = Button(win,text="SIGN IN",font=("Comic Sans MS", 12, "bold"),width=15,command=search)
btn_sign_in.place(x=290,y=330)







win.mainloop()