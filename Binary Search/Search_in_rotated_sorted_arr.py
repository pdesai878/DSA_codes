# arr=[0,1,2,4,5,6,7] this is normal sorted arr
# rotate once: [7,0,1,2,3,4,5,6]
# rotate twice: [6,7,0,1,2,3,4,5]
#.. rotate 4 times=[4,5,6,7,0,1,2]

# how do you search for target element in this rotated sorted arr
# observations: arr inc first--> reaches max --> increases again
# we can call the max element a pivot ele. there are two sorted subarrays 0 to pivot and from pivot+1 to n
# you have to first find pos of pivot element and then apply bs ascending on both ascendinly sorted subarrays

# how do you find position of pivot element?
# observe carefully:  arr= [4,5,6,7,0,1,2]
# 1. if 7 is pivot then elment towards its right is going to be smaller always
# 2. if we are at element 0 and element towards its left is greater, then pos(0)-1 is the pivot index
# 3. lets say we are at element 1:
	# pivot el will never be smaller then any element towards its left.
	# lets compare 1 with start of arr. i.e 4 so, 1<4 where should which direction should we head to find pivot
	  #  left side for finding pivot (remember pivot is the largest el)
# 4. lets say we are at element 5, comapre it with 4, 5>4 so where can we find more greater element?
	# obviously we will head to right side

#note observations 3 & 4 will only come in action if obs 1 & 2 dont apply.


# lets now implement the above observations in form of binary search code
def find_pivot(arr):
	l=0
	r=len(arr)-1
	while l<=r:
		mid=l+(r-l)//2
		# case1
		if mid<len(arr) and arr[mid]>arr[mid+1]:
			return mid
		# case2
		if mid>0 and arr[mid]<arr[mid-1]:
			return mid-1

		# case3
		if arr[mid]<arr[l]:
			r=mid-1 # go to left side to hunt for pivot

		# case4
		else:
			l=mid+1   # if el at mid is greater than leftmost arr el. hunt in search of pivot towards right

	return -1     # if pivot==-1 this means that the arr is sorted and not rotated


def bs(arr,start,end,target):
	l=start
	r=end-1
	while l<=r:
		mid=l+(r-l)//2
		if target<arr[mid]:
			r=mid-1
		else:
			l=mid+1
	return -1

arr=[4,5,6,7,0,1,2]
target=1
pivot=find_pivot(arr)  # index 3
if pivot==-1:  # arr is not rotated
	return bs(arr,0,len(arr)-1,target)
left_search=bs(arr,0,pivot,target) # left search ==> will return -1
if left_search!=-1:  
	return left_search
return bs(arr,pivot+1,len(arr),target) #right search ===> will return 5



