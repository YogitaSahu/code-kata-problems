n=input()
l=input().split(" ")
d={}
s=[]
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
for x,y in d.items():
    if(y==1 ):
        s.append(x)
s.sort(reverse=True)
for i in range(0,len(s)-1):
    print(s[i],end=" ")
print(s[len(s)-1],end="")
