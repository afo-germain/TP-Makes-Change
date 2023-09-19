def make_change(coins, amount):
    # Sort the list of coin denominations in descending order
    coins.sort(reverse=True)
    
    combinations = []
    i=0
    
    while amount!=0 and i<len(coins):
        combination = int(round(amount, 2)//coins[i])
        print(combination, " coins of ", coins[i], "euros")
        combinations.append(combination)
        amount-=coins[i]*combination
        i+=1
    return combinations

def make_change_recursive(coins, amount, combination=None, index=0):
    # Base case: If the amount becomes zero, we've found a valid combination
    if amount == 0:
        if combination:
            print("\nChange:")
            for coin, count in combination.items():
                print(f"{count} coins of {coin} euros")
        else:
            print("No valid change possible")
        return

    # If we've exhausted all denominations or the amount becomes negative, backtrack
    if index >= len(coins) or amount < 0:
        return

    coin = coins[index]

    # Explore using different numbers of the current coin denomination
    for count in range(int(amount // coin) + 1):
        if combination is None:
            combination = {}

        if count > 0:
            combination[coin] = count

        make_change_recursive(coins, amount - count * coin, combination, index + 1)

        if combination.get(coin):
            del combination[coin]

coins = [5, 2, 1, 0.5, 0.2, 0.1, 0.05]
amount = 12.35

# Simple
combinations = make_change(coins, amount)

# Recursive
#make_change_recursive(coins, amount)
