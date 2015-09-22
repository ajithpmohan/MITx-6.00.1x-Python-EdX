balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalpaid=0.00

for month in range(1,13):
  monthlyinterestrate = annualInterestRate/12.00
  monthlypayment = monthlyPaymentRate * balance
  unpaidbalance = round((balance - monthlypayment),2)
  totalpaid += monthlypayment
  balance = round((unpaidbalance + (monthlyinterestrate * unpaidbalance)),2)
  
  print 'Month: '+ str(month)
  print 'Minimum monthly payment: ' + str(round(monthlypayment,2))
  print 'Remaining balance: ' + str(round(balance,2))

print 'Total paid: '+ str(round(totalpaid,2))
print 'Remaining balance: ' + str(balance)