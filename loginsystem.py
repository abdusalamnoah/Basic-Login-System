users = {}
name = input("What is your username? ").strip().upper()


while True:
   password = input("Type a password: ").strip()
   upperc, lowerc, symbols, digit, fails = 0, 0, 0, 0, 0


   if len(password) >= 8:
       for x in password[:]:
           if x.isalpha() and x.islower():
               lowerc += 1
           elif x.isalpha() and x.isupper():
               upperc += 1
           elif x.isnumeric():
               digit += 1
           elif not x.isalnum():
               symbols += 1
   else:
       print("Not long enough (8 characters minimum)")


   if upperc == 0:
       fails += 1
   if lowerc == 0:
       fails += 1
   if digit == 0:
       fails += 1
   if symbols == 0:
       fails += 1


   if fails == 0:
       print("Password strength: Strong")
   elif fails == 1 or fails == 2:
       print("Password strength: Medium")
   else:
       print("Password strength: Weak")


   attempt = input("Want to test another password?(Y/N) ")
   if attempt.upper() != "Y":
       break
if fails <= 2:
   users[name] = password
   print("Accoutn created successfully!\n")
else:
   print("Account not created due to weak password.\n")


name = input("What is your username? ").strip().upper()
if name.upper() in users:
   passw = input("This account already exists. What is the password? ")
   for x in range(2):
       if passw == users[name]:
           print("You got it right. You may enter.")
           break
       else:
           passw = input("Wrong password. Try again: ")
   else:
       print("You got it wrong 3 times. You cannot enter.")
else:
   print("Username not found.")