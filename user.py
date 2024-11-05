"""模拟用户的类"""
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