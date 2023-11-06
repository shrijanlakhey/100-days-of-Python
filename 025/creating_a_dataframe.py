import pandas

# creating a dataframe from scratch
data_dict = {
    "students" : ["Ram", "Hari", "Shyam"],
    "score" : [90, 60, 70],
}

# converting the 'data_dict' dictionary to a DataFrame
data = pandas.DataFrame(data_dict)
print(data)


# converting the dataframe to a CSV(comma-separated values) file
data.to_csv("025/new_data.csv")