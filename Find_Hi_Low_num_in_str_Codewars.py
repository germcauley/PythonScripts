def high_and_low(numbers):
    # ...

    myArr =[]
    ans = ""
    for i in numbers.split(" "):
        myArr.append(int(i))
    myArr.sort()
    ans = str(myArr[0]) +" "+ str(myArr[len(myArr)-1])
    return  ans


    # return ans

num = '4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'

print(high_and_low(num))