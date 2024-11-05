from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['Bob'] = 'c'
favorite_languages['DK'] = 'python'
favorite_languages['yuhui'] = 'java'
favorite_languages['kishi'] = 'none'
for name,language in favorite_languages.items():
    message = name.title()+"'s favorite language is "
    message += language.title()
    print(message)