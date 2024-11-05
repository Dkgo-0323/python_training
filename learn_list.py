# .append()
# .insert(2,)
# del List[2]
# .pop() 弹出列表末尾的值，并存储起来
# poped_component = List.pop()
# remove()
'''motorcycles = ['honda','yamaha','suzuki','ducati']#define a list
print(motorcycles)
too_expensive = 'ducati'#define a varible
motorcycles.remove(too_expensive)#remove 'ducati' from the list
print(motorcycles)

print("\nA "+ too_expensive.title()+' is too expensive for me.')'''

guests =['Newton','Einstein','Tesla']
message = "would you please have dinner with me?"
print('"'+str(guests[0:])+','+message+'"')
not_coming_guest = guests[0]
print(not_coming_guest+" is not coming.")
# 替换 Newton 为 Gauss
guests[0]='Gauss'
print('\n"'+str(guests[0:])+','+message+'"')
print('Now i have found a much bigger dinner table!')

# 再邀请三位客人（向List里添加三位客人）
guests.insert(0,'strang')
guests.insert(2,'陈雨慧')
guests.append('罗辑')
print('\n"'+str(guests[0:])+','+message+'"')
print('i have invite '+str(len(guests)) + " guests.")

# 弹出（pop）四位客人，并解释原因
print("danm,the dinner table can't be delivered on time,now i can only invite two guests.")
information = "im so sorry to tell you that we have no extra seats here,you can come next time."
poped_guest1=guests.pop()
print('\n"'+poped_guest1+","+information+'"')
poped_guest2=guests.pop()
print('"'+poped_guest2+","+information+'"')
poped_guest3=guests.pop()
print('"'+poped_guest3+","+information+'"')
poped_guest4=guests.pop()
print('"'+poped_guest4+","+information+'"')

# 对剩余客人发出邀请
invitation = "you're still on the list,welcome to dinner!"
print('\n"'+guests[0]+","+invitation+'"')
print('"'+guests[1]+","+invitation+'"')

# 清空（del）列表
del guests[0:]
print(guests)