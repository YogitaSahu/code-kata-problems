n=int(input())
inp= input()
l=inp.split(" ")
j=1
for x in l[0:n-1]:
    for i in l[j:n-1]:
        if (int(i)<int(x)):
            print(i,end=" ")
            break
    else:
        print("-1",end=" ")
    j+=1
print("-1",end="")
