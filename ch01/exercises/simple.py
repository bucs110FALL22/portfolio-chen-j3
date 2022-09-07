print(10*5)
print(10**2)
print(15/10)
print(15//10)
print(-15//10)
print(15%10)
print(10%10)
print(0%10)
print(10/15)
#What is wrong with the last answer?
#The last answer is 0.666666. The 6 is repeating.

#part 2

rate = (input("What is the exchange rate for the Euro to Dollar?\n"))
#dont want to use int for percentage. use float.
rate = float(rate)
amount = float(input("What is the amount of currency you need to exchange?\n"))
total = rate*amount
result = total-3
print("Your result is $",result)