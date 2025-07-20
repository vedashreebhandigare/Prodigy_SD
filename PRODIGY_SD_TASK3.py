import pandas as pd
import os

FILENAME = 'contact management system.xlsx'

# Load data if exists, else create empty DataFrame
if os.path.exists(FILENAME):
    df = pd.read_excel(FILENAME)
else:
    df = pd.DataFrame(columns=['num', 'name', 'email'])

def save_df():
    df.to_excel(FILENAME, index=False)

def addfirst(num, name, email):
    global df
    df = pd.DataFrame({'num': [num], 'name': [name], 'email': [email]})
    save_df()
    print("First record added and saved.")

def add(num, name, email):
    global df
    new_data = pd.DataFrame({'num': [num], 'name': [name], 'email': [email]})
    df = pd.concat([df, new_data], ignore_index=True)
    save_df()
    print("Record added.")

def display():
    if os.path.exists(FILENAME):
        df_display = pd.read_excel(FILENAME)
        print(df_display)
    else:
        print("No records found.")

def delete(num):    
    global df
    df = df[df['num'] != num]
    save_df()
    print(f"Record with num {num} deleted.")

# Main program
print("Welcome to Contact Management System")

while True:
    print("\n1. First record")
    print("2. Add record")
    print("3. Display records")
    print("4. Delete record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        num = input("Enter number: ")
        name = input("Enter name: ")
        email = input("Enter email: ")
        addfirst(num, name, email)
    elif choice == '2':
        num = input("Enter number: ")
        name = input("Enter name: ")
        email = input("Enter email: ")
        add(num, name, email)
    elif choice == '3':
        display()
    elif choice == '4':
        display()
        num = input("Enter number to delete: ")
        delete(num)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
