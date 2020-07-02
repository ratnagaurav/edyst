class Solution:
    def cntBits(self, A):
        # write your method here
        s=0
        for i in range(32):
            
            a=0
            b=0
            for j in range(len(A)):
                
                if (A[j] & (1<<i)):
                    
                    a+=1
                else:
                    b+=1
            s=s+(2*a*b)
        return s 
           
                
                