names_ages = {
    "abdullah": 15,
    "hamzah baaqeil": 14.6,
    "hamzah": 16,
    "ali": 17,
    "salem": 21,
}
print(type(names_ages))

print(names_ages["abdullah"])
names_ages["salem"] = 21
names_ages.pop("hamzah baaqeil")

new_dict = {
    "mohammed": 36,
    "hussain": 78
}

names_ages.update()
print(names_ages)