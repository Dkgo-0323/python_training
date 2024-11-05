numbers = []
for i in range(0,5) :
    number = int(input("Enter a number here :"))
    numbers.append(number)
numbers.sort(reverse=True)
print(numbers)
print("\n")


names = ['张三','李四','王五','赵六','王麻子']
print(names)
grades = [100,23,45,60,81]
dic = {}
n = 1
for name in names :
    dic[name] = grades[n - 1]
    n += 1
while True :
    name = input("输入学生姓名查询成绩 :(输入q退出)")
    if name == "q" :
        break
    print(dic[name])
while True :
    entry=input("\n请选择要查询的项目: 平均分/最高分/最低分(输入q退出)")
    if entry == "q" :
        break
    elif entry == '平均分' :
        average = sum(grades) / 5
        print(average)
    elif entry == '最高分' :
        print(max(grades))
    elif entry == '最低分' :
        print(min(grades))