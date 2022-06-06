rulers=["Bob","Alice"]
v=["a","e","i","o","u","A","E","I","O","U"]

#t testcases
t=int(input())
for i in range(0,t):
    #k kingdom
    k=input()
    if k[-1]=="y" or k[-1]=="Y":
        print(f"Case #{i+1}: {k} is ruled by nobody.")
    elif k[-1] in v:
        print(f"Case #{i+1}: {k} is ruled by {rulers[1]}.")
    else:
        print(f"Case #{i+1}: {k} is ruled by {rulers[0]}.")