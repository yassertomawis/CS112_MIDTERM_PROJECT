# ATM Simulator Program

# Initial balance
balance = 10000


# Function to display balance
def display_balance():
    print(f"Your balance is: ₱{balance}")


# Function to withdraw money
def withdraw():
    global balance  # Using global to modify the balance variable
    amount = float(input("Enter the amount to withdraw: ₱"))
    if amount > balance:
        print("Insufficient funds. Withdrawal failed.")
    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: ₱{balance}")


# Function to transfer money
def transfer():
    global balance
    amount = float(input("Enter the amount to transfer: ₱"))
    if amount > balance:
        print("Insufficient funds. Transfer failed.")
    else:
        recipient = input("Enter the recipient's account number: ")
        print(f"₱{amount} transferred to {recipient}.")
        balance -= amount
        print(f"Remaining balance: ₱{balance}")


# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: ₱"))
    balance += amount
    print(f"Deposit successful. Updated balance: ₱{balance}")


# Main program
while True:
    print("\n===== ATM Simulator =====")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Transfer Money")
    print("4. Deposit Money")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_balance()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        transfer()
    elif choice == '4':
        deposit()
    elif choice == '5':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
