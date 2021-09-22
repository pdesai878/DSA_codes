arr=[0,1,2,2,1,0,0,1,1,2]
#task is to sort the array without using any sorting algo

"""
one approach is to get freq of 0,1 and 2. then append 0 till freq0, append 1 till freq1 and append2 till freq2.
this will take O(n) to get freq + O(n) to create sorted array from frequencies. and obv O(n) space.
"""

"""
approach2
single pass O(n) and taking O(1) space

==> assume that mid is unknown area that we must evaluate. if we encounter 0, we know that it would belongs
to the lower end and if we encounter 2, we know that it belongs to the higher end.
Each time we evaluate mid, we apply the logic.
"""

low=0
mid=0
high=len(arr)-1
for el in arr:
    if el==0:
        arr[mid],arr[low]=arr[low],arr[mid]
        low+=1
        mid+=1
    elif el==2:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
        mid+=1
    else:
        mid+=1
print(arr)

