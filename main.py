# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

    # Use a breakpoint in the code line below to debug your script.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("你想输入1华氏度 or 0摄氏度")
    type=input()
    cntin=input()
    tem=cntin[1:]
    if type=="1" :
        c=(float(cntin)-32)/18
        print(c)
    elif type == "0" :
        f=float(cntin)*1.8+32
        print(f)
    else:
        print("error")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
