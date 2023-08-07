my_friends = ("mohammed","omar","yousef","omar")

print(my_friends[0:2])
print(len(my_friends))
print(my_friends.count("omer"))
print(my_friends.index("yousef"))


# update tuple
my_friends_list = list(my_friends)# convert tuple to list
my_friends_list.append("abdullah")
my_friends_list[0] = "ali"
print(type(my_friends_list))

my_friends = tuple(my_friends_list)# convert list to tuple
print(type(my_friends))