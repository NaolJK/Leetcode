class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1-=1
        account2-=1
        if account1 >=0 and account1 < len(self.balance) and account2 >=0 and account2 < len(self.balance):
            account_bal = self.balance[account1]
            # print(self.balance[account1])
            if account_bal - money >= 0:
                self.balance[account2]+=money
                self.balance[account1]-=money
                return True
            return False
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        account-=1
        # print(self.balance)
        if account >=0 and account < len(self.balance):
            self.balance[account]+=money 
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        account-=1
        if account >=0 and account < len(self.balance):
            account_balance = self.balance[account]
            if account_balance - money >= 0:
                self.balance[account]-=money
                return True
            return False
        return False
    
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)