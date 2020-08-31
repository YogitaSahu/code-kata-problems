n=int(input())
array=input().split(" ")
size=int(input())
for i in range(n-size):
    if len(array[i:i+size])==size:
       for l in array[i:i+size]:
            if int(l)<0:
              print(l,end=" ")
              break
       else:
           print("0",end=" ")
for i in range(n-size,n):
    if len(array[i:i+size])==size:
       for l in array[i:i+size]:
           if int(l)<0:
              print(l,end="")
              break
       else:
           print("0",end="")
