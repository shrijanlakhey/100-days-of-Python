with open("026/file1.txt") as file:
    content_file1 = file.readlines()

file1_data = [int(number) for number in content_file1]

with open("026/file2.txt") as file:
    content_file2 = file.readlines()

file2_data = [int(number) for number in content_file2]

result = [number for number in file1_data if number in file2_data]
print(result)