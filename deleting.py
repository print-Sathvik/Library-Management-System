import tkinter
from tkinter import messagebox
from os import rename
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
    
    confirm_delete=messagebox.askquestion("Delete","Are you sure to delete the book permanently?\nThis action can't be reversed")
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
    deletewindow=tkinter.Tk()
    height=deletewindow.winfo_screenheight()
    width=deletewindow.winfo_screenwidth()
    deletewindow.geometry("{}x{}".format(width,height))

    entry_var1=tkinter.StringVar()
    entry_var2=tkinter.StringVar()
    e_name=tkinter.Entry(deletewindow,width=40,textvariable=entry_var1,font=("open sans",14),bd=4,highlightthickness=4,highlightcolor='black')
    e_no=tkinter.Entry(deletewindow,width=40,textvariable=entry_var2,bd=4,font=("open sans",14),highlightthickness=4,highlightcolor='black')
    e_name.bind('<Return>',lambda a=None:delete_book())
    e_no.bind('<Return>',lambda a=None:delete_book())

    img=tkinter.PhotoImage(master=deletewindow,file=r"click.png")
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


if __name__=='__main__':
    delete()











