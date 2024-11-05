'''names_of_users = ['admin','kobe','good man','wegame','yuhui']
#del names_of_users[0:]
if names_of_users :
    for name in names_of_users :
        if name == 'admin' :
            print('"hello admin,would you like yo see a status report?"')
        else :
            print('"hello '+ name + ',thank you for logging in again."')
else :
    print('"We need to find some users!"')'''

current_users = ['Admin','KOBE','good mAn','wegame','yuhui']
new_users = ['admin','kobe','godfather','Jay','Mars']
#current_users = [current_user.lower() for current_user in current_users]
current_users1 = []
for current_user in current_users :
    current_users1.append(current_user.lower())
for new_user in new_users :
    if new_user.lower() in current_users1 :
        print("sorry,the name has been used.please choose another.")
    else :
        print("the name has not been used,good job!")
