programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of done something over and over again."
    }
#retrieving items from dictionary
# print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of done something over and over again."
# print(programming_dictionary)

#Create an empty dictioary
# empty_dictionary = {}

#Wiping an existing dictionary
# programming_dictionary = {} 
# print(programming_dictionary)

#Edit an item in a dictionary
# programming_dictionary["Bug"] = "A bug is actually a moth in your computer"
# print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])