from random import randint

length = 5
a = 1
b = 100
password = []

for i in range(length):
    password.append(randint(a, b))
    
print(password)
