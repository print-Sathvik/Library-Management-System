import tkinter
from tkinter import messagebox
def encrypt(roll,password):
    n=int(roll[-3:])
    moves=n%26
    encrypted=""
    cipher=""
    for i in password:
        if(i.isupper()):
            if(moves+ord(i)>=65 and moves+ord(i)<=90):
                cipher=cipher+chr(ord(i)+moves)
            else:
                cipher=cipher+chr(64+moves-(90-ord(i)))
        elif(i.islower()):
            if(moves+ord(i)>=97 and moves+ord(i)<=122):
                cipher=cipher+chr(ord(i)+moves)
            else:
                cipher=cipher+chr(96+moves-(122-ord(i)))
        elif(i.isnumeric()):
            cipher=cipher+str(int(i)+moves)[-1]
        else:
            cipher=cipher+i
    symbols={'A':'☺','B':'☻','C':'♥','D':'♦','E':'♣','F':'♠','G':'•','H':'◘','I':'○','J':'◙','K':'♂','L':'♀','M':'♪','N':'♫','O':'☼','P':'►','Q':'◄','R':'↕','S':'‼','T':'¶','U':'§','V':'▬','W':'↨','X':'↑','Y':'↓','Z':'→',
             'a':'←','b':'∟','c':'↔','d':'▲','e':'▼','f':'Ɯ','g':'!','h':'*','i':'.','j':'`','k':'⌂','l':'Ç','m':'ü','n':'¡','o':'¢','p':'£','q':'¤','r':'¥','s':'¦','t':'¨','u':'©','v':'«','w':'¬','x':'®','y':'¯','z':'±',
             '0':'ƍ','1':'Ƃ','2':'ƛ','3':'Ɵ','4':'Ƣ','5':'ƪ','6':'ƾ','7':'Ǣ','8':'ȡ','9':'ʘ'}
    for i in cipher:
        if(symbols.get(i)==None):
            encrypted=encrypted+i
        else:
            encrypted=encrypted+symbols.get(i)
    return encrypted






def signup():
    file1=open('student_ids.txt','ab+')
    global stu_id_var
    global pass_var
    global confirmpass_var
    global oper
    stu_id=stu_id_var.get()
    
    alphabet=0
    digits=0
    specialChar=0
    caps=0
    low=0
    message_text=""
    confirm_status=True
    pswrd=pass_var.get()
    if(stu_id==""):
        messagebox.showerror("Error","User ID cannot be empty")
        f1.focus()
        f1.config(highlightcolor="red",highlightthickness=6)
        return
    else:
        f1.config(highlightcolor="black",highlightthickness=6)
    if(len(pswrd)<6):
        message_text=message_text+'The password must be atleast 6 characters\n'
    if(len(pswrd)>16):
        message_text=message_text+'The password should not exceed 16 characters\n'
    for x in range(len(pswrd)):
       if(pswrd[x].isalpha()):
           alphabet+=1
       if(pswrd[x].isnumeric()):
           digits+=1
       if(pswrd[x].isupper()):
           caps+=1
       if(pswrd[x].islower()):
           low+=1
       if not pswrd[x].isalpha() and not pswrd[x].isnumeric():
           specialChar+=1
    if(alphabet==0):
        message_text=message_text+'Password should contain atleast one alphabet\n'
    if(caps==0):
        message_text=message_text+'Password should contain atleast one Capital letter\n'
    if(low==0):
        message_text=message_text+'Password should contain atleast one Small letter\n'
    if(digits==0):
        message_text=message_text+'Password should contain atleast one digit\n'
    if(specialChar==0):
        message_text=message_text+'Password should contain atleast one special character\n'
    if(pswrd!=confirmpass_var.get()):
        confirm_status=False
    if(alphabet==0 or caps==0 or low==0 or digits==0 or specialChar==0 or caps==0):
        message_text=message_text+'Password is invalid\n'
        message_text=message_text+'Please try again\n'
    elif(confirmpass_var.get()!=pswrd):
        message_text=message_text+'The confirmation password did not match the original password\n'
        message_text=message_text+'Please recheck your password\n'
    else:
        file1.seek(0)
        s=file1.readline().decode("utf-8").split('\t')
        while(s[0]!=""):
            if(s[0]==stu_id):
                messagebox.showinfo("Id error",'The student has already signed up, please sign in')
                return
            s=file1.readline().decode("utf-8").split('t')
        if(oper=='a'):
            file1.write(bytes(stu_id+'\t',"utf-8"))
            encrypted_pswrd=encrypt(stu_id,pswrd)
            file1.write(bytes(encrypted_pswrd+'\n',"utf-8"))
            pswd=2
            messagebox.showinfo("Info","Signed up Successfully\nSign in to continue")
            loginwindow.after(5000,loginwindow.destroy)
    if(message_text!=""):
        messagebox.showwarning("Warning",message_text)
        f2.config(highlightcolor="red",highlightthickness=6)
        f3.config(highlightcolor="red",highlightthickness=6)
    else:
        f2.config(highlightcolor="green",highlightthickness=6)
        f3.config(highlightcolor="green",highlightthickness=6)
    #listbox.place(x=200,y=450)
    return




