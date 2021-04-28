import os
import cv2

s = 'video.mp4'

vidcap = cv2.VideoCapture(s)

try: 
      
    # creating a folder named data 
    if not os.path.exists("Path"): 
        os.makedirs("Path") 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 


def getFrame(sec):
    name = "Path" + str(count) + ".jpg"
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("Path\\test" + str(count) + ".jpg", image)     # save frame as JPG file
    return hasFrames

sec = 0
frameRate = 0.04 #//it will capture image in each 0.05 second
count=1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    print ('Read a new frame: ', success)

vidcap.release()
cv2.destroyAllWindows()

