import os, cv2
import numpy as np
import xml.dom.minidom
from numpy.linalg import inv
import time

pattern_size = (9, 6)
obj_points = []
img_left_points = []
img_right_points = []
hor = 9
ver = 6
squareSize = 39
###########  give value  two 94--verson:0814 ,time
cameraMatrix1 = np.zeros((3, 3))
cameraMatrix1[0] = [1.4601622710695899e+03, 0., 9.5060348833584487e+02]
cameraMatrix1[1] = [0., 1.4601622710695899e+03, 5.5663199038169216e+02]
cameraMatrix1[2] = [0, 0, 1]
distCoeffs1 = np.zeros((8, 1))
distCoeffs1[:, 0] = (-4.3354527381228575e-01, 2.5055888546436650e-01, 0., 0., 0., 0., 0., 1.3973155669687001e-01)
cameraMatrix2 = np.zeros((3, 3))
cameraMatrix2[0] = [1.4601622710695899e+03, 0., 9.4928788850847491e+02]
cameraMatrix2[1] = [0., 1.4601622710695899e+03, 5.5388241675440713e+02]
cameraMatrix2[2] = [0, 0, 1]
distCoeffs2 = np.zeros((8, 1))
distCoeffs2[:, 0] = (-4.8047019707585348e-01, 2.9465654272185005e-01, 0., 0., 0., 0., 0., 1.1910267151260959e-01)
R1 = np.zeros((3, 3))
R1[0] = [ 9.9386763972998704e-01, 2.1602849597064586e-02, -1.0844552359056292e-01 ]
R1[1] = [-2.2940118007723338e-02, 9.9967523188538221e-01, -1.1098726985514283e-02]
R1[2] = [1.0817053981254074e-01, 1.3518418701677453e-02, 9.9404043512951201e-01]
R2 = np.zeros((3, 3))
R2[0] = [9.9926322699251602e-01, 2.2362541510237026e-02, -3.1191664234318697e-02]
R2[1] = [-2.1976255951802595e-02, 9.9967817261760861e-01, 1.2672622706437573e-02]
R2[2] = [3.1465017953982023e-02, -1.1977809863317366e-02, 9.9943308165981459e-01]
P1 = np.zeros((3, 4))
P1[0] = [8.9016364173284990e+02, 0., 1.0855335845947266e+03, 0.]
P1[1] = [0., 8.9016364173284990e+02, 5.5919826126098633e+02, 0.]
P1[2] = [0., 0., 1., 0.]
P2 = np.zeros((3, 4))
P2[0] = [8.9016364173284990e+02, 0., 1.0855335845947266e+03, -1.9308716478556665e+05]
P2[1] = [0., 8.9016364173284990e+02, 5.5919826126098633e+02, 0.]
P2[2] = [0., 0., 1., 0.]
Q = np.zeros((4, 4))
Q[0] = [1., 0., 0., -1.0855335845947266e+03]
Q[1] = [0., 1., 0., -5.5919826126098633e+02]
Q[2] = [0., 0., 0., 8.9016364173284990e+02]
Q[3] = [0., 0., 4.6101647549769706e-03, 0.]

# 73==55==1809==980
# 54==41==1805==979

# roi1=73:1809,55:980 
# roi2=54:1805,41:979

