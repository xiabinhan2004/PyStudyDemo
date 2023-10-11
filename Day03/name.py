name = input()
if len(name)<=2:
    n=name.replace(name[1],"*")
else:
    n=name.replace(name[1:],"*"*len(name[1:]))
print(n)
