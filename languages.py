'''languages = ['javascipt','c','r','python','c++']
message = 'my favorite language is '+ languages[-1]+'.'
print(message)'''

languages = ['javascipt','c','r','python','c++']
for language in languages :
    print('i like '+language)
print('i really like to code\n')
friend_languages = languages[0:]
print('"my favorite languages are:"')
for language in languages:
    print(language)
print('"my friend'+"'s favorite languages are:")
for language in friend_languages:
    print(language)