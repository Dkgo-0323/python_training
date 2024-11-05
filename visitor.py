message = input("Please enter your name here: ")
file_name = 'guest.txt'
with open(file_name,'w') as file_object:
    file_object.write(message.title())