# roi1 125  63  1773  963
# roi2 17 50 1777 968
############  give value
# rectify_scale = 1 # 0=full crop, 1=no crop
# R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(cameraMatrix1,distCoeffs1,cameraMatrix2,distCoeffs2,image_size,R,T,alpha = rectify_scale)
###### HARTLEY'S METHOD .use intrinsic parameters of each camera, but compute the rectification transformation directly from the fundamental matrix
# retval, mask = cv2.findFundamentalMat(np.asarray(img_left_points[0]),np.asarray(img_right_points[0]),cv2.FM_8POINT,0,0)
# retval, H1, H2 = cv2.stereoRectifyUncalibrated(np.asarray(img_left_points[0]),np.asarray(img_right_points[0]), retval, image_size)
# # print '===========   R1   =============',R1
# R1 = inv(cameraMatrix1) * H1 * cameraMatrix1
# R2 = inv(cameraMatrix2) * H2 * cameraMatrix2
# # print '===========  new  R1   =============',R1
# R1 = H1
# R2 = H2
# print '==========',H1
# P1 = cameraMatrix1
# P2 = cameraMatrix2
########  Precompute maps for cv::remap()
left_maps = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, R1, P1, (1920, 1080), cv2.CV_16SC2)
right_maps = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2, P2, (1920, 1080), cv2.CV_16SC2)
right_imagepath = '/home/westwell/Downloads/cali_1097/1534311097/right/'
left_imagepath = '/home/westwell/Downloads/cali_1097/1534311097/left/'
count = 10000
debug = True
for left_image in sorted(os.listdir(left_imagepath)):
    image_order = left_image.split('_')[0]
    right_image = image_order + '_R.png'
    left_img = cv2.imread(left_imagepath + left_image, cv2.CV_8UC1)
    right_img = cv2.imread(right_imagepath + right_image, cv2.CV_8UC1)
    print right_imagepath + right_image,left_imagepath + left_image
    left_img = cv2.resize(left_img, (0,0), fx=0.75, fy=0.75)
    right_img = cv2.resize(right_img, (0,0), fx=0.75, fy=0.75)
    print left_img.shape

    start_time = int(1000*time.time())
    left_img_remap = cv2.remap(left_img, left_maps[0], left_maps[1], cv2.INTER_LINEAR)  # cv2.INTER_LANCZOS4
    duration = int(1000*time.time() )- start_time
    print duration,'      ',start_time
    right_img_remap = cv2.remap(right_img, right_maps[0], right_maps[1], cv2.INTER_LINEAR)
    #########################
    # full_image = np.concatenate((left_img_remap, right_img_remap), 1)
    # full_image_crop = full_image[90:960, :]

    # left = full_image_crop[:, 0+40:int(0.5 * full_image_crop.shape[1])-130]
    # right = full_image_crop[:, int(0.5 * full_image_crop.shape[1])+130:-40]
    # left = cv2.resize(left, (0,0), fx=0.5, fy=0.5)
    # right = cv2.resize(right, (0,0), fx=0.5, fy=0.5)
    # print full_image.shape, left.shape, right.shape, ' is full_image shape'
    # if debug:
    #     full_image_crop_cp = cv2.resize(full_image_crop, (0, 0), fx=0.3, fy=0.3)
    #     cv2.imshow('hi', full_image_crop_cp)

    #     # cv2.imshow('hi', full_image_crop[:, 0:int(0.5 * full_image_crop.shape[1])])
    #     # cv2.imshow('hi00', left)
    #     # cv2.imshow('right', full_image_crop[:, int(0.5 * full_image_crop.shape[1]):])
    #     # cv2.imshow('right111', right)
    #     cv2.waitKey()
    ############################
#     the roi region is 169 182  1523  699
#  the roi region is 292 208  1514  706

    left_img_remap = left_img_remap[208:881,292:1692]
    right_img_remap = right_img_remap[208:881, 292:1692]
    # full_image = np.concatenate((left_img_remap, right_img_remap), 1)
    print left_img_remap.shape, right_img_remap.shape
    # print 'left_maps[0] ', left_maps[0]
    # print 'left_maps[1] ', left_maps[1]
    # left = cv2.resize(left_img_remap, (0,0), fx=0.5, fy=0.5)
    # right = cv2.resize(right_img_remap, (0,0), fx=0.5, fy=0.5)
    ###########################

    cv2.imwrite('/home/westwell/Downloads/cali_1097/1534311097/SAVE/' + str(count) + '_left_big.png', left_img_remap)
    cv2.imwrite('/home/westwell/Downloads/cali_1097/1534311097/SAVE/' + str(count) + '_right_big.png', right_img_remap)
    # cv2.imwrite('/cv/cindy/stereo_vision/save/ok/result_1/' + str(count) + '_full.png', full_image)

    count += 1
