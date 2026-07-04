arr = [1, 2, 3, 4, 5, 6]

even_num = 0
odd_num = 0
for i in arr:
    if i%2==0:
        even_num+=1
    else:
        odd_num+=1

print("even : ",even_num)
print("odd : ",odd_num)