class User():
    '''
    模拟用户的简单尝试
    '''
    def __init__(self,name,age,gender,hobby = 'none'):
        """初始化用户属性"""
        self.name = name
        self.age = age
        self.gender = gender
        self.hobby = hobby
        self.login_attempts = 0
    def describe_user(self):
        """描述用户的基本信息"""
        if self.gender == 'man':
            print("This guy is "+self.name+",the age of him is "+
                  str(self.age)+",he has a hobby,and that is "+self.hobby)
        elif self.gender == 'wommen':
            print("This lady is "+self.name+",the age of him is "+
                  self.age+",he has a hobby,and that is "+self.hobby)
    def greet_user(self):
        """个性化问候"""
        print("Hi,"+self.name+",It's great to meet you!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
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


user_1 = User('Bob',21,'man','playing golf')
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)

admin_1 = Admin('Alice',23,'women','writing code')
admin_1.privileges.show_privileges()