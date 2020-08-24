
n=int(input())
inp=input()
l=inp.split(" ")
s=0
l=[int(x) for x in l]
for x in l:
    s+=x
if s%30==0:
    print("1")
else:
    print("0")
