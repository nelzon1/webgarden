import cv2 as cv

cap = cv.VideoCapture('/dev/video0', cv.CAP_V4L)

fps = cap.get(cv.CAP_PROP_FPS)

# set dimensions
cap.set(cv.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 400)

def snapshot(filename):
    ret,frame = cap.read()
    if ret:
        cv.imwrite(filename,frame)
        print('success. image saved at: ' + filename)

snapshot('test2022.jpg')

# release camera 
cap.release()
