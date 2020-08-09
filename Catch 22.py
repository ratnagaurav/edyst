T=int(input())
for _ in range(T):
    FM,BM,t,FBS,BBS=input().split()
    FM=int(FM)
    BM=int(BM)
    t=int(t)
    FBS=int(FBS)
    BBS=int(BBS)
    state=0
    points=0
    if FM==BM:
        if FM>FBS:
            print(FBS*t,'F')
        else:
            if BM>BBS:
                print(BBS*t,'B')
            else:
                print("No Ditch")
    else:
        while True:
            if state==-BBS:
                print(points*t,'B')
                break

            if state+FM>=FBS:
                if state+FM==FBS:
                    points+=FM
                    print(points*t,'F')
                    break
                else:
                    points+=(FBS-state)
                    print(points*t,'F')
                    break
            state+=FM
            points+=FM
            if state-BM<-BBS:
                points+=abs(state+BBS)
                print(points*t,'B')
                break
            state-=BM
            points+=BM
    