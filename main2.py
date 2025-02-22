# name = "Tanjumul"

# age = 25 

# cgpa = 3.46 

# is_student = True
 
# age = float(age)

# cgpa = int(cgpa)

# print(f"This is the demonstration of the age as float and cgpa as int {cgpa} , {age}")

#typecast teh age as string as str() && to see the type of every variable 


age = 25
age = str(age)

print(age)
# print(type(age))

age += "1"

print(age)

#we can use the boolean to see anyone is filled the name section or not by using the typecast and the boolean function

is_name = True

name = ""
name = bool(name)
print(name)
#see the name is not filled and the output will be: False 

#now i will use a filled name string to see that the output is working or not

name = "Tanju"
name = bool(name)
print(name)
# working as true 


#use of input function to input data 

name = input("what is your name ? ")
age = input("What is your age now ?")
print(f"Hello {name}, You are {age} years old") #we will need f to insert variables in the string of the print output
