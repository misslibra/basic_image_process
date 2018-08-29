import os,sys
import cv2
from os.path import join, isfile, split
import numpy as np
import time
# import Image
import PIL
import shutil
    
# ################ Rename image Files
# imagepath = '//cv/cindy/stereo_vision/image/0814_horizon_image/result_image_to_doublecheck/result_left/'
# imageorder = 10000
# # if not os.path.exists(imagepath + 'affined/'):
# #     os.mkdir(imagepath + 'affined/')
# # new_imagepath = imagepath + 'affined/'
# for imagename in sorted(os.listdir(imagepath)):
    
#     print imagename
#    # imname = imagename.split('.')[0]+'.jpg'
# #    newname = util.GenerateFileName(imageorder)
#     new_imname = str(imageorder)+'.jpg'
# #    print imagepath+imname
# #    print new_imagepath+new_imname
#     os.rename(imagepath+imagename,imagepath+new_imname)
#     imageorder+=1    

################## rename  format 
# imagepath = '/cv/Rongqi/digits/LorryNumRegion/image/'
# for imagename in os.listdir(imagepath):
#    new_imname = imagename.split('.')[0]+'.bmp'
#    os.rename(imagepath+imagename,imagepath+new_imname)

############  rename  mat ###############
# imagepath = '/cv/Rongqi/digits/LorryNumRegion/Annotations_later/'
# imageorder = 17485
# for imagename in sorted(os.listdir(imagepath)):
#     # print imagename
#     # print imagename.split('.')[0]
#     new_imname = str(imageorder) + '.xml'
#     os.rename(imagepath+imagename,imagepath+ new_imname)
#     imageorder += 1

############  rename image ###############
# imagepath = '/cv/Rongqi/digits/LorryNumRegion/add_0621/step2/image/'
# annotaionpath = '/cv/Rongqi/digits/LorryNumRegion/add_0621/step2/annotation/'
# imageorder = 23989
# for imagename in sorted(os.listdir(imagepath)):
#     oldimageorder = imagename.split('.')[0]
#     oldanntationorder = oldimageorder + '.mat'
#     # print oldimageorder
#     os.rename(imagepath+imagename,imagepath+ str(imageorder) + '.bmp')
#     os.rename(annotaionpath+oldanntationorder,annotaionpath + str(imageorder) + '.mat')
#     imageorder += 1


############ resize image#############
# imagepath = "/cv/cindy/panorama/test_image/"
# imagesavepath = "/cv/cindy/panorama/test_image_800*600/"
# for imagename in sorted(os.listdir(imagepath)):
    
#     # if imagename[5] == '_':
#     # print imagename[5]
#     image = cv2.imread(imagepath + imagename)
#     print image.shape,imagename
#     # cv2.imshow("hi",image)
#     # cv2.waitKey(30)
#     small = cv2.resize(image,(800,600) ,interpolation=cv2.INTER_LINEAR) 
#     # small = cv2.resize(image, (1296,972),interpolation=cv2.INTER_LINEAR )
#     print small.shape
    
#     # print "done"
#     # print imagesavepath + imagename
#     cv2.imwrite(imagesavepath + imagename,small)


############ resize image in folder loop #############
# all_folder = "/cv/cindy/panorama_old/yancan.6.12.11/mix/"
# imagesavepath = "/cv/cindy/panorama_old/yancan.6.12.11/scale_mix_half_half/"
# for folder in sorted( os.listdir(all_folder) ):
#     print folder
#     os.mkdir(imagesavepath + folder)
#     for imagename in sorted(os.listdir(all_folder + folder + '/')):

#         print imagename
#         # if imagename[5] == '_':
#         # print imagename[5]
#         image = cv2.imread(all_folder + folder + '/' + imagename)
#         print image.shape,imagename
#         # cv2.imshow("hi",image)
#         # cv2.waitKey(30)
#         small = cv2.resize(image,( int(image.shape[1]*0.25),int(image.shape[0]*0.25) ) ,interpolation=cv2.INTER_LINEAR) 
#         # small = cv2.resize(image, (1296,972),interpolation=cv2.INTER_LINEAR )
#         print small.shape
#         # print "done"
#         print imagesavepath + folder + '/' + imagename
#         cv2.imwrite(imagesavepath + folder + '/' + imagename,small)



