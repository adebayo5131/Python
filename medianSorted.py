
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    i = 0
    j = 0
    sortedNums = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sortedNums.append(nums1[i])
            i += 1
        else:
            sortedNums.append(nums2[j])
            j += 1

    while i < len(nums1):
        sortedNums.append(nums1[i])
        i += 1
    while j < len(nums2):
        sortedNums.append(nums2[j])
        j += 1
    mid = len(sortedNums)//2

    if len(sortedNums) % 2 == 0:
        return (sortedNums[mid-1]+sortedNums[mid])/2
    else:
        return sortedNums[mid]


nums1 = [1, 2]
nums2 = [3, 4]

print(findMedianSortedArrays(nums1, nums2))
