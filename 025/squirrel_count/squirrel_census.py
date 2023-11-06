import pandas

data = pandas.read_csv("025/squirrel_count/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["Gray", "Cinnamon", "Black"]
color_count = []

for color in colors:
    count_value = data["Primary Fur Color"].value_counts()[color]
    color_count.append(count_value)

# alternative way to count
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color" : colors,
    "Count" : color_count,
}

# converting the 'data_dict' dictionary to a DataFrame
df = pandas.DataFrame(data_dict)

# converting the dataframe to a CSV(comma-separated values) file
df.to_csv("025/squirrel_count/  squirrel_count.csv")