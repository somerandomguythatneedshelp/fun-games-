import os
import random

cpunum = random.randint(1, 10)
usernum = int(input("What a silly game! Pick a number between 1-10: "))


if cpunum == usernum:
    print("yay")
else:
    os.remove("C:/Users/Admin/Documents/test") 