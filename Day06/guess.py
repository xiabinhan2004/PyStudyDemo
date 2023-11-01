import random

di={
    "十五大":"1997",
    "十六大":"2002",
    "十七大":"2007",
    "十八大":"2012",
    "十九大":"2019"
}
print(list(di.items()))
# ran=random.random
random_key = random.choice(list(di.items()))
print(random_key)
print(random_key[0])
inw=input("year")
while(inw!=random_key[1]):
    inw=input()
    if(inw==random_key[1]):
        break
    else:
        print("wrong")
