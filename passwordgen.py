import random
uletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
special = '!"£$%^&*(){}:@~<>?/[]-=_+`¬'

upper, lower, nums, spec = True, True, True ,True

all = ""

if upper:
    all += uletters
if lower:
    all += letters
if nums:
    all += num
if spec:
    all += special

length = int(input("Enter length of passwords: "))
amount = int(input("Enter amount of passwords: "))

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)