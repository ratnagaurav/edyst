T=int(input())
for _ in range(T):
    s=input()
    t=input()
    n=len(s)
    k=int(input())
    alpha={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    chk=[] #for storing difference btw s[i] and t[i]
    flag=True
    for i in range(n):
        if s[i]!=t[i]:
            if s[i]<t[i]:
                val=alpha[t[i]]-alpha[s[i]]
                if val not in chk:
                    chk.append(val)
                else:
                    chk.append(26+val)
            else:
                print("No")
                flag=False
                break
    if flag:
        mx=max(chk)
        if mx<=k:
            print("Yes")
        else:
            print('No')

