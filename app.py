from django.shortcuts import render
from flask import Flask, render_template
# import model as m
import os
import numpy as np
import cv2 as cv
# import numpy as np
from PIL import Image,ImageFilter
import os
import shutil


# def filtermin(im):
#     im="./media/"+im
#     # print(im)
#     # i=Image.open(im)
#     # i.filter(ImageFilter.MinFilter(size=25))
#     # i.save('filteredmin.png')
#     # # shutil.move("filtered.png", "./image_app/templates/images/filtered.png")
#     # shutil.move("filteredmin.png", "./static/filteredmin.png")
#     # print('-------------done------------------')
#     # return('-------------done------------------')

#     cap = cv.VideoCapture(cv.samples.findFile(im))
#     ret, frame1 = cap.read()
#     prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
#     hsv = np.zeros_like(frame1)
#     hsv[..., 1] = 255
#     while(1):
#         ret, frame2 = cap.read()
#         if not ret:
#             print('No frames grabbed!')
#             break
#         next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
#         flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
#         mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
#         hsv[..., 0] = ang*180/np.pi/2
#         hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
#         bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#         # cv.imshow('frame2', bgr)
#         # k = cv.waitKey(30) & 0xff
#         # if k == 27:
#         #     break
#         # elif k == ord('s'):
#         prvs = next
#     cv.imwrite('opticalfb.png', frame2)
#     cv.imwrite('opticalhsv.png', bgr)
#     shutil.move("opticalfb.png", "./static/opticalfb.png")
#     shutil.move("opticalhsv.png", "./static/opticalhsv.png")

    # cv.destroyAllWindows()



def of(im):
    im="./media/"+im
    cap = cv.VideoCapture(cv.samples.findFile(im))
    ret, frame1 = cap.read()
    prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frame1)
    hsv[..., 1] = 255
    i=0
    while(i<20):
        i+=1
        ret, frame2 = cap.read()
        if not ret:
            print('No frames grabbed!')
            break
        next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
        flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang*180/np.pi/2
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
        bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
        prvs = next
        a=str(i)
        ofb=a+'opticalfb.png'
        ohsv=a+'opticalhsv.png'
        ofbs='./static/fb/'+ofb
        ohsvs='./static/hsv/'+ohsv
        cv.imwrite(ofb, frame2)
        shutil.move(ofb, ofbs)
        cv.imwrite(ohsv, bgr)
        shutil.move(ohsv, ohsvs)


def imgvid(image_folder,video_name):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv.VideoWriter(video_name, 0, 5, (width,height))
    for image in images:
        video.write(cv.imread(os.path.join(image_folder, image)))
    cv.destroyAllWindows()
    video.release()






app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('./templates')
app.config['UPLOAD_FOLDER'] =  PEOPLE_FOLDER








# --------------------FUNCTIONS -------------------------------------
@app.route('/of')
def imgfilter():
  x=os.listdir('media')[0]
  of(x)
  i= 'static/fb'
#   v = 'video1.avi'
  v = 'video1.mp4'
  imgvid(i,v)
  i= 'static/hsv'
#   v = 'video2.avi'
  v = 'video2.mp4'
  imgvid(i,v)
  shutil.move("video1.mp4", "./static/video1.mp4")
  shutil.move("video2.mp4", "./static/video2.mp4")
#   shutil.move("video1.avi", "./static/video1.avi")
#   shutil.move("video2.avi", "./static/video2.avi")
  return render_template('./min.html')







if __name__ == '__main__':
  app.run()
