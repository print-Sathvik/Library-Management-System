import tkinter
from os import path,rename,remove
from tkinter import messagebox

def addbooks(name,no,author,publisher,year,location,copies):
    global e
    global addwindow
    global width
    global height
    global entrys
    global warning
    global warn_label
    global warn_image
    try:
        warn_label.destroy()
        warn_image.destroy()
    except NameError:
        pass
    for i in entrys:
        if(i.get()==""):
            warn_label=tkinter.Label(addwindow,text='This field cannot be empty',bg="red",font=("open sans",12))
            warning=tkinter.PhotoImage(master=addwindow,file="warningbutton.png")
            warn_image=tkinter.Label(addwindow,image=warning)
            warn_image.place(x=960,y=(160+100*entrys.index(i))*height/1280)
            warn_label.place(x=1050,y=(180+100*entrys.index(i))*height/1280)
            e[entrys.index(i)].focus()
            return
    book_id=""
    for i in no:
        if(i=="-"):continue
        if(i.isdigit()):
            book_id=book_id+i
        else:
            messagebox.showerror("Entry Error","Wrong input for ISBN",parent=addwindow)
            e[1].focus()
            return
    no=book_id
    if(len(year)==4 and year.isdigit()):
        pass
    else:
        messagebox.showerror("Entry Error","Wrong input for year",parent=addwindow)
        return
    if(copies.isdigit()):
        pass
    else:
        messagebox.showerror("Entry Error","Wrong input for number of copies",parent=addwindow)
        return
    for i in range(7):
        e[i].delete(0,"end")
    e[0].focus()
    if(path.isfile("books.txt")==False):
        f=open("books.txt","a+")
        f.writelines(["\n\n",str(no)+'\n',name+'\n',author+'\n',publisher+'\n',str(year)+'\n',location+'\n'+str(copies)+'\n'])
        f.close()
        added_label=tkinter.Label(addwindow,text="Book is added to the library",width=35,bg="green2",font=("open sans",16))
        added_label.place(x=450*width/1280,y=900*height/1280)
        addwindow.after(1500,added_label.destroy)
    else:
        check=True
        f=open("books.txt","a+")
        f.seek(0,2)
        end=f.tell()
        f.seek(end-6)
        if(f.read()=='\n\n\n'):
            f.writelines([str(no)+'\n',name+'\n',author+'\n',publisher+'\n',str(year)+'\n',location+'\n'+str(copies)+'\n'])
            check=False
        if(check==True):
            f.writelines(["\n\n",str(no)+'\n',name+'\n',author+'\n',publisher+'\n',str(year)+'\n',location+'\n'+str(copies)+'\n'])
        f.close()
        added_label=tkinter.Label(addwindow,text="Book is added to the library",width=35,bg="green2",font=("open sans",16))
        added_label.place(x=450*width/1280,y=900*height/1280)
        addwindow.after(1500,added_label.destroy)
    return



def addbook():
    global addwindow
    global e
    global width
    global height
    global warning
    global entrys
    addwindow=tkinter.Toplevel(root)
    height=addwindow.winfo_screenheight()
    width=addwindow.winfo_screenwidth()
    addwindow.geometry("{}x{}".format(width,height))
    entrys=list()
    e=list()
    labels=list()
    for i in range(7):
        entrys.append(tkinter.StringVar())
    for i in range(7):
        e.append(tkinter.Entry(addwindow,width=35,textvariable=entrys[i],bd=4,font=("open sans",14),highlightthickness=4,highlightcolor='black'))
        labels.append(tkinter.Label(addwindow,width=15,anchor='e',font=("open sans",14)))

    e[0].focus()
    img=tkinter.PhotoImage(master=addwindow,file=r"click.png")
    b=tkinter.Button(addwindow,image=img,borderwidth=0,
                     command=lambda:addbooks(entrys[0].get(),entrys[1].get(),entrys[2].get(),entrys[3].get(),entrys[4].get(),entrys[5].get(),entrys[6].get()))
    b.pack(side="bottom")

    process_label=tkinter.Label(addwindow,width=10,height=1,text="Add Books",font=("open sans",32))
    process_label.place(x=500*width/1280,y=10*height/1280)#process_label.place(x=500,y=10)
    labels[0].config(text="Name  :")
    labels[1].config(text="ISBN  :")
    labels[2].config(text="Author  :")
    labels[3].config(text="Publisher  :")
    labels[4].config(text="Year  :")
    labels[5].config(text="Location  :")
    labels[6].config(text="copies  :")

    labels[0].place(x=220*width/1280,y=180*height/1280)#labels[0].place(x=220,y=180)
    labels[1].place(x=220*width/1280,y=280*height/1280)#labels[1].place(x=220,y=240)
    labels[2].place(x=220*width/1280,y=380*height/1280)#labels[2].place(x=220,y=300)
    labels[3].place(x=220*width/1280,y=480*height/1280)#labels[3].place(x=220,y=360)
    labels[4].place(x=220*width/1280,y=580*height/1280)#labels[4].place(x=220,y=420)
    labels[5].place(x=220*width/1280,y=680*height/1280)#labels[5].place(x=220,y=480)
    labels[6].place(x=220*width/1280,y=780*height/1280)#labels[6].place(x=220,y=540)

    e[0].place(x=480*width/1280,y=180*height/1280)#e[0].place(x=480,y=180)
    e[1].place(x=480*width/1280,y=280*height/1280)#e[1].place(x=480,y=240)
    e[2].place(x=480*width/1280,y=380*height/1280)#e[2].place(x=480,y=300)
    e[3].place(x=480*width/1280,y=480*height/1280)#e[3].place(x=480,y=360)
    e[4].place(x=480*width/1280,y=580*height/1280)#e[4].place(x=480,y=420)
    e[5].place(x=480*width/1280,y=680*height/1280)#e[5].place(x=480,y=480)
    e[6].place(x=480*width/1280,y=780*height/1280)#e[6].place(x=480,y=540)


    e[0].bind('<Return>',lambda a=None:e[1].focus())
    e[1].bind('<Return>',lambda a=None:e[2].focus())
    e[2].bind('<Return>',lambda a=None:e[3].focus())
    e[3].bind('<Return>',lambda a=None:e[4].focus())
    e[4].bind('<Return>',lambda a=None:e[5].focus())
    e[5].bind('<Return>',lambda a=None:e[6].focus())
    e[6].bind('<Return>',lambda a=None:addbooks(entrys[0].get(),entrys[1].get(),entrys[2].get(),entrys[3].get(),entrys[4].get(),entrys[5].get(),entrys[6].get()))
    addwindow.mainloop()
    return




