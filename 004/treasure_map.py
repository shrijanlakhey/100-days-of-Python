# accessing value form a list eg, print(list[list_index][values_index])
# new = [["apple", "beer"], ["Shampoo", "Green", "lever"]]
# print(new[1][0]) output: Shampoo

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

index_1 = int(position[0]) - 1 # horizontal (row) 
index_2 = int(position[1]) - 1 # vertical (column)

map[index_2][index_1] = "X"

print(f"{row1}\n{row2}\n{row3}")
