# OOP (object oriented programming)
from turtle import Turtle, Screen

# creating a new object (timmy)
timmy = Turtle()
# here turtle is a module and Turtle is a class
print(timmy)
timmy.shape("turtle")
timmy.color("lightgreen")
timmy.forward(100)

# creating a new object (my_screen)
my_screen = Screen()
# Screen is a class
print(my_screen.canvheight)
# canvheight is a attribute
my_screen.exitonclick()
# exitonclick() is a method

# importing a pretty table package
from prettytable import PrettyTable

pretty_table = PrettyTable()
table = pretty_table
# adds column
table.add_column("Pokemon", ["Pikachu", "Weedle", "Raichu"])
table.add_column("Type", ["Electric", "Poison", "Electric"])
# align the words inside to right
table.align = "r"
print(table)