class Search:
    @staticmethod
    def byname(key):
        f=open("books.txt","a+")
        f.seek(0)
        check=False
        n=f.tell()+1
        while(True):
            if(f.tell()==n):break
            n=f.tell()
            li=[]
            for i in range(9):
                if(i!=3):
                    li.append(f.readline().rstrip("\n"))
                else:
                    book_name=f.readline().rstrip("\n").lower()
                    if(key==book_name):
                        check=True
                        li.append(book_name)
            if(check==True):
                li.pop(0)
                li.pop(0)
                return li
            li=[]
        return False
    def byno(key):
        f=open("books.txt","a+")
        f.seek(0)
        check=False
        n=f.tell()+1
        while(True):
            if(f.tell()==n):break
            n=f.tell()
            li=[]
            for i in range(9):
                if(i!=2):
                    li.append(f.readline().rstrip("\n"))
                else:
                    book_no=f.readline().rstrip("\n").lower()
                    if(key==book_no):
                        check=True
                        li.append(book_no)
            if(check==True):
                li.pop(0)
                li.pop(0)
                return li
            li=[]
        return False
    def byauthor(key):
        f=open("books.txt","a+")
        f.seek(0)
        check=False
        author_books=[]
        n=f.tell()+1
        while(True):
            if(f.tell()==n):break
            n=f.tell()
            li=[]
            for i in range(9):
                if(i!=4):
                    li.append(f.readline().rstrip("\n"))
                else:
                    author_name=f.readline().rstrip("\n").lower()
                    if(key==author_name):
                        check=True
                        li.append(author_name)
            if(check==True):
                li.pop(0)
                li.pop(0)
                author_books.append(li)
            li=[]
            check=False
        return author_books
    def bypublisher(key):
        f=open("books.txt","a+")
        f.seek(0)
        check=False
        publisher_books=[]
        n=f.tell()+1
        while(True):
            if(f.tell()==n):break
            n=f.tell()
            li=[]
            for i in range(9):
                if(i!=5):
                    li.append(f.readline().rstrip("\n"))
                else:
                    publisher_name=f.readline().rstrip("\n").lower()
                    if(key==publisher_name):
                        check=True
                        li.append(publisher_name)
            if(check==True):
                li.pop(0)
                li.pop(0)
                publisher_books.append(li)
            li=[]
            check=False
        return publisher_books
    def bylocation(key):
        f=open("books.txt","a+")
        f.seek(0)
        check=False
        location_books=[]
        n=f.tell()+1
        while(True):
            if(f.tell()==n):break
            n=f.tell()
            li=[]
            for i in range(9):
                if(i!=7):
                    li.append(f.readline().rstrip("\n"))
                else:
                    location_name=f.readline().rstrip("\n").lower()
                    if(key==location_name):
                        check=True
                        li.append(location_name)
            if(check==True):
                li.pop(0)
                li.pop(0)
                location_books.append(li)
            li=[]
            check=False
        return location_books



class AdvancedSearch:
    @staticmethod
    def byname(key):
        import re
        f=open("books.txt","a+")
        f.seek(0)
        check=False
        name_books=[]
        n=f.tell()+1
        while(True):
            if(f.tell()==n):break
            n=f.tell()
            li=[]
            for i in range(9):
                if(i!=3):
                    li.append(f.readline().rstrip("\n"))
                else:
                    book=f.readline().rstrip("\n").lower()
                    searchlist=key.split() #list containing each word of key
                    for i in searchlist:
                        if(re.search(i,book)):
                            check=True
                            li.append(book)
                            break
            if(check==True):
                li.pop(0)
                li.pop(0)
                name_books.append(li)
            li=[]
            check=False
        return name_books
    def byauthor(key):
        import re
        f=open("books.txt","a+")
        f.seek(0)
        check=False
        auth_books=[]
        n=f.tell()+1
        while(True):
            if(f.tell()==n):break
            n=f.tell()
            li=[]
            for i in range(9):
                if(i!=4):
                    li.append(f.readline().rstrip("\n"))
                else:
                    author=f.readline().rstrip("\n").lower()
                    searchlist=key.split()#list containing each word of key
                    for i in key:
                        if(re.search(i,author)):
                            check=True
                            li.append(author)
                            break
            if(check==True):
                li.pop(0)
                li.pop(0)
                auth_books.append(li)
            li=[]
            check=False
        return auth_books
    def bypublisher(key):
        import re
        f=open("books.txt","a+")
        f.seek(0)
        check=False
        publ_books=[]
        n=f.tell()+1
        while(True):
            if(f.tell()==n):break
            n=f.tell()
            li=[]
            for i in range(9):
                if(i!=5):
                    li.append(f.readline().rstrip("\n"))
                else:
                    publisher=f.readline().rstrip("\n").lower()
                    searchlist=key.split()
                    for i in key:
                        if(re.search(i,publisher)):
                            check=True
                            li.append(publisher)
                            break
            if(check==True):
                li.pop(0)
                li.pop(0)
                publ_books.append(li)
            li=[]
            check=False
        return publ_books

