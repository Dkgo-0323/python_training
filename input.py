'''car = input("please tell us what car you want to rant:")
print("\nLet me see if i can find you a "+car)'''

'''number =input("Please tell me how many people you are:")
number = int(number)
if number > 8 :
    print("Sorry,we have no seats left.")
else:
    print("Ok,the reservation is done!")'''

'''number = int(input("please enter a number:"))
number = number%10
if number == 0 :
    print("10的整数倍")
else :
    print("bushi")'''

'''current_number = 1
while current_number <=5 :
    print(current_number)
    current_number +=1'''

'''prompt ="\nplease tell me something,and i will repeat it back to you."
prompt += "\nif you wanna stop, just enter 'quit' and that's ok:"
active = True 
while active:
    message = input(prompt)
    if message == "quit" :
        print("quit loop,i'll see you again!")
        break
    else :
        print(message)'''

'''current_number = 0
while current_number <10 :
    current_number += 1
    if current_number %2 == 0 :
        continue
    print(current_number)'''

'''x = 1
while x<= 10 :
    print(x)'''

'''ss=[2,3,6,9,7,1]
for i in ss :
    print(max(ss),end=',')
    ss.remove(max(ss))'''

'''sandwich_orders =['BLT','pastrami','Turkey club','pastrami',
                'Caprese','Grilled Cheese','Reuben','pastrami']
finished_sandwhiches =[]
while sandwich_orders :
    poped_sandwhich=sandwich_orders.pop()
    print("i made your "+poped_sandwhich+' sandwhich.')
    finished_sandwhiches.append(poped_sandwhich)
print("\nhere's finished sandwiches :")
for sandwhich in finished_sandwhiches :
    print(sandwhich)'''

'''sandwich_orders =['BLT','pastrami','Turkey club','pastrami',
    'Caprese','Grilled Cheese','Reuben','pastrami']
finished_sandwhiches = []
while sandwich_orders :
    poped_sandwhich=sandwich_orders.pop()
    if poped_sandwhich == 'pastrami' :
        print('we have no pastrami left.')
    else:
        print("i made your "+poped_sandwhich+' sandwhich.')
    finished_sandwhiches.append(poped_sandwhich)
while 'pastrami' in finished_sandwhiches :
    finished_sandwhiches.remove('pastrami')
print("\nhere's finished sandwiches :")
for sandwhich in finished_sandwhiches :
    print(sandwhich)'''

'''survey = {}
# 设置一个标志，指出调查是否要继续
polling_active = True
while polling_active :
# 提示输入被调查者的名字和回答
    name = input("\nWhat is your name ?") 
    massage ="If you could visit one place in the world,where would you go?"
    reseponse = input(massage)
# 将答卷存储在字典里
    survey[name] = reseponse
# 看看是否有人还要参与调查
    repeat = input("Would you like to let another person respond?(yes/ no)")
    if repeat == "no" :
        polling_active = False
# 调查结束，显示结果
print("\n---poll response---")
for name,reseponse in survey.items() :
    print(name+ "would like to visit "+reseponse)'''

def favorite_book(title) :
    '''介绍自己最喜爱的图书'''
    print("one of my favorite books is "+title.title()+"!")
favorite_book('三体')
