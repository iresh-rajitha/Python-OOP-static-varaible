class Account:
    annual_interest_rate = 0

    def __init__(self, ):
        self.__balance = 0

    def modify_interest_rate(self, rate):
        Account.annual_interest_rate = rate

    def set_balacce(self, balance):
        self.__balance = balance

    def cal_monthly_interest(self):
         self.__balance += self.__balance * ((Account.annual_interest_rate / 100) / 12)
         return self.__balance
