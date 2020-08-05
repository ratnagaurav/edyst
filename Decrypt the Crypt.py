T=int(input())
for _ in range(T):
    try:
        encrypt=input().split('||')
        #assert len(encrypt)==2
        arr=input()
        assert len(set(arr))==10
        A=int(encrypt[1][-1])
        pos=encrypt[1][:-1]


        temp=encrypt[0].split('|')
        assert len(temp)==10


        d={}
        for i in temp:
            if len(i)>1:
                val=i[-1]
                for k in i[:-1]:
                    d[k]=int(val)
        for i in pos:
            d[i]+=10
        t=A
        for i in sorted(d,reverse=True):
            d[i]-=t
            t=d[i]
        password=""
        for i in sorted(d):
            password+=arr[d[i]]


        print(password)


    except:
        print(-1)
