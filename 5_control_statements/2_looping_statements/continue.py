lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = []
odd_nums = []
for i in lst:
    if not i % 2 == 0:
        odd_nums.append(i)
        continue
    even_nums.append(i)
print(odd_nums)
print(even_nums)


even_nums, odd_nums = 0, 0
n = int(input('enter a number\n'))
for i in range(1, n+1):
    if not i % 2 == 0:
        odd_nums = odd_nums+i
        continue
    even_nums = even_nums+i

print(odd_nums)
print(even_nums)


