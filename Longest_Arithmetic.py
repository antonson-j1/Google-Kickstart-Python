t = int(input())
for i in range(t):
    n= int(input())
    a= list(map(int, input().split()))
    indiff = a[1] - a[0]
    count=[1]
    for j in range(2,len(a)):
        if a[j]- a[j-1]== indiff:
            count.extend([count[j-2]+1])
        else:
            indiff = a[j]- a[j-1]
            count.extend([1])
    print("Case #{}: {}".format(i+1, max(count)+1))
    del a[:]