##########  clip image folder

# imagepath = '/cv/cindy/panorama/panorama0/1520926648073/'

# for image in sorted(os.listdir(imagepath)):
    
#     img = cv2.imread(imagepath+image)
#     print img.shape
#     # img_clip = cv2.resize(img, (0,0), fx=1.15540, fy=1.38440) 
#     img_clip = img[200:,:,:]
#     print img_clip.shape
#     # cv2.imshow("clip",img_clip)
#     # cv2.waitKey(0)
#     # small = cv2.resize(img_clip, (0,0), fx=0.5, fy=0.5) 
#     cv2.imwrite('/cv/cindy/panorama/panorama0/1520926648073_clip/'+image ,img_clip)

##########  clip a image 

# imagepath = '/cv/cindy/lorry_sealing/TEST__IMAGE/1111/new-01.jpg'

# img = cv2.imread(imagepath)
# print img.shape
# img_clip = img[800:2000,0:1200]
# cv2.imwrite("/cv/cindy/lorry_sealing/TEST__IMAGE/1111/clip.jpg",img_clip)

# print img_clip.shape
# img_clip_resize = cv2.resize(img_clip, (0,0), fx=2, fy=2) 
# print img_clip_resize.shape
# # cv2.imshow("clip",img_clip)
# # cv2.waitKey(0)
# cv2.imwrite("/cv/cindy/lorry_sealing/TEST__IMAGE/1111/clip_2.jpg",img_clip_resize)

###########  rotate image 

# imagepath = "/cv/cindy/OpenPano/OpenPano-master/src/test/video_03.14_clip/"
# for imagename in sorted(os.listdir(imagepath)):
#     # print imagename
#     roiimage = cv2.imread(imagepath+imagename)
#     rows = roiimage.shape[0]
#     cols = roiimage.shape[1]
#     print rows,cols
#     M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
#     dst = cv2.warpAffine(roiimage,M,(cols,rows))
#     # cv2.imshow("hi",dst)
#     # cv2.waitKey(1500)
#     cv2.imwrite("/cv/cindy/OpenPano/OpenPano-master/src/test/video_03.14_clip_rotate/" + imagename,dst)


############ rename with order
# impath = '/cv/cindy/container_accuracy/'
# #impath = 'F:/BaiduYunDownload/chengwu/images/rareletters/'
# #    impath = 'F:/BaiduYunDownload/matting2016_7_16/xiaochecherare/rareletters/4/original/'
# #impath='horizontal/notilt/'
# imorder = 30000
# files = [join(a,f) for a,b,c in os.walk(impath) for f in c if isfile(join(a,f)) ]
# #FileNames = [filename for filename in os.listdir(impath) if \
# #os.path.isfile(os.path.join(impath, filename))] 

# for img in files:
#     imgpath, imname = split(img)
#     newname = ''
#     for i in range(5-len(str(imorder))):
#         newname += '0'
#     newname = newname + str(imorder) + '.jpg'
#     os.rename(img,join(imgpath, newname))
#     imorder += 1
#     print join(imgpath, newname)

############ rename with other name logic
# impath = '/cv/cindy/lorry_video_accuracy/clip_video/in/'
# # impath = 'F:/BaiduYunDownload/chengwu/images/rareletters/'
# #    impath = 'F:/BaiduYunDownload/matting2016_7_16/xiaochecherare/rareletters/4/original/'
# #impath='horizontal/notilt/'
# # imorder = 30000
# # files = [join(a,f) for a,b,c in os.walk(impath) for f in c if isfile(join(a,f)) ]
# #FileNames = [filename for filename in os.listdir(impath) if \
# #os.path.isfile(os.path.join(impath, filename))] 

# for img in sorted(os.listdir(impath)):
#     imname = img.split('_')[0] + '_hicindy_' + img.split('_')[2] 
#     # print imname
#     # newname = ''
#     # for i in range(5-len(str(imorder))):
#     #     newname += '0'
#     # newname = newname + str(imorder) + '.jpg'
#     os.rename(impath+img,impath+imname)
#     # imorder += 1
#     # print join(imgpath, newname)

