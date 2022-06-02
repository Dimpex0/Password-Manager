from tkinter import *
from tkinter import messagebox
from Pmw import ScrolledText
from cryptography.fernet import Fernet


def main_app():
    def create_add():
        windwo_add = Tk()
        windwo_add.geometry('400x200')
        l1_add = Label(windwo_add, text='Website:')
        l1_add.pack()
        en1_add = Entry(windwo_add, bg='white', bd=5)
        en1_add.pack(side=TOP)

        def confirm():
            key = b'2fw657Yh1ENl1XlUboHSuYkijMLCH_2DBz7UzDif1p4='
            fer = Fernet(key)
            f = open('my_passwords.txt', 'a')
            data = en1_add.get() + '|' + en2_add.get()
            encrypted = fer.encrypt(data.encode())
            passwords = []
            passwords.append(encrypted.decode())
            # print(passwords)
            for i in range(0, len(passwords)):
                f.write(passwords[i] + '\n')
            f.close()
            en1_add.delete(0, 'end')
            en2_add.delete(0, 'end')

        def toggle_password():
            if en2_add.cget('show') == '':
                en2_add.config(show='*')
                btn2_add.config(text='Show Password')
            else:
                en2_add.config(show='')
                btn2_add.config(text='Hide Password')

        l2_add = Label(windwo_add, text='Password:')
        l2_add.pack()
        en2_add = Entry(windwo_add, show='*', bg='white', bd=5)
        en2_add.pack(side=TOP)
        btn2_add = Button(windwo_add, text='Show Password', command=toggle_password)
        btn2_add.pack()
        btn1_add = Button(windwo_add, text='CONFIRM', bg='white', command=confirm)
        btn1_add.pack(pady=5)
        windwo_add.mainloop()

    def create_view():
        key = b'2fw657Yh1ENl1XlUboHSuYkijMLCH_2DBz7UzDif1p4='
        fer = Fernet(key)
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

        with open(filename, 'r') as file:
            store = []
            for line in file:
                decrypted = fer.decrypt(line.encode().rstrip(b'\n'))
                store.append(decrypted.decode())
        with open(filename, 'w') as file:
            count = 0
            for i in range(len(store)):
                element = store[i]
                count += 1
                print(element)
                file.write(element + '\n')

        text.insert('end', open(filename, 'r').read())

        with open(filename, 'r') as file:
            store_2 = []
            for line in file:
                encrypted = fer.encrypt(line.encode().rstrip(b'\n'))
                store_2.append(encrypted.decode())
        with open(filename, 'w') as file:
            count = 0
            for i in range(len(store)):
                element = store_2[i]
                count += 1
                print(element)
                print(fer.decrypt(element.encode()))
                file.write(element + '\n')

        Button(top, text='Quit', command=windwo_view.destroy).pack(pady=15)
        windwo_view.mainloop()

    def delete():
        res = messagebox.askquestion('Are you sure?', 'Are you sure?')
        if res == 'yes':
            f = open('my_passwords.txt', 'r+')
            f.truncate(0)
            f.close()
        elif res == 'no':
            pass

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
    btn4 = Button(root, text=' EXIT ', bg='red', command=root.destroy)
    btn4.place(x=370, y=70)
    root.mainloop()


def key_write():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


def authentication():
    auth = Tk()
    auth.title('Authentication')
    auth.geometry("300x200")
    l1 = Label(auth, text='Welcome!', bg='white', fg='black', font='Helvetica 13')
    l1.place(x=110, y=0)
    l2 = Label(auth, text='Password:', bg='white')
    l2.place(x=115, y=50)
    en1 = Entry(auth, show='*', bg='white')
    en1.place(x=85, y=80)

    def register():
        key = b'2fw657Yh1ENl1XlUboHSuYkijMLCH_2DBz7UzDif1p4='
        fer = Fernet(key)
        f = open('master_password.txt', 'wb')
        en1_encode = en1.get().encode()
        en1_encrypt = fer.encrypt(en1_encode)
        f.write(en1_encrypt)
        f.close()
        msg = messagebox.showinfo(title='Success', message='Success!')
        en1.delete(0, 'end')

    def login():
        key = b'2fw657Yh1ENl1XlUboHSuYkijMLCH_2DBz7UzDif1p4='
        fer = Fernet(key)
        f = open('master_password.txt', 'rb')
        line = ''
        for line in f:
            decoded = fer.decrypt(line)
            line = decoded.decode()

        if line == en1.get():
            auth.destroy()
            main_app()
        else:
            msg = messagebox.showerror(title='Error', message='Incorrect details!')
            en1.delete(0, 'end')
        f.close()

    btn1 = Button(auth, text='Login', bg='white', command=login)
    btn1.place(x=85, y=120)
    btn2 = Button(auth, text='Register', bg='white', command=register)
    btn2.place(x=155, y=120)
    auth.mainloop()


authentication()
