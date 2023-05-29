import runpy

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
    return



def replace():
    global handleerror
    global return_check
    global p
    for i in stu_frame1.winfo_children():
        i.place_forget()
    '''for i in stu_frame2.winfo_children():
        i.pack_forget()'''
    p=tkinter.IntVar(value=0)
    '''q=tkinter.IntVar(value=0)
    r=tkinter.IntVar(value=0)'''
    return_check=[None,None,None]
    return_check[0]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=1,font=("open sans",16))
    return_check[1]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=2,font=("open sans",16))
    return_check[2]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=3,font=("open sans",16))
    return_button=tkinter.Button(stu_frame1,text="Return",bd=6,font=("open sans",14,"bold"),bg="red",command=lambda:student_operations(3))
    return_button.place(x=500,y=500)

    '''return_check[0].pack(pady=20)
    return_check[1].pack(pady=20)
    return_check[2].pack(pady=20)'''
    no_of_books=0
    with open("Student_logs\\"+username+".txt","a+") as f:
        f.seek(0)
        while(f.readline()!=''):
            no_of_books=no_of_books+1
        from datetime import date
        f.seek(0)
        handleerror=no_of_books
        for i in range(no_of_books):
            result=Search.byno(f.readline().split('\t')[0])
            if(result!=False):
                return_check[i].config(text=result[1].title()+" ("+result[0]+")")
                return_check[i].place(x=500,y=100+100*i)
    stu_frame1.place(x=201,y=100)



def student_operations(operation):
    #operation=int(input())
    if(operation==1):
        place_search_widgets()
    if(operation==2):
        global e_name
        global e_no
        global e_date
        import os
        cwd=os.getcwd()
        try:
            os.mkdir(cwd+"\\Student_logs")
        except:
            pass
        if(date_var.get()==""):
            messagebox.showerror("Empty","Date cannot be empty")
            return
        d=list(map(int,date_var.get().split("-")))
        from datetime import date, timedelta
        borrow_date=date(d[2],d[1],d[0])
        return_date=borrow_date+timedelta(days=15)
        
        no_of_books=0
        with open("Student_logs\\"+username+".txt","a+") as stlogs:
            #n=int(input("Enter number of books you are borrowing : "))
            stlogs.seek(0)
            while(stlogs.readline()!=''):
                no_of_books=no_of_books+1
            if(no_of_books<3):
                #book=int(input("Enter book to borrow : "))
                if(entry_var1.get()!="" and entry_var2.get()==""):
                    result=Search.byname(entry_var1.get())
                elif(entry_var1.get()=="" and entry_var2.get()!=""):
                    result=Search.byno(entry_var2.get())
                elif(entry_var1.get()=="" and entry_var2.get()==""):
                    messagebox.showerror("Entry Error","Both the fields cannot be empty")
                    return
                elif(entry_var1.get()!="" and entry_var2.get()!=""):
                    messagebox.showwarning("Entry Warning","Enter only name or ISBN, not both")
                    return
                if(result!=False):
                    stlogs.write(result[0]+'\t'+str(borrow_date)+'\t'+str(return_date)+'\n')
                    messagebox.showinfo("Return date","You must return the book by "+str(return_date.strftime("%d-%m-%Y")))
                    e_name.delete(0,"end")
                    e_no.delete(0,"end")
                    e_date.delete(0,"end")
                else:
                    messagebox.showerror("Wrong book","No book with given name or number")
                borr=open("borrowers.txt","ab+")
                end=borr.seek(0,2)
                borr.close()
                borr=open("borrowers.txt","a+")
                borr.seek(0)
                present=False
                while(borr.tell()<end):
                    if(username==borr.readline().rstrip('\n')):
                        present=True
                        break
                if(present==False):
                    borr.write(username+'\n')
                borr.close()
            else:
                messagebox.showwarning("Warning","You cannot borrow more than 3 books")
    if(operation==3):
        global handleerror
        borr=open("borrowers.txt","a+")
        no_of_books=0
        with open("Student_logs\\"+username+".txt","a+") as f:
            f.seek(0)
            while(f.readline()!=''):
                no_of_books=no_of_books+1
            from datetime import date
            #t=list(map(int,input("Enter today's date as DD-MM-YYYY : ").split("-")))#or date.today()
            todAy=date.today()#(t[2],t[1],t[0])
            f.seek(0)
            newremovedlist=[None,None,None]
            n=p.get()
            return_check[n-1].place_forget()
            f.seek(0)
            lis=f.readlines()
            remove=lis.pop(n-1).split('\t')
            handleerror=handleerror-1
            actual_return=list(map(int,remove[2].rstrip('\n').split('-')))
            actual_return_date=date(actual_return[0],actual_return[1],actual_return[2])
            if((todAy-actual_return_date).days>0):
                fine=(todAy-actual_return_date).days*10
                messagebox.showwarning("Late Submission","You have returned the book late by "+str((todAy-actual_return_date).days)+" days\nYou need to pay a fine of Rs."+str(fine))
        f=open("Student_logs\\"+username+".txt","w+")
        f.writelines(lis)
        f.seek(0)
        s=f.read()
        f.close()
        if(s==""):
            from os import remove, rename
            remove("Student_logs\\"+username+".txt")
            bd=open("borrowers_dup.txt",'w')
            borr.seek(0,2)
            end=borr.tell()
            borr.seek(0)
            while(borr.tell()<end):
                s=borr.readline()
                if(s.rstrip('\n')==username):
                        pass
                else:
                    bd.write(s)
            borr.close()
            bd.close()
            rename("borrowers.txt","temporary.txt")
            rename("borrowers_dup.txt","borrowers.txt")
            rename("temporary.txt","borrowers_dup.txt")
        borr.close()
        if(handleerror>0):replace()
    if(operation==6):
        f=open("requested_books.txt","a+")
        f.seek(0,2)
        end=f.tell()
        f.seek(0)
        s=f.readline().split('\t')
        presence=False
        while(f.tell()<end):
            if(s[0].lower()==requestvar.get().lower()):
                s[1]=str(int(s[1].strip('\n'))+1)+'\n'
                presence=True
                break
            s=f.readline().split('\t')
        g=open("requested_books_duplicate.txt","w+")
        f.seek(0)
        if(presence==True):
            s1=f.readline()
            while(s1!=""):
                if(s1.split('\t')[0].lower()==requestvar.get().lower()):
                    f.readline()
                    continue
                g.write(s1)
                s1=f.readline()
            g.write(s[0]+'\t'+s[1])
            from os import rename
            f.close()
            g.close()
            rename("requested_books.txt","temporar.txt")
            rename("requested_books_duplicate.txt","requested_books.txt")
            rename("temporar.txt","requested_books_duplicate.txt")
        else:
            f.write(requestvar.get()+'\t'+'1\n')
            f.close()
            g.close()





