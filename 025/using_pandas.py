import pandas

# no need to use 'open'
data = pandas.read_csv("025/weather_data.csv")


# getting a hold of temperatures only
# it takes the first row as the names of each column and finds the data based on the name of the column  
print(data["temp"])


# data types in pandas
# a whole table is a 'DataFrame'(1-dimensional) and a single column is a 'Series'(2-dimensional)
print(type(data))
print(type(data["temp"]))


# we can convert a DataFrame(table) to a dictionary
# converts the data to dictionary
data_dict = data.to_dict()
print(data_dict)


# we can convert a Series(column) to a list
temp_list = data["temp"].to_list()
print(temp_list)

# finding average of temperatures
avg = data["temp"].mean()
print(avg)

# finding the maximum value from the temperature column
maximum_value = data["temp"].max()
print(maximum_value)

# another way to get data in columns
print(data.condition)

# get data in row
print(data[data.day == "Monday"].count()) # returns the row which has "Monday" in the column day

# returns the row which has maximum temperature
print(data[data.temp == data.temp.max()])

# getting temperature from the row which has "Monday" 
monday = data[data.day == "Monday"]
print(monday.temp)


# celcius to temperature

# this method of converting it to integer is deprecated
# monday_temp = int(monday.temp)

# use this instead (recommended by pandas itself)
monday_temp = int(monday.temp[0]) # '0' is index as in the CSV file, Monday is the first piece of data in the 'weather_data.csv' file
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)
