balance = 3926
annualInterestRate = 0.2

flag = True
start = 10
while (flag):
    copyBalance = balance
    for i in range(1,13) :
	    unpaid = copyBalance - start
	    copyBalance = unpaid + (annualInterestRate/12.0) * unpaid
    if (copyBalance<=0):
        break
    start += 10
		
print ('Lowest Payment: ' +str(start))
