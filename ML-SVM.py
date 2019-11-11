# Python file which reads passes the input to the model for training

import pickle
from sklearn.svm import SVC

with open('gesture_input','rb') as f:
    X=pickle.load(f)

with open('gesture_labels','rb') as f:
    y=pickle.load(f)


svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X,y)

with open('trained_model','wb') as f:
    pickle.dump(svm_model_linear,f)
