print("Enter two numbers and I'll divide them")
print("(Enter q to quit)")
while True:
    num1 = input("Enter first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter second number: ")
    if num2 == 'q':
        break
    try:
        result = int(num1) / int(num2)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(result)