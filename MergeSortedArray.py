'''
Given two sorted integer arrays nums1 and nums2, merge nums2
into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2.'''

def merge( nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """  
    j = 0
    for i in range(m,len(nums1)):
        if nums1[i] == 0:
            nums1[i] = nums2[j]
            j+=1
    x =nums1.sort()
    print(x)
    return nums1.sort()

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
print(merge(nums1,m,nums2,n))
