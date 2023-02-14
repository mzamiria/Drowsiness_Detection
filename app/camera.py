import cv2
from model import Awakeness
import numpy as np

#from playsound import playsound
#from threading import Thread



def start_alarm(sound):
    """Play the alarm sound"""
    playsound('alarm.wav')

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
left_eye_cascade = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
right_eye_cascade = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
model = Awakeness("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.count=0
        self.alarm_on=False
        self.alarm_sound = "alarm.wav"

    def __del__(self):
        self.video.release()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):
        _, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray, 1.3, 5)
        
        
        for (x, y, w, h) in faces:
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            left_eye = left_eye_cascade.detectMultiScale(roi_gray)
            right_eye = right_eye_cascade.detectMultiScale(roi_gray)
			
            for (x1, y1, w1, h1) in left_eye:
                cv2.rectangle(roi_color,(x1,y1),(x1+w1,y1+w1),(0,255,0),1)
                eye1 = roi_gray[y1:y1+h1, x1:x1+w1]
                eye1 = cv2.resize(eye1, (86, 86))
                pred1 = model.predict_eye_status(eye1[np.newaxis, :, :, np.newaxis])
                #cv2.putText(frame, pred1, (10, 50), font, 1, (255, 255, 0), 2)
			
            for (x2, y2, w2, h2) in right_eye:
                cv2.rectangle(roi_color,(x2,y2),(x2+w2,y2+w2),(0,255,0),1)
                eye2 = roi_gray[y2:y2+h2, x2:x2+w2]
                eye2 = cv2.resize(eye2, (86, 86))
                pred2 = model.predict_eye_status(eye2[np.newaxis, :, :, np.newaxis])
                #cv2.putText(frame, pred2, (400, 50), font, 1, (255, 255, 0), 2)
                
            if pred1=='Close' and pred2=='Close':
                self.count += 1
                cv2.putText(frame, "Eyes Closed " + str(self.count), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                if self.count >= 20:
                    cv2.putText(frame, "WAKE UP!!!", (200, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                    #if not self.alarm_on:
                         #self.alarm_on = True
                     #play the alarm sound in a new thread
                    #winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
                    #t.daemon = True
                    #t.start()
                    #winsound.PlaySound(None, winsound.SND_PURGE)
                    
		    	
            else:
                cv2.putText(frame, "Eyes Open", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
                self.count = 0

                
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
