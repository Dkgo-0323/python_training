from count_words import count_words
alice = r"C:\《Python编程》源代码文件-更新\《Python编程》源代码文件\chapter_10\alice.txt"
little_women = r"C:\《Python编程》源代码文件-更新\《Python编程》源代码文件\chapter_10\little_women.txt"
moby_dict = r"C:\《Python编程》源代码文件-更新\《Python编程》源代码文件\chapter_9\moby_dict.txt"
siddhartha = r"C:\《Python编程》源代码文件-更新\《Python编程》源代码文件\chapter_10\siddhartha.txt"
clasic_books = [alice,little_women,moby_dict,siddhartha]
for book in clasic_books:
    count_words(book)