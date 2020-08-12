from heapq import heappop,heappush,heapify
T=int(input())
for _ in range(T):
    N=int(input())
    Candies=list(map(int,input().split()))
    heapify(Candies)
    
    def minimumtime(A,i):
        time=0
        while(i!=1):
            a=heappop(A)
            b=heappop(A)
            c=a+b
            time+=c
            heappush(A,c)
            i-=1
            
        print(time)
    r=minimumtime(Candies,N)