def disp_result(optionsvar):
    global search_query
    global options
    global listbox
    try:
        listbox.destroy()
    except:
        pass
    listbox=tkinter.Listbox(search_w,width=105,height=25,font=("courier new",14))
    if(optionsvar=="Search by Book Name"):
        result = Search.byname(search_query.get().lower())
        if(result==False):
            listbox.insert(1,"Given book is NOT present in the library")
            adv_result=AdvancedSearch.byname(search_query.get().lower())
            if(len(adv_result)!=0):
                listbox.insert(2,"Books with similar names are :")
                s_no=1
                listbox.insert(3,"="*95)
                listbox.insert(4,"S.No.".ljust(5)+"Book Name".center(20)+"ISBN no.".center(19)+"Author".center(15)+"Publisher".center(15)+"Location".center(9))
                listbox.insert(5,"="*95)
                for i in adv_result:
                    listbox.insert(s_no+5,str(s_no).ljust(5)+i[1].center(20)+i[0].center(19)+i[2].center(15)+i[3].center(15)+i[5].center(9))
                    s_no=s_no+1
            else:
                listbox.insert(2,"No books found with given name even with Advanced Search in the library")
            listbox.pack(pady=10)
        else:
            copies=int(result[6])
            count=copies
            borr=open("borrowers.txt","a+")
            borr.seek(0,2)
            end=borr.tell()
            borr.close()
            from datetime import date
            borr=open("borrowers.txt","r")
            latestdate=date(1,1,1)
            while(borr.tell()<end):
                stud=open("Student_logs\\"+borr.readline().rstrip('\n')+".txt",'r')
                s=stud.readline()
                while(s!=""):
                    if(result[0]==s.split('\t')[0]):
                        count=count-1
                        retdatelist=list(map(int,s.split('\t')[2].strip('\n').split('-')))
                        thisdate=date(retdatelist[0],retdatelist[1],retdatelist[2])
                        if((latestdate-thisdate).days<0):latestdate=thisdate
                    s=stud.readline()
                stud.close()
            borr.close()
            listbox.insert(1,"The given book is present at location "+str(result[5]))
            if(count==0):
                listbox.insert(2,"This book is CURRENTLY UNAVAILABLE but it is present in the library")
                listbox.insert(3,"The book will be available by "+latestdate)
            listbox.insert(4,"Book details are :")
            listbox.insert(5,"Name".ljust(25)+":   "+result[1])
            listbox.insert(6,"ISBN no".ljust(25)+":   "+result[0])
            listbox.insert(7,"Author".ljust(25)+":   "+result[2])
            listbox.insert(8,"Publisher".ljust(25)+":   "+result[3])
            listbox.insert(9,"Year Published".ljust(25)+":   "+result[4])
            listbox.pack(pady=10)
    elif(optionsvar=="Search by ISBN"):
        result = Search.byno(search_query.get().lower())
        if(result==False):
            listbox.insert(1,"Book with given ISBN is NOT present in the library")
        else:
            copies=int(result[6])
            count=copies
            borr=open("borrowers.txt","rb")
            borr.seek(0,2)
            end=borr.tell()
            borr.close()
            from datetime import date
            latestdate=date(1,1,1)
            borr=open("borrowers.txt","r")
            while(borr.tell()<end):
                stud=open("Student_logs\\"+borr.readline().rstrip('\n')+".txt",'r')
                s=stud.readline()
                while(s!=""):
                    if(result[0]==s.split('\t')[0]):
                        count=count-1
                        retdatelist=list(map(int,s.split('\t')[2].strip('\n').split('-')))
                        thisdate=date(retdatelist[0],retdatelist[1],retdatelist[2])
                        if((latestdate-thisdate).days<0):latestdate=thisdate
                    s=stud.readline()
                stud.close()
            borr.close()
            listbox.insert(1,"The given book is present at location "+str(result[5]))
            if(count==0):
                listbox.insert(2,"This book is CURRENTLY UNAVAILABLE but it is present in the library")
                listbox.insert(3,"The book will be available by "+str(latestdate))
            listbox.insert(4,"Book details are :")
            listbox.insert(5,"Name".ljust(25)+":   "+result[1])
            listbox.insert(6,"ISBN no".ljust(25)+":   "+result[0])
            listbox.insert(7,"Author".ljust(25)+":   "+result[2])
            listbox.insert(8,"Publisher".ljust(25)+":   "+result[3])
            listbox.insert(9,"Year Published".ljust(25)+":   "+result[4])
        listbox.pack(pady=10)
    elif(optionsvar=="Search by Author name"):
        result = Search.byauthor(search_query.get().lower())
        if(len(result)==0):
            listbox.insert(1,"Books written by given author are NOT present in the library")
            adv_result=AdvancedSearch.byauthor(search_query.get().lower())
            if(len(adv_result)!=0):
                listbox.insert(2,"Books written by similar author names are :")
                s_no=1
                listbox.insert(3,"="*95)
                listbox.insert(4,"S.No.".ljust(5)+"Book Name".center(20)+"ISBN no.".center(19)+"Author".center(15)+"Publisher".center(15)+"Location".center(9))
                listbox.insert(5,"="*95)
                for i in adv_result:
                    listbox.insert(s_no+5,str(s_no).ljust(5)+i[1].center(20)+i[0].center(19)+i[2].center(15)+i[3].center(15)+i[5].center(9))
                    s_no=s_no+1
            else:
                listbox.insert(2,"No books found in the library with given author name even with Advanced Search")
        else:
            listbox.insert(1,"The books written by "+search_query.get()+" are :")
            listbox.insert(2,"="*95)
            listbox.insert(3,"S.No.".ljust(5)+"Book Name".center(20)+"ISBN no.".center(19)+"Author".center(15)+"Publisher".center(15)+"Location".center(9))
            listbox.insert(4,"="*95)
            s_no=1
            for i in result:
                listbox.insert(s_no+4,str(s_no).ljust(5)+i[1].center(20)+i[0].center(19)+i[2].center(15)+i[3].center(15)+i[5].center(9))
                s_no=s_no+1
        listbox.pack(pady=10)
    elif(optionsvar=="Search by Publisher"):
        result = Search.bypublisher(search_query.get().lower())
        if(len(result)==0):
            listbox.insert(1,"Books from given publisher are NOT present in the library")
            adv_result=AdvancedSearch.bypublisher(search_query.get().lower())
            if(len(adv_result)!=0):
                listbox.insert(2,"Books written by similar publisher names are :")
                s_no=1
                listbox.insert(3,"="*95)
                listbox.insert(4,"S.No.".ljust(5)+"Book Name".center(20)+"ISBN no.".center(19)+"Author".center(15)+"Publisher".center(15)+"Location".center(9))
                listbox.insert(5,"="*95)
                for i in adv_result:
                    listbox.insert(s_no+5,str(s_no).ljust(5)+i[1].center(20)+i[0].center(19)+i[2].center(15)+i[3].center(15)+i[5].center(9))
                    s_no=s_no+1
            else:
                listbox.insert(2,"No books found in the library from given publisher even with Advanced Search")
        else:
            listbox.insert(1,"The books from "+search_query.get()+" are :")
            listbox.insert(2,"="*95)
            listbox.insert(3,"S.No.".ljust(5)+"Book Name".center(20)+"ISBN no.".center(19)+"Author".center(15)+"Publisher".center(15)+"Location".center(9))
            listbox.insert(4,"="*95)
            s_no=1
            for i in result:
                listbox.insert(s_no+4,str(s_no).ljust(5)+i[1].center(20)+i[0].center(19)+i[2].center(15)+i[3].center(15)+i[5].center(9))
                s_no=s_no+1
        listbox.pack(pady=10)
    elif(optionsvar=="Search by location"):
        result=Search.bylocation(search_query.get().lower())
        if(len(result)==0):
            listbox.insert(1,"No book is present at given location in the library")
        else:
            listbox.insert(1,"The books at "+search_query.get()+" are :")
            listbox.insert(2,"="*95)
            listbox.insert(3,"S.No.".ljust(5)+"Book Name".center(20)+"ISBN no.".center(19)+"Author".center(15)+"Publisher".center(15)+"Location".center(9))
            listbox.insert(4,"="*95)
            s_no=1
            for i in result:
                listbox.insert(s_no+4,str(s_no).ljust(5)+i[1].center(20)+i[0].center(19)+i[2].center(15)+i[3].center(15)+i[5].center(9))
                s_no=s_no+1
        listbox.pack(pady=10)
    return



