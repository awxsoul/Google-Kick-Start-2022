from posixpath import split

t=int(input())
for i in range(1,t+1):
    no_p=0
    h_p=1
    index=0
    no_c=[]
    papers=int(input())
    list=input()
    print(f"Case #{i}: ",end="")
    list=list.split()
    for j in list:
        check=0
        j=int(j)
        no_p+=1
        no_c.append(j)
        for k in no_c:
            if k>=h_p:
                check+=1
        if check>=h_p:
            h_p+=1
        print(h_p-1,end=" ")
    print("")

            



