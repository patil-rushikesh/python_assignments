class Bank:
    def __init__(self, name="Unknown", acc=0, type="None", bal=0):
        self.name = name
        self.acc = acc
        self.type = type
        self.bal = bal
        self.statement = []

    def show(self):
        print(f"Name: {self.name}, Account: {self.acc}, Type: {self.type}, Balance: {self.bal} Rs")

    def add(self, amt):
        self.bal += amt
        self.statement.append(f"Deposited: {amt} Rs")

    def sub(self, amt):
        if self.bal >= amt:
            self.bal -= amt
            self.statement.append(f"Withdrew: {amt} Rs")
        else:
            raise ValueError("Insufficient balance.")

    def display_balance(self):
        print(f"Balance: {self.bal} Rs")

    def display_statement(self):
        print("Statement:")
        for entry in self.statement:
            print(entry)

custs = {}
while True:
    print("\n1. Create Account\n2. Update Account\n3. Withdraw Amount\n4. Deposit Amount\n5. Display Balance\n6. Display Statement\n7. Exit")
    try:
        ch = int(input("Choice: "))
        
        if ch == 1:
            name = input("Name: ")
            acc = len(custs)  # Unique account number
            type = input("Account Type: ")
            bal = float(input("Initial Deposit: "))
            custs[acc] = Bank(name, acc, type, bal)
            print(f"Account {acc} created for {name}.")
        
        elif ch == 2:
            acc = int(input("Account Number: "))
            if acc in custs:
                name = input("New Name: ")
                custs[acc].name = name
                print("Account updated.")
            else:
                raise ValueError("Account number invalid.")

        elif ch == 3:
            acc = int(input("Account Number: "))
            if acc in custs:
                amt = float(input("Amount: "))
                custs[acc].sub(amt)
            else:
                raise ValueError("Account number invalid.")

        elif ch == 4:
            acc = int(input("Account Number: "))
            if acc in custs:
                amt = float(input("Amount: "))
                custs[acc].add(amt)
            else:
                raise ValueError("Account number invalid.")

        elif ch == 5:
            acc = int(input("Account Number: "))
            if acc in custs:
                custs[acc].display_balance()
            else:
                raise ValueError("Account number invalid.")

        elif ch == 6:
            acc = int(input("Account Number: "))
            if acc in custs:
                custs[acc].display_statement()
            else:
                raise ValueError("Account number invalid.")

        elif ch == 7:
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")
    except ValueError as e:
        print(e)