###### scan a image 
# /////  replace
#   // for(int j = 0; j<inputimageMat.rows; j++)     //jpg->height
#   // {
#   // for(int i = 0; i<inputimageMat.cols; i++)       //jpg->width   *inputimageMat.channels()
#   // {     
#   // uchar* temp_ptr  = (uchar*)(inputimageMat.data+j*inputimageMat.step[0]+i*inputimageMat.step[1])  ;
#   // ptrBlue = temp_ptr[0];     
#   //  ptrGreen = temp_ptr[1];      
#   //  ptrRed = temp_ptr[2];          
#   //  ppm << ptrRed << ptrGreen << ptrBlue;     
#   // }}
#   //////////
#   ////// replace 2
#   //  for(int j = 0; j<inputimageMat.rows; j++)     //jpg->height
#   // {
#   // for(int i = 0; i<inputimageMat.cols; i++)       //jpg->width   *inputimageMat.channels()
#   // {     
#   //  ptrBlue = inputimageMat.at<cv::Vec3b>(j,i)[0];     
#   //  ptrGreen = inputimageMat.at<cv::Vec3b>(j,i)[1];      
#   //  ptrRed = inputimageMat.at<cv::Vec3b>(j,i)[2];          
#   //  ppm << ptrRed << ptrGreen << ptrBlue;     
#   // }}
#   ////////replace 3
#     for(int j = 0; j<inputimageMat.rows; j++)     //jpg->height
#   {
#    uchar* temp_ptr = inputimageMat.ptr<uchar>(j);     
#   for(int i = 0; i<inputimageMat.cols; i++)       //jpg->width   *inputimageMat.channels()
#   {     
#       ptrBlue = temp_ptr[3*i];     
#    ptrGreen = temp_ptr[3*i+1];      
#    ptrRed = temp_ptr[3*i+2];         
#    ppm << ptrRed << ptrGreen << ptrBlue;     
#   }}

##############   edge 
    #    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #     sobel_row = cv2.Sobel(image,cv2.CV_64F,0,1)
    #     cv2.imshow("sobel_row", sobel_row)
    #     cv2.waitKey(0)

######### sift -feature point detection

# img = cv2.imread('/cv/cindy/my-save-function/function/stereo_rectify/image_rectyied/clip (copy)/0.png')
# # gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = img
# # sift = cv2.xfeatures2d.SIFT_create()
# sift=cv2.SIFT()
# kp = sift.detect(gray,None)
# print len(kp)
# # print kp
# cv2.drawKeypoints(gray,kp,img)
# cv2.imwrite('/cv/cindy/my-save-function/function/stereo_rectify/image_rectyied/clip (copy)/sift_keypoints_sharp_left.jpg',img)

###############  scale image sature

# imagepath = '/cv/Rongqi/digits/LorryNumRegion/JPEGImages/'
# imagecount=17485
# for image in sorted(os.listdir(imagepath)):
#     img = cv2.imread(imagepath + image)
#     img_scale = (img[:,:,:] * 0.6).astype(int)

#     # cv2.imshow("img",img)
#     # cv2.imshow("img_scale",img_scale)
#     cv2.imwrite('/cv/Rongqi/digits/LorryNumRegion/image/' + str(imagecount) + '.bmp',img_scale)
#     imagecount += 1
#     # cv2.waitKey(0)

###### move a lot of images from a lot of folders

# imagpath = '/cv/cindy/lorry_number_rec/lianyungang/video_clip/'
# image = [os.path.join(dp, f) for dp, dn, fs in os.walk(imagpath) for f in fs]
# # print len(image),image[0]
# count = 10000
# for index in range(len(image)):
#     os.rename(image[index],'/cv/cindy/lorry_number_rec/lianyungang/all_image/' + str(count) + '.png' )
#     count += 1

########### show image
# imagepath = '/cv/cindy/stereo_vision/calibration_rectify/fisheye-stereo-calibration-master/DongHuaFisheyecamera/'
# for image in sorted(os.listdir(imagepath)):
#     print imagepath+image
#     img = cv2.imread(imagepath+image)
#     print img.shape
#     cv2.imshow('hi',img)
#     cv2.waitKey()


