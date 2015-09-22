balance = 3329
annualInterestRate = 0.2
monthlypayment=0
current_balance=balance
while(current_balance>0):
    current_balance=balance
    monthlypayment+=10
    for month in range(1,13):
      monthlyInterestRate = annualInterestRate/12.00
      unpaidbalance = (current_balance - monthlypayment)
      current_balance = unpaidbalance + (monthlyInterestRate * unpaidbalance)
print 'Lowest Payment: %d' % (monthlypayment)

