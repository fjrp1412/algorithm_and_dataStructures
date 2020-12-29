def DPChange(money, coins):
    #Create a array will save the change for the amount of coins in the range from 0 to money
    MinNumCoins = [0]

    for m in range(1, money+1):
        #For default, will be a None value or "infinite"
        MinNumCoins.append(None)


        #For every value between 0 and money, will get the minimum amount of coins to complete that value
        for i in range(0, len(coins)):

            #If m(the number "m" between 0 and money what we want to know minimum change) es equal or higher than the every coin in the array coins
            if(m >= coins[i]):
                #we save the number of coins needed for that coin[i] 
                numCoins = MinNumCoins[m - coins[i]] + 1

                if(not bool(MinNumCoins[m])):
                    MinNumCoins[m] = numCoins
                else:
                    if(numCoins < MinNumCoins[m]):
                        MinNumCoins[m] = numCoins

    return MinNumCoins[money]

if __name__ == "__main__":
    money = 15
    coins = [1, 5, 6]
    print(DPChange(money, coins))

