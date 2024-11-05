message = """
输入1,查询当前余额
输入2,查询当前剩余流量
输入3,查询当前剩余通话
输入0,退出自助查询系统！
"""

flag = 1

while flag :
    number = int(input(message))
    if number == 1 :
        print("当前余额为:  999元")
    elif number == 2 :
        print("当前剩余流量为:  5G")
    elif number == 3 :
        print("当前剩余通话为:  189分钟")
    elif number == 0 :
        print("退出自助查询系统!")
        flag = 0



message1 = """
车次    出发站-到达站   出发时间    到达时间      历时
T40     长春-北京       00:12       12:20       12:08
T298    长春-北京       00:06       10:50       10:44
Z158    长春-北京       12:48       21:06       8:18
Z62     长春-北京       21:58       6:08        8:20
"""

print(message1)

time = {
    "T40" : "00:12",
    "T298" : "00:06",
    "Z158" : "12:48",
    "Z62" : "21:58",
}

train = input("请输入要购买的车次: ")
person = input("请输入乘车人: ")

print("你已购买"+train+"次列车 长春-北京 "+ time[train]+"开,请"
      +person+"尽快换取纸质车票。【铁路客服】")


class Credicard():
    """创建信用卡类"""
    def __init__(self,card,code = 123456) :
        """初始化卡号和密码"""
        self.card = card
        self.code = code
    def reset(self,code):
        """重置密码"""
        self.code = code

card1 = Credicard(4013735633800642)
print(card1.card)
print(card1.code)
card1.reset(200311)
print(card1.code)