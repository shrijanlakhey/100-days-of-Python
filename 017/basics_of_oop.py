class User:
    
    # constructor (it will be called everytime a new object is created from this class)
    def __init__(self, user_id,username): 
        # self = object being initiallized
        
        # attributes
        self.id = user_id 
        self.username = username
        self.followers = 0 # difining default value
        self.following = 0

    # method needs to always have 'self' parameter as the first parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Shrijan")
user_2 = User("002", "Ken")
# print(user_1.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

# user_2.follow(user_1)
print(user_2.followers)
print(user_2.following)



# possible way for adding attributes but dont do this

# user1.id = "001"
# user1.username = "Ram"
# print(user1.username)