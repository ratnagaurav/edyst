T=int(input())
for _ in range(T):
    try:
        N=int(input())
        assert (20000 <= N <= 10000000)
        SV=float(input())
        assert (20.00 <= SV <= 10000.00)
        CSV=float(input())
        assert (-2000.00 <= CSV <= 2000.00)
        R=float(input())
        assert (0.01 <= R <= 99.99)
        CR=float(input())
        assert (-10.00 <= CR <= 10.00)

        if CSV<0:
            assert CR<=0

        SVdash=SV-CSV

        Rdash=R-CR

        CV=N*min(SV,SVdash)

        CE=CV * 0.5
        
        CA=(CE * min(Rdash,R))/100
        #rounding part is important
        SVdash = round(SVdash * 100) / 100
        Rdash = round(Rdash * 100) / 100
        CV = round(CV * 100) / 100
        CE = round(CE * 100) / 100
        CA = round(CA * 100) / 100

        assert (20.00 <= SVdash <= 10000.00)

        assert ((0.01 <= Rdash <= 99.99))
        
        print("{:.2f}".format((SVdash)))
        print("{:.2f}".format((Rdash)))
        print("{:.2f}".format((CV)))
        print("{:.2f}".format((CE)))
        print("{:.2f}".format((CA)))
    except:
        print("Invalid Input")
