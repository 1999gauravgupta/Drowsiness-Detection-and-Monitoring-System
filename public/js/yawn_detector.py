import cv2
import dlib
import numpy as np
import warnings
import imutils
import threading
from threading import Thread
import playsound
from scipy.spatial import distance as dist
from imutils import face_utils
import time
from tkinter import *
import socket
from datetime import datetime
import drowsiness
import fetch_data

warnings.simplefilter(action='ignore', category=FutureWarning)
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(PREDICTOR_PATH)
detector = dlib.get_frontal_face_detector()

#COMMON
def sound_alarm():                
	playsound.playsound("alarm.wav")

def get_landmarks(im):
    rects = detector(im, 1)
    if len(rects) > 1:
        return "error"
    if len(rects) == 0:
        return "error"
    return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])

# YAWN
def top_lip(landmarks):
    top_lip_pts = []
    for i in range(50,53):
        top_lip_pts.append(landmarks[i].item(1))
    for i in range(61,64):
        top_lip_pts.append(landmarks[i].item(1))
    top_lip_all_pts = np.squeeze(np.asarray(top_lip_pts))
    top_lip_mean = np.mean(top_lip_pts, axis=0)
    return int(top_lip_mean)

def bottom_lip(landmarks):
    bottom_lip_pts = []
    for i in range(65,68):
        bottom_lip_pts.append(landmarks[i].item(1))
    for i in range(56,59):
        bottom_lip_pts.append(landmarks[i].item(1))
    bottom_lip_all_pts = np.squeeze(np.asarray(bottom_lip_pts))
    bottom_lip_mean = np.mean(bottom_lip_pts, axis=0)
    return int(bottom_lip_mean)

def mouth_open(landmarks,image):
    if landmarks == "error":
        return image, 0
    top_lip_center = top_lip(landmarks)
    bottom_lip_center = bottom_lip(landmarks)
    lip_distance = abs(top_lip_center - bottom_lip_center)
    return lip_distance

#EYES
def eye_aspect_ratio(eye):
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
	C = dist.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear

def left_eye(landmarks):
    l_eye_points=[]
    for i in range(37,43):
        l_eye_points.append(landmarks[i])
    return l_eye_points

def right_eye(landmarks):
    r_eye_points=[]
    for i in range(43,49):
        r_eye_points.append(landmarks[i])
    return r_eye_points

cap = cv2.VideoCapture(0)
yawns = 0
yawn_count=0
eye_count=0
yawn_status = False 
EYE_AR_THRESH = 4
EYE_AR_CONSEC_FRAMES = 8
COUNTER=0
while True:
    #print(1,threading.enumerate())
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    landmarks = get_landmarks(gray) 
    if landmarks=="error":
        continue 

    # shape = predictor(gray, landmarks)
    # shape = face_utils.shape_to_np(landmarks)
    leftEye = left_eye(landmarks)
    rightEye = right_eye(landmarks)
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)
    ear = (leftEAR + rightEAR) / 2.0
    # leftEyeHull = cv2.convexHull(leftEye)
    # rightEyeHull = cv2.convexHull(rightEye)
    # cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
    # cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1) 
    if ear > EYE_AR_THRESH:
        COUNTER += 1
        if COUNTER >= EYE_AR_CONSEC_FRAMES:
            
            if threading.active_count()==2:
               # print(2,threading.enumerate())
                eye_count+=1
                t = Thread(target=sound_alarm)
                t.deamon = True
                t.start()
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        COUNTER = 0
    cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    lip_distance = mouth_open(landmarks,frame)  
    prev_yawn_status = yawn_status
    if lip_distance > 20:
        yawn_status = True  
        cv2.putText(frame, "Subject is Yawning", (50,450), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
##        output_text = " Yawn Count: " + str(yawns)
##        cv2.putText(frame, output_text, (50,50),cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
        if threading.active_count()==1:
                t = Thread(target=sound_alarm)
                t.deamon = True
                t.start()      
    else:
        yawn_status = False          
    if prev_yawn_status == True and yawn_status == False:
        yawns += 1
    cv2.imshow('Highway Helper', frame )  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
        
cap.release()
cv2.destroyAllWindows()
stri=f'Yawns: {yawns}\nEyes Closed: {eye_count}'


machine=str(socket.gethostname())
#print(machine)
now=datetime.now()
drowsiness.uptodate(machine,now,yawns,eye_count)
root=Tk()
root.title("Welcome")
l=Label(root,text=stri,font=('Arial',23))
l.grid(row=0,column=0)
root.mainloop()
fetch_data.graph()

