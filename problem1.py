password = input("Enter your password: ")
length = len(password)
if length >= 8 and length <= 15:
print("Password length is valid.")
else:
print("Password too short or too long. Please try again.")
