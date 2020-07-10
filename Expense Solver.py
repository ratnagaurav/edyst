try:
    friends=input().split()
    assert len(friends)>=1
    T=int(input())
    d={}
    for i in friends:
        d[i]=0

    for _ in range(T):
        arr=input().split()
        assert len(arr)>=2
        n=len(arr)-1
        amt=int(arr[1])
        assert amt>=0
        share=amt/n
        d[arr[0]]+=amt-share
        for i in arr[2::]:
            d[i]-=share
    for i in friends:
        print(i,"{:.2f}".format(d[i]))
except:
    print("Invalid Input")