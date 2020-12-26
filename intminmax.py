name = input("Full Name: ")
print(name)
if len(name) < 3:
    print("Name must be 3 characters long")
elif len(name) > 50:
    print("Name muyst not be longer than 50 charecters")
else:
    print("Name looks good")
