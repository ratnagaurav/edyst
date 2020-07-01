from math import gcd

player={'Darrell':0,'Sally':0}
def cal(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm
try:
    N=int(input())
    N=N//2
    for p in range(N):
        name1,l1=input().split()
        l=[int(x) for x in l1.split(',')]
        assert 2<=len(l)<=7
        for num in l:
            assert 1<=num<=100

        ans,name2,answer=input().split()
        if p==0:
            player1=name1
            player2=name2
        #actual val calculation logic
        val=cal(l)
        print(name1+"'s","question is :",l1)
        if answer=="PASS":
            print("Question is PASSed")
            print("Answer is:",val)
            print(name2+':',"0points")
        else:
            if int(answer)==val:
                print("Correct Answer")
                print(name2+":","10points")
                player[name2]+=10
            else:
                print("Incorrect Answer")
                print(name2+":","0points")

        if p==N-1:
            print("Total Points:")
            print(player1+':',str(player[player1])+"points")
            print(player2+':',str(player[player2])+"points")
            if player['Darrell']>player['Sally']:
                print("Game Result: Darrell is winner")
            elif player['Sally']>player['Darrell']:
                print("Game Result: Sally is winner")
            else:
                print("Game Result: Draw")
except:
    print("Invalid Input")



