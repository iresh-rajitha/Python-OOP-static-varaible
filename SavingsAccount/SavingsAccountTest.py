from Account import Account

if __name__ == '__main__':
    s1 = Account()
    s2 = Account()

    s1.set_balacce(2000)
    s2.set_balacce(3000)

    # 1 st month
    print("======= 1st Month rate= 4% ==============")
    Account.annual_interest_rate = 4
    print("Account 1 balance after 1st month : " + str(s1.cal_monthly_interest()))
    print("Account 2 balance after 1st month : " + str(s2.cal_monthly_interest()))
    print("======= 2nd Month rate= 5% ==============")
    Account.annual_interest_rate = 5
    print("Account 1 balance after 2nd month : " + str(s1.cal_monthly_interest()))
    print("Account 2 balance after 2nd month : " + str(s2.cal_monthly_interest()))

