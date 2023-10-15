







class User:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
    
    def print_info(self,one_line):
        if one_line:
            print(f"Username: {self.name} User Age: {self.age} User Country: {self.country}")
        else:
            print(f"Username: {self.name}\nUser Age: {self.age}\nUser Country: {self.country}")

user1 = User(name = "Hamzah",age = 16,country = "Saudi Arabia")
user1.print_info(False)







print("---------------------")

class Enemy:
    def __init__(self,name,speed,health):
        self.name = name
        self.speed = speed
        self.health = health
    
    def die(self):
        print(f"{self.name} is Dead")
    
    def hit(self,demage):
        print(f"{self.name} hit you demage = {demage}")
    
    def show_health(self):
        print(self.health)

enemy = Enemy(name = "Hamzah Small",speed = 120,health = 1)
enemy.show_health()
enemy.hit(demage = 102)
enemy.die()


print("---------------------")
























class Parent:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
    
    def print_info(self,one_line):
        if one_line:
            print(f"Username: {self.name} User Age: {self.age} User Country: {self.country}")
        else:
            print(f"Username: {self.name}\nUser Age: {self.age}\nUser Country: {self.country}")

class Son(Parent):
    def __init__(self,name,age,country,school):
        super().__init__(name,age,country)

        self.school = school

son1 = Son("Abdullah",15,"Saudi Arabia","Ebn Habban High School")
son1.print_info(False)
