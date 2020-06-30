## optimal

P = 10**9 + 7

def get_rank(N):
    limit = 10 # max digits in number
    
    N_arr = [0]*(limit - len(str(N)))
    N_arr.extend(list(map(int, str(N))))

    target_arr = [0]*limit
    
    rank = 0

    if N==0:
        rank = 1
    else:
        for i in range(len(target_arr)):
            if i == (len(target_arr)-1):
                sum_so_far = sum(target_arr[:i])
                for j in range(0,N_arr[i]+1):                    
                    if ((sum_so_far+j) % 5) ==0:
                        rank+=1
                        target_arr[i] = j
            else:
                while(target_arr[i] < N_arr[i]):
                    target_arr[i]+=1
                    rank = rank + 2*(10**(limit-2-i))
    return rank

def get_number(desired_rank):
    limit = 10 # max digits in number

    ans = [0]*limit
    
    curr_rank = 0

    target = desired_rank

    for i in range(len(ans)):
        
        if i == (len(ans)-1)  and curr_rank != desired_rank:
            sum_so_far = sum(ans[:i])
            for j in range(0,10):                    
                if curr_rank == desired_rank:
                    break
                if ((sum_so_far+j) % 5) ==0:
                    curr_rank+=1
                    ans[i]=j
        
        elif i<(len(ans)-1):
            jump = (2*(10**(limit-2-i)))
            possible_increase = target// jump
            
            if target % (2*(10**(limit-2-i))) == 0 and (possible_increase + sum(ans)) %5!=0:
                    possible_increase = max(0, possible_increase-1)
            target = target - ((possible_increase)*(2*(10**(limit-2-i))))
            ans[i] = ans[i] + possible_increase
            if possible_increase > 0:
                curr_rank = curr_rank + possible_increase*(2*(10**(limit-2-i)))
            
        
    
    final_ans = 0

    for i in range(len(ans)):
        final_ans = final_ans*10+ ans[i]

    return final_ans



T = int(input())

for case in range(T):
    N = int(input())
    K = int(input())

    curr_rank = get_rank(N)

    desired_rank = curr_rank+K

    #print(f'desired_rank: {desired_rank}')

    ans = get_number(desired_rank)

    temp_rank = get_rank(ans)
    prev_rank = get_rank(ans-1)

    while temp_rank != desired_rank or prev_rank ==temp_rank:
        if temp_rank > desired_rank or prev_rank==temp_rank:
            ans-=1
        else:
            ans+=1
        temp_rank = get_rank(ans)
        prev_rank = get_rank(ans-1)
    
    print(ans)  
        

''' brute force

T = int(input())

for case in range(T):
    N = int(input())
    K = int(input())

    i = 1
    candidate = N

    while i <= K:
        candidate+=1
        sum_of_digits = sum(map(int, str(candidate)))
        if sum_of_digits %5 == 0:
            i+=1
    
    candidate = candidate % (10**9 + 7)
    print(candidate)
'''