#1 Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# 2 Loop through the letters in the word "banana":

for x in "banana":
  print(x) 
  #output b a n a n a separate by line
  
  
#3 Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#4 
for x in range(2, 30, 3):
  print(x)
#output 2,5,8,11,14,17,20,23,26,29

#5 If the loop breaks, the else block is not executed.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#6 Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
    
#7 having an empty for loop like this, would raise an error without the pass statement
for x in [0, 1, 2]:
  pass

