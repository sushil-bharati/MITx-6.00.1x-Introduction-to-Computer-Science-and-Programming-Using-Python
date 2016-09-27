balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for i in range(1,13):
    unpaid = balance - monthlyPaymentRate * balance
    balance = unpaid + (annualInterestRate / 12.0) * unpaid

print ('Remaining balance :{0:.2f}' .format(balance))