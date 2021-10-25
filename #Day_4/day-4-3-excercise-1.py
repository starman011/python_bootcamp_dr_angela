#program for treasure map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal_pos = int(position[0])
vertical_pos = int(position[1])
map[vertical_pos -1][horizontal_pos - 1] = '⚔️'

print(f"{row1}\n{row2}\n{row3}")