import random
import string
def load_passwords():
    
    passwords = {}
    
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                account, password = line.strip().split(":")
                passwords[account] = password
    except FileNotFoundError:
        pass
    return passwords

def save_passwords(passwords):
    with open("passwords.txt", "w") as file:
        for account, password in passwords.items():
            file.write(f"{account}:{password}\n")
        file.close()

def add_password(passwords):
    account = input("Enter the account name: ")
    password = input("Enter the password: ")
    passwords[account] = password
    print("Password added successfully!")

def get_password(passwords):
    account = input("Enter the account name to retrieve the password: ")
    print(passwords.get(account, 'account not found'))
    
def delete_password(passwords):
    account = input("Enter the account name to delete the password: ")
    if account in passwords:
        del passwords[account]
        print("Password deleted successfully!")
    else:
        print("Account not found.")

def show_all_services(passwords):
    for account in passwords:
        print(account)

def count_passwords(passwords):

    print(f"You have {len(passwords)} stored passwords")

def generate_password():
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for _ in range(length):
        password += random.choice(characters)
    print(f"Generated Password: {password}")

def search_service(passwords):
    keyword = input("Enter the service name to search for: ")

    for account in passwords:
        if keyword.lower() in account.lower():
            print(account)
def log_action(action):
    with open("log.txt", "a") as file:
        file.write(f"{action}\n")


passwords = load_passwords()


while True:
    print("""
MENU
1 Add password
2 Get password
3 Delete password
4 Show services
5 Count passwords
6 Generate password
7 Search service
8 Exit
""")
    

    choice = (input("\nEnter your choice: "))
    if choice == "1":
        add_password(passwords)
        save_passwords(passwords)
        log_action("Password added")

    elif choice == "2":
        get_password(passwords)
        log_action("Password retrieved")
        
    elif choice == "3":
        delete_password(passwords)
        save_passwords(passwords)
        log_action("Password deleted")

    elif choice == "4":
        show_all_services(passwords)
        log_action("Services shown")
        
        
    elif choice == "5":
        count_passwords(passwords)
        log_action("Password count")

    elif choice == "6":
        generate_password()
        log_action("Password generated")

    elif choice == "7":
        search_service(passwords)
        log_action("Service searched")
        
    elif choice == "8":
        print("Exiting the program.")
        log_action("Program exited")
        break
       
    else:
        print("Invalid choice. Please try again.")