
s = "Dr5e2a89me9r6s"

# Method 1

digit = "1234567890"
cnt = 0
for i in s:
    if i in digit:
        cnt += 1

print("Total digits =", cnt)

# Method 2
cnt = 0
for i in s:
    if i.isdigit(): #isnumeric() is same
        cnt += 1
print("Total digits =", cnt)


#Reverse of a list

d = [4,5,6,7,9]

print(d[::-1])
