from tkinter import *
from cryptography.fernet import Fernet
from tkinter import messagebox
import os
import os.path
from Pmw import ScrolledText

key = b'2fw657Yh1ENl1XlUboHSuYkijMLCH_2DBz7UzDif1p4='
fer = Fernet(key)

mp_file_path = 'C:/Users/Public/Documents'
completename_mp = os.path.join(mp_file_path, 'mp.txt')
with open(completename_mp, 'a') as f1:
    f1.writelines('')



passwords_path = 'C:/Users/Public/Documents'
completename_passwords = os.path.join(passwords_path, 'passwords.txt')
with open(completename_passwords, 'a') as f2:
    f2.writelines('')



def Main_Window():
    mainWindow = Tk()
    mainWindow.title('Password Manager')
    mainWindow.config(bg='#63666A')
    mainWindow.geometry('400x200')
    website_label = Label(mainWindow, text='Enter Website:', font='Helvetica 10')
    website_label.place(x=147, y=30)
    entry_website = Entry(mainWindow, bg='white', bd=5)
    entry_website.place(x=130, y=50)

    def add_password():
        add_password_window = Tk()
        add_password_window.title('Add password')
        add_password_window.geometry('300x100')
        add_password_window.config(bg='#63666A')
        password_entry = Entry(add_password_window, bg='white', bd=5)
        password_entry.place(x=60, y=25)

        def show_hide_pass():
            if password_entry.cget('show') == '':
                password_entry.config(show='*')
            else:
                password_entry.config(show='')

        show_password_button = Button(add_password_window, text='show/hide', bg='white', command=show_hide_pass)
        show_password_button.place(x=200, y=24)

        def confirm_password():
            encrypted_website = fer.encrypt(entry_website.get().encode())
            encrypted_password = fer.encrypt(password_entry.get().encode())
            with open(completename_passwords, 'a') as f:
                data = entry_website.get() + ' | ' + password_entry.get()
                encrypted = fer.encrypt(data.encode())
                passwords = [encrypted.decode()]
                # print(passwords)
                for i in range(0, len(passwords)):
                    f.write(passwords[i] + '\n')
                entry_website.delete(0, 'end')
                password_entry.delete(0, 'end')
                add_password_window.destroy()

        confirm_pass_button = Button(add_password_window, text='Confirm', bg='white', command=confirm_password)
        confirm_pass_button.place(x=120, y=65)
        add_password_window.mainloop()
        entry_website.delete(0, 'end')

    button_add = Button(mainWindow, text='    Add Password    ', bg='white', command=add_password)
    button_add.place(x=70, y=100)

    def remove_password():
        with open(completename_passwords, 'r+') as file:
            store = []
            for line in file:
                decrypted = fer.decrypt(line.encode().rstrip(b'\n')).decode()
                store.append(decrypted)
                print(decrypted)

            print(store)

            f = open(completename_passwords, 'r+')
            f.truncate(0)
            f.close()

            with open(completename_passwords, 'a') as file:
                count = 0
                for i in range(len(store)):
                    element = store[i]
                    count += 1
                    print(element)
                    website = element.split(' | ')[0]
                    print(website)
                    if website.lower() != entry_website.get().lower():
                        encrypted_line = fer.encrypt(element.encode())
                        file.writelines(encrypted_line.decode() + '\n')
                    else:
                        pass

        entry_website.delete(0, 'end')

    button_remove = Button(mainWindow, text='Remove password', bg='white', command=remove_password)
    button_remove.place(x=210, y=100)

    def view_passwords():
        filename = completename_passwords
        windwo_view = Tk()
        windwo_view.geometry('400x200')
        windwo_view.config(bg='#63666A')
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
                file.write(element + '\n')

        Button(top, text='Quit', command=windwo_view.destroy).pack(pady=15)
        windwo_view.mainloop()

    view_passwords_button = Button(mainWindow, text='View passwords', bg='white', command=view_passwords)
    view_passwords_button.place(x=145, y=140)
    mainWindow.mainloop()


def Authentication_Window():
    AuthWindow = Tk()
    AuthWindow.title('Authentication')
    AuthWindow.config(bg='#63666A')
    AuthWindow.geometry('300x350')
    label_name = Label(AuthWindow, text='Enter Username:', bg='#63666A', font='Helvetica 13')
    label_name.place(x=90, y=70)
    entry_name = Entry(AuthWindow, bg='white', bd=5, width=30)
    entry_name.place(x=60, y=100)
    label_password = Label(AuthWindow, text='Enter Password:', bg='#63666A', font='Helvetica 13')
    label_password.place(x=92, y=150)
    entry_password = Entry(AuthWindow, show='*', bg='white', bd=5, width=30)
    entry_password.place(x=60, y=180)

    def login():
        if os.stat(completename_mp).st_size == 0:
            msg = msg = messagebox.showwarning(title='Error', message="No registered user")
        else:
            f = open(completename_mp, 'r')
            data = f.read().split(', ')
            auth = False
            username = data[0]
            print(username)
            password = data[1]
            print(password)
            decrypted_username = fer.decrypt(username.encode())
            decrypted_password = fer.decrypt(password.encode())
            print(decrypted_username.decode())
            print(decrypted_password.decode())
            if entry_name.get() == fer.decrypt(username.encode()).decode() and entry_password.get() == fer.decrypt(
                    password.encode()).decode():
                auth = True
            if auth:
                AuthWindow.destroy()
                Main_Window()
            else:
                msg = messagebox.showwarning(title='Error', message="Wrong username or password")

        entry_password.delete(0, 'end')
        entry_name.delete(0, 'end')

    button_login = Button(AuthWindow, text='Login', height=1, width=10, command=login)
    button_login.place(x=60, y=250)

    def register(username, password):
        if os.stat(completename_mp).st_size == 0:
            f = open(completename_mp, 'a')
            encrypted_username = fer.encrypt(username.encode())
            encrypted_password = fer.encrypt(password.encode())
            f.writelines(f"{encrypted_username.decode()}, {encrypted_password.decode()}")
            f.close()
            msg = messagebox.showinfo(title='Registration', message=f"You've been registered as {username}")
        else:
            msg = messagebox.showwarning(title='Error', message="Can't register more users")

        entry_password.delete(0, 'end')
        entry_name.delete(0, 'end')

    button_register = Button(AuthWindow, text='Register', height=1, width=12,
                             command=lambda: register(entry_name.get(), entry_password.get()))
    button_register.place(x=160, y=250)
    AuthWindow.mainloop()


Authentication_Window()
