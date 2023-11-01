de={}
de={"zhangsan":"1","lisi":"2","wamhwu":3
}
print(de)
de1=dict(zhangsan=1,lisi=2,wangwu=3)
print(de1)
key=["zhangsan","lisi","wangwu"]
value=[1,2,3]
de2=dict(zip(key,value))
print(de2)
get = de2.get("zhangsan")
print(get)
pop = de2.pop("lisi", "error")
print([pop])
print(de2)
popitem = de2.popitem()
print(popitem)

