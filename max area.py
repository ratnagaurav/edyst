class Solution:
    def maxArea(self, A):
        # write your method here
        l=0
        r=len(A)-1
        area=0
        while l<r:
            area=max(area,(r-l)*min(A[l],A[r]))
            if A[l]<A[r]:
                l+=1
            else:
                r-=1
        return area