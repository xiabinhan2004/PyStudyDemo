# 结果返回成绩列表
lsCJ = []
while True:
    line = input()
    ls = line.split(",")
    if len(line) == 0:
        break
    elif len(ls) != 5:
        print("最后一行成绩有误，请重新输入改行！！")
    else:
        ls[2] = eval(ls[2])
        ls[3] = eval(ls[3])
        ls[4] = eval(ls[4])
        lsCJ.append(ls)

# 根据成绩输出排名
for line in lsCJ:
    score = line[2] + line[3] + line[4]
    line.append(score)
    lsCjRank = lsCJ.copy()
lsCjRank.sort(key=lambda x: x[5], reverse=True)

# 成绩统计
lsStatCj = []
lx = tuple(zip(*lsCJ))
lsStatCj.append(["最高分", max(lx[2]), max(lx[3]), max(lx[4])])
lsStatCj.append(["最低分", min(lx[2]), min(lx[3]), min(lx[4])])
lsStatCj.append(["平均分", sum(lx[2]) / len(lx[2]), sum(lx[3]) / len(lx[3]), sum(lx[4]) / len(lx[4])])
print("班级成绩排名".center(74, "*"))

# 排名结果输出模块
heads = ["学号", "姓名", "操作系统", "数据结构", "数据库原理", "排名"]
print(heads[0].center(12 - len(heads[0])) + heads[1].center(12 - len(heads[1])) + \
      heads[2].center(12 - len(heads[2])) + heads[3].center(12 - len(heads[3])) + \
      heads[4].center(12 - len(heads[4])) + heads[5].center(12 - len(heads[5])))
rank = 1
for line in lsCjRank:
    print(line[0].center(12) + line[1].center(12 - len(line[1])) + str(line[2]).center(12) + \
          str(line[3]).center(12) + str(line[4]).center(12, " ") + str(rank).center(12, " "))
    rank = rank + 1
print("统计".center(78, "*"))

# 统计结果输出
heads = ["统计项", "操作系统", "数据结构", "数据库原理"]
print("{:^9}\t {:^8}\t {:^8}\t {:^7} ".format(heads[0], heads[1], heads[2], heads[3]))
for line in lsStatCj:
    print("{:^9}\t {:^12.1f}\t {:^12.1f}\t {:^12.1f} ".format(line[0], line[1], line[2], line[3]))