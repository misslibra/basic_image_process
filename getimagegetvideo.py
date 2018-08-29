import cv2 
import os,time
import numpy as np
# from  VideoCapture import Device
 ############# image to video
imagepath = '/cv/cindy/share_file_conflict/small/'
newvideo_name = "/cv/cindy/share_file_conflict/right.avi"
count = 0
framesize =(1920,1080)# (2448, 3264)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_FPS = 10
newvideo = cv2.VideoWriter(newvideo_name,fourcc,video_FPS,framesize)
for image in sorted(os.listdir(imagepath)):
    img = cv2.imread(imagepath+image)
    img = cv2.resize(img,(1920,1080),interpolation=cv2.INTER_CUBIC)
    # cv2.imwrite("/cv/cindy/METALLIC/rec_ver11/" + str(count) + ".jpg",img1)
    # count +=1
    # cv2.imshow("hi",img1)
    # cv2.waitKey(25)
    # print img.shape
    newvideo.write(img)
newvideo.release() 
print "done"


###############  video to image
# videopath = '/home/westwell/Downloads/1534311097.58.avi'
# videocap = cv2.VideoCapture(videopath)
# res,image = videocap.read()
# imagecount = 10000
# save_path = '/home/westwell/Downloads/cali_1097/' + (videopath.split('/')[-1]).split('.')[0]
# print 'path ', save_path
# os.mkdir(save_path)
# while res:
#     # newimg = cv2.resize(image,(0,0), fx=1.35, fy=1.8)
#     #image = np.rot90(image)
#     cv2.imwrite(save_path + '/' + str(imagecount) + '.jpg', image)
#     imagecount += 1
#     res,image = videocap.read()
# videocap.release()

############# video resize
# videopath = '/cv/cindy/after/1_right.mp4'
# videocap = cv2.VideoCapture(videopath)
# res,image = videocap.read()
# imagecount = 10000
#
# framesize =(1920,1080)# (2448, 3264)
# fourcc = cv2.cv.CV_FOURCC(*'XVID')
# # fourcc = cv2.VideoWriter_fourcc(*'XVID')
# video_FPS = 10
# newvideo_name = '/cv/cindy/after/1_right_1080.avi'
# newvideo = cv2.VideoWriter(newvideo_name,fourcc,video_FPS,framesize)
#
# while res:
#     res,image = videocap.read()
#     if image is not None:
#         newimg = cv2.resize(image,(1920,1080),interpolation=cv2.INTER_LINEAR)
#         # print newimg,newimg.shape
#         # cv2.imshow('hi',image)
#         # cv2.waitKey(30)
#         newvideo.write(newimg)
#
# videocap.release()
# newvideo.release()
# print "done"

###### read from camera
# cap = cv2.VideoCapture(0)
# count = 20000
# # cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,720)
# # cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,1280)
# print 'hihii  ',cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
# while True:
#    ret,img = cap.read()
#    cv2.imshow('hi',img)
#    cv2.waitKey(25)
# #    print img.shape
#    imageR = img[:,0:0.5*img.shape[1],:]
#    imageL = img[:,0.5*img.shape[1]:img.shape[1],:]
#    cv2.imwrite('/cv/cindy/stereo_vision/stereo_camera_module/lena_camera/left_' +str(count) + '.png',imageL)
#    cv2.imwrite('/cv/cindy/stereo_vision/stereo_camera_module/lena_camera/right_' +str(count) + '.png',imageR)
# #    time.sleep(1)
#    count += 1

# cap.release()
# cv2.destroyWindows()


##########   use python method to read image from camera
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from VideoCapture import Device
# import time
# MAX_PIC_NUM = 5
# SLEEP_TIME_LONG = 30
# cam = Device(devnum=0, showVideoWindow=0)
# iNum = 0
# while True:
#     cam.saveSnapshot(str(iNum)+ '.jpg', timestamp=3, boldfont=1, quality=75)
#     time.sleep(SLEEP_TIME_LONG)
#     if iNum == MAX_PIC_NUM:
#         iNum = 0
#     else:
#         iNum += 1
