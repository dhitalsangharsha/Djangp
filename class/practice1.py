'''create a class Bank Account.
    Which can be initialized with name,age,gender
    Which has "withdraw" and "deposit" functions (can't withdraw more than balance)
    Which maintains total moneyavailable at the bank
    that is printed using "bank_balance" function'''
class Bank_Account:
    bank_balance = 0
    bank_accounts = []

    def __init__(self,Name,Age,Gender):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.Balance=0
        Bank_Account.bank_accounts.append(self)

    @classmethod
    def Deposit(cls):
        name = input("enter name of account holder:")
        account_to_deposit = None
        for account in Bank_Account.bank_accounts:
            if account.Name == name:
                account_to_deposit = account
        if account_to_deposit == None:
            print("Invalid name")
            return
        d=int(input("enter the amount you want to deposit:"))
        account_to_deposit.Balance += d
        Bank_Account.bank_balance += d

    @classmethod
    def Withdraw(cls):
        name = input("enter name of account holder:")
        account_to_deposit = None
        for account in Bank_Account.bank_accounts:
            if account.Name == name:
                account_to_deposit = account
        if account_to_deposit == None:
            print("Invalid name")
            return
        w=int(input("entet the amount you want to withdraw"))
        if w>account_to_deposit.Balance:
            print("You don't have sufficient balance")
        else:
            account_to_deposit.Balance-=w
            Bank_Account.bank_balance -= w

    @classmethod
    def Bank_balance(cls):
        print("total cash in the bank is:", cls.bank_balance)

sailesh = Bank_Account('Sailesh', 30, 'M')

# l = [('Sangharsha',20,'M')]
# for i in l:
#     i_obj = Bank_Account(i[0], i[1],i[2])

f = open('filename.csv', 'r')
for line in f:
    line = line.strip()
    cells = line.split(',')
    name = cells[0]
    age = int(cells[1])
    gender = cells[2]
    account = Bank_Account(name, age, gender)
Bank_Account.Deposit()
Bank_Account.Withdraw()
Bank_Account.Deposit()
Bank_Account.Bank_balance()
print(sailesh.Balance)
