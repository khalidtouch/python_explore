# print("Hello main")

# item = "Car"

# if item == "Car":
#     # do something
#     print("This is a car")
# else: 
#     # do something else
#     print("This is definitely not a car")

## LOOPS 

# print("Today is Tuesday")

# while loop and for loop 

# count = 0 # initial
# while count < 100000: # while count is 0,1,2,.......99999
#     print("Today is Tuesday", count + 1)
#     count += 1 # next the count

# i = 0 
# while i < 10:
#     print("This is the", i, "th iteration")
#     i += 1 # i = i + 1, i = i - 1, i = i * 2, i = i / 2, i = i ** 2

## days of the week 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# print(days)

## Today is Monday 
# for each in days: 
#     print("Today is", each)


# for i in range(0,10): # 0 -> in, 10 -> out 
#     print(i)

# i = 0 
# while i < 10: 
#     print(i)
#     i += 1

# print even numbers 
# num = 0 
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#     num += 1

## PRIME NUMBERS 

# check for prime number # a prime number can be divider by 1 and itself (num) 
def is_prime(num): 
    i = 2 
    if(num <= 1):
        return False 
    while i < num:
        if(num % i == 0):
            return False 
        i += 1
    return True 


num = 0 
while num <= 10:
    # divided by itself and 2,3,5,7,11,13,17,19
    if(is_prime(num) == True): 
        print(num) # only run when if is True 
    num += 1

# 1, 2, 3, 4, 5
## ASSIGNMENT 

def ten_multiples_of(num): 
    pass 

def factors_of(num): 
    pass 

