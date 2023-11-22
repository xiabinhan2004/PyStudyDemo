a=input()
t=[]
while(a!=''):
    str=a.split(",")
    sum=eval(str[2])+eval(str[3])+eval(str[4])
    str1=[str[0],str[1],sum,str[2],str[3],str[4]]
    t.append(str1)
    a=input()


t.sort(key=lambda x:x[2],reverse=True)
print(t)

for j in range(3, 6):
    t.sort(key=lambda x:x[j], reverse=True)
    print(t[0][j])
    print(t[len(t)-1][j])
    sum = 0
    for i in range(len(t)):
        sum += eval(t[i][j])
    print(sum/len(t))

    