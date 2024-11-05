'''def describe_pet(pet_name,animal_type='dog') :
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='杰克')
describe_pet(animal_type='cat',pet_name='mimi')
describe_pet('金豆')'''

'''def make_shirt(size,sentence='I love python') :
    print("\nThe size of the T-shirt is "+size +".")
    print("It is printed that"+"'"+sentence+"'")

make_shirt('medium',"Forgat all of your fears.")
make_shirt(size='large',sentence='The days roll on they turn to years.')
make_shirt(size='medium')
make_shirt(size='large')'''

'''def describe_city(name,country='中国') :
    print(name +" is in "+country)
describe_city('西安')
describe_city('杭州')
describe_city('NewYork','America')'''

'''def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name,}
    return person
musician = build_person('John','Lennon')
print(musician)'''

'''def city_coutry(city_name,coutry) :
    message='"'+city_name+','+coutry+'"'
    return message
message1=city_coutry('西安','中国')
message2=city_coutry('New York','America')
message3=city_coutry('金边','缅甸')
print(message1)
print(message2)
print(message3)'''

'''def make_album(singer,album,num_of_songs) :
    music_album ={'singer':singer,'album':album}
    if  num_of_songs :
        music_album['num_of_songs']=num_of_songs
    return music_album
message = "(you can quit by entering 'q')"
active = True
while active :
    singer =input("\nPlease enter singer's name :"+message)
    if singer == 'q':
       break
    album =input("\nPlease enter album's name :"+message)
    if album == 'q':
        break
    question =input("\nDo you know the number of the songs in this album?(y/n)")
    if question == 'y' :
        num_of_songs = input("Please enter the number of the songs:"+message)
        if num_of_songs =='q':
            break
    else :
        num_of_songs = 'unknow'    
    album_maked=make_album(singer,album,num_of_songs)
    print('\n'+str(album_maked))
'''
'''
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name+''+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q'at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello,"+formatted_name+"!")'''

'''def greet_users(names) :
    for name in names :
        msg = "hello,"+name.title()+"!"
        print(msg)
username = ['hannah','ty','margot']
greet_users(username)'''

'''def show_magicians(names) :
    for name in names :
        print(name)

def make_great(names,new_names) :
    while names :
        current_names = names.pop()
        new_name = "the Great " + current_names
        new_names.append(new_name)

magicians = ['David','刘谦','yif','简']
great_mgc = []
make_great(magicians[:],great_mgc)
show_magicians(great_mgc)
show_magicians(magicians)'''

'''def make_pizza(*toppings) :
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings :
        print("- "+topping)
make_pizza('pepperroni')
make_pizza('mushrooms','green peppers','extra')'''

'''def build_profile(first,last,**user_info) :
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items() :
        profile[key] = value
    return profile
user_profile = build_profile('天驰','王',
                             location = '李园子',
                             age = 20,
                             专业 = '计算机',)
print(user_profile)'''

'''def make_car(manufacturer,model,**car_info) :
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key,value in car_info.items() :
        car[key] = value
    return car
car = make_car('subaru','outback',
               color = 'blue',
               two_package = True)
print(car)'''

'''from car import *
car_1 = make_car('subaru','outback',
               color = 'blue',
               two_package = True)
print(car_1)'''

#import module_name

#from module_name import fuction_name

#import module_name as m

#from module_name import function_name as f

#from module_name import *

#所有的import 语句都要放在项目开头（除非有注释）