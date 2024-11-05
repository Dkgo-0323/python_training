'''class Restaurant() :
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self) :
        print("The name of the restaurant is "+self.restaurant_name+"."
              "\nAnd the cuisine type of it is "+self.cuisine_type+".")
    def open_restaurant(self) :
        print(self.restaurant_name+" is opening!Welcome to taste!")
restaurant = Restaurant('KFC','fast food')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant('金拱门','fast food')
restaurant2 = Restaurant('沙县小吃','小吃')
restaurant3 = Restaurant('TACO station','墨西哥菜')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
'''
'''
import make_dic

class User() :
    def __init__(self,first_name,last_name,
                 age,sex,motto) :
        self.full_name = first_name +" "+ last_name
        self.age = age
        self.sex = sex
        self.motto = motto
    def describe_user(self) :
        user_info = make_dic.make_dic(full_name = self.full_name.title(),
                            age = self.age,
                            sex = self.sex.title(),
                            )
        print(user_info)
    def greet_user(self) :
        print("Hi,"+self.full_name+"! I like your motto:"+self.motto)
        print("")
user1 = User('bob','dylan',90,'man',
             'how many roads must a man walk down?before you call him a man.')
user2 = User('ed','sheeran','29','man','loving can hurt sometimes.')
user3 = User('talor','sweeft',30,'female',
             'drop everything now,meet me in the pouring rain.')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
'''

'''class Restaurant() :
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self) :
        print("The name of the restaurant is "+self.restaurant_name+"."
              "\nAnd the cuisine type of it is "+self.cuisine_type+".")
    def open_restaurant(self) :
        print(self.restaurant_name+" is opening!Welcome to taste!")
    def set_number_served(self,number) :
        self.number_served = number
    def incresement_number_served(self,incresement) :
        self.number_served += incresement
restaurant = Restaurant('KFC','fast food')
print(restaurant.number_served)
restaurant.number_served = 20
print(restaurant.number_served)
restaurant.set_number_served(30)
print(restaurant.number_served)
restaurant.incresement_number_served(5)
print(restaurant.number_served)
'''
'''import make_dic
class User() :
    def __init__(self,first_name,last_name,
                 age,sex,motto) :
        self.full_name = first_name +" "+ last_name
        self.age = age
        self.sex = sex
        self.motto = motto
        self.login_attempts = 0
    def describe_user(self) :
        user_info = make_dic.make_dic(full_name = self.full_name.title(),
                            age = self.age,
                            sex = self.sex.title(),
                            )
        print(user_info)
    def greet_user(self) :
        print("Hi,"+self.full_name+"! I like your motto:"+self.motto)
        print("")
    def incease_login_attempts(self) :
        self.login_attempts += 1
    def reset_loging_attempts(self) :
        self.login_attempts = 0
user1 = User('bob','dylan',90,'man',
             'how many roads must a man walk down?before you call him a man.')
attempts = user1.login_attempts
print(attempts)
user1.incease_login_attempts()
user1.incease_login_attempts()
user1.incease_login_attempts()
user1.incease_login_attempts()
user1.incease_login_attempts()
attempts = user1.login_attempts
print(attempts)
user1.reset_loging_attempts()
attempts = user1.login_attempts
print(attempts)'''
