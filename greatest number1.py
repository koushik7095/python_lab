a=int(input("enter number1:\t"))
b=int(input("enter number2:\t"))
c=int(input("enter number3:\t"))
if a>b and a>c:
    print(a,"is greatest",end="\n")
elif b>a and b>c:
    print(b,"is greatest",end="\n")
elif c>a and c>b:
    print(c,"is greatest",end="\n")
else:
    if a==b and b==c:
        print(f"all a={a},b={b},c={c} are equal")
    elif a==b:
        print("a=b")
    elif b==c:
        print("b=c")
    elif a==c:
        print("a=c")
    else:
        print("try again")
