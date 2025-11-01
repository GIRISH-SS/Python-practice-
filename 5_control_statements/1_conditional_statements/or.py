num = int(input('enter a number\n'))
if num % 3 == 0 or num % 5 == 0:
    print(f'{num} is divisible by either by 3 or 5')
else:
    print(f'{num} is not divisible by either by 3 or 5')
