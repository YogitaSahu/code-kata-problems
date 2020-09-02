n=input()
li=input().split(" ")
s=0
s1=0
minn=int(li[0])
maxx=int(li[0])
for i in li:
    if int(i)>maxx:
        maxx=int(i)
for j in li:
    if int(j)<minn:
        minn=int(j)
for i,j in enumerate(li):
    if (int(j))==minn:
        index2=i
        break
for i,j in enumerate(li):
    if int(j)==maxx:
        index1=i
        break
print(index1-index2)   
