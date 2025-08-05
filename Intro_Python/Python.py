#the assigning of operation and numbers

num1 = float(input("Enter the first number"))
num2 = float(input("Enter the first number"))
operation = input("Enter the desired operation (+, -, /, * ): ")

#Operation 

if operation == "+":
    results = num1 + num2
    print(f"{num1} + {num2} = {results}")
elif operation == "-":
    results = num1 + num2
    print(f"{num1} - {num2} = {results}")
elif operation == "*":
    results = num1 * num2
    print(f"{num1} * {num2} = {results}")
elif operation == "/":
    if num2 != 0:
        results = num1 / num2
        print(f"{num1} / {num2} = {results}")

    else:
        print("Error: A number equal to 0 s not divisible")
else: 
    print ("Invalid operation please use the operations")