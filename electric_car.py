"""用于模拟电动汽车的类"""
from car import Car
class Battery():
    """模拟汽车电瓶"""
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        """打印电瓶容量"""
        print("This car has a "+str(self.battery_size)+"-KW/h battery.")
    def get_range(self):
        """指出续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """
        初始化父类的属性
        同时初始化电动汽车的特有属性
        """
        super().__init__(make,model,year)
        self.battery = Battery()