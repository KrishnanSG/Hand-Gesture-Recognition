# Python file to train/calibrate the gestures

import serial
import time
import pickle
import sys

ser = serial.Serial('COM3', 9600)
i=0
a=[]

coordinates=[]
labels=[]
try:
    with open('gesture_input','rb') as f:
        coordinates=pickle.load(f)

    with open('gesture_labels','rb') as f:
        labels=pickle.load(f)
except:
    pass

count=0
while(1):
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    flt = float(string)
    a.append(flt)
    i+=1
    if i==3:
        i=0
        coordinates.append([a[0],a[1],a[2]])
        labels.append(sys.argv[1])
        print([a[0],a[1],a[2]])
        ser.write(bytes("Training Model",'utf-8'))
        a.clear()
        count+=1
    if count>=50:
        break

with open('gesture_input','wb') as f:
    pickle.dump(coordinates,f)

with open('gesture_labels','wb') as f:
    pickle.dump(labels,f)
