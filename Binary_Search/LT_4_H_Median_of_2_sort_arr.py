class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
                
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2

        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) -1
        while True:
            i = (l+r)//2 #A
            j = half - i - 2

            Aleft = A[i] if i >=0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total%2 :
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            
            elif Aleft < Bright:
                l = i+1
            else:
                r = i-1

def main():
    nums1 = [1,3]
    nums2 = [2,4]
    res = Solution()
    print(res.findMedianSortedArrays(nums1, nums2))

if __name__ == "__main__":
    main()
