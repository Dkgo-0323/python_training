"""用于模拟管理员的类"""
from user import User
class Admin(User):
    def __init__(self,name,age,gender,hobby = 'none'):
        super().__init__(name,age,gender,hobby)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self):
        for item in self.privileges:
            print(item)