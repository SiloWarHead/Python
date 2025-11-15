import random

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
print(n1, n2)

letter = "qwertyuiopasdfghjklzxcvbnm"
l1 = letter[random.randint(0, 25)]
l2 = letter[random.randint(0, 25)]
print(l1, l2)

letter_U = letter.upper()
L1 = letter_U[random.randint(0, 25)]
L2 = letter_U[random.randint(0, 25)]
print(L1, L2)

sym = "!@#$%^&*"
s1 = sym[random.randint(0, 7)]
s2 = sym[random.randint(0, 7)]
print(s1, s2)

p = [str(n1), str(n2), l1, l2, L1, L2, s1, s2]
print("Before shuffle:", p)

random.shuffle(p)
print("After shuffle:", p)

password = ''.join(p)
print("Generated password:", password)
