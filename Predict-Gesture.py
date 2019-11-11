# Final output file to predict the trained/calibrated gestures

import pickle
import sys
import serial

with open('trained_model','rb') as f:
    svm_model_linear = pickle.load(f)

ser = serial.Serial('COM3', 9600)
i=0
a=[]
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
        svm_predictions = svm_model_linear.predict([[a[0],a[1],a[2]]])
        ser.write(bytes(str(svm_predictions[0]),'utf-8'))
        print(str(svm_predictions[0]))
        a.clear()
