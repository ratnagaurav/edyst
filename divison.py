# # optimal, without overflows
 
T = int(input())
 
for case in range(T):
    a,b,c = list(map(int, input().split()))
    
    if b>=a:
        print(-1)
        continue
 
    curr_remainder = c%a
 
    if curr_remainder > b:
        num = c - (curr_remainder-b)
    else:
        num = c - (curr_remainder) - (a-b)
    
    if num <= 0:
        print(-1)
        continue
 
    print(num)
 
    
 
#brute force
# T = int(input())
 
# for case in range(T):
#     a,b,c = list(map(int, input().split()))
 
     
#     Q = (c-b)//a
    
#     if b>=a:
#         print(-1)
#         continue
 
#     x = Q*a + b
#     print(x)
