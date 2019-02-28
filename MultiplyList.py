#Omar De La Torre
#2/28/2019

#Muliplies all values in list

def multiplyList(numbers):
    total=1
    for n  in numbers:
        total *= n
    return (total)

n=(1, 5, 3, -8, 10)

print(multiplyList(n))
