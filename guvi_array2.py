def sort_key(sort_num,n1):
     for i in range(n1):
        for j in range(i+1,n1):
            a= sort_num[i][1]
            b= sort_num[j][1]
            if a== b:
               if int(sort_num[i][0])>int(sort_num[j][0]):
                   b=sort_num[i]
                   sort_num[i]=sort_num[j]
                   sort_num[j]=b
            else:
                pass
     return(sort_num)

n= int(input())
s= input()
l=s.split(" ")
c={}
for x in l:
    if x not in c:
       c[x]=1
    else:
        c[x]=c[x]+1
sort_num=sorted(c.items(),key= lambda x:x[1])
sort=sort_key(sort_num,len(sort_num))
for x in range(len(sort_num)-1):
    print(sort[x][0],end=" ")
print(sort[len(sort)-1][0],end="")

                   
              

       
    
