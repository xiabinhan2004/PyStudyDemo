ln=10
for i in range(1,ln+1):
    for j in range(1,ln-i+1):
        print(" ",end="")
    for k in range(1,2*i+1,):
        print(chr(64+k),end="")
    print()


