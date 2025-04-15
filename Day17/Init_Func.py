class Demo():
    
    
# normal way of obj creation
#     pass
# user = Demo()
# user.id = "01"
# print(user.id)

# another way ,In this way we can create more new objects in less line of code
    def __init__(self, user_id, user_name):   
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1
        
user_1 = Demo(21,"parthi")

user_2 = Demo("001" , "hello")

# print(user_2.user_id)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
