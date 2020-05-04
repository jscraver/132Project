import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
from sklearn.tree import DecisionTreeClassifier
from PIL import Image


im = cv2.imread("images/One2.jpg")
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

lst = []
im.resize((28, 28))

for i in im:
    for x in i:
        lst.append(x)

for i in range(len(lst)):
    if lst[i] > 128:
        difference = lst[i] - 128
        lst[i] -= ((2 * difference) + 5)
    else:
        difference = 128 - lst[i]
        lst[i] += 2 * difference

for i in range(len(lst)):
    if lst[i] < 91:
        lst[i] = 0



##for i in im:
##    for x in i:
##        if x < 80:
##            x = 0
##        lst.append(x)


        

##neighbors = []
##for i in range(len(lst)):
##    if i == 255:
##        neighbors.append(i+1)
##        neighbors.append(i-1)
##        neighbors.append(i+2)
##        neighbors.append(i-2)
##for i in neighbors:
##    lst[i] = 255
        


data = pd.read_csv("mnist_train.csv").as_matrix()
clf = DecisionTreeClassifier()

xtrain = data[0:60000, 1:]
train_label = data[0:60000, 0]

clf.fit(xtrain, train_label)

##xtest = data[21000: ,1:]
##actual_label = data[60000: ,0]
#12
d = np.array(lst)
d.shape = (28,28)
plt.imshow(d, cmap = "gray")
prediction = clf.predict([lst])
print prediction
plt.show()







