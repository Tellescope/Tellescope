from imutils.video import VideoStream 
from imutils import face_utils
import datetime 
import time as t 
import dlib 
import cv2
import imutils
import arbys.py as a

shape_predictor = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)


vs = VideoStream(usePiCamera=True).start() 
t.sleep(2)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF 

    if key == ord("q"):
        break
cv2.destroyAllWindows()
vs.stop()
