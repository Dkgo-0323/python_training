# 排序后无法恢复
# .sort()
# .sort(reverse=True) 按字母倒序

# 临时排序
# sorted(List)

# reverse the list
# .reverse()

## sort & reverse 是操作列表的方法，直接对原列表操作，sorted是函数，返回的是一个新列表。

coutries = ['china','american','thailand','japan','uk']
print(coutries)
print(sorted(coutries))
print(coutries)
print(sorted(coutries,reverse=True))
print(coutries)
coutries.reverse()
print(coutries)
coutries.reverse()
print(coutries)
coutries.sort()
print(coutries)
coutries.sort(reverse=True)
print(coutries)