class Solution:
    def MET(self, str):
        # write your method here
        def swap(arr,x,y):
            temp=arr[x]
            arr[x]=arr[y]
            arr[y]=temp
        def permute(arr,l,r):
            if l==r:
                s.append(''.join(arr))
            else:
                for i in range(l,r+1):
                    swap(arr,l,i)
                    permute(arr,l+1,r)
                    swap(arr,l,i)
        arr=list(str)
        n=len(arr)
        s=[]
        permute(arr,0,n-1)
        s.sort()
        return s