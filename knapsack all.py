val=[int(x) for x in input().split()]
wt=[int(x) for x in input().split()]
w=int(input())
n=len(val)
def knapsack(val,wt,w,n):
    if n==0 or w==0:
        return 0
    if wt[n-1]<=w:
        return max(val[n-1]+knapsack(val,wt,w-wt[n-1],n-1),knapsack(val,wt,w,n-1))
    else:
        return knapsack(val,wt,w,n-1)
print(knapsack(val,wt,w,n))

#memoization
val=[int(x) for x in input().split()]
wt=[int(x) for x in input().split()]
w=int(input())
n=len(val)
t=[[-1 for j in range(w+1)] for i in range(n+1)]
def knapsack(val,wt,w,n):
    if n==0 or w==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    if wt[n-1]<=w:
        t[n][w]=max(val[n-1]+knapsack(val,wt,w-wt[n-1],n-1),knapsack(val,wt,w,n-1))
        return t[n][w]
    else:
        t[n][w]=knapsack(val,wt,w,n-1)
        return t[n][w]
print(knapsack(val,wt,w,n))

#top down 
val=[int(x) for x in input().split()]
wt=[int(x) for x in input().split()]
w=int(input())
n=len(val)
t=[[-1 for i in range(w+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(w+1):
        if i==0 or j==0:
            t[i][j]=0
for i in range(1,n+1):
    for j in range(1,w+1):
        if wt[i-1]<=j:
            t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
        else:
            t[i][j]=t[i-1][j]
print(t[n][w])