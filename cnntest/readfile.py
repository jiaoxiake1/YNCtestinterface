#!/usr/bin/env python

# # from matplotlib import image as mpimg
# from matplotlib import pyplot as plt
# import numpy as np
# import cv2
# from skimage import io
# from PIL import Image


# f1 = open("../report/image/12.png","rb")
# i = Image.open(r"E:\python_lianxi\webinterface\YNCtestinterface\report\image\12.png")


# img = io.imread(r"E:\python_lianxi\webinterface\YNCtestinterface\report\image\12.png")
# io.imshow(img)

#
# lena = mpimg.imread(r"E:\python_lianxi\webinterface\YNCtestinterface\report\image\12.png")
#
# print(plt.imshow(lena))






# f = open("../report/image/13.txt","rb")
f1 = open("../report/image/12.png","rb")
# # print(f.readlines())
print(f1.readlines())
# print(f1.read(20))

# x = np.fromfile(f1,dtype=np.ubyte)
# plt.imshow(x)
# print(x)



import cv2
import numpy as np
import struct

# print(cv2.__version__)

image = cv2.imread("../report/image/12.png")

#imageClone = np.zeros((image.shape[0],image.shape[1],1),np.uint8)

#image.shape[0]为rows
#image.shape[1]为cols
#image.shape[2]为channels
#image.shape = (480,640,3)
rows = image.shape[0]
cols = image.shape[1]
channels = image.shape[2]

#把图像转换为二进制文件
#python写二进制文件，f = open('name','wb')
#只有wb才是写二进制文件
fileSave = open('patch.bin','wb')
for step in range(0,rows):
    for step2 in range(0,cols):
        fileSave.write(image[step,step2,2])
for step in range(0,rows):
    for step2 in range(0,cols):
        fileSave.write(image[step,step2,1])
for step in range(0,rows):
    for step2 in range(0,cols):
        fileSave.write(image[step,step2,0])
fileSave.close()