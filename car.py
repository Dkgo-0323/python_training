'''用于模拟普通汽车'''
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