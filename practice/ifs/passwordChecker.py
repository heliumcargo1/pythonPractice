password = input("input password:")

if len(password) <6:
    print("weak")
elif len(password) <11:
    print("medium")
else:
    print("strong")