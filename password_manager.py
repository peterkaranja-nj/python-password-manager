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

passwords = load_passwords()


while True:
    print("\n1 Add password")
    print("2 Get password")
    print("3 Delete password")
    print("4 Show services")
    print("5 count passwords")
    print("6 Exit")

    choice = (input("\nEnter your choice: "))
    if choice == "1":
        add_password(passwords)
        save_passwords(passwords)
    elif choice == "2":
        get_password(passwords)
        
    elif choice == "3":
        delete_password(passwords)
        save_passwords(passwords)
    elif choice == "4":
        show_all_services(passwords)
        
        
    elif choice == "5":
        count_passwords(passwords)
        
    elif choice == "6":
        print("Exiting the program.")
        break
       
    else:
        print("Invalid choice. Please try again.")