l=[1,2,3,3,3,34,5,123,1]
l2=l.copy()
print(l2)
l2.reverse()
print(l2)
print(l)
l.sort(reverse=True)
print(l)
s=["dawsa","sajowa","hoa","hsiaow","djiawqew"]
s.sort(key=lambda x1:x1[len(x1)-1])
print(s) 