nums = [4, 2, 4, 1, 2, 4]

freq = {}

for num in nums:
    freq[num] = freq.get(num,0)+1


for key in freq:
    print(key ,"appears", freq[key],"Times")


nums = [1, 2, 1, 3, 2, 1]

freq = [0] * 4

print("Using List DS")

for num in nums:
    freq[num]+=1

for i in range(1,len(freq)):
    print(i,"appears",freq[i],"Times")


print("character hashing using dictionary")
text = "banana"

freq = {}

for i in text:
    freq[i] = freq.get(i,0)+1

for i in freq:
    print(i,"->",freq[i],end=" ")


print("set")

nums = [4, 2, 4, 1, 2, 4, 5]

seen = set()

for i in nums:
    if i in seen:
        print(i,"found a duplicate.")
        break
    seen.add(i)

nums = [1, 4, 3, 2]
flag = False
seen = set()
for i in nums:
    if i in seen:
        flag=True
        break
    seen.add(i)
print(flag) 


print("Find the first repeated number")

nums = [5, 2, 8, 2, 5]
# Output: 2

seen = set()
result = -1
for i in nums:
    if i in seen:
        result = i
        break
    seen.add(i)

print(result)