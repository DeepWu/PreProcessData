#coding:utf-8

'''
读取图片目录listdir
图片命名rename+random
图片尺寸标准化resize
标签提取label
'''
from PIL import Image
import os
import random
seed = 'abcdefghijklmnopqrstuvwxyz0123456789'
import numpy as np


# 统一重命名照片名
def FileReName(FileType,FilePath):
    type_counter = 0
    filecase_counter = 0
    for filetype in FileType:   #循环扫描image目录下的NanJing、XiAn文件夹
        file_counter = 0
        filecase_counter +=1         #使用数字表示类别 1南京 2 西安
        subfolder = os.listdir(FilePath+str(filetype))
        print(subfolder)   #输出文件夹下所有的文件
        for subclass in subfolder:      #遍历文件夹下所有的文件
            file_counter+=1
            print(file_counter)
            print('file_type:',filetype)
            print('subclass:{0}--{1}'.format(file_counter,subclass))
            print('\n')
            #如果文件目录存在os.rename可以移动文件
            os.rename(FilePath+filetype+'/'+subclass,FilePath+filetype+'/'+str(filecase_counter)+'_'+filetype+'_'+str(file_counter)+'.jpg')


#统一照片的尺寸
def FileResize(Output_folder,FileType,FilePath,Width=512,Height = 512):
    for type in FileType:
        for subclass in os.listdir(FilePath+type):
            img_open = Image.open(FilePath+type+'/'+ subclass)
            # print(img_open)
            convert_RGB = img_open.convert('RGB')
            Resized_img = convert_RGB.resize((Width,Height),Image.BILINEAR)
            Resized_img.save(os.path.join(Output_folder,os.path.basename(subclass)))


# 读取图片返回array数组
def ReadImage(filename,train_floder):
    img = Image.open(train_floder+filename)
    return np.array(img)


#存入图片与标签
def DataSet(train_folder):
    Train_list_img = []        #存储图片的列表
    Train_list_label = []         #存储标签的列表
    for file_img in os.listdir(train_folder):
        file_img_to_array = ReadImage(file_img,train_folder)
        Train_list_img.append(file_img_to_array)
        Train_list_label.append(int(file_img.split('_')[0]))
    # print(Train_list_label)
    # print(Train_list_img)
        '''
        此时存储数据的只是普通列表，需要将其转为numpy数组
        '''
    Train_list_img = np.array(Train_list_img)
    Train_list_label = np.array(Train_list_label)
    print(Train_list_img.shape)


if __name__ == '__main__':
    '''
    定义一些相关常量
    '''
    FileType = ['NanJing','XiAn']
    FilePath = 'image/'
    Output_folder = 'train_data/'
    train_folder = 'train_data/'

    # 批量修改图片名称
    # FileReName(FileType,FilePath)

    # 批量修改图片尺寸
    FileResize(Output_folder,FileType,FilePath)
    DataSet(train_folder)