####  convert to pgm

# image_path = '/cv/cindy/stereo_vision/image/0814_horizon_image/result_right/'
# for img in sorted(os.listdir(image_path)):
#     img_name = img.split('.')[0]
#     image = Image.open(image_path + img)
#     image.save(image_path + img_name + '.pgm')

# image = Image.open('/cv/cindy/stereo_vision/bob_sugg/depth/libelas/png/10000_left.pgm')
# print image[0]

# ##### split into two images
# imagepath = '/home/westwell/Downloads/cali_1097/1534311097/selcet/'
# savepath = '/home/westwell/Downloads/cali_1097/1534311097/1/'
# for i in os.listdir(imagepath):
#     newname = i.split('.')[0]
#     img = cv2.imread(imagepath+i)
#     print img.shape
#     imageL = img[:,0:0.5*img.shape[1],:]
#     imageR = img[:,0.5*img.shape[1]:img.shape[1],:]

#     print imageL.shape,imageR.shape
    
#     cv2.imwrite(savepath + newname + '_L.png',imageL)
#     cv2.imwrite(savepath + newname + '_R.png',imageR)
    
    # cv2.imshow('image',imageR)
    # cv2.waitKey(0)

#### concat two image
# img_L = ''
# img_R = ''
# full_image = np.concatenate((left_image,right_image),1)

##### rename image
# imagepath = '/cv/cindy/stereo_vision/image_0605/'
# count = 1
# for image in sorted(os.listdir(imagepath)):
#     newname = str(count)+ '_right'  + '.jpg'
#     count += 1
#     print image, newname
#     os.rename(imagepath+image,imagepath+newname)


########### move image  with order
# impath = '/cv/cindy/defect_check/'
# new_impath='/cv/cindy/rename_1219/'
# imorder = 100000
# files = [join(a,f) for a,b,c in os.walk(impath) for f in c if isfile(join(a,f)) ]
# for img in files:
#     newname = str(imorder) + '.jpg'
#     os.rename(img,join(new_impath, newname))
#     imorder += 1

#############  get image according to name
# imagepath = '/cv/cindy/panorama/tianjin_pano_result/pano_imaghe_ver2/'
# savepath = '/cv/cindy/panorama/tianjin_pano_result/pano_result_ver2/'
# files = [join(a,f) for a,b,c in os.walk(imagepath) for f in c if isfile(join(a,f)) ]
# for img in files:
#     panom = img.split('/')[-1].split('.')[0]
#     folder_name = img.split('/')[-2]
#     # print panom
#     if panom == 'panorama':
#         print folder_name ,savepath+folder_name+'.jpg'#,img
#         os.rename(img,savepath+folder_name+'.jpg')

############ get image in folder'folder and rename with folder name
# rootpath = '/cv/cindy/panorama/data/6.25/result0625/right/'
# images = [os.path.join(dp, f) for dp, dn, fs in os.walk(rootpath) for f in fs]
# for img in images:
#     new_name = (img.split('/')[-2])
#     # print img
#     print "111"

#     # new_path = '/cv/cindy/panorama/data/6.25/result_left/'+new_name+'.jpg'
#     os.rename(img,'/cv/cindy/panorama/data/6.25/result_right/'+new_name+'.jpg')

##############move image to folder
imagepath = '/cv/cindy/pics/'
root = '/cv/cindy/1111/'
folder = str(int(1000*time.time() ) )+'/'
if not os.path.exists(root + folder):
    os.mkdir(root + folder)
stone = 0
for index in sorted(os.listdir(imagepath)):
    num = int(index.split('.')[0] )
    # print num,stone
    if (num -stone)<200:
        shutil.move(imagepath+index,root + folder+str(num)+'.jpg')
    else:
        folder = str(int(1000*time.time()) ) + '/'
        if not os.path.exists(root + folder):
            os.mkdir(root + folder)
        shutil.move(imagepath+index,root + folder+str(num)+'.jpg')
        stone += 200
 