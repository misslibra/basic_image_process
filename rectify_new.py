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
###
# pattern_points = np.zeros((hor*ver,3), np.float32)
# pattern_points[:,:2] = np.mgrid[0:hor,0:ver].T.reshape(-1,2)
# print 'pattern_points  is ',pattern_points
###
# right_imagepath = '/cv/cindy/my-save-function/function/camera_calibration/image/right_select_0719/'
# left_imagepath = '/cv/cindy/my-save-function/function/camera_calibration/image/left_selec_0719/'
# for left_image in sorted(os.listdir(left_imagepath) ):
#     image_order = left_image.split('_')[1]
#     right_image = 'right_' + image_order
#     left_img = cv2.imread(left_imagepath + left_image, cv2.CV_8UC1)
#     right_img = cv2.imread(right_imagepath + right_image, cv2.CV_8UC1)
#     # left_img = left_img[100:1080,:]
#     # right_img = right_img[100:1080,:]
#     # cv2.imshow('clip',left_img)
#     # cv2.waitKey(0)
#     image_size = left_img.shape
#     # print 'image_size ',image_size
#     find_chessboard_flags = cv2.CALIB_CB_ADAPTIVE_THRESH | cv2.CALIB_CB_NORMALIZE_IMAGE | cv2.CALIB_CB_FAST_CHECK
#     left_found, left_corners = cv2.findChessboardCorners(left_img, pattern_size, flags = find_chessboard_flags)
#     right_found, right_corners = cv2.findChessboardCorners(right_img, pattern_size, flags = find_chessboard_flags)
#     if left_found:
#         # cv2.cornerSubPix(left_img, left_corners, (11,11), (-1,-1), (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1))
#         cv2.cornerSubPix(left_img, left_corners, (11,11), (-1,-1), (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01))
#     if right_found:
#         # cv2.cornerSubPix(right_img, right_corners, (11,11), (-1,-1), (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1))
#         cv2.cornerSubPix(right_img, right_corners, (11,11), (-1,-1), (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01))
#     pattern_points = np.zeros((hor*ver,3), np.float32)
#     # pattern_points[:,:2] = np.mgrid[0:hor,0:ver].T.reshape(-1,2)
#     pattern_points[:,:2] = squareSize * np.mgrid[0:hor,0:ver].T.reshape(-1,2)
#     # print 'pattern_points  ======  ',pattern_points
#     if left_found and right_found:
#         img_left_points.append(left_corners)
#         img_right_points.append(right_corners)
#         obj_points.append(pattern_points)
# cv2.imshow("left", left_img)
# cv2.drawChessboardCorners(left_img, pattern_size, left_corners, left_found)
# cv2.drawChessboardCorners(right_img, pattern_size, right_corners, right_found)
# cv2.imshow("left chess", left_img)
# cv2.imshow("right chess", right_img)
# cv2.waitKey(0)
# cv2.imwrite('/cv/cindy/my-save-function/function/camera_calibration/image/test_set/corner_left.png',left_img)
# cv2.imwrite('/cv/cindy/my-save-function/function/camera_calibration/image/test_set/corner_right.png',right_img)
# stereocalib_criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 100, 1e-5)
# stereocalib_flags = cv2.CALIB_FIX_ASPECT_RATIO | cv2.CALIB_ZERO_TANGENT_DIST | cv2.CALIB_SAME_FOCAL_LENGTH | cv2.CALIB_RATIONAL_MODEL | cv2.CALIB_FIX_K3 | cv2.CALIB_FIX_K4 | cv2.CALIB_FIX_K5
# print 'obj_points   ',obj_points
# print 'img_right_points  ',len(img_right_points[0])
# print 'img_left_points  ',len(img_left_points)
# print 'image_size  ',image_size
# stereocalib_retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(obj_points,img_left_points,img_right_points,image_size,criteria = stereocalib_criteria, flags = stereocalib_flags)
# stereocalib_retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(obj_points,img_left_points,img_right_points,image_size)
# print 'R,T',R,T
########## check calibrate
# undistortPoints(imgpt[k], imgpt[k], cameraMatrix[k], distCoeffs[k], Mat(), cameraMatrix[k]);
# computeCorrespondEpilines(imgpt[k], k+1, F, lines[k]);
########## check calibrate
# R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(data["cameraMatrix1"], data["distCoeffs1"], data["cameraMatrix2"], data["distCoeffs2"], (640, 480), data["R"], data["T"], alpha = rectify_scale)
# left_maps = cv2.initUndistortRectifyMap(data["cameraMatrix1"], data["distCoeffs1"], R1, P1, (640, 480), cv2.CV_16SC2)
# right_maps = cv2.initUndistortRectifyMap(data["cameraMatrix2"], data["distCoeffs2"], R2, P2, (640, 480), cv2.CV_16SC2)
############  give value  two 20--verson:0719
# cameraMatrix1 = np.zeros((3,3))
# cameraMatrix1[0] = [2.0473023624434254e+03,0,9.5950000000000000e+02]
# cameraMatrix1[1] = [0,2.0473023624434254e+03,5.3950000000000000e+02]
# cameraMatrix1[2] = [0,0,1]
# distCoeffs1 = np.zeros((5,1))
# distCoeffs1[:,0] = (-1.6260979535494091e-01, -1.2793966915216981e-01, 0, 0,1.6039296247838072e-01)
# cameraMatrix2 = np.zeros((3,3))
# cameraMatrix2[0] = [2.0569245734476654e+03,0, 9.5950000000000000e+02]
# cameraMatrix2[1] = [0,2.0569245734476654e+03,5.3950000000000000e+02]
# cameraMatrix2[2] = [0,0,1]
# distCoeffs2 = np.zeros((5,1))
# distCoeffs2[:,0] = (-8.9995534925558687e-02,-1.2367560970440128e+00, 0, 0,5.1299703197014486e+00)
# R1=np.zeros((3,3))
# R1[0]=[9.9924041135945407e-01, 1.2998565356426853e-02,-3.6737414237580091e-02]
# R1[1]=[-1.3140681273308965e-02,9.9990706990766665e-01, -3.6296066368279251e-03]
# R1[2]=[3.6686820547195964e-02, 4.1096042801585094e-03,9.9931836186012224e-01]
# R2=np.zeros((3,3))
# R2[0]=[9.9963752591935462e-01, 1.1600409478121786e-02,-2.4295005119808116e-02]
# R2[1]=[-1.1506284113485648e-02,9.9992575794511307e-01, 4.0104892208984106e-03]
# R2[2]=[2.4339724725874548e-02, -3.7294902910580208e-03,9.9969678838257625e-01]
# P1=np.zeros((3,4))
# P1[0]=[1.8660780897956606e+03, 0., 1.0831389083862305e+03, 0.]
# P1[1]=[0.,1.8660780897956606e+03, 5.5306327056884766e+02, 0.]
# P1[2]=[ 0., 0., 1.,0.]
# P2= np.zeros((3,4))
# P2[0]=[ 1.8660780897956606e+03, 0., 1.0831389083862305e+03,9.0807842358763282e+03]
# P2[1]=[ 0., 1.8660780897956606e+03,5.5306327056884766e+02, 0]
# P2[2]=[ 0., 0., 1., 0.]
# Q=np.zeros((4,4))
# Q[0]=[1., 0., 0.,-1.0831389083862305e+03]
# Q[1]=[0., 1., 0.,-5.5306327056884766e+02]
# Q[2]=[0., 0., 0., 1.8660780897956606e+03]
# Q[3]=[0.,0., -2.0549745939598107e-01, 0.]

