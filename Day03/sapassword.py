stri=input()

for i in stri:
    if ord(i)>=97 and ord(i)<=122:
        # 凯撒密码
        print(chr((ord(i)-97+3)%26+97),end="")
    else:
        print(i,end="")
print()
