T=int(input())
s=[]
for _ in range(T):
    s.append(input())
curr=list(s[0])
n=len(curr)
d={}
d[''.join(curr)]=0
for i in range(n-1):
    z=curr.pop(0)
    curr.append(z)
    d[''.join(curr)]=0
flag=False
for i in s:
    c=0
    temp=list(i)
    for _ in range(n-1):
        z=temp.pop(0)
        temp.append(z)
        c+=1
        st=''.join(temp)
        if st not in d:
            flag=True
            break
        else:
            d[st]+=c
    if flag:
        print(-1)
        break
else:
    print(min(d.values()))





###########################correct
'''
1. Take input
2. Get all unique rotations
3. Increase vote of each unique rotation
4. for each rotation, also store if all strings contributed
'''


def rotate(word, k):
    new_word = word[k:] + word[:k]
    return new_word

n = int(input())
all_words = []
all_rotations = {}
min_rotations = 10**6
lengths = set()
for case in range(n):
    curr_word = input()
    curr_rotations = set()
    lengths.add(len(curr_word))

    if len(lengths) > 1:
        print(-1)
        exit(0)

    for i in range(0,len(curr_word)):
        rot_word = rotate(curr_word, i)
        #print(rot_word, case)
        if rot_word in curr_rotations:
            continue
        if rot_word in all_rotations:
            all_rotations[rot_word]+=i
        elif case == 0:
            all_rotations[rot_word]=i
            curr_rotations.add(rot_word)
        else:
            #print(rot_word, case, 'caused')
            print(-1)
            exit(0)
        
        if case == n-1:
            min_rotations = min(min_rotations,all_rotations[rot_word])
    
print(min_rotations)