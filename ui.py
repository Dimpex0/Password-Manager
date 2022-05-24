from tkinter import *
import Pmw, sys
import top as top


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
    text = Pmw.ScrolledText(top, borderframe=5,
                            vscrollmode='dynamic',
                            hscrollmode='dynamic',
                            labelpos='n',
                            label_text='file %s' % filename,
                            text_width=40,
                            text_height=4,
                            text_wrap='none', )
    text.pack()
    text.insert('end', open(filename, 'r').read())
    Button(top, text='Quit', command=windwo_view.destroy).pack(pady=15)
    windwo_view.mainloop()


def delete():
    f = open('my_passwords.txt', 'r+')
    f.truncate(0)
    f.close()


def exit_app():
    exit()


root = Tk()
root.title('Password Manager')
root.geometry("500x150")
l1 = Label(text='Password manager', fg='black', bg='white', font='Helvetica 13')
l1.pack()
l2 = Label(text='Choose if you want to view your passwords, create new, delete them or exit the app.', font='Helvetica 10')
l2.pack()
btn1 = Button(text='ADD', bg='white', command=create_add)
btn1.pack()
btn2 = Button(text='VIEW', bg='white', command=create_view)
btn2.pack()
btn3 = Button(text='DELETE', bg='white', command=delete)
btn3.pack()
btn4 = Button(text='EXIT', bg='white', command=exit_app)
btn4.pack()
root.mainloop()
