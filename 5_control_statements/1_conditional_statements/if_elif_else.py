print("when there are multiple condition to be checked we use if_elif_else")

num1 = int(input('enter a number\n'))
num2 = int(input('enter a number\n'))
num3 = int(input('enter a number\n'))

if num1 == num2 == num3:
    print("All are equal")
elif num1 >= num2 and num1 >= num3:
    print("num1 is the largest or tied")
elif num2 >= num1 and num2 >= num3:
    print("num2 is the largest or tied")
else:
    print("num3 is the largest or tied")
