class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B= nums1,nums2
        tot = len(nums1)+len(nums2)
        half = tot//2
        if len(B)<len(A):
            A,B = B,A
        l,r = 0,len(A)-1
        while True:
            i=(l+r)//2
            j=half-i-2
            if i>=0:
                Aleft = A[i] 
            else:
                Aleft = float('-infinity')
            if (i+1)<len(A):
                Aright = A[i+1]
            else:
                Aright = float('infinity')
            if j>=0:
                Bleft = B[j]
            else:
                Bleft = float('-infinity')
            if (j+1)<len(B):
                Bright = B[j+1]
            else:
                Bright = float('infinity')
            
            if Aleft <= Bright and Bleft <= Aright:
                if tot%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1