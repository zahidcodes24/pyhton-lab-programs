def max_profit(prices):
    if not prices:
        return 0
        
    min_price = float('inf')
    max_p = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_p:
            max_p = price - min_price
            
    return max_p

# Test
print(f"Max Profit: {max_profit([7, 1, 5, 3, 6, 4])}") 
# Output: 5 (Buy at 1, sell at 6)