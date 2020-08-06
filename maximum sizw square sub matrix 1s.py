class Solution:
    def maxSubMatrix(self, Arr):
        # write your method here
        m=len(Arr)
        n=len(Arr[0])
        t=[[0 for i in range(n+1)]for j in range(m+1)]
        mx=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if Arr[i-1][j-1] == 1:
                    t[i][j] = 1 + min(t[i][j-1] , t[i-1][j] , t[i-1][j-1])
                    mx = max(mx ,t[i][j])
        return mx
        
        
        