print("A condition is passed if it is true the statements under if gets executed, if it is false then the statements under else or false condition gets executed")

n = int(input("enter a number\n"))
if n % 2 == 0:
    print(f'{n} is a even number')
else:
    print(f'{n} is a odd number')