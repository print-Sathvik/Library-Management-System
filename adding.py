from os import path
from tkinter import messagebox
def addbooks(name,no,author,publisher,year,location,copies):
    global e
    global w
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
            warn_label=tkinter.Label(w,text='This field cannot be empty',bg="red",font=("open sans",12))
            warning=tkinter.PhotoImage(master=w,file="warningbutton.png")
            warn_image=tkinter.Label(w,image=warning)
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
            messagebox.showerror("Entry Error","Wrong input for ISBN")
            e[1].focus()
            return
    no=book_id
    if(len(year)==4 and year.isdigit()):
        pass
    else:
        messagebox.showerror("Entry Error","Wrong input for year")
        return
    if(copies.isdigit()):
        pass
    else:
        messagebox.showerror("Entry Error","Wrong input for number of copies")
        return
    for i in range(7):
        e[i].delete(0,"end")
    e[0].focus()
    if(path.isfile("books.txt")==False):
        f=open("books.txt","a+")
        f.writelines(["\n\n",str(no)+'\n',name+'\n',author+'\n',publisher+'\n',str(year)+'\n',location+'\n'+str(copies)+'\n'])
        f.close()
        added_label=tkinter.Label(w,text="Book is added to the library",width=35,bg="green2",font=("open sans",16))
        added_label.place(x=450*width/1280,y=900*height/1280)
        w.after(1500,added_label.destroy)
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
        added_label=tkinter.Label(w,text="Book is added to the library",width=35,bg="green2",font=("open sans",16))
        added_label.place(x=450*width/1280,y=900*height/1280)
        w.after(1500,added_label.destroy)
    return



import tkinter
def addbook():
    global w
    global e
    global width
    global height
    global warning
    global entrys
    w=tkinter.Tk()
    height=w.winfo_screenheight()
    width=w.winfo_screenwidth()
    w.geometry("{}x{}".format(width,height))
    entrys=list()
    e=list()
    labels=list()
    for i in range(7):
        entrys.append(tkinter.StringVar())
    for i in range(7):
        e.append(tkinter.Entry(w,width=35,textvariable=entrys[i],bd=4,font=("open sans",14),highlightthickness=4,highlightcolor='black'))
        labels.append(tkinter.Label(w,width=15,anchor='e',font=("open sans",14)))

    e[0].focus()
    img=tkinter.PhotoImage(master=w,file=r"click.png")
    b=tkinter.Button(w,image=img,borderwidth=0,
                     command=lambda:addbooks(entrys[0].get(),entrys[1].get(),entrys[2].get(),entrys[3].get(),entrys[4].get(),entrys[5].get(),entrys[6].get()))
    b.pack(side="bottom")

    process_label=tkinter.Label(w,width=10,height=1,text="Add Books",font=("open sans",32))
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
    w.mainloop()

if __name__=='__main__':
    addbook()






































