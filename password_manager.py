import os

while True:
    command = input('Do you want to add a password or view your passwords (view, add), type q to quit or del to delete '
                    'all of you passwords: ')


    def delete():
        f = open('my_passwords.txt', 'r+')
        f.truncate(0)
        f.close()


    def add():
        f = open('my_passwords.txt', 'a')
        website = input('Enter website:')
        password = input('Enter password:')
        f.writelines(website + '|' + password + '\n')
        f.close()


    def view():
        f = open('my_passwords.txt', 'r')
        for line in f.readlines():
            data = line.rstrip()
            website, password = data.split('|')
            print("Website:", website, "| Password:", password)
            print('---------------------------------')
        f.close()


    if command == 'q':
        print('Thx for using password manager :)')
        quit()
    if command == 'del':
        sure = input('Are you sure you want to delete everything: y/n')
        if sure == 'n':
            print("Files won't be deleted!")
            continue
        elif sure == 'y':
            print('Everything is being deleted....')
            delete()
            print('Everything is deleted!')
            print('---------------------------------')
            cont = input('Do you want to continue or exit the app: (q, continue)')
            if cont == 'q':
                print('Thx for using password manager :)')
                quit()
            elif cont == 'continue':
                continue

    if command == 'view':
        view()
    elif command == 'add':
        add()
