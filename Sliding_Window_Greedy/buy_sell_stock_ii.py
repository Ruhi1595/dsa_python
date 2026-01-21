#Best time to Buy and Sell stock II (LeetCode 122)
#Buy and sell multiple times

def max_profit(prices):
    profit = 0

    for i in range(1, len(prices)):
        #if today's price is heigher than yesterday, take the profit
        if prices[i] > prices [i-1]:
            profit += prices[i] - prices[i-1]
    
    return profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print("Input:",prices)
    print("Output:", max_profit(prices)) #7