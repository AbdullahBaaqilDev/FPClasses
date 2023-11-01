# how to create a class
class User:
    def __init__(self,user_number):
        self.name = "Abdullah"
        self.age = 16
        self.email = "abaageel@gmail.com"
        self.password = "abdullah2098"
        self.user_number = user_number
    
    def print_infos(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"email: {self.email}")
        print(f"password: {self.password}")

new_user = User(user_number = 1)
new_user.print_infos()






# classes inheritance
class Zombie:
    def __init__(self,speed,health,damage):
        self.speed = speed
        self.health = health
        self.damage = damage
    
    def take_damage(self,damage):
        self.health -= damage
    
    def give_damage(self):
        print(f"Zombie hit you with {self.damage} damage")

    def die(self):
        print("Zombie has died")

class ElectronicZombie(Zombie):
    def __init__(self,speed,health,damage,electro_power):
        super().__init__(speed,health,damage)
        
        self.electro_power = electro_power

    def give_damage(self):
        print(f"Electronic Zombie hit you with {self.damage}")
    
    def teleport(self):
        print(f"Electronic Zombie has teleported to you")

new_zombie = ElectronicZombie(125, 550, 45, 172)
new_zombie.take_damage(50)
new_zombie.teleport()
new_zombie.give_damage()