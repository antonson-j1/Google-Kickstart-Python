'''
Final Solution will be updated soon. This code below is to give you all only a idea on how to solve the question
Thanks
'''

t = int(input())
def column_sum(lst):  
    return list(map(sum, zip(*lst)))

for i in range(t):
    n = int(input())
    er=[]
    div=[]

    for j in range(n):
        er.append([int(x) for x in input().split()])
        div.append([float(er[j][1])/float(er[j][0])])

    flag=0    
    for j in range(n):    
        sum = column_sum(er)
        if sum[0]>=sum[1]:
            print("INDEFINITE")
            break
        else:
            if str(max(div))>=str(1):
                del er[div.index(max(div))]
                del div[div.index(max(div))]
                flag+=1
            else:
                print("done bro {}".format(flag))
                break
        del sum[:]
        