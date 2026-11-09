class BankAccount:
    total_accounts=0
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.__balance=balance
        BankAccount.total_accounts+=1
    def deposit(self,amount):
      if amount>0:
        self.__balance+=amount
        print("Deposit successfull..")
      else:
         print("Invalid amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
         self.__balance=self.__balance-amount
         print("withdraw successfull")
        else:
         print("Invalid operation")
    def check_balance(self):
       print("Current balance : ",self.__balance)
    def display_details(self):
       print("Name: ",self.name)
       print("Account Number: ",self.account_number)
       self.check_balance()

account=BankAccount("sai",1001,5000)
while True:
    print("\n--- BANK MANAGEMENT SYSTEM ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.display_details()

    elif choice == "5":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice!")
