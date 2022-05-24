from tkinter import *
from tkinter import messagebox
from Pmw.Pmw_2_0_1.lib.PmwScrolledText import ScrolledText


def create_add():
    windwo_add = Tk()
    windwo_add.geometry('400x200')
    l1_add = Label(windwo_add, text='Website')
    l1_add.pack()
    en1_add = Entry(windwo_add, bg='white', bd=5)
    en1_add.pack(side=TOP)

    def confirm():
        f = open('my_passwords.txt', 'a')
        f.writelines(en1_add.get() + '|' + en2_add.get() + '\n')
        f.close()
        en1_add.delete(0, 'end')
        en2_add.delete(0, 'end')

    l2_add = Label(windwo_add, text='Password')
    l2_add.pack()
    en2_add = Entry(windwo_add, bg='white', bd=5)
    en2_add.pack(side=TOP)
    btn1_add = Button(windwo_add, text='CONFIRM', bg='white', command=confirm)
    btn1_add.pack()
    windwo_add.mainloop()


def create_view():
    filename = 'my_passwords.txt'
    windwo_view = Tk()
    windwo_view.geometry('400x200')
    top = Frame(windwo_view)
    top.pack(side='top')
    text = ScrolledText(top, borderframe=5,
                        vscrollmode='dynamic',
                        hscrollmode='dynamic',
                        labelpos='n',
                        label_text='Your passwords:',  # 'file %s' % filename
                        text_width=40,
                        text_height=4,
                        text_wrap='none', )
    text.pack()
    text.insert('end', open(filename, 'r').read())
    Button(top, text='Quit', command=windwo_view.destroy).pack(pady=15)
    windwo_view.mainloop()


def delete():
    res = messagebox.askquestion('are you sure?', 'Are you sure?')
    if res == 'yes':
        f = open('my_passwords.txt', 'r+')
        f.truncate(0)
        f.close()
    elif res == 'no':
        pass


def exit_app():
    exit()


root = Tk()
root.title('Password Manager')
root.geometry("500x150")
l1 = Label(root, text='Password manager', fg='black', bg='white', font='Helvetica 13')
l1.grid(row=0)
l2 = Label(root, text='Choose if you want to view your passwords, create new, delete them or exit the app.',
           font='Helvetica 10')
l2.grid(row=1)
btn1 = Button(root, text=' ADD  ', bg='green', command=create_add)
btn1.place(x=80, y=70)
btn2 = Button(root, text=' VIEW ', bg='white', command=create_view)
btn2.place(x=175, y=70)
btn3 = Button(root, text='DELETE', bg='white', command=delete)
btn3.place(x=265, y=70)
btn4 = Button(root, text=' EXIT ', bg='red', command=exit_app)
btn4.place(x=370, y=70)
root.mainloop()
