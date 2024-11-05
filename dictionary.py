alien_0 ={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = str(alien_0['points'])
print("you just get"+" "+new_points+" points")

alien_0 ={'x_position':0,'y_position':25,'speed':'slow'}
print("original x_position: "+ str(alien_0['x_position']))
if alien_0['speed'] == 'slow' :
    x_increment = 1
elif alien_0['speed'] == 'medium' :
    x_increment = 2
elif alien_0['speed'] == 'fast' :
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x_position: "+ str(alien_0['x_position']))

yuchen = {'first_name':"yuchen",'last_name':"Han",'age':"18",'city':"Xi'an"}
print(yuchen['first_name'])
print(yuchen['last_name'])
print(yuchen['age'])
print(yuchen['city'])

favorite_number ={'jessie':3,'yuchen':6,'kunge':9,'wegame':233,"help":666}
print("jessie's favorite number is "
      +str(favorite_number['jessie'])
      )
print("yuchen's favorite number is "
      + str(favorite_number['yuchen'])
      )

# 排序后无法恢复
# .sort()
# .sort(reverse=True) 按字母倒序

# 临时排序
# sorted(List)

# reverse the list
# .reverse()

## sort & reverse 是操作列表的方法，直接对原列表操作，sorted是函数，返回的是一个新列表。

tips = {'.sort':'按字母排序',
        '.sort(reverse=True)':'按字母倒叙',
        'sorted(List)':'临时排序',
        '.reverse()':'reverse the list',
        }
print("'.sort':\n"+"    "+tips['.sort'])
print("'.sort(reverse=True)':\n"+"    "+tips['.sort(reverse=True)'])
print("'sorted(List)':\n"+"    "+tips['sorted(List)'])
print("'.reverse()':\n"+"    "+tips['.reverse()']) 

favorite_languages = {
    'yuchen':'javascript',
    'dukai': 'c',
    'hongyuan': 'c++',
    'alsome': 'python',
    'beida' : 'r',
    }
friends =['yuchen','hongyuan']
for name in favorite_languages.keys(): #.keys()可以看成把 dictionary搞成 list of keys了
    print(name.title())
    if name in friends :
        print("Hi!"+name.title()+
              " i see your favorite language is "+
              favorite_languages[name].title()+"!")

# keys_list =sorted(dictionary.keys())

favorite_languages = {
    'yuchen':'javascript',
    'dukai': 'c',
    'hongyuan': 'c++',
    'alsome': 'python',
    'beida' : 'r',
    }
keys_list =sorted(favorite_languages.keys())
print(keys_list)
for name in keys_list:
    print(name)

tips = {'.sort':'按字母排序',
        '.sort(reverse=True)':'按字母倒叙',
        'sorted(List)':'临时排序',
        '.reverse()':'reverse the list',
        }
tips['.items()']='遍历所有的key_value pairs.'
tips['.keys()']='生成一个键列表'
tips['.values()']='生成一个值列表'
tips['set(list)']='生成集合&&去掉重复元素'
for key,value in tips.items():
    print(key+":"+value)

rivers = {
    'nile':'egypt',
    'mississippi':'america',
    'changjiang':'china',
    }
for river in rivers.keys() :
    print("The "+river.title()+
          " runs through "+
          rivers[river].title()+".")
for river in rivers.keys():
    print(river.title())
for country in rivers.values() :
    print(country.title())

favorite_languages = {
    'yuchen':'javascript',
    'dukai': 'c',
    'hongyuan': 'c++',
    'alsome': 'python',
    'beida' : 'r',
    }
friends =['yuchen','hongyuan']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends :
        print("Hi!"+name.title()+
              " i see your favorite language is "+
              favorite_languages[name].title()+"!")
people = ['yuchen','yuhui','tengfei','chouxiang','wegame','dukai']
for name in people :
    if name in set(favorite_languages.keys()) :
        print(name+",thank you for your time!")
    else :
        print(name+",please reseponses us soon!")

alien_0 ={'color':'green','points':5}
alien_1 ={'color':'yellow','points':10}
alien_2 ={'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens :
    print(alien)

for number in range(1,10):
    print(number)

# 创建一个用于存储外星人的空列表
aliens = []
# 创建 30个绿色的外星人
for alien_number in range(30) :
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
# 显示前 5个外星人
for alien in aliens[:5] :
    print(alien)
print('...')
# 显示创建了多少个外星人
print("Total number of aliens :"+str(len(aliens)))

# 创建一个外星人列表
aliens = []
# 创建三十个外星人
for alien_number in range(0,30) :
    alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(alien)
# 改掉前三个为黄色外星人
for alien in aliens[0:3] :
    if alien['color'] == 'green' :
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
# 打印前五个外星人
for alien in aliens[0:5] :
    print(alien)
print('...')
# 改黄色为红色
for alien in aliens[0:5] :
    if alien['color'] == 'yellow' :
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'
# 打印前五个外星人
for alien in aliens[0:5] :
    print(alien)
print('...')

# 存储所点比萨的信息
pizza = {
    'crust':'thick',
    'toppings':['mashrooms','extra cheese'],
    }
# 概述所点的比萨
print("you ordered a " + pizza['crust']+" crust pizza"+
    " with the following toppings :")
for topping in pizza['toppings'] :
    print("\t"+topping)

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'phil':['python','haskell'],
    'edward':['ruby','go'],
    }
for name,languages in favorite_languages.items() :
    if len(languages) == 1 :
        print(name.title()+"'s favorite language is :")
    else :
        print(name.title()+ "'s favorite languages are :")
    for language in languages :
        print("\t"+language.title())

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username,user_info in users.items() :
    print("\nUsername:"+username)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']
    print("\tFull name:"+full_name.title())
    print("\tLocation:"+location.title())

yuchen = {'first_name':"yuchen",'last_name':"Han",'age':"18",'city':"Xi'an"}
print(yuchen['first_name'])
print(yuchen['last_name'])
print(yuchen['age'])
print(yuchen['city'])

people = [{
    'first':'yuchen',
    'last':'han',
    'age':18,
    'city':"xi'an",
    },
    {
    'first':'qiangqiang',
    'last':'wang',
    'age':20,
    'city':'yaoxian',
    },
    {
    'first':'jiaxin',
    'last':'hu',
    'age':19,
    'city':'xianyang',
    }]
for person in people :
    print(person)

mimi = {
    'name':'mimi',
    'variety':'cat',
    'owner':'qiangqiang',
    }
dasheng = {
    'name':'dasheng',
    'variety':'dog',
    'owner':'jiaxin',
    }
kk = {
    'name':'kk',
    'variety':'cat',
    'owner':'jiege',
    }
jack = {
    'name':'jack',
    'variety':'dog',
    'owner':'kaige',
    }
xiaohei = {
    'name':'xiaohei',
    'variety':'dog',
    'owner':'dukai',
    }
pets = [mimi,dasheng,kk,jack,xiaohei]
for pet in pets :
    print(' ')
    for key,value in pet.items():
        print(key+":"+value)

favorite_places = {
    'yuchen':["xi'an","xiqu","wuhan"],
    'qiangqiang':["yaoxian","chengdu","xiyou"],
    'quanzi':['xingzhi','caotang','fanxue'],
    }
for name,places in favorite_places.items():
    print("\nHi!"+name.title()+" i see your favorite places!"+
          "here are they:")
    for place in places :
        print(place.title())

cities = {
    "xi'an":{
        "country":'china',
        "population":1299.6,
        "fact":'it has a long history',
        },
    "new york":{
        "country":'america',
        "population":882.35,
        "fact":'centrer of the world',
        },
    "tokyo":{
        "country":'japan',
        "population":14042127,
        "fact":'capital of japan',
        },
    }
for city,city_dic in cities.items():
    print("\nWhere is "+ city.title() +"?")
    print("It is in "+ city_dic["country"].title())
    print("And the population of "+city.title()+"is "+
          str(city_dic["population"]))
facts =[]
for city_name in cities.keys() : 
    dic_cities=cities[city_name]
    fact=dic_cities["fact"]
    facts.append(fact)
print("\nFollowing are some facts about these three cities:")
for fact in facts :
    print("\t"+fact)