def place_stud_widgets(k):
    if(k==1):
        place_search_widgets()
    elif(k==2):
        global e_name
        global e_no
        global e_date
        global entry_var1
        global entry_var2
        global date_var
        for i in stu_frame1.winfo_children():
            i.place_forget()
        '''for i in stu_frame2.winfo_children():
            i.pack_forget()'''
        #stu_frame2.destroy()
        entry_var1=tkinter.StringVar()
        entry_var2=tkinter.StringVar()
        date_var=tkinter.StringVar()
        e_name=tkinter.Entry(stu_frame1,width=40,textvariable=entry_var1,font=("open sans",14),bd=4,highlightthickness=4,highlightcolor='black')
        e_no=tkinter.Entry(stu_frame1,width=40,textvariable=entry_var2,bd=4,font=("open sans",14),highlightthickness=4,highlightcolor='black')
        e_date=tkinter.Entry(stu_frame1,width=40,textvariable=date_var,bd=4,font=("open sans",14),highlightthickness=4,highlightcolor='black')
        e_name.bind('<Return>',lambda a=None:e_date.focus())
        e_no.bind('<Return>',lambda:student_operations(k))
        borrow_button=tkinter.Button(stu_frame1,text="Borrow",bd=6,font=("open sans",14,"bold"),bg="red",command=lambda:student_operations(k))
        borrow_button.place(x=570,y=500)
        borrow_by_name=tkinter.Label(stu_frame1,text="Name  :",width=12,anchor='e',font=("open sans",14))
        borrow_by_no=tkinter.Label(stu_frame1,text="ISBN  :",width=12,anchor='e',font=("open sans",14))
        date_of_issue=tkinter.Label(stu_frame1,text="Date of issue  :",width=12,anchor='e',font=("open sans",14))
        borrow_by_name.place(x=220,y=120)
        borrow_by_no.place(x=220,y=300)
        date_of_issue.place(x=220,y=390)
        or_label=tkinter.Label(stu_frame1,width=3,height=1,text="Or",bd=4,font=("open sans",24))
        e_name.place(x=480,y=120)
        e_no.place(x=480,y=300)
        e_date.place(x=480,y=390)
        or_label.place(x=650,y=210)
        stu_frame1.place(x=201,y=40)
    elif(k==3):
        global handleerror
        global return_check
        global p
        for i in stu_frame1.winfo_children():
            i.place_forget()
        '''for i in stu_frame2.winfo_children():
            i.pack_forget()'''
        p=tkinter.IntVar(value=0)
        return_check=[None,None,None]
        return_check[0]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=1,font=("open sans",16))
        return_check[1]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=2,font=("open sans",16))
        return_check[2]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=3,font=("open sans",16))
        return_button=tkinter.Button(stu_frame1,text="Return",bd=6,font=("open sans",14,"bold"),bg="red",command=lambda:student_operations(k))
        return_button.place(x=540,y=500)

        no_of_books=0
        from os import listdir
        if(str(username)+".txt" in listdir("Student_logs")):
            pass
        else:
            no_book=tkinter.Label(stu_frame1,font=("open sans",16),text="You have Not borrowed any book")
            no_book.place(x=50,y=100)
            return
        with open("Student_logs\\"+username+".txt","a+") as f:
            f.seek(0)
            while(f.readline()!=''):
                no_of_books=no_of_books+1
            from datetime import date
            f.seek(0)
            handleerror=no_of_books
            for i in range(no_of_books):
                result=Search.byno(f.readline().split('\t')[0])
                if(result!=False):
                    return_check[i].config(text=result[1].title()+" ("+result[0]+")")
                    return_check[i].place(x=540,y=100+100*i)
        stu_frame1.place(x=201,y=100)
    elif(k==4):
        for i in stu_frame1.winfo_children():
            i.place_forget()
        '''for i in stu_frame2.winfo_children():
            i.place_forget()'''
        borrowed_box=tkinter.Listbox(stu_frame1,height=25,width=50,font=("open sans",16))
        from os import path
        if(path.isfile("Student_logs\\"+username+".txt")):
            from datetime import date,datetime
            #t=list(map(int,input("Enter today's date as DD-MM-YYYY : ").split("-")))#or date.today()
            todAy=date.today()#date(t[2],t[1],t[0])
            borr=open("Student_logs\\"+username+".txt","r")
            borr.seek(0,2)
            end=borr.tell()
            borr.seek(0)
            with open("Student_logs\\"+username+".txt","r") as u:
                s=u.readlines()
                if(s!=""):
                    c=0
                    for i in s:
                        actual_return=list(map(int,(i.rstrip('\n').split('\t')[2]).split('-')))
                        actual_return_date=date(actual_return[0],actual_return[1],actual_return[2])
                        borrowed_no=i.rstrip('\n').split('\t')[0]
                        borrowed_date_str=i.rstrip('\n').split('\t')[1]
                        borrowed_date=datetime.strptime(borrowed_date_str,"%Y-%m-%d")
                        if((todAy-actual_return_date).days>0):
                            late_days=(todAy-actual_return_date).days
                            #print(user.center(16),str(actual_return_date).center(25),str(late_days).center(6))
                        borrowed_box.insert(c+1,"Book Name  :  "+Search.byno(borrowed_no)[1])
                        borrowed_box.insert(c+2,"ISBN  :  "+borrowed_no)
                        borrowed_box.insert(c+3,"Date of Issue  :  "+str(borrowed_date.day)+'-'+str(borrowed_date.month)+'-'+str(borrowed_date.year))
                        borrowed_box.insert(c+4,"Return Date  :  "+str(actual_return_date.strftime("%d-%m-%Y")))
                        borrowed_box.insert(c+5,"")
                        borrowed_box.insert(c+6,"")
                        c=c+6
                else:
                    borrowed_box.insert(1,"The are NO books borrowed by you currently")
        else:
            borrowed_box.insert(1,"The are NO books borrowed by you currently")
        borrowed_box.place(x=15,y=10)
        stu_frame1.place(x=201,y=100)
    elif(k==6):
        global requestvar
        for i in stu_frame1.winfo_children():
            i.place_forget()
        requestvar=tkinter.StringVar()
        e_request=tkinter.Entry(stu_frame1,width=40,textvariable=requestvar,font=("open sans",14),bd=4,highlightthickness=4,highlightcolor='black')
        request_button=tkinter.Button(stu_frame1,text="Request Book",bd=6,font=("open sans",14,"bold"),bg="red",command=lambda:student_operations(k))
        name_label=tkinter.Label(stu_frame1,text="Name  :",width=10,anchor='e',font=("open sans",16))
        name_label.place(x=150,y=200)
        e_request.place(x=450,y=200)
        request_button.place(x=480,y=450)
        stu_frame1.place(x=201,y=100)
    elif(k==7):
        confirm_logout=messagebox.askquestion("Log out","Are you sure to log out?")
        if(confirm_logout=="yes"):
            stuwindow.destroy()




