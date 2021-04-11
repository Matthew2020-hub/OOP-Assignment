class Budget:
    # budget app for different categories (clothing, food, and entertainment)
    def __init__(self, categoryname):
        self.ledger = list()
        self.funds = 0
        self.categoryname = categoryname
        

		
    def deposit(self):

        amount = int(input("how much would you like to deposit\n "))
        self.ledger.append({ amount})
        self.funds += amount
        return f"{self.funds} has been deposited"

    def withdraw(self, amount,):
       
        if self.check_funds(amount):
            amount *= -1
            self.ledger.append({"amount": amount})
            self.funds += amount
            return f"you're withdrawing #{amount}: balance = #{self.funds}"
        else:
            return "Insufficient fund"

    def get_balance(self):
        return f"Amount available at the moment is: {self.funds}"


    def transfer (self, amount) :
        category_name = input("category name: ")
        self.categoryname = category_name
        if amount <= self.funds : 
            amount *= 1
            self.ledger.append({"amount": amount})
            self.funds -= amount
			# call withdraw method
            self.withdraw(amount)
            return f"{amount} has been transferred to {category_name} successfully: balance ={self.funds}"
			# call deposit method
            self.categoryname = self.funds
            self.deposit(amount)
        else:
            return "Transaction failed due to insufficient fund"

    def check_funds(self, amount):
        
        if amount < self.funds:
            return f"low funds: available funds = {self.funds}"
        else:
            return f" available fund is: {self.funds}"

