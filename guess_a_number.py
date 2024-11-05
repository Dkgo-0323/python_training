import random
random_number = random.randint(1,10)
for i in range(0,3) :
    x = int(input("please enter a number :"))
    if x > random_number :
        print("输入数字偏大,请重新输入 :")
        continue
    elif x < random_number :
        print("输入数字偏小,请重新输入 :")
        continue
    elif x == random_number :
        print("恭喜你猜对了！")
        break
while x != random_number :
    x = int(input("please enter a number :"))
    if x > random_number :
        print("输入数字偏大,请重新输入 :")
    elif x < random_number :
        print("输入数字偏小,请重新输入 :")
    elif x == random_number :
        print("恭喜你猜对了！")