def stu():
    global oper
    oper=input("Enter a or b : ")
    studentwidgets()
    global stuwindow
    global handleerror
    global return_check
    global stu_frame1
    global username
    if(oper=='a'):
        oper=='b'
        studentwidgets()
    elif(oper=='b'):
        username=stu_id_var.get()#
    username=stu_id_var.get()
    from datetime import date, timedelta
    stuwindow=tkinter.Toplevel()
    height=stuwindow.winfo_screenheight()
    width=stuwindow.winfo_screenwidth()
    stuwindow.geometry("{}x{}".format(width,height))
    stu_frame1=tkinter.Frame(stuwindow,width=width-200,height=height-50,bd=10)

    c1=tkinter.Canvas(stuwindow,bg="sky blue",width=200)
    c2=tkinter.Canvas(stuwindow,bg="sky blue",height=250)
    c1.pack(side="left",fill="y")
    c2.pack(side="top",fill="x")
    process_label=tkinter.Label(c2,width=10,height=2,text="User "+str(username),font=("open sans",25),bg="sky blue")
    process_label.pack(fill="both")


    c1b1=tkinter.Button(c1,text="Search",bg="sky blue",bd=0,width=13,anchor='w',font=("open sans",14),command=lambda:place_stud_widgets(1))
    c1b2=tkinter.Button(c1,text="Borrow Book",bg="sky blue",bd=0,width=13,anchor='w',font=("open sans",14),command=lambda:place_stud_widgets(2))
    c1b3=tkinter.Button(c1,text="Return Book",bg="sky blue",bd=0,width=13,anchor='w',font=("open sans",14),command=lambda:place_stud_widgets(3))
    c1b4=tkinter.Button(c1,text="View your books",bg="sky blue",bd=0,width=13,anchor='w',font=("open sans",14),command=lambda:place_stud_widgets(4))
    c1b5=tkinter.Button(c1,text="Change password",bg="sky blue",bd=0,width=16,anchor='w',font=("open sans",14),command=lambda:place_stud_widgets(5))
    c1b6=tkinter.Button(c1,text="Request Book",bg="sky blue",bd=0,width=12,font=("open sans",14),command=lambda:place_stud_widgets(6))
    c1b7=tkinter.Button(c1,text="Log Out",bg="sky blue",bd=0,width=6,font=("open sans",14),command=lambda:place_stud_widgets(7))
    c1b1.place(x=15,y=180)
    c1b2.place(x=15,y=250)
    c1b3.place(x=15,y=320)
    c1b4.place(x=15,y=390)
    c1b5.place(x=15,y=460)
    c1b6.place(x=15,y=530)
    c1b7.place(x=15,y=600)
    c1.create_line(5,235,200,235,width=2)
    c1.create_line(5,305,200,305,width=2)
    c1.create_line(5,375,200,375,width=2)
    c1.create_line(5,445,200,445,width=2)
    c1.create_line(5,515,200,515,width=2)
    c1.create_line(5,585,200,585,width=2)

    stuwindow.mainloop()

if __name__=='__main__':
    stu()

















