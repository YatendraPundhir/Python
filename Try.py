print("Enter A First Number")
n1 = input()
print("Enter A Second Number")
n2 = input()
try:
  print("Sum of two numbers is :",int(n1)+int(n2))

except Exception as e :
    print(e)
    print("Hello Your are out of Exception")