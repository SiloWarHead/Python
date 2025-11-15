print("Choose Operation (1 or 2)")
want = input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n")

if want == "1":
    c = float(input("Enter Celsius value: "))
    f = (9 * c / 5) + 32
    f = round(f, 1)
    print(f, "°F")

elif want == "2":
    f = float(input("Enter Fahrenheit value: "))
    c = (f - 32) * 5 / 9
    c = round(c, 1)
    print(c, "°C")

else:
    print("Wrong keyword!")
