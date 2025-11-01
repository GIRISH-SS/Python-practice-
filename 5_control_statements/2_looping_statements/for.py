lst = [10, 20, 30, 40, 50]
for i in lst:
    print(i)

#| Loop Type              | What `i` represents | Example       | Output     |
 
#while                    | Index               | print(lst[i]) | 10, 20, 30 |
#for i in lst             | Value               | print(i)      | 10, 20, 30 |
#for i in range(len(lst)) | Index               | print(lst[i]) | 10, 20, 30 |

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for j in range(2, len(lst)-2):
    print(lst[j])


#range() function
for k in range(4):
    print("python")
print(range(5))
print(list(range(5)))
print(list(range(2, 10))) #2-inclusive 10-exclusive
print(list(range(2,20,2))) #increment
print(list(range(20,1,-2))) #decrement


#example Banking application
#when we are  sure about how many iterations must be performed

balance = 15500
min_balance = 500
print("before transaction", balance)
for i in range(5):
    balance = balance - 1000
print("after transaction", balance)

