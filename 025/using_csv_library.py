import csv

with open("025/weather_data.csv") as data_file: 
    data = csv.reader(data_file)
    temperatures = []
    # getting a hold of temperatures only
    for row in data:
        if not row[1] == "temp":
            temperatures.append(int(row[1]))
    
    print(temperatures)