import sys
for i in range(0,3) :
    id = input("请输入身份证号 :")
    if len(id) != 18 :
        print("错误,身份证号必须是18位。")
        continue
    else :
        if not id[0:-1].isdigit() :
            print("错误,非数字。")
            continue
        else :
            break
year = id[6:10]
month = id[10:12]
date = id[12:14]
print("出生日期 :" + year + "年" +
       month + "月" + date + "日")
age = 2023 - int(year)
print("您的年龄是 :" + str(age))
location = {
    11:"北京",
    12:"天津",
    13:"河北",
    14:"山西",
    15:"内蒙古",
    21:"辽宁",
    22:"吉林",
    23:"黑龙江",
    31:"上海",
    32:"江苏",
    33:"浙江",
    34:"安徽",
    35:"福建",
    36:"江西",
    37:"山东",
    41:"河南",
    42:"湖北",
    43:"湖南",
    44:"广东",
    45:"广西",
    46:"海南",
    50:"重庆",
    51:"四川",
    52:"贵州",
    53:"云南",
    54:"西藏",
    61:"陕西",
    62:"甘肃",
    63:"青海",
    64:"宁夏",
    65:"新疆",
    71:"台湾",
    81:"香港",
    82:"澳门",
}
print("您来自于"+location[int(id[:2])]+"。")