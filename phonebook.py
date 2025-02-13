from tkinter import *
m=Tk()
phoNum_list=[]
def addpho():
    global phoNum_list
    if[Name.get(),pho.get()] not in phoNum_list:
        phoNum_list.append([Name.get(),pho.get()])
    Listboxupdate()
    print(phoNum_list)
    
def Listboxupdate():
    global phoNum_list
    lbox.delete(0,END)
    for name,phone in phoNum_list:
        lbox.insert(END,name) 

def phodel():
    global phoNum_list
    del phoNum_list[lbox.curselection()[0]]
    Listboxupdate()

def phoview():
    global phoNum_list
    n,p=phoNum_list[lbox.curselection()[0]]
    Name.set(n)
    pho.set(p)

m.title("Abhinav project_06")
m.geometry("250x350+1000+100")

name=Label(m,text="Name")
name.grid(row=0,column=0,padx=10,pady=10)
mob=Label(m,text="Mobile")
mob.grid(row=1,column=0,padx=10,pady=10)
Name=StringVar()
ename=Entry(m,textvariable=Name)
ename.grid(row=0,column=1,padx=10,pady=10)
pho=IntVar()
epho=Entry(m,textvariable=pho)
epho.grid(row=1,column=1,padx=10,pady=10)

b1=Button(m,text="Add",width=6,command=addpho,height=2,bg='#21B121')
b1.grid(row=3,column=0,padx=10,pady=10)

b1=Button(m,text="View",width=6,height=2,command=phoview,bg='#E9AFCB')
b1.grid(row=4,column=0,padx=10,pady=10)

b1=Button(m,text="Delete",width=6,command=phodel,height=2,bg='#C1B7E1')
b1.grid(row=5,column=0,padx=10,pady=10)

b1=Button(m,text="Exit",width=6,height=2,command=lambda:m.destroy(),bg="red")
b1.grid(row=6,column=0,padx=10,pady=10)

lbox=Listbox(m)
lbox.grid(row=3,column=1,rowspan=6,padx=10,pady=10)

scroll=Scrollbar(m,orient=VERTICAL)
scroll.grid(row=2,column=2,rowspan=6,padx=10,pady=10)



m.mainloop()