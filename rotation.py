import cv2
import glob 


def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]

    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)

    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    # 返回旋转后的图像
    return rotated


vc = cv2.VideoCapture('1.mp4') #读入视频文件  
c=0  
rval=vc.isOpened()  
#timeF = 1  #视频帧计数间隔频率  
while rval:   #循环读取视频帧  
    c = c + 1  
    rval, frame = vc.read()  
#    if(c%timeF == 0): #每隔timeF帧进行存储操作  
#        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像  
    if rval: 
        frame = rotate(frame,90)
        cv2.imwrite('./1/'+str(c).zfill(8) + '.jpg', frame) #存储为图像  
        cv2.waitKey(1)  
    else:  
        break  
vc.release()  

 
  
fps = 21    #保存视频的FPS，可以适当调整  
  
#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg  
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  
videoWriter = cv2.VideoWriter('saveVideo.avi',fourcc,fps,(360,480))#最后一个是保存图片的尺寸  
imgs=glob.glob('./1/*.jpg')  
for imgname in imgs:  
    frame = cv2.imread(imgname)  
    videoWriter.write(frame)  
videoWriter.release()  
