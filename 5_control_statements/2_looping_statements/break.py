num = int(input("enter a number\n"))
for i in range(2,num+1):
    if num % i == 0:
        break

if i == num:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
