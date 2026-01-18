#Best Time to Buy and Sell stock (leetcode 121)
#Return the maximum profit you can achieve from one transaction

def max_profit(prices):
    min_price = float ('inf') #start with very large number
    best_profit = 0           #profit cant be negative so start with 0

    for price in prices:
        #update minimum buying price seen so far
        if price < min_price:
            min_price = price

        #profit if we sell today
        profit_today = price - min_price

        #update best profit
        if profit_today > best_profit:
            best_profit = profit_today

    return best_profit

if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]

    print("Input:", prices1)
    print("Output:", max_profit(prices1))  # 5

    print("Input:", prices2)
    print("Output:", max_profit(prices2))  # 0

