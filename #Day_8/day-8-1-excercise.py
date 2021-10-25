#program to make a paint area calculator
import math

def paint_calc(height, width, cover):
    area = height * width
    total_paint_can = math.ceil(area/cover)
    print(f"You'll need {total_paint_can} cans of paint.")

# Define a function called paint_calc() so that the code below works.   

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)