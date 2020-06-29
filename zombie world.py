try:
    B,n=[int(x) for x in input().split()]
    zombies=[int(x) for x in input().split()]
    zombies.sort(reverse=True)
    for i in zombies:
        val=(i%2) + (i//2)
        if B>i:
            B=B-val
        else:
            print("NO")
            break
    else:
        print("YES")
except ValueError:
    print("Invalid Input")




