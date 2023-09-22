# dictionry = {
#     "key1" : [list],
#     "key2" : [dict],
# }

# Nesting

# Normal dictionary
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin", 
}

# Nesting list in a dictionary

travel_log = {
    # "France" : "Paris", "Lille", "Dijon", # not allowed as each key can only have one value
    "France" : ["Paris", "Lille", "Dijon"], # allowed as the value is a list
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting list in a list
["a", "b", ["c", "d"], "e"] # this is valid but it is not quite as useful as nesting a list in a dictionary or a dictionary in a dictionary


# Nesting dictionary in a dictionary
travel_log = {
    "France" : {"cities_visted" : ["Paris", "Lille", "Dijon"], "total_visits": 12}, 
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 14},
}


# Nesting dictionary in a list
travel_log = [
    {
        "country": "France", 
        "cities_visted" : ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    }, 
    
    {
        "country": "Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 14
    },
]