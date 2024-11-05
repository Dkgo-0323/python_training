file_path = r"C:\《Python编程》源代码文件-更新\《Python编程》源代码文件\chapter_10\pi_million_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:100]+'...')
print(len(pi_string))
birthday = input("Enter your birthday,in the form mmddyy:") 
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")