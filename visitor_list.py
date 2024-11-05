file_name = 'Visitor_list.txt'
while True:
    message = input('Please enter your name here: ')
    print("Hi,"+message.title()+"!Welcome to visit!")
    with open(file_name,'a') as file_object:
        file_object.write(message.title()+" has visited.\n")