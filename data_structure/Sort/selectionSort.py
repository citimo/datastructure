# 选择排序
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

if __name__ == '__main__':
    mylist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectionSort(mylist)
    print(mylist)
