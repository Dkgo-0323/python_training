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
class IceCreamStand(Restaurant):
    """模拟冰激凌店"""
    def __init__(self,name,cuisine_type):
        '''
        初始化父类的属性
        初始化冰激凌店的独特之处
        '''
        super().__init__(name,cuisine_type)
        self.flavors = [
            'strawberry',
            'apple',
            'milk',
            'chocola',
            'blueberry',
        ]
    def show_flavors(self) :
        for item in self.flavors :
            print(item)


restaurant = Restaurant("starbucks","coffie")
print(restaurant.name.title())
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant("KFC","fried chicken")
restaurant_1.describe_restaurant()
print("There're "+str(restaurant_1.number_served)+" people have comed here.")
restaurant_1.number_served = 100
print("There're "+str(restaurant_1.number_served)+" people have comed here.")
restaurant_1.set_number_served(211)
print("There're "+str(restaurant_1.number_served)+" people have comed here.")
restaurant_1.increment_number_served(774)
print("There're "+str(restaurant_1.number_served)+" people have comed here.")

icecreamstand = IceCreamStand('Xuexue','icecream')
icecreamstand.describe_restaurant()
icecreamstand.show_flavors()