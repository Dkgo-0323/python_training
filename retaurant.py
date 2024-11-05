"""模拟餐馆的类"""
class Restaurant():
    """模拟餐馆"""
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("This name of the restaurant is "+self.name.title()
              +",and the cuisine_type is "+self.cuisine_type+".")
    def open_restaurant(self):
        print(self.name.title()+" is opening.")
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,increment):
        self.number_served += increment