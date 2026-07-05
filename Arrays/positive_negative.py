arr = [-5,10,-2,15,0,-1]

positive = 0
negative = 0
for num in arr:
    if num > 0:
        positive+=1
    elif num < 0:
        negative+=1


print("no of positive : ",positive)
print("no of negative : ",negative)