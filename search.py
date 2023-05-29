import tkinter
bor=open("borrowers.txt",'w')
bor.close()
result=False
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
    listbox=tkinter.Listbox(search_w,width=105,height=25,font=("courier new",12))
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
        print(search_query.get())
        result = Search.byno(search_query.get().lower())
        print(result)
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
                listbox.insert(3,"The book will be available by "+latestdate)
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
    search_w=tkinter.Tk()
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



if __name__=='__main__':
    place_search_widgets()




















