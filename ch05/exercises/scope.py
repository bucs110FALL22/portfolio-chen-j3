def multiply(num1,num2):
  result = 0
  for i in range(num2):
    result = result + num1 
  return result
  
#print("Your product is", multiply(11,2))

def exponential(number,exponent):
  result = 1
  for i in range(exponent):
    result = result * number
  return result

print("Your result is", exponential(3,3))

def square(squareNum):
  result = multiply(squareNum,squareNum)
  return result
  
#print("Your result of the square is", square(3))

def main():
  res1 = multiply(11,2)
  print("Your product is", res1)
  res2 = exponential(3,3)
  print("Your result is", res2)
  res3 = square(3)
  print("Your result is", res3)

main()