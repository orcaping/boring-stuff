"""Password Locker - Projectgit  Chapter 6"""
import pyperclip

logins = {'Youtube': 'liaubflsufbl4vlu4pufhlsiufe', 'Google': 'mn,bxhvbleuwprupqiuerqegzoefqu9382'}

while True:
    name = input("Enter an account (blank to quit!): ")
    if name == '':
        break
    if name == '/help':
        for key in logins:
            print(key)

    if name in logins:
        print('Password for account: ' + name + ' has been copied to clipboard')
        pyperclip.copy(logins[name])

    if (name != '' and name != '/help' and name not in logins):
        print("No records available in database for login: " + name + " ")
        login = input("Enter the password for " + name + ": ")
        logins[name] = login
        print("Database updated succesfully")
        print(logins)
        choice = input ('do you want to copy the new password to your clipboard (yes/no)?')
        if choice == "yes":
            pyperclip.copy(logins[name])
        if choice == "no":
            break
