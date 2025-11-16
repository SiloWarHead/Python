import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# BASIC OPERATIONS
# ---------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero!"
    return a % b

# ---------------------------
# SINGLE NUMBER OPERATIONS
# ---------------------------

def square_root(a):
    if a < 0:
        return "Error: Negative square root!"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial can't be negative!"
    return math.factorial(int(a))

# ---------------------------
# QUADRATIC EQUATION SOLVER
# ---------------------------
# Solves ax² + bx + c = 0

def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c  # discriminant
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"Two real roots: {x1}, {x2}"
    elif D == 0:
        x = -b / (2*a)
        return f"One real root: {x}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        return f"Complex roots: {real}+{imag}i , {real}-{imag}i"

# ---------------------------
# GRAPHING FUNCTION
# ---------------------------

def plot_graph(expr):
    x = np.linspace(-10, 10, 400)
    try:
        y = eval(expr)
    except:
        print("Invalid math expression!")
        return

    plt.plot(x, y)
    plt.title("Graph of y = " + expr)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# ---------------------------
# MAIN PROGRAM LOOP
# ---------------------------

print("=== POWERED PYTHON CALCULATOR ===")

while True:
    print("\nChoose an option:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (a^b)")
    print("6. Modulo (%)")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Solve Quadratic Equation")
    print("10. Plot Graph")
    print("0. EXIT")

    choice = input("Enter choice: ")

    if choice == "0":
        print("Goodbye!")
        break

    # ----------- Basic two-number operations ------------
    if choice in ["1", "2", "3", "4", "5", "6"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        elif choice == "5":
            print("Result:", power(a, b))
        elif choice == "6":
            print("Result:", modulo(a, b))

    # ----------- Square root ------------
    elif choice == "7":
        a = float(input("Enter a number: "))
        print("Result:", square_root(a))

    # ----------- Factorial ------------
    elif choice == "8":
        a = float(input("Enter a number: "))
        print("Result:", factorial(a))

    # ----------- Quadratic ------------
    elif choice == "9":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print(solve_quadratic(a, b, c))

    # ----------- Graphing ------------
    elif choice == "10":
        print("Use x as the variable. Example: x**2 + 2*x + 1")
        expr = input("Enter function f(x): ")
        plot_graph(expr)

    else:
        print("Invalid option!")