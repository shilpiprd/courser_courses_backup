#this code works
n,w = map(int,input().split())
temp = {}
for _ in range(n):
    a,b = map(int,input().split()) #a/b is unit price
    # unit_price = a/b
    unit_price = ("{:.9f}".format(a/b))
    temp[float(unit_price)] = b #unit_price: weight total present of that substance 
    
temp = dict(sorted(temp.items(),reverse = True))
loot = 0
for k,v in temp.items():
    if w!=0:
        if v<=w:
            loot += k * v #taking the entire item
            w-=v
        else: #taking fraction of the item
            loot += w*k
            w = 0
    else:
        break
print("{:.4f}".format(loot))
