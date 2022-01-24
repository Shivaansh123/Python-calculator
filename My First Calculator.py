first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("----press keys for operator (+ or - or * or/)----------")
operator = input("Enter operator here : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
else:
   print("Invalid Operation")

   print ("Thanks for using the calculator !")
   print("Run again if you want to use it again.")
   