def place_widgets(op):
    global search_entry
    global search_query
    global search_label
    search_entry.delete(0,"end")
    if(op=="Search by Book Name"):search_label.configure(text="Enter book name")
    elif(op=="Search by ISBN"):search_label.configure(text="Enter ISBN")
    elif(op=="Search by Author name"):search_label.configure(text="Enter author name")
    elif(op=="Search by Publisher"):search_label.configure(text="Enter publisher")
    elif(op=="Search by location"):search_label.configure(text="Enter location")
    search_entry.focus()
    search_entry.bind('<Return>',lambda a=None:disp_result(optionsvar.get()))
    return





def place_search_widgets():
    global search_w
    global search_label
    global search_entry
    global search_query
    global optionsvar
    global options
    search_w=tkinter.Toplevel(root)
    width=search_w.winfo_screenwidth()
    height=search_w.winfo_screenheight()
    search_w.geometry("{}x{}".format(width,height))
    search_label=tkinter.Label(search_w,text="",font=("open sans",18))

    optionsvar=tkinter.StringVar()
    optionsvar.set("---Select the Search Operation---")
    options=tkinter.OptionMenu(search_w,optionsvar,"Search by Book Name","Search by ISBN","Search by Author name","Search by Publisher","Search by location",command=lambda a:place_widgets(optionsvar.get()))
    options.configure(width=30,height=2,font=("open sans",16))
    search_query=tkinter.StringVar()
    search_entry=tkinter.Entry(search_w,width=35,textvariable=search_query,bd=4,font=("open sans",14),highlightthickness=4,highlightcolor='black')
    options.pack()
    search_label.pack(pady=25)
    search_entry.pack(pady=15)


    search_button =tkinter.Button(search_w,bg="yellow",bd=8,text="Search",font=("open sans",16,"bold"),command=lambda:disp_result(optionsvar.get()))
    search_button.pack(side="bottom",pady=10)
    search_w.mainloop()





