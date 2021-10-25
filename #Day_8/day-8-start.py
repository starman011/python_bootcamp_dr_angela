# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet(): 
    print("HI")
    print("Hello")
    print("Done")

greet()

#Function that allow for input 
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")
    
greet_with_name("Khan")

#Function with more than 1 input 
#example of positional argument
def greet_with_name_location(name, location): 
    print(f"Your name is {name} and you belong to {location}.")

greet_with_name_location("Khan", "Delhi")

#Functions with keyword arguments| even if we change the parameter position while calling it will still be right
def greet_with_name(name,location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}")

greet_with_name(location = "Delhi", name = "khan")
