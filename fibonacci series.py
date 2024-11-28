num=int(input("enter the limit:"))
x,y=0,1
print(x,y,end=' ')
i=0
while(i<num-2):
    z=x+y
    print(z,end=' ')
    x=y
    y=z
    i=i+1
