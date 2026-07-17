s = "hello"

stack = []

for ch in s:
    stack.append(ch)

print(stack)

while(stack):
    print(stack.pop())