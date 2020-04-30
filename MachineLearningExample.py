import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("train.csv").as_matrix()
clf = DecisionTreeClassifier()

xtrain = data[0:21000, 1:]
train_label = data[0:21000, 0]

clf.fit(xtrain, train_label)

xtest = data[21000: ,1:]
actual_label = data[21000: ,0]

d = xtest[8]
d.shape = (28,28)
plt.imshow(255 - d, cmap = "gray")
prediction = clf.predict([xtest[8]])
print prediction
plt.show()
