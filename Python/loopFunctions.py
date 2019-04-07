# Function counts the number of items divisible by 10 in a list
def divisible_by_ten(nums):
    under_ten = [i for i in nums if i%10 ==0]
    return len(under_ten)

print(divisible_by_ten([20, 25, 30, 35, 40]))



# Function adds the gretting "Hello, " to each name in a list
def add_greetings(names):
    greeting = []
    for i in names:
        greeting.append("Hello, " + i)
    return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))



# Function deletes the even numbers out of the begining of a list
def delete_starting_evens(lst):
    while (len(lst) > 0) and (lst[0]%2 == 0):
        lst = lst[1:]
    return lst



# Function places all of the odd index into a list
def odd_indices(lst):
    new = []
    for i in range(1, len(lst), 2):
        new.append(lst[i])
    return new

print(odd_indices([4, 3, 7, 10, 11, -2]))



# Function takes two lists, bases & powers
# and returns a list of all bases raised to all powers
def exponents(bases, powers):
    raised = []
    for b in bases:
        for p in powers:
            raised.append(b**p)
    return raised

print(exponents([2, 3, 4], [1, 2, 3]))




# Function determines which sum of the lists is greater
# and returns that list. If equal, returns list 1
def larger_sum(lst1, lst2):
    sum1 = sum(lst1)
    sum2 = sum(lst2)
    if sum1 > sum2 or sum1 == sum2:
        return lst1
    elif sum2 > sum1:
        return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))



# Function sums a list until the total goes over 9000
def over_nine_thousand(lst):
    total = 0
    if len(lst) == 0:
        return total
    else:
        for i in lst:
            total += i
            if total > 9000:
               break
    return total

print(over_nine_thousand([8000, 900, 120, 5000]))



# Function returns the max value in a list
def max_num(nums):
    big = nums[0]
    for i in nums:
        if i > big:
            big = i
        else:
            continue
    return big

print(max_num([50, -10, 0, 75, 20]))


#Write your function here
def same_values(lst1, lst2):
    if len(lst1) != len(lst2):
        return "Lists must have same length"
    else:
        i = 0
        indices = []
        while i < len(lst1):
            if lst1[i] == lst2[i]:
                indices.append(i)
            i += 1
    return indices
                                                              
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



# Function tests if list 1 is the same as the reverse of list 2
def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != (lst2[len(lst2) - 1 - i]):
            return False
    return True
                    
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
