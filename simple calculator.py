def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2  # Fixed here

def divide(n1, n2):
    if n2 == 0:
        return "Can't be divided by zero"
    else:
        return n1 / n2

def squared(n1, n2):
    return n1*n1

op = input("Choose Operation (+, -, *, /): ")
n1 = float(input("Num1: "))
n2 = float(input("Num2: "))

if op == "+":
    print(n1, "+", n2, "=", add(n1, n2))
elif op == "-":
    print(n1, "-", n2, "=", subtract(n1, n2))
elif op == "*":
    print(n1, "*", n2, "=", multiply(n1, n2))
elif op == "/":
    print(n1, "/", n2, "=", divide(n1, n2))
else:
    print("Invalid Keyword!") 