user_infos = {
    "name": "Abdullah",
    "age": 15,
    "country": "Yamen",
    "gender": "Male",
    "exp": [
        "Python",
        "Java",
        "C++",
        "Lua",
        "GDScript"
        ],
}# it can be write in this way several lines
other_infos = {"weight": 36,"height": 78}# or just one line

print(type(user_infos))

user_infos.pop("gender")# delete the key and value by the key
user_infos.setdefault("country",None)# make a new key and value if the key is not exist
user_infos.get("exp",[])# get the value of the key if it exist if not it well return None by defult
user_infos.update(other_infos)# add another dict to the main dict
print(user_infos.keys())# retrun an array with all of dict keys
print(user_infos.values())# retrun an array with all of dict values
print(user_infos.items())# retrun an array with all of dict items [(key,value),(key,value),(key,value)]

print(user_infos)