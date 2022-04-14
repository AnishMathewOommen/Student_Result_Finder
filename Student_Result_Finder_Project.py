from tkinter import *
from tkinter import ttk
from  tkinter.font import Font
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


def clear(s=" "):
    T1.set(s)
    T2.set(s)
def submit():
    data1=T1.get()
    data2=T2.get()




    if data1=="ANISH_RMKCET" and data2=="111619104006" :
        top=Tk()
        top.title("RESULT FINDER")
        top.geometry("1000x1000")
        top.config(bg="#2980b9")



        n1=Label(top,text="Common Exam Result Finder",font=("Cambria",25,"bold"),bg="#2c3e50",fg="white",height=2,width=40,relief="raised")
        n1.pack(pady=30,fill=X)

        Frame=LabelFrame(top,bg="#7f8c8d")
        Frame.pack()
        v=StringVar(top)
        f=0

        def clr(s=" "):
            v.set(s)
        def sub():
            conn=sqlite3.connect("RESULT.db")
            cur=conn.cursor()
            tree=ttk.Treeview(top,columns=(1,2,3,4,5),show='headings',height=10)
            tree.pack()
            tree.column('#1',stretch=NO,width=100)
            tree.column('#2',stretch=NO,width=100)
            tree.column('#3',stretch=NO,width=100)
            tree.column('#4',stretch=NO,width=100)
            tree.column('#5',stretch=NO,width=100)
            tree.heading(1,text="SNO")
            tree.heading(2,text="ENO")
            tree.heading(3,text="SNAME")
            tree.heading(4,text="SUBJECT")
            tree.heading(5,text="Grade")
            value=v.get()
            sql="""SELECT * FROM List WHERE ENO='101'"""
            cur.execute(sql)
            rows=cur.fetchall()
            for row in rows:
                tree.insert(parent='',index=0,iid=0,text=' ',values=row)
                f=1

            if f==0:
               n2=Label(top,text="DATA NOT FOUND",font=("Cambria",25,"bold"),bg="#badc58",fg="black",height=2,width=40,relief="raised").pack(pady=50)

        #CREATION
        n2=Label(Frame,text="Enter Your En_Number",font=("Cambria",22,"bold"),bg="#fbc531",width=25).grid(row=0,column=1,pady=20)
        e1=Entry(Frame,textvariable=v,width=20,font=("Cambria",23,"bold"),bg="#ff7675",fg="#192a56").grid(row=0,column=2,padx=5,pady=20)
        Bu=Button(top,text="Submit",font=("Georgia",15,"bold"),bg="white",activebackground="light green",width=15,height=1,command=sub)
        Bu1=Button(top,text="Clear",font=("Georgia",15,"bold"),bg="white",activebackground="RED",width=15,height=1,command=lambda:clr(" "))
        Bu.pack(pady=10,anchor="s")
        Bu1.pack(pady=10,anchor="n")

        top.mainloop()

    else:
        messagebox.showwarning("showwarning", "\tINVALID\n  USERNAME / PASSWORD")







root=Tk()
root.title("RMKCET LOGIN ")
root.geometry("1000x1000")
root.config(bg="#01a3a4")
myfont=Font(family="Cambria",size=22,weight="bold")


#RMKCET COLLGE LOGO
img = ImageTk.PhotoImage(Image.open("E:\collegelogo.png"))
ImageLabel=Label(root,image=img).pack(padx=20,pady=20,side="left",anchor="nw")
l=Label(root,text="STUDENT LOGIN",font=myfont,bg="brown",fg="white",height=2,width=65,relief="raised").pack(side="top",pady=30)
F1=LabelFrame(root,bg="White")
F1.pack()
T1=StringVar(root)
T2=StringVar(root)
l1=Label(F1,text="Enter UserName ",font=myfont,bg="#192a56",fg="#dcdde1",width=15).grid(row=1,column=0,padx=5,pady=10)
l2=Label(F1,text="Password",font=myfont,bg="#192a56",fg="#dcdde1",width=15).grid(row=2,column=0,pady=10)
#Entry
E1=Entry(F1,text=T1,width=15,font=myfont,bg="#8395a7",fg="#192a56").grid(row=1,column=1)
E2=Entry(F1,text=T2,width=15,font=myfont,bg="#8395a7",fg="#192a56").grid(row=2,column=1)
#Button
B=Button(root,text="Submit",font=("Georgia",15,"bold"),bg="pink",activebackground="light green",width=15,height=1,command=submit).pack(anchor="c",padx=40,pady=20)
B1=Button(root,text="Clear",font=("Georgia",15,"bold"),bg="pink",activebackground="RED",width=15,height=1,command=lambda:clear(" ")).pack(anchor="c",padx=40)


root.mainloop()
