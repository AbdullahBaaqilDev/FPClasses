
file_path = "D:\\Abdullah\\PROGRAMES\\Coding\\FutureProgramers\\FPClasses\\TextFile.txt"

name = "Ibrahem"
age = 45
country = "Yamen"

with open(file_path, "w") as file:
    file.write(f"My name is {name}\nMy age is {age}\nI am from {country}")

with open(file_path, "r") as file:
    text = file.read()
print(text)