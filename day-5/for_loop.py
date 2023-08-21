fruits=["Banana", "Mango", "Apple"]
for fruit in fruits:
    print(fruit)
    # print(fruits) Output: prints ["Banana", "Mango", "Apple"] 3 times

# for loop with range
for number in range(1, 11): # prints form 1 - 10
    print(number)

print("\n")

for number in range(1, 11, 3): # here 3 is step, i.e. defining by how much the number shall be incremented
    print(number) 

print("\n")

sum = 0
for number in range(1, 101):
    sum += number

print(f"Sum of all the numbers from 1 to 100 is {sum}")