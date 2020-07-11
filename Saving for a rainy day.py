T=int(input())
for _ in range(T):
    m=float(input())
    t=int(input())
    r=float(input())
    required=m
    for i in range(t):
        present=required/(1+r/1200) #RA=PA+PA*(R/100)*/(1/12)
        interest=required-present
        required=required+(m-interest)
    val=float("{:.11f}".format(present))
    print(round(val))