def delete_book():
    global deletewindow
    global entry_var1
    global entry_var2
    global error_label
    global warn_label
    global warning_img
    global success_label
    global e_name
    global e_no
    try:
        error_label.destroy()
        warn_label.destroy()
        success_label.destroy()
    except NameError:
        pass
    error_label=tkinter.Label(deletewindow,text="",font=("open sans",16),bg="red")
    warning_img=tkinter.PhotoImage(master=deletewindow,file=r"warningbutton.png")
    warn_label=tkinter.Label(deletewindow,image=warning_img)
    if(entry_var1.get()=="" and entry_var2.get()==""):
        error_label.config(text="Both the entries cannot be empty")
        error_label.pack(side="bottom",pady=2)#error_label.place(x=450,y=700)
        warn_label.pack(side="bottom",pady=20)#warn_label.place(x=600,y=610)
        return
    elif(entry_var1.get()=="" and entry_var2.get()!=""):
        book_id=""
        for i in entry_var2.get():
            if(i=="-"):continue
            if(i.isdigit()):
                book_id=book_id+i
            else:
                error_label.config(text="Wrong input for ISBN")
                error_label.pack(side="bottom",pady=2)#error_label.place(x=515,y=700)
                warn_label.pack(side="bottom",pady=20)#warn_label.place(x=600,y=610)
                e_no.focus()
                return
        result=Search.byno(book_id)
        if(result==False):
            error_label.config(text="No book with such ISBN")
            error_label.pack(side="bottom",pady=2)#error_label.place(x=505,y=700)
            warn_label.pack(side="bottom",pady=20)#warn_label.place(x=600,y=610)
            e_no.focus()
            return
    elif(entry_var1.get()!="" and entry_var2.get()==""):
        result=Search.byname(entry_var1.get().lower())
        if(result!=False):
            book_id=result[0]
        else:
            error_label.config(text="No book with such name")
            error_label.pack(side="bottom",pady=2)#error_label.place(x=505,y=700)
            warn_label.pack(side="bottom",pady=20)#warn_label.place(x=600,y=610)
            e_name.focus()
            return
    elif(entry_var1.get()!="" and entry_var2.get()!=""):
        error_label.config(text="Enter either book name or ISBN. Not both")
        error_label.pack(side="bottom",pady=2)#error_label.place(x=440,y=700)
        warn_label.pack(side="bottom",pady=20)#warn_label.place(x=600,y=610)
        return
    
    confirm_delete=messagebox.askquestion("Delete","Are you sure to delete the book permanently?\nThis action can't be reversed",parent=deletewindow)
    if(confirm_delete=='yes'):
        pass
    else:
        return
    file2=open('books_dup.txt','w')
    file1=open("books.txt",'rb')
    file1.seek(0,2) #taking to end
    end_pos=file1.tell()
    file1.close()
    file1=open('books.txt','r')
    file2.write(file1.readline())
    file2.write(file1.readline())
    while(file1.tell()<end_pos):
        s=file1.readline()
        if(s.rstrip('\n')==book_id):
            for i in range(8):
                file1.readline()
        else:
            for i in range(6):
                file2.write(s)
                s=file1.readline()
            file2.write(s)
            file2.write(file1.readline())
            file2.write(file1.readline())
    file1.close()
    file2.close()

    rename("books.txt","temporary.txt")
    rename("books_dup.txt","books.txt")
    rename("temporary.txt","books_dup.txt")
    success_label=tkinter.Label(deletewindow,text="Book deleted",bg="green2",font=("open sans",16,'bold'))
    success_label.pack(side="bottom",pady=10)#success_label.place(x=570,y=610)
    deletewindow.after(1500,success_label.destroy)
    return



def delete():
    global deletewindow
    global entry_var1
    global entry_var2
    global error_label
    global warn_label
    global warning_img
    global success_label
    global e_name
    global e_no
    global img
    deletewindow=tkinter.Toplevel(root)
    height=deletewindow.winfo_screenheight()
    width=deletewindow.winfo_screenwidth()
    deletewindow.geometry("{}x{}".format(width,height))

    entry_var1=tkinter.StringVar()
    entry_var2=tkinter.StringVar()
    e_name=tkinter.Entry(deletewindow,width=40,textvariable=entry_var1,font=("open sans",14),bd=4,highlightthickness=4,highlightcolor='black')
    e_no=tkinter.Entry(deletewindow,width=40,textvariable=entry_var2,bd=4,font=("open sans",14),highlightthickness=4,highlightcolor='black')
    e_name.bind('<Return>',lambda a=None:delete_book())
    e_no.bind('<Return>',lambda a=None:delete_book())

    img=tkinter.PhotoImage(master=deletewindow,file=r"deletebutton.png")
    delete_button=tkinter.Button(deletewindow,image=img,borderwidth=0,command=delete_book)
    #delete_button.place(x=570,y=850)
    delete_button.pack(side="bottom",pady=20)


    del_by_name=tkinter.Label(deletewindow,text="Name  :",width=10,anchor='e',font=("open sans",14))
    del_by_no=tkinter.Label(deletewindow,text="ISBN  :",width=10,anchor='e',font=("open sans",14))
    del_by_name.place(x=220,y=180)
    del_by_no.place(x=220,y=360)
    or_label=tkinter.Label(deletewindow,width=3,height=1,text="Or",bd=4,font=("open sans",24))


    e_name.place(x=480,y=180)
    e_no.place(x=480,y=360)
    or_label.place(x=650,y=270)
    process_label=tkinter.Label(deletewindow,width=10,height=1,text="Delete Books",font=("open sans",32))
    process_label.place(x=500,y=10)
    return




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
        messagebox.showerror("Error","User ID cannot be empty",parent=loginwindow)
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
                messagebox.showinfo("Id error",'The student has already signed up, please sign in',parent=loginwindow)
                return
            s=file1.readline().decode("utf-8").split('t')
        if(oper=='a'):
            file1.write(bytes(stu_id+'\t',"utf-8"))
            encrypted_pswrd=encrypt(stu_id,pswrd)
            file1.write(bytes(encrypted_pswrd+'\n',"utf-8"))
            pswd=2
            messagebox.showinfo("Info","Signed up Successfully\nSign in to continue",parent=loginwindow)
            loginwindow.after(1200,loginwindow.destroy)
    if(message_text!=""):
        messagebox.showwarning("Warning",message_text,parent=loginwindow)
        f2.config(highlightcolor="red",highlightthickness=6)
        f3.config(highlightcolor="red",highlightthickness=6)
    else:
        f2.config(highlightcolor="green",highlightthickness=6)
        f3.config(highlightcolor="green",highlightthickness=6)
    return




