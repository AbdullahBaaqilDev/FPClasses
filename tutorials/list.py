my_friends = ["Hamzah","Abdullah","Salem","Ali"]
print(my_friends[2])

print(len(my_friends))

for friend_name in my_friends:
    print(friend_name)

my_friends.append("Ali")
print(my_friends)
my_friends.insert(1,"Ahmed")
print(my_friends)
my_friends.pop(0)
print(my_friends)
my_friends.remove("Ahmed")
print(my_friends)
my_friends.sort()
print(my_friends)

print(my_friends.count("Ali"))
print(my_friends.index("Ali"))