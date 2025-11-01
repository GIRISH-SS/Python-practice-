#In while loop as long as condition is True, body of while lopp repeats its execution"

lst = [10, 20, 30, 40, 50]
i = 0
while i<5:
    print(lst[i])
    i = i+1

j = 0
while j<11:
    if j == 10:
        print(j)
    else:
        print(j, end = ",")
    j=j+1

#example Banking application
#when we are not sure about how many iterations must be performed
balance = 15500
min_balance = 500
print("before transaction", balance)
while min_balance < balance:
    balance = balance - 1000 
print("after transaction", balance)

