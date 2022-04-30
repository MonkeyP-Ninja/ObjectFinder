import cv2
import cv2.cv2
import numpy as np




img = cv2.imread('images/game.jpg',0)
img_copy=cv2.imread('images/game.jpg',0)
test=cv2.imread('images/game.jpg')

template = cv2.imread('images/Capture.png',0)
w, h = template.shape[::-1]
window_name='Find minions'
cv2.cv2.namedWindow(window_name)
minion_detector=cv2.CascadeClassifier('cascade.xml')

def call(t):
   print(t)






cv2.createTrackbar('Threshold',window_name,75,100,call)




def evaluate(img,color=(0, 255, 0),line=3):
    result = []
    format_coords = []
    rectangles = []

    #use methode to find matching pair
    #cv::TM_SQDIFF = 0
    #cv::TM_SQDIFF_NORMED = 1
    #cv::TM_CCORR = 2
    #cv::TM_CCORR_NORMED = 3
    #cv::TM_CCOEFF = 4
    #cv::TM_CCOEFF_NORMED = 5

    while True:
        newImage = img.copy()
        rgbcopy = test.copy()
        print('e')



        t=cv2.getTrackbarPos('Threshold', window_name)
        threshold = t/100
        result = cv2.matchTemplate(newImage,template,5)

        #make a list from results based on the given threshold

        coords = np.where(result>=threshold)

        format_coords = list(zip(*coords[::-1]))
        rectangles=zip(format_coords)
        rec = []
        for r in rectangles:

                x,y = r[0]
                rectangle=[(x,y),((x+w),(y+h))]
                cv2.rectangle(rgbcopy, rectangle[0],rectangle[1], (0, 255, 0), 3)

        cv2.imshow(window_name, rgbcopy)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break












def evaluateCascade(img,color=(0, 255, 0),line=3):
    result = []
    format_coords = []
    rectangles = []

    #use methode to find matching pair
    #cv::TM_SQDIFF = 0
    #cv::TM_SQDIFF_NORMED = 1
    #cv::TM_CCORR = 2
    #cv::TM_CCORR_NORMED = 3
    #cv::TM_CCOEFF = 4
    #cv::TM_CCOEFF_NORMED = 5

    while True:
        newImage = img.copy()
        rgbcopy = test.copy()
        print('e')



        t=cv2.getTrackbarPos('Threshold', window_name)
        threshold = t/100
        result = minion_detector.detectMultiScale(rgbcopy)

        #make a list from results based on the given threshold

        

        
        
        print(result)
        for r in result:

                x,y,w,h = r
                rectangle=[(x,y),((x+w),(y+h))]
                cv2.rectangle(rgbcopy, rectangle[0],rectangle[1], (0, 255, 0), 2)

        cv2.imshow(window_name, rgbcopy)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('find.jpg',rgbcopy)
            break




evaluate(img,color=(0, 255, 0),line=3)















