print('Hello world !')
def linear_search(myList, target):
    for i in range (len(myList)):
        if myList[i]==target:
            return target
    return 0
print(linear_search([22,15,12,33,45],45))
