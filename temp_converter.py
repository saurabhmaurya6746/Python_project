from tkinter import *
m=Tk()

def f_to_c():
    f=tpm.get()
    f=float(f)
    c=(f-32)*5/9
    rl["text"]=f'{f} fahrenheit = {c:2f} celsius'

def c_to_f():
    c=tpm.get()
    c=float(c)
    f=c*9/5+32
    rl["text"]=f'{c} celsius  = {c:2f} fahrenheit'

def C_to_F():
    mf1.pack_forget()
    mf1.pack(fill=BOTH,expand=True)

def F_to_C():
    mf2.pack_forget()
    mf2.pack(fill=BOTH,expand=True)

m.title(" project 05: by saurabh maurya")
m.geometry("350x255+1000+250")

sf=Frame(m)
sf.pack(fill=BOTH,expand=True)
mf1=Frame(sf)
mf1.pack(fill=BOTH,expand=True)
ftodl=Label(mf1,text="fohrenheit",width=8)
ftodl.pack(side=LEFT,padx=15)
tpm=StringVar()
ftode=Entry(mf1,textvariable=tpm)
ftode.pack(side=LEFT,padx=15)
ftodb=Button(mf1,text="Convert",bg="Red",command=f_to_c)
ftodb.pack(side=LEFT,padx=15)

mf2=Frame(sf)
mf2.pack(fill=BOTH,expand=True)
ftodl=Label(mf2,text="Celsius",width=8)
ftodl.pack(side=LEFT,padx=15)
tpm=StringVar()
ftode=Entry(mf2,textvariable=tpm)
ftode.pack(side=LEFT,padx=15)
ftodb=Button(mf2,text="Convert",bg="green",command=c_to_f)
ftodb.pack(side=LEFT,padx=15)


rl=Label(m,text="Welcome")
rl.pack()
lf=LabelFrame(m,text="Option")
lf.pack(fill=BOTH,expand=True)
val=IntVar()
val.set(1)
r1=Radiobutton(lf,text="C to F ",value=1, variable=val , command=C_to_F)
r1.pack(side=LEFT,padx=20)
r2=Radiobutton(lf,text="F to C ",value=0,variable=val,command=F_to_C)
r2.pack(side=RIGHT,padx=20)



m.mainloop()