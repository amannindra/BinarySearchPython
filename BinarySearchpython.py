def binarySearch(thelist, x, low, high, steps):
    if high >= low:
        mid = (low + high)//2
        if thelist[mid] == x:
            return mid
        elif thelist[mid] < x:
            steps += 1
            return binarySearch(thelist, x, mid-1, high, steps)
        else:
            steps += 1
            return binarySearch(thelist, x, low, mid+1, steps)
    else:
        return -1


thelist = [55, 88, 168, 203, 235, 257, 322, 372, 398,
           585, 626, 702, 711, 746, 782, 783, 805, 945, 983]

steps = 0
x = 711
print(binarySearch(thelist, x, 0, len(thelist)-1, steps))