# roi1=46:1804,42:973 
# roi2=96:1783,63:973

###########  give value  two 20--verson:0801 ,time 
# cameraMatrix1 = np.zeros((3,3))
# cameraMatrix1[0] = [ 2.0612748491782340e+03, 0., 9.7260494298560354e+02]
# cameraMatrix1[1] = [0.,2.0612748491782340e+03, 5.0492898062550142e+02]
# cameraMatrix1[2] = [0,0,1]
# distCoeffs1 = np.zeros((8,1))
# distCoeffs1[:,0] = (-1.7679600964030751e-01, -7.9715775683488532e-02, 0., 0., 0.,0., 0., -9.0121821053367829e-02)
# cameraMatrix2 = np.zeros((3,3))
# cameraMatrix2[0] = [2.0612748491782340e+03, 0., 9.7560072473205582e+02]
# cameraMatrix2[1] = [0.,2.0612748491782340e+03, 5.1025043081695418e+02]
# cameraMatrix2[2] = [0,0,1]
# distCoeffs2 = np.zeros((8,1))
# distCoeffs2[:,0] = (-1.7294095658979922e-01, -1.9502355830962248e-01, 0., 0., 0.,0., 0., -7.8963649827716542e-01)
# R1=np.zeros((3,3))
# R1[0]=[9.9906066521470793e-01, -4.5684099196493626e-03,-4.3091958084442300e-02]
# R1[1]=[4.6773994925781819e-03,9.9998611146943039e-01, 2.4287449917332563e-03]
# R1[2]=[4.3080264097752605e-02, -2.6280218899562904e-03,9.9906815800835824e-01]
# R2=np.zeros((3,3))
# R2[0]=[9.9865609858540927e-01, -5.7595283080179183e-03,-5.1505578259431743e-02]
# R2[1]=[5.6292096490419231e-03,9.9998057828494236e-01, -2.6748928276223347e-03]
# R2[2]=[5.1519984053728513e-02, 2.3813623372499352e-03,9.9866912456354751e-01]
# P1=np.zeros((3,4))
# P1[0]=[ 1.8515091427615780e+03, 0., 1.0908555603027344e+03, 0.]
# P1[1]=[ 0.,1.8515091427615780e+03, 5.0684360885620117e+02, 0.]
# P1[2]=[ 0., 0., 1.,0.]
# P2= np.zeros((3,4))
# P2[0]=[ 1.8515091427615780e+03, 0., 1.0908555603027344e+03,-8.7510950740882690e+03]
# P2[1]=[ 0., 1.8515091427615780e+03,5.0684360885620117e+02, 0.]
# P2[2]=[ 0., 0., 1., 0.]
# Q=np.zeros((4,4))
# Q[0]=[1., 0., 0., -1.0908555603027344e+03]
# Q[1]=[0., 1., 0., -5.0684360885620117e+02]
# Q[2]=[0., 0., 0., 1.8515091427615780e+03]
# Q[3]=[0., 0., 2.1157456604989258e-01, 0.]

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