def signin():
    file1=open('student_ids.txt','ab+')
    global username
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
                messagebox.showinfo("Login","Login Successful",parent=loginwindow)
                stu()
                login='success'
                f2.config(highlightcolor="green",highlightthickness=6)
                #loginwindow.after(1200,loginwindow.destroy)
            else:
                messagebox.showerror("Login Error",'Password is incorrect\nPlease try again',parent=loginwindow)
                f2.focus()
                f2.config(highlightcolor="red",highlightthickness=6)
    
    if id_status==False:
        messagebox.showerror("Login Error",'Invalid username\nSignup if you are new\nPlease try again',parent=loginwindow)
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
    loginwindow=tkinter.Toplevel(root)
    width=loginwindow.winfo_screenwidth()
    height=loginwindow.winfo_screenheight()
    loginwindow.geometry("{}x{}".format(width,height))
    t=tkinter.Canvas(loginwindow)
    t.pack(fill="both",expand=True)
    login_bg=tkinter.PhotoImage(file="login.png")
    t.create_image(0,0,image=login_bg,anchor="nw")
    user_img=tkinter.PhotoImage(file="user.png")
    t.create_image(700,140,image=user_img)
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
        t.create_text(650,30,text="Sign up",anchor="w",fill="white",font=("open sans",28,"bold"))
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
    if(oper=='b'):
        b1.config(text="Login",command=signin)
        t.create_text(650,30,text="Login",anchor="w",fill="white",font=("open sans",28,"bold"))
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
    if(oper=='c'):
        b1.config(text="Login",command=admin_signin)
        t.create_text(650,30,text="Login",anchor="w",fill="white",font=("open sans",28,"bold"))
        t.create_text(550,285,text="USERNAME  :",anchor="e",fill="white",font=("open sans",16,"bold"))
        t.create_text(550,380,text="PASSWORD  :",anchor="e",fill="white",font=("open sans",16,"bold"))
        e_id.pack(side="left",fill="y")
        e_password.pack(side="left",fill="y")
        e_confirm.pack(side="left",fill="y")
        f1.place(x=600,y=260)
        f2.place(x=600,y=350)
        b1.place(x=580,y=500)
        e_id.bind('<Return>',lambda a=None:e_password.focus())
        e_password.bind('<Return>',lambda a=None:admin_signin())
    return



def replace():
    global handleerror
    global return_check
    global p
    for i in stu_frame1.winfo_children():
        i.place_forget()
    from os import listdir
    if(str(username)+".txt" in listdir("Student_logs")):
        pass
    else:
        no_book=tkinter.Label(stu_frame1,font=("open sans",20),text="You have currently Not borrowed any book")
        no_book.place(x=100,y=100)
        return
    p=tkinter.IntVar(value=0)
    return_check=[None,None,None]
    return_check[0]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=1,font=("open sans",16))
    return_check[1]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=2,font=("open sans",16))
    return_check[2]=tkinter.Radiobutton(stu_frame1,variable=p,text="",value=3,font=("open sans",16))
    return_button=tkinter.Button(stu_frame1,text="Return",bd=6,font=("open sans",14,"bold"),bg="red",command=lambda:student_operations(3))
    return_button.place(x=500,y=500)

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
            messagebox.showerror("Empty","Date cannot be empty",parent=stuwindow)
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
                    messagebox.showerror("Entry Error","Both the fields cannot be empty",parent=stuwindow)
                    return
                elif(entry_var1.get()!="" and entry_var2.get()!=""):
                    messagebox.showwarning("Entry Warning","Enter only name or ISBN, not both",parent=stuwindow)
                    return
                if(result!=False):
                    stlogs.write(result[0]+'\t'+str(borrow_date)+'\t'+str(return_date)+'\n')
                    messagebox.showinfo("Return date","You must return the book by "+str(return_date.strftime("%d-%m-%Y")),parent=stuwindow)
                    e_name.delete(0,"end")
                    e_no.delete(0,"end")
                    e_date.delete(0,"end")
                else:
                    messagebox.showerror("Wrong book","No book in library with given name or number",parent=stuwindow)
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
                messagebox.showwarning("Warning","You cannot borrow more than 3 books",parent=stuwindow)
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
                messagebox.showwarning("Late Submission","You have returned the book late by "+str((todAy-actual_return_date).days)+" days\nYou need to pay a fine of Rs."+str(fine),parent=stuwindow)
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
        confirm_logout=messagebox.askquestion("Log out","Are you sure to log out?",parent=stuwindow)
        if(confirm_logout=="yes"):
            stuwindow.destroy()




