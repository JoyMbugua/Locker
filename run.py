#!/usr/bin/env python3
from creds import Credentials
from user import User
import string
import random
import pyperclip


def main ():
    new_login_name = input("Create your password manager username:\n")
    new_login_password = input("Create a password for your locker:\n")
    new_user = User(new_login_name, new_login_password)
    new_user.save_manager()
    print(f"Welcome {new_login_name}")
    print("- " * 50)
    print("\n")

    login_name = input("Enter you login name:\n")
    password = input("Enter your password:\n")

    def login():
        return login_name in User.users and User.users[login_name] == password
            
        

    while True:    
        
        if login():
            choice = input("Enter 'create' to create new credentials, 'display' to view your saved credentials, 'delete' to delete credentials, or 'copy' to copy an account's password and 'none' to exit:\n")
            if choice == 'none':
                break

            if choice == "create":
                # if account exists or not
                exists = input("Does the account exist already? Enter 'yes' or 'no': ")

                # create credentials for an existing account
                new_platform = input("Enter platform: ")
                new_username = input("Enter the username: ")
                if exists == 'yes':
                    new_password = input("Enter password: ")
                    # create credentials for a non-existing account
                elif exists == 'no':
                    # generate passowrd or create?
                    pswd_option = input("Enter 'generate' to autogenerate a password or 'create' to create your own\n")

                    if pswd_option == 'create':
                        new_password = input("Enter password: ")
                    elif pswd_option == "generate":
                        # generate a password using random
                        pswd_string = ''

                        for i in range(3):
                            pswd_string = pswd_string + random.choice(string.ascii_letters) + str(random.randint(1, 10)) + random.choice('!$%&(*>?@^_')
                        
                        new_password = pswd_string
                    else:
                        print("Incorrect input. Please try again")
                        continue #test these continues
                else:
                    print("Incorrect input. Please try again")
                    continue
                # create the account and print a message
                new_account = Credentials(new_platform, new_username, new_password)
                print(f"Successfully saved credentials for {new_account.platform}!\nUsername - {new_account.username}\nPassword - {new_account.password}")
                new_account.save_password()
            elif choice == "display":
                # Credentials.display_password() 
                for item in Credentials.locker:
                    print(item,'.....')
                    item = Credentials.locker[item]
                    for key in item:
                        print(f"Username: {key}; Password: {item[key]}\n")
            elif choice == "delete":
                to_delete = input("Enter the account to delete from locker\n")
                # check if it's in locker
                if to_delete in Credentials.locker:
                    inp = input(f"Are you sure you would like to delete {to_delete} details from locker? y/n: ")
                    if inp == 'y':
                        new_account.delete_password()
                    elif inp == 'n':
                        continue
                else:
                    print("Sorry. You don't seem to have such an account in locker")
            elif choice == "copy":
                copy = input("Enter account you would like to copy password:")
                if copy in Credentials.locker:
                    copied = Credentials.locker[copy][new_username]
                    pyperclip.copy(copied)
                else:
                    print("Sorry. You don't seem to have such an account in locker. Please check your spelling or save it first")
            else:
                print("Incorrect input. Please try again")
        else:
            print("Incorrect username or password!")
            break
if __name__ == "__main__":
    main()
    
      

    