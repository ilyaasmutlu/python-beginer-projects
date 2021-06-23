# Using the input command, we get an int (integer) value from the user.
number1=int(input(("Enter the first number: ")))
number2=int(input("Enter the second number: "))
# Using the input command, we get the value of the action from the user.
operation=int(input("Enter the transaction number: n1-Addition 2-Subtraction 3-Multiplication 4-Division "))
# We check the transaction number entered by the user
if (operation==1):
    print("result: ",int(number1+number2))
elif (operation==2):
    print("result: ",int(number1-number2))
elif (operation==3):
    print("result: ",int(number1*number2))
elif(operation==4):
    print("result: ",float(number1/number2))
else:
    print("Invalid transaction")