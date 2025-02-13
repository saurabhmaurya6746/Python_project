from tkinter import *
from random import randint

m=Tk()

ch=5
sys_num=randint(0,10)
def check_num():
    global ch
    global sys_num
    print(sys_num)
    if(ch>0):
        user_num=num.get()
        if(sys_num==user_num):
            ch=ch-1
            msg="you won ! "
        else:
            ch-=1
            msg= " you have chance --> {}".format(ch)
    else:
        msg="you have no chance !"
    lb2["text"]=msg

def res():
    global ch 
    global sys_num
    ch=5
    sys_num=randint(0,10)
    lb2["text"]="---> start <--"

m.title("saurabh projetc 05".center(20,'_'))
m.geometry('500x500')
LF=LabelFrame(m,text="Number Gussing ",font=(18),bg="pink")
LF.pack(fill=BOTH,expand=1)
lb=Label(LF,bg='#2838F2',text="guess any number for 0 to 9 ",font=18)
lb.pack(fill=X,expand=1)

num=IntVar()
le=Entry(LF,font=18,justify=CENTER,textvariable=num)
le.pack(fill=X,expand=1)
bt=Button(LF,text="Guess",font=(18),bg="#67c441",command=check_num)
bt.pack(expand=1)
lb2=Label(LF,text='---> start <--',bg='#2838F2',font=18)
lb2.pack(fill=X,expand=1)

res=Button(m,text='Restart',font=18,bg="#67c441",command=res)
res.pack(side=LEFT,padx=40,pady=40)

ex=Button(m,text='Exit',bg='red',font=18,command=lambda:m.destroy())
ex.pack(side=RIGHT,padx=40,pady=40)



m.mainloop()


# pack method
'''             this method is used to oraginized the parent of main windows 
syntax -->    widget.pack(---pack option )
pack option --> a> expand - if you want to expand the widget then expand is true
                b> fill - the fill option is use an extra space to the widget (fill = x or fill =y or fill=both )
                c> side - the side option is used to set the widget position 
                d>i-padding
                e> padding
                '''