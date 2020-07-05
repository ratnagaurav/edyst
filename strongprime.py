def binary_search(key, arr):
    low = 0
    high = len(arr)-1
    mid = (low+high)//2

    while(high>low):
        if(arr[mid]==key):
            return mid
        if(arr[mid] > key):
            high = mid-1
        elif(arr[mid] < key):
            low = mid+1
        mid = (low+high)//2
    
    return mid
    
    


# take input

Q = int(input())
queries = []

# getting minimum L and max R to construct the primes list

min_L = 1000000 
max_R = 2

for _ in range(Q):
    current_query = list(map(int, input().split()))
    queries.append(current_query)
    curr_L = current_query[0]
    curr_R = current_query[1]

    min_L = min(min_L, curr_L)
    max_R = max(max_R, curr_R)

# construct list between 1 and max_R using sieve

primes_sieve = [True]*(2*max_R+1) # (1 based indexing)

primes_sieve[0] = False
primes_sieve[1] = False
primes_sieve[2] = True

prev = []
strong_primes = []

factor = 2

while(True):
    if(primes_sieve[factor] == False):
        factor+=1
        continue
    for num in range(2*factor, len(primes_sieve), factor):
        primes_sieve[num] = False
    
    if(len(prev)==3):
        prev.pop(0)
    
    prev.append(factor)
    
    if(len(prev)==3):
        low, mid, high = prev
        if(2*mid > (low + high)):
            strong_primes.append(mid)
    
    if(factor > max_R):
        break
    factor+=1


#print(strong_primes)

for q in queries:
    L,R = q[0], q[1]
    
    if R < 11:
        print(0)
        continue


    start_range = 0
    end_range = len(strong_primes)-1

    if(L>strong_primes[0]):
        start_range = binary_search(L, strong_primes)
        if(strong_primes[start_range]<L):
            start_range+=1
    
    if(R<strong_primes[-1]):
        end_range = binary_search(R, strong_primes)
        if(strong_primes[end_range]>R):
            end_range-=1

    #print(start_range,end_range)
    
    print(end_range-start_range+1)






######################################################################################


T=int(input())
arr=[0]*1000001
for i in range(3,1000001,2):
    arr[i]=1

for i in range(3,1000001,2):
    if arr[i]==1:
        for j in range(i*i,1000001,i):
            arr[j]=0
arr[1]=arr[0]=0
arr[2]=1
prime=[]
strong=[]
for i in range(2,1000001):
    if arr[i]==1:
        prime.append(i)
        if i>5:
            if 2*prime[-2]>prime[-3]+prime[-1]:
                strong.append(prime[-2])
for _ in range(T):
    L,R=[int(x) for x in input().split()]
    c=0
    for i in range(L,R+1):
        left=0
        right=len(strong)-1
        mid=(left+right)//2
        while left<=right:
            if i==strong[mid]:
                c+=1
                break
            elif i<strong[mid]:
                right=mid-1
            else:
                left=mid+1
            mid=(left+right)//2
    print(c)




##########################################
T=int(input())
arr=[0]*1000001
for i in range(3,1000001,2):
    arr[i]=1

for i in range(3,1000001,2):
    if arr[i]==1:
        for j in range(i*i,1000001,i):
            arr[j]=0
arr[1]=arr[0]=0
arr[2]=1
prime=[]
strong=[]
for i in range(2,1000001):
    if arr[i]==1:
        prime.append(i)
        if i>5:
            if 2*prime[-2]>prime[-3]+prime[-1]:
                strong.append(prime[-2])
for _ in range(T):
    L,R=[int(x) for x in input().split()]
    c=[]
    for i in [L,R+1]:
        left=0
        right=len(strong)-1
        mid=(left+right)//2
        while left<=right:
            if i==strong[mid]:
                c.append(mid)
                break
            elif i<strong[mid]:
                right=mid-1
            else:
                left=mid+1
            mid=(left+right)//2
        c.append(left)
    print(len(strong[c[0]:c[1]]))




