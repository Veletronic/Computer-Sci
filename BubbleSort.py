
def sort():
    MyList = [1,4,6,7,8,9,2]
    for i in range(len(MyList) - 1,0, -1):
        for j in range(i):
            if MyList[j] > MyList[j + 1]:
                Temp = MyList[j]
                MyList[j] = MyList[j + 1]
                MyList[j + 1] = Temp
    return MyList

print (sort())

sort()

