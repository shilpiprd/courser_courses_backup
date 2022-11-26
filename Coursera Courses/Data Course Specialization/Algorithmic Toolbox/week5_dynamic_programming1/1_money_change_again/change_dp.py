#money denomination problem: doesn't pass all tests
from numpy import inf 
coins = [1,3,4]
def moneyexchange(money,coins):
    min_num_coins = [float(inf)]*(money+1)
    min_num_coins[0] = 0
    for m in range(1,money+1):
        for coin in coins:
            if m>=coin:
                count = min_num_coins[m-coin] + 1
                if count < min_num_coins[m]:
                    min_num_coins[m] = count
    if min_num_coins[money] == float(inf):
        return -1
    return min_num_coins[money]

money = int(input())
value = moneyexchange(money,coins)
print(value)
    
