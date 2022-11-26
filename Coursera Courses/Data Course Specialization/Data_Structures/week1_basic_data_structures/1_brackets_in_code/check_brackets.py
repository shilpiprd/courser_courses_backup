def IsBalanced(arr,stack):
    openi =['(','{','[']
    closei = [')','}',']']
    for i in range(len(arr)):
        if arr[i] in openi:
            stack.append((arr[i],i)) # ('(',1) 
        elif arr[i] in closei:
            if len(stack) == 0:
                stack.append((arr[i],i))
                return False
            top = stack.pop() #is a tuple, opening bracket('[',1)
            if (arr[i] == ')' and top[0] == '(') or (arr[i] == '}' and top[0] == '{') or (arr[i] == ']' and top[0] =='['):
                pass
            else:
                stack.append((arr[i],i))
                return False
    return len(stack)==0
#driver code
openi = ['(','{','[']
closei = [')','}',']']
stack = []
arr = list(input())
output = IsBalanced(arr,stack)
if (output == False):
    top = stack.pop(-1)
    if top[0] in closei:
        print(top[1]+1)
    elif top[0] in openi:
        print(top[1]+1)
else:
    print('Success')
