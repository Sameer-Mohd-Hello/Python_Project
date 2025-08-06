import random as rd

a = [rd.randint(1, 9) for _ in range(6)]

print("Your OTP is -> ", end="")
for i in a:
    print(i, end="")