def stu():
    global oper
    
    global stuwindow
    global handleerror
    global return_check
    global stu_frame1
    global username
    if(oper=='a'):
        return
    elif(oper=='b'):
        username=stu_id_var.get()#
    username=stu_id_var.get()
    from datetime import date, timedelta
    stuwindow=tkinter.Toplevel(loginwindow)
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
    #c1b5.place(x=15,y=460)
    c1b6.place(x=15,y=460)
    c1b7.place(x=15,y=530)
    c1.create_line(5,235,200,235,width=2)
    c1.create_line(5,305,200,305,width=2)
    c1.create_line(5,375,200,375,width=2)
    c1.create_line(5,445,200,445,width=2)
    c1.create_line(5,515,200,515,width=2)

    stuwindow.mainloop()



root=tkinter.Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("{}x{}".format(width,height))
c=tkinter.Canvas(root)
c.pack(fill="both",expand=True)
main_bg=tkinter.PhotoImage(file="librarybackground.png")
c.create_image(0,0,image=main_bg,anchor="nw")
c.create_rectangle(240,2,1200,70,fill="white")
c.create_text(250,5,fill="black",text="WELCOME TO CBIT LIBRARY",anchor='nw',font=("calibre",50,"bold"))
c2=tkinter.Canvas(c,bg="sky blue",width=250,height=350)
c2.place(x=570,y=250)

##-----------------------------------------------------------------------------------------------------------------------------------


def admin_signin():
    global stu_id_var
    global pass_var
    login='unsuccess'
    flag='flse'
    id_status=False
    username=stu_id_var.get()
    if username.lower()=="Library Admin".lower():
        id_status=True
        paswrd=pass_var.get()
        if paswrd=='Admin@123':
            messagebox.showinfo("Login","Login Successful",parent=loginwindow)
            login='success'
            f2.config(highlightcolor="green",highlightthickness=6)
            adm()
            #loginwindow.after(1000,loginwindow.destroy)
        else:
            messagebox.showerror("Login Error",'Password is incorrect\nPlease try again',parent=loginwindow)
            f2.focus()
            f2.config(highlightcolor="red",highlightthickness=6)
    
    if id_status==False:
        messagebox.showerror("Login Error",'Invalid username\nPlease try again',parent=loginwindow)
        f1.focus()
        f1.config(highlightcolor="red",highlightthickness=6)
    else:
        f1.config(highlightcolor="green",highlightthickness=6)
    return




def admin_widgets(k):
    if(k==1):
        addbook()
    elif(k==2):
        delete()
    elif(k==3):
        place_search_widgets()
    elif(k==4):
        for i in stu_frame1.winfo_children():
            i.place_forget()
        f=open("requested_books.txt","a+")
        f.seek(0,2)
        end=f.tell()
        f.seek(0)
        reqbox1=tkinter.Listbox(stu_frame1,height=3,width=70,font=("courier new",16))
        reqbox2=tkinter.Listbox(stu_frame1,height=3,width=70,font=("courier new",16))
        reqbox1.insert(1,"="*70)
        reqbox1.insert(2,"S.No".ljust(6)+"Requested Book Name".center(30))
        reqbox1.insert(3,"="*70)
        sno=0
        while(f.tell()<end):
            sno=sno+1
            s=f.readline().strip('\n').split('\t')
            reqbox2.insert(sno,str(sno).ljust(6)+s[0].center(30))
        reqbox1.place(x=15,y=10)
        reqbox2.place(x=15,y=80)
        stu_frame1.place(x=201,y=100)
    elif(k==5):
        for i in stu_frame1.winfo_children():
            i.place_forget()
        borr=open("borrowers.txt","r")
        latebox=tkinter.Listbox(stu_frame1,width=75,height=20,font=("courier new",12))
        latebox.insert(1,'='*75)
        latebox.insert(2,"S.No".ljust(5)+'USER'.center(20)+"ISBN of BOOK ISSUED".center(20)+"ISSUE DATE".center(14)+'RETURN DATE'.center(14))
        latebox.insert(3,'='*75)
        sno=4
        while(True):
            user=borr.readline().rstrip('\n')
            if(user==""):break
            with open("Student_logs\\"+user+".txt","r") as u:
                s=u.readlines()
                for i in s:
                    actual_issue=i.rstrip('\n').split('\t')[1].split('-')
                    issue_date=actual_issue[2]+'-'+actual_issue[1]+'-'+actual_issue[0]
                    actual_return=i.rstrip('\n').split('\t')[2].split('-')
                    actual_return_date=actual_return[2]+'-'+actual_return[1]+'-'+actual_return[0]
                    borrod_isbn=i.split('\t')[0]
                    latebox.insert(sno,str(sno-3).ljust(5)+user.center(20)+borrod_isbn.center(20)+issue_date.center(14)+actual_return_date.center(14))
                    sno=sno+1
        latebox.place(x=10,y=10)
        stu_frame1.place(x=201,y=100)
    elif(k==6):
        for i in stu_frame1.winfo_children():
            i.place_forget()
        borr=open("borrowers.txt","r")
        from datetime import date
        #t=list(map(int,input("Enter today's date as DD-MM-YYYY : ").split("-")))#or date.today()
        todAy=date.today()#date(t[2],t[1],t[0])
        latebox=tkinter.Listbox(stu_frame1,width=70,height=20,font=("courier new",12))
        latebox.insert(1,'*'*70)
        latebox.insert(2,"S.No".ljust(5)+'USER'.center(20)+"ACTUAL RETURN DATE".center(25)+'Late by days'.center(15))
        latebox.insert(3,'*'*70)
        sno=4
        while(True):
            user=borr.readline().rstrip('\n')
            if(user==""):break
            with open("Student_logs\\"+user+".txt","r") as u:
                s=u.readlines()
                for i in s:
                    actual_return=list(map(int,(i.rstrip('\n').split('\t')[2]).split('-')))
                    actual_return_date=date(actual_return[0],actual_return[1],actual_return[2])
                    if((todAy-actual_return_date).days>0):
                        late_days=(todAy-actual_return_date).days
                        latebox.insert(sno,str(sno-3).ljust(5)+user.center(20)+str(actual_return_date).center(25)+str(late_days).center(15))
                        sno=sno+1
        latebox.place(x=10,y=10)
        stu_frame1.place(x=201,y=100)
            
    elif(k==7):
        confirm_logout=messagebox.askquestion("Log out","Are you sure to log out?",parent=stuwindow)
        if(confirm_logout=="yes"):
            stuwindow.destroy()




