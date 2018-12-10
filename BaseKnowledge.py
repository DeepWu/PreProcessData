import os
import random
seed = 'abcdefghijklmnopqrstuvwxyz0123456789'


#自定义名字:方法一
random_name = []
for i in range(7):
    choice = random.choice(seed)   #随机选择一个字母或者数字
    random_name.append(choice)   #此时random_name为列表
    # print(random_name)
print(''.join(random_name))

# # 自定义名字：方法二
# random_name2 = ''.join([name2 for name2 in random.sample(seed,6)]) #random.sample可以从种子中取指定数量的字母数字
# print(random_name2)
#
# #自定义名字：方法三
# random_name3 = random.randint(1,10000)
# print(random_name3)


# 获取路径中文件名
path = 'C:\\User\Administrator\Desktop\PreProcessData\image\\2.png'
print(os.path.basename(path))


#文件名的分割
file = '2.png'
print(file.split('.')[0])