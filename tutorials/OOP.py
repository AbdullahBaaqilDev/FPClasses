
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