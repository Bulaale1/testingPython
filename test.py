# Python review


# leaner search

def linear_search(myList, target):
    for i in range (len(myList)):
        if myList[i]==target:
            return target
    return 0
print(linear_search([22,15,12,33,45],45))
print('FIZZ, BUZZ, FIZZBUZZ')

# Task: Print numbers from 1 to 30, but:

# Print "Fizz" for multiples of 3

# Print "Buzz" for multiples of 5

# Print "FizzBuzz" for multiples of both
for i in range(1, 31):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    
    print(i, output if output else "")
   