num = eval(input())
month="0一二三四五六七八九十"
if num<10:
    print(month[num]+"月份")
elif num==11:
    print("十一月份")
else :
    print("十二月份")
