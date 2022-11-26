#stack queries [ optimized ] using auxillary stack Q4
aux_stack = []

def push(aux_stack,a):
    # global stack
    if len(aux_stack) == 0:
        aux_stack.append(a)
    elif aux_stack[-1] < a:
        aux_stack.append(a)
    elif aux_stack[-1] > a:
        aux_stack.append(aux_stack[-1])
        
def pop(aux_stack):
    return aux_stack.pop()

def maxima(aux_stack):
    return aux_stack[-1]

#driver code
q = int(input())
for _ in range(q):
    a = list(input().split())
    # print(a)
    if a[0] == 'push':
        # print(a[0],a[1])
        push(aux_stack,a[1])
    elif a[0] == 'pop':
        pop(aux_stack) #calling the method pop
    elif a[0] == 'max':
        value = maxima(aux_stack)
        print(value)
        