def adm():
    global stuwindow
    global handleerror
    global return_check
    global stu_frame1
    from datetime import date, timedelta
    stuwindow=tkinter.Toplevel(loginwindow)
    height=stuwindow.winfo_screenheight()
    width=stuwindow.winfo_screenwidth()
    stuwindow.geometry("{}x{}".format(width,height))
    stu_frame1=tkinter.Frame(stuwindow,width=width-200,height=height-50,bd=10)

    c1=tkinter.Canvas(stuwindow,bg="pink",width=200)
    c2=tkinter.Canvas(stuwindow,bg="pink",height=250)
    c1.pack(side="left",fill="y")
    c2.pack(side="top",fill="x")
    process_label=tkinter.Label(c2,width=10,height=2,text="ADMIN",font=("open sans",25),bg="pink")
    process_label.pack(fill="both")


    c1b1=tkinter.Button(c1,text="Add book",bg="pink",bd=0,width=16,anchor='w',font=("open sans",14),command=lambda:admin_widgets(1))
    c1b2=tkinter.Button(c1,text="Delete book",bg="pink",bd=0,width=16,anchor='w',font=("open sans",14),command=lambda:admin_widgets(2))
    c1b3=tkinter.Button(c1,text="Search",bg="pink",bd=0,width=16,anchor='w',font=("open sans",14),command=lambda:admin_widgets(3))
    c1b4=tkinter.Button(c1,text="Requested books",bg="pink",bd=0,width=16,anchor='w',font=("open sans",14),command=lambda:admin_widgets(4))
    c1b5=tkinter.Button(c1,text="Borrowed Books",bg="pink",bd=0,width=16,anchor='w',font=("open sans",14),command=lambda:admin_widgets(5))
    c1b6=tkinter.Button(c1,text="Overdues",bg="pink",bd=0,width=16,anchor='w',font=("open sans",14),command=lambda:admin_widgets(6))
    c1b7=tkinter.Button(c1,text="Log Out",bg="pink",bd=0,width=16,anchor='w',font=("open sans",14),command=lambda:admin_widgets(7))
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





def place_admin_widgets(m):
    global oper
    global cont
    global s1
    global s2
    try:
        s1.place_forget()
        s2.place_forget()
        cont.destroy()
    except:
        pass
    if(m==1):
        oper='c'
        studentwidgets()
    elif(m==2):
        def setsign(o):
            global oper
            if(o==1):
                oper='a'
                studentwidgets()
            else:
                oper='b'
                studentwidgets()
        s1=tkinter.Button(root,text="Sign up",bg="green2",bd=0,width=10,font=("open sans",14),command=lambda:setsign(1))
        s2=tkinter.Button(root,text="Sign in",bg="green2",bd=0,width=10,font=("open sans",14),command=lambda:setsign(2))
        s1.place(x=900,y=300)
        s2.place(x=900,y=350)
    elif(m==3):
        place_search_widgets()
    elif(m==4):
        cont=tkinter.Listbox(root,font=("open sans",14),width=50)
        cont.insert(1,"Phone no. : 12345678990")
        cont.insert(1,"Email : cbitlibrary@gmail.com")
        cont.insert(3,"Address: Cbit, Hyderabad")
        cont.place(x=900,y=300)
    elif(m==5):
        root.destroy()







cb1=tkinter.Button(c2,text="Admin",bg="sky blue",bd=0,width=16,font=("open sans",14),command=lambda:place_admin_widgets(1))
cb2=tkinter.Button(c2,text="User",bg="sky blue",bd=0,width=16,font=("open sans",14),command=lambda:place_admin_widgets(2))
cb3=tkinter.Button(c2,text="Search",bg="sky blue",bd=0,width=16,font=("open sans",14),command=lambda:place_admin_widgets(3))
cb4=tkinter.Button(c2,text="Contact",bg="sky blue",bd=0,width=16,font=("open sans",14),command=lambda:place_admin_widgets(4))
cb5=tkinter.Button(c2,text="Exit",bg="sky blue",bd=0,width=16,font=("open sans",14),command=lambda:place_admin_widgets(5))
cb1.place(x=25,y=20)
cb2.place(x=25,y=90)
cb3.place(x=25,y=160)
cb4.place(x=25,y=230)
cb5.place(x=25,y=290)
c2.create_line(5,75,300,75,width=2)
c2.create_line(5,145,300,145,width=2)
c2.create_line(5,215,300,215,width=2)
c2.create_line(5,275,300,275,width=2)

root.mainloop()
