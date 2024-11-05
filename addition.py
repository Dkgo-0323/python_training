# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:58:23 2024

@author: Dukai
"""

print("This is a calculator.")
print("Give me two number and I'll add them together:")
while True:
    try:
        num1 = int(input("Enter your first number:"))
    except ValueError:
        print("Enter number instead of word.")
        continue
    else:
        while True:
            try:
                num2 = int(input("Enter your second number:"))
            except ValueError:
                print("Enter number instead of word.")
                continue
            else:
                num = num1 + num2
                print(num)
                break