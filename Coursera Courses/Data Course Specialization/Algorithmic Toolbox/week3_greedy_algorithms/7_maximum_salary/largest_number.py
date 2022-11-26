n =  int(input())
numbers = list(map(str,input().split()))
salary = []
while len(numbers) != 0:
    max_digit = 0
    for digit in numbers:
        a = list(digit)
        b = list(str(max_digit)) #max_digit by default is b
        if int(a[0]) < int(b[0]):
            continue
        elif int(a[0]) == int(b[0]): # go for second digit
            try:
                if int(a[1]) > int(b[1]):
                    max_digit = int(digit)
                elif int(a[1]) == int(b[1]): # go for next digit
                    try:
                        if int(a[2]) < int(b[2]):
                            continue
                        elif int(a[2]) > int(b[2]):
                            max_digit = int(digit)
                        elif int(a[2]) == int(b[2]): # check for last digit 
                            try:
                                if int(b[3]) ==0:#only possible case 1000 for 4 digits
                                     max_digit = digit                             
                            except:
                                pass
                                # max_digit = max(digit,max_digit # case of 100 and 1000                 
                    except:#one of the digits has only2 digits
                        if len(a) > len(b): #a has 3 digits
                            if int(a[2]) > int(b[1]):
                                max_digit = int(digit)
                            else:
                                continue
                        elif len(b) > len(a):
                            if int(b[2]) > int(a[1]):
                                continue
                            elif int(b[2]) < int(a[1]):
                                max_digit = int(digit)
                            
                elif a[1] < b[1]:
                    continue        
            except: #either a or b has only 1 digit 
                if len(a) > len(b):
                    if int(a[1]) > int(b[0]):
                        max_digit = int(digit)
                        continue
                    elif int(a[1]) == int(b[0]):
                        try:
                            if int(a[2]) > int(b[0]):
                                max_digit = int(digit)
                                continue
                        except:
                            continue
                    else:
                        continue # b remains as max_digit
                elif len(b) > len(a):
                    if int(b[1]) > int(a[0]):
                        continue
                    elif int(b[1]) == int(a[0]): #checking if b has 3 numbers
                        try:
                            if int(b[2]) > int(a[0]):
                                pass
                            else:
                                max_digit = int(digit)
                                continue
                        except:
                            continue
                    else:
                        max_digit = int(digit)

        elif a[0] > b[0]:
            max_digit = int(digit)
            
    salary.append(str(max_digit))
    numbers.remove(str(max_digit))

print(''.join(salary))

