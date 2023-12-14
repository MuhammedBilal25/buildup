class Bank:
    ac_number:int
    name:str
    account_type:str
    ifsc_code:int
    branch:str
    balance:int
    def create_account(self,ac_no,name,ac_type,ifsc,brh,bal):
        self.ac_number=ac_no
        self.account_type=ac_type
        self.balance=bal
        self.ifsc_code=ifsc
        self.branch=brh
        self.name=name
    def deposite(self,amount):
        self.balance=self.balance+amount
        print(f"your {self.ac_number} is credited with amount of Rs{amount}. the available balance is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("INSUFITIENT BALANCE")
        else:
            self.balance=self.balance-amount
            print(f"your {self.ac_number} is debited  by an amount of Rs{amount}. the available balance is {self.balance}")
    def get_balance(self):
        print(f" The available balance is {self.balance}")
        
acc_1=Bank()
acc_1.create_account(12345,"Bilal","savings","qwe1235rsbi","ekm",12000)
acc_1.get_balance()
acc_1.deposite(3200)
acc_1.withdraw(450)
