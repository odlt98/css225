#Omar De La Torre
#2/28/2019

#Function receives list and prints unique elements

def uniqueList(numbers):
    newList=[]
    for n in numbers:
        if n not in newList:
            newList.append(n)
        return newList

x=[1, 2, 2, 3, 3, 3, 7, 4, 3, 10]

print(uniqueList(x))
