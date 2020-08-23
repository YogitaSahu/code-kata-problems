n= int(input())
l=[]
s=0
inp=input()
l=inp.split(" ")
for i in range(n):
    if l[i] in l[i+1:n]:
        print(l[i])
    else:
        s=s+1
if s==n:
    print("-1")
