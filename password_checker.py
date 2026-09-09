#Password Strength Checker

password = input("Enter your password:")

score = 0

#Check password length
if len(password)>=8:
  score+=1

#Check uppercase Letter
if any(char.isupper()for char in password):
  score += 1

#Check lowercase letter
if any(char.islower() for char in password):
  score += 1

#Check number
if any(char.isdight()for char in password):
  score += 1

#check special character
if any(not char.isalnum() for char in password):
  score += 1

#Display password strength
if score <= 2:
  print("Password Strength:WEAK")
elif score ==3 or score == 4;
  print("Password Strenght:MEDIUM")
else:
  print("Password Strength:STRONG")
