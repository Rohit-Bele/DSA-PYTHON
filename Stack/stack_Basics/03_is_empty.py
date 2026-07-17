def check_stack_is_empty(stack):
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("stack is not empty")



stack = []
check_stack_is_empty(stack)

stack.append(10)
check_stack_is_empty(stack)
