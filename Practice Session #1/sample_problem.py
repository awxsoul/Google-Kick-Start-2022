# x to be the no. of test cases
x=int(input())
for i in range(0,x):
    #y is the input of N and M
    y=input()
    y=y.split()
    #z is the input of No, of candies in N bags
    z=input()
    z=z.split()
    #sum is the total no. of candies
    sum=0
    for j in z:
        sum=sum+int(j)
    #a is the candies left after dividing
    a=sum%int(y[1])
    print(f"Case #{i+1}: {a}")