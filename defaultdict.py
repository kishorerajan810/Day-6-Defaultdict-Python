a,b=map(int,input("enter :").split())
m=[str(input("Enter :")) for i in range(a)]
n=[str(input("enter :")) for j in range(b)]
i,j,count=0,0,0
for i in range(b):
    for j in range(a):
        if(n[i]==m[j]):
            print(j+1,end=" ")
            j+=1
            count+=1
        print("-1")
        print()
    
