# SELECTION SORT
"""
In selection sort, you select an element and put that element into its right place.
1) Ascending Order: For every index, you can pick the min element out of the remaining unosorted part and swap with current index.
											or
2) Descending Order: For every index, you can pick the max element out of the remaining unosorted part and swap with current index.


#Space Complexity:  O(1)
#Time complexity: O(n^2) for both best case and worst case since for every pass the algo involves finding the max/min element.

USE CASE: It performs well on small lists/arrays.
"""



#sort the given array in ascending order
arr=[3,1,4,2,5]
n=len(arr)

for i in range(n-1):		  # we go upto n-1 index since if arr upto n-2 is sorted, it means whole array will be sorted.
	min_el=min(arr[i:n])      #find min el from current index to last index
	ind=arr.index(min_el)	  #find index of min element found
	arr[ind],arr[i]=arr[i],arr[ind] #swap min index element with the curr index element
	
print(arr) #result is sorted array

#note: Selection sort is inplace sorting algorithm. It is not stable since the order is not maintained in case of elements having same value.
