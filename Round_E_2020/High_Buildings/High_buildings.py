t = int(input())
for i in range(t):
    n, a, b, c = map(int,input().split())
    h =[]
    for j in range(a-c,0,-1):
        h.extend([n- j])
    for k in range(c):
        h.extend([n])
    for l in range(b-c):
        h.extend([n-l-1])
    while len(h)<n:
        h.insert(a,1)
    if len(h)==n:
        print("Case #{}: ".format(i+1) + ' '.join(map(str, h)))
    else:
        print("Case #{}: IMPOSSIBLE".format(i+1))