def signin():
    file1=open('student_ids.txt','ab+')
    global stu_id_var
    global pass_var
    global oper
    
    file1.seek(0,2)
    end=file1.tell()
    file1.close()
    file1=open('student_ids.txt','rb')
    login='unsuccess'
    flag='flse'
    id_status=False
    username=stu_id_var.get()
    while file1.tell()<end:
        lt_ids=file1.readline().decode("utf-8").strip('\n').split('\t')
        if username==lt_ids[0]:
            id_status=True
            paswrd=pass_var.get()
            encrypted_pswrd=encrypt(username,paswrd)
            if encrypted_pswrd==lt_ids[1]:
                messagebox.showinfo("Login","Login Successful")
                login='success'
                f2.config(highlightcolor="green",highlightthickness=6)
                loginwindow.after(4000,loginwindow.destroy)
            else:
                messagebox.showerror("Login Error",'Password is incorrect\nPlease try again')
                f2.focus()
                f2.config(highlightcolor="red",highlightthickness=6)
    
    if id_status==False:
        messagebox.showerror("Login Error",'Invalid username\nSignup if you are new\nPlease try again')
        f1.focus()
        f1.config(highlightcolor="red",highlightthickness=6)
        file1.seek(0)
    else:
        f1.config(highlightcolor="green",highlightthickness=6)
    return




def studentwidgets():
    global loginwindow
    global login_bg
    global user_img
    global idbox_img
    global password_img
    global stu_id_var
    global pass_var
    global confirmpass_var
    global oper
    global f1
    global f2
    global f3
    loginwindow=tkinter.Tk()
    width=loginwindow.winfo_screenwidth()
    height=loginwindow.winfo_screenheight()
    loginwindow.geometry("{}x{}".format(width,height))
    t=tkinter.Canvas(loginwindow)
    t.pack(fill="both",expand=True)
    login_bg=tkinter.PhotoImage(file="login.png")
    t.create_image(0,0,image=login_bg,anchor="nw")
    user_img=tkinter.PhotoImage(file="user.png")
    t.create_image(650,140,image=user_img)
    stu_id_var=tkinter.StringVar()
    pass_var=tkinter.StringVar()
    confirmpass_var=tkinter.StringVar()



    f1=tkinter.Frame(t,bg="snow",highlightcolor="black",highlightthickness=5)
    idbox_img=tkinter.PhotoImage(file="idbox.png")
    idbox_label=tkinter.Label(f1,image=idbox_img)
    idbox_label.pack(side="left")
    f2=tkinter.Frame(t,bg="snow",highlightcolor="black",highlightthickness=5)
    password_img=tkinter.PhotoImage(file="passwordbox.png")
    passwordbox_label=tkinter.Label(f2,image=password_img)
    passwordbox_label.pack(side="left")
    f3=tkinter.Frame(t,bg="snow",highlightcolor="black",highlightthickness=5)
    confirmbox_label=tkinter.Label(f3,image=password_img)
    confirmbox_label.pack(side="left",fill="y")



    e_id=tkinter.Entry(f1,textvariable=stu_id_var,width=30,bd=0,font=('open sans',16))
    e_password=tkinter.Entry(f2,show="•",textvariable=pass_var,width=30,bd=0,font=('open sans',16,'bold'))
    e_confirm=tkinter.Entry(f3,show="•",textvariable=confirmpass_var,width=30,bd=0,font=('open sans',16,'bold'))
    label1=tkinter.Label(t,text='USERNAME  :',anchor='e',width=21,font=('open sans',14))
    label2=tkinter.Label(t,text='PASSWORD  :',anchor='e',width=21,font=('open sans',14))
    label3=tkinter.Label(t,text='CONFIRM PASSWORD  :',anchor='e',width=21,font=('open sans',14))
    b1=tkinter.Button(t,text='Sign up',bd=10,fg='blue',bg='red',activebackground='purple',activeforeground='pink',command=signup,width=11,font=('open sans',14,'bold'))
    listbox=tkinter.Listbox(t,width=75,font=("open sans",14))
    e_id.focus()



    oper=input("Enter a or b : ")
    if(oper=='a'):
        t.create_text(550,30,text="Sign up",anchor="w",fill="white",font=("open sans",28,"bold"))
        t.create_text(550,285,text="USERNAME  :",anchor="e",fill="white",font=("open sans",16,"bold"))
        t.create_text(550,380,text="PASSWORD  :",anchor="e",fill="white",font=("open sans",16,"bold"))
        t.create_text(550,475,text="CONFIRM PASSWORD  :",anchor="e",fill="white",font=("open sans",16,"bold"))
        e_id.pack(side="left",fill="y")
        e_password.pack(side="left",fill="y")
        e_confirm.pack(side="left",fill="y")
        '''e_id.place(x=660,y=260)
        e_password.place(x=660,y=350)
        e_confirm.place(x=660,y=440)'''
        f1.place(x=600,y=260)
        f2.place(x=600,y=350)
        f3.place(x=600,y=440)
        b1.place(x=580,y=550)
        e_id.bind('<Return>',lambda a=None:e_password.focus())
        e_password.bind('<Return>',lambda a=None:e_confirm.focus())
        e_confirm.bind('<Return>',lambda a=None:signup())
        loginwindow.mainloop()
    if(oper=='b'):
        b1.config(text="Login",command=signin)
        t.create_text(580,30,text="Login",anchor="w",fill="white",font=("open sans",28,"bold"))
        t.create_text(550,285,text="USERNAME  :",anchor="e",fill="white",font=("open sans",16,"bold"))
        t.create_text(550,380,text="PASSWORD  :",anchor="e",fill="white",font=("open sans",16,"bold"))
        e_id.pack(side="left",fill="y")
        e_password.pack(side="left",fill="y")
        e_confirm.pack(side="left",fill="y")
        '''e_id.place(x=620,y=110)
        e_password.place(x=620,y=180)'''
        f1.place(x=600,y=260)
        f2.place(x=600,y=350)
        b1.place(x=580,y=500)
        e_id.bind('<Return>',lambda a=None:e_password.focus())
        e_password.bind('<Return>',lambda a=None:signin())
        loginwindow.mainloop()



if __name__=='__main__':
    studentwidgets()













