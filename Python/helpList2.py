inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

# Get the LENGTH of a list
inventory_len = len(inventory)
print(inventory_len)

# First item in a list
first = inventory[0]
print(first)

# Last item in a list
last = inventory[-1]
print(last)

# Slice of list, from index 2 (item 3) to just before index 6 (item 6)
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

# First 3 items in a list
first_3 = inventory[:3]
print(first_3)

# Count the number of times an item appears in a list
twin_beds = inventory.count('twin bed')
print(twin_beds)

# Sort a list and store it in the same list
inventory.sort()
print(inventory)

# Sort a list and store it in a different list
sorted_list = sorted(inventory)

########################################################################################
# list of pizza toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# list of prices for each kind of pizza
prices = [2, 6, 1, 3, 2, 7, 2]

# The number of toppings options
num_pizzas = len(toppings)
print("We sell "+str(num_pizzas)+ " different kinds of pizza!")

# New list with pizza and price
pizzas = list(zip(prices, toppings))
print(pizzas)

# Sort pizzas, lowest price will be first
pizzas.sort()
print(pizzas)

# Index cheapest and most expensive pizza
cheapest_pizza = pizzas[0]
print(cheapest_pizza)

priciest_pizza = pizzas[-1]
print(priciest_pizza)

# Three cheapest pizzas
three_cheapest = pizzas[0:3]
print(three_cheapest)

# Find the number of $2 pizzas
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#########################################################################################

# Function to double a given item in a list
def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        lst[index] = lst[index]*2
        return lst

# Function test
print(double_index([3, 8, -10, 12], 3))


# Function to test if an item ocurs in a list more than 'n' times
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False
                  
# Test more_than_n function
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# Function to determine which item occurs more
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) > lst.count(item2):
        return item1
    elif lst.count(item2) > lst.count(item1):
        return item2
    elif lst.count(item1) == lst.count(item2):
        return "Same number of occurances"
    else:
        return "Could not determine"

# Function Test
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# Function to find the middle value of the list
# if the list has an even number of elements the average of the two middle items is returned
def middle_element(lst):
    if len(lst)%2 == 1:
        return lst[int(len(lst)/2)]
    elif len(lst)%2 == 0:
        return ((lst[int(len(lst)/2)])+(lst[int(len(lst)/2)-1]))/2
    else:
        return "Middle Element Function Falied"


# Function Test
print(middle_element([5, 2, -10]))
print(middle_element([5, 2, -10, -4, 4, 5]))


# Function to sum the last two elements in a list and append the value to the end of the list
# This repeats three times
def append_sum(lst):
    lst.append(lst[-1]+lst[-2])
    lst.append(lst[-1]+lst[-2])
    lst.append(lst[-1]+lst[-2])
    return lst

# Function Test
print(append_sum([1, 1, 2]))


# Function returns the last value of the larger list
# If the lists are the same size it returns the last value of the first list
def larger_list(lst1, lst2):
    if len(lst1) > len(lst2) or len(lst1) == len(lst2):
        return lst1[-1]
    elif len(lst2) > len(lst1):
        return lst2[-1]
    else:
        return "Larger list function failed"

# Function check
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# Function to combine two lists and sort them
def combine_sort(lst1, lst2):
    lst = lst1 + lst2
    lst.sort()
    return lst

# Function Test
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


# Function to append the size of a list to the end of the list
def append_size(lst):
    lst.append(len(lst))
    return lst

# Function to create a range and skip every 3 numbers goint to 100
def every_three_nums(start):
    if start > 100:
        lst = []
        return lst
    else:
        lst = list(range(start, 101, 3))
        return lst


 ######################################################################################
