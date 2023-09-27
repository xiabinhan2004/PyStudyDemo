flag = input('')
USD='USD'
if flag == USD:
    usd =eval(input('请输入美元数值：'))
    rmb = usd*6.78
    print('转换人民币的数值如下：')
    print("RMB{}".format(rmb))
else:
    rmb = eval(input('请输入人民币数值：'))
    usd = rmb/6.78
    print('转换成美元的数值如下：')
    print('USD{}'.format(usd))