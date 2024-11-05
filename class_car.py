class Car():
    """模拟汽车"""
    def __init__(self,make,model,year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回一个描述性的信息"""
        long_name = str(self.year) +" " +self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        """读取里程数"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """
        更新里程数
        禁止将里程数读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("里程表禁止调回")
    def increace_odometer(self,miles):
        """里程表增加指定的量"""
        if miles >= 0 :
            self.odometer_reading += miles
        else :
            print("里程表禁止调回")
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

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(22)
my_new_car.increace_odometer(100)
my_new_car.read_odometer()