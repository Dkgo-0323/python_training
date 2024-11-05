def count_words(file_path):
    '''计算文本文件大约多少单词'''
    try:
        with open(file_path) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry,the file you asked didn't exist."
        print(msg)
    else :
        words = contents.split()
        number = str(len(words))
        print("There're about "+number+" words in the file.")