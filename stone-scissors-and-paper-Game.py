import random
import time

print("login...")
time.sleep(2)
print("start C:/windows/python3/python.exe")
time.sleep(2)
print("欢迎来到石头剪刀布游戏！")
time.sleep(2)
print("制作者：huang")
玩家选择 = input("请输入你的选择（石头、剪刀、布）：")
选择 = ["石头", "剪刀", "布"]
电脑选择 = random.choice(选择)

if 玩家选择 == 电脑选择:
    time.sleep(3)
    print("你所选的选项和电脑的选择相同，平局")
    print("        *")
    print("       *  *")
    print("       *  *")
    print("       *********")
    print("*******         *")
    print("       ********")
    print("*******         *")
    print("       ********")
    print("                *")
    print("      *********")

    input("按任意键退出游戏...")
elif  (玩家选择 == "石头" and 电脑选择 == "剪刀") or \
     (玩家选择 == "剪刀" and 电脑选择 == "布") or \
     (玩家选择 == "布" and 电脑选择 == "石头"):
    print(f"电脑的选择是：{电脑选择}")
    time.sleep(3)
    print("所以，你赢了！")
    print("        *")
    print("       *  *")
    print("       *  *")
    print("       *********")
    print("*******         *")
    print("       ********")
    print("*******         *")
    print("       ********")
    print("                *")
    print("      *********")

    input("按任意键退出游戏...")
    
else:
    print(f"电脑的选择是：{电脑选择}")
    time.sleep(3)
    print("所以，你输了！")
    print("       *********")
    print("*******         *")
    print("       ********")
    print("*******         *")
    print("       ********")
    print("                *")
    print("      *********")
    print("          *  *")
    print("          *  *")
    print("           *")

    input("按任意键退出游戏...")


