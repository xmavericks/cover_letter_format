? Print first and last name in reverse order with a space between them

example - 
first_name = amod
last_name = kumar

output should be = kumar amod

Code solution: Solution 1 using 4 for loops for every basic iteration
  
first_name = input("Enter your first name: ") # Taking input of first name
last_name = input("Enter your last name: ")   # Taking input of last name
f_name_reverse = []                           # Declaring list variable to store reversed names respectively
l_name_reverse = []
first_name_reversed = ""                      # Declaration of empty string variable fo storing each char from reversed name and append it invertly
last_name_reversed = ""
for i in range(len(first_name)):
    f_name_reverse.append(first_name[i])
for j in range(len(last_name)):
    l_name_reverse.append(last_name[j])

for k in range(len(f_name_reverse)):
    first_name_reversed += f_name_reverse[k]
for l in range(len(l_name_reverse)):
    last_name_reversed += l_name_reverse[l]
print("First name was: ",first_name)
print("Last name was: ",last_name)
print("Reversed name is: "+last_name_reversed+" "+first_name_reversed)
