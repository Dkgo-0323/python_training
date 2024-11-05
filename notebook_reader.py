with open('python_notebook.txt') as file_object:
    contents= file_object.read()
    print(contents)

with open ('python_notebook.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

contents = ''
with open ('python_notebook.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    contents += line
    print(line.rstrip())

contents = contents.replace('Python','c++')
print(contents)