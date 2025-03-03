## Écrivez votre code ici !

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        return f"Nom du propriétaire du compte :{self.account_holder}. Solde : {self.balance}"

    def deposit(self, amount):
            self.balance += amount
            return f"Solde actuel : {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Vous avez retiré {amount}. Solde actuel : {self.balance}"
        else:
            print("Vous ne disposez pas des fonds nécessaire pour effectuer le retrait.")

Jeremy_account = BankAccount("Jeremy", 480)

print(Jeremy_account.display_balance())
print(Jeremy_account.withdraw(400))
