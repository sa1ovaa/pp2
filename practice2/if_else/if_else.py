#1 If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#2 Multiple statements in an if block:
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
  
#3 Using a boolean variable:
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#4 Testing multiple conditions:
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
  
#5 Checking even or odd numbers:

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")
  
#6 collapse if elif else Temperature classifier:

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")