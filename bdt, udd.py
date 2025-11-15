print("Choose Operation (1 or 2)")
want = input("1. USD to BDT\n2. BDT to USD\n")

if want == "1":
    usd = float(input("Enter USD value: "))
    bdt = usd * 125
    print(usd, "USD =", bdt, "BDT")

elif want == "2":
    bdt = float(input("Enter BDT value: "))
    usd = bdt / 125
    print(bdt, "BDT =", round(usd, 2), "USD")

else:
    print("Wrong keyword!")
