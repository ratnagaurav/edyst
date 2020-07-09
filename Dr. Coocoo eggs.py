class Solution:
    def Met(self, eggs, goal):
        # write your method here
        n=len(eggs)
        t=[[False]*(goal+1)]
        for i in range(1,n+1):
            t.append([True])
        t[0][0]=True
        for i in range(1,n+1):
            for j in range(1,goal+1):
                if eggs[i-1]<=j:
                    t[i].append(t[i-1][j-eggs[i-1]] or t[i-1][j])
                else:
                    t[i].append(t[i-1][j])
        return t[-1][-1]