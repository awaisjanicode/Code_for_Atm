class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
HI, how can I help you?
1. Press 1 to create a PIN.
2. Press 2 to change PIN.
3. Press 3 to check balance.
4. Press 4 to withdraw.
5. Anything else to exit.""")
        
        if user_input == '1':
         self.create_pin()
        #  self.menu()
        elif user_input == '2':
           self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        elif user_input == '5':
            pass  # Exit
        else:
            exit()
        
        
    def create_pin(self):
        user_pin=input("Enter your pin. ")
        self.pin=user_pin
        
        user_balance=int(input("Enter your balance "))
        self.balance=user_balance
    
        print("Pin created successfully.")
        self.menu()
        
    def change_pin(self):
        old_pin=input("Enter your old pin. ")
        if old_pin==self.pin:
            new_pin=input("Enter your new pin ")
            self.pin=new_pin
            print("Pin change successful. ")
            self.menu()
        else:
            print("Invalid pin")
            self.menu()
    def check_balance(self):
        user_pin=input("enter your pin. ")
        if user_pin==self.pin:
         print("Your balance is", self.balance)
        else:
            print("incorrect pin.")
        self.menu()
        
        
    def withdraw(self):
        user_pin=input("Enter your pin.")
        if user_pin==self.pin:
         withdraw_amount=int(input("Enter amount to withdraw: "))
                  
         if withdraw_amount<=self.balance:
             print(f"You have withdraw an amount of {withdraw_amount} from {self.balance}")
             self.balance -= withdraw_amount
         else:
             print("Amount exceeded.")
             
        else:
            print("Incorrect pin.")
        self.menu()
        

# Creating an object of the Atm class
obj = Atm()
