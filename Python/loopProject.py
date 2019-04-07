# List of hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Prices of hairstyles
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Number of each hairstyle purchased the previous week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Find Average Prices of Haircuts
total_price = 0

for i in prices:
    total_price += i
        
average_price = total_price/len(prices)

print("Average Haircut Price")
print(average_price)


# Subtract 5 dollars from the price of each haircut
new_prices = [i-5 for i in prices]
print(new_prices)

# Find the average daily revenue from the previous week
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i]*last_week[i]
                
print("Total Revenue: " +str(total_revenue))

average_daily_revenue = total_revenue/7

# List of all haircuts priced under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print(cuts_under_30)
