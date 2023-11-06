import pandas

student_dict = {
    "student": ["Shrijan", "Ram", "Hari"],
    "score": [56, 76, 98],
}

# Looping through dictionary
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Looping through dataframe
# but this method is not useful 
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)


# iterrows(): inbuilt method to loop through each of the row of the dataframe in pandas
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)

    if row.student == "Shrijan":
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}