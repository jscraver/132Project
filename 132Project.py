from skimage.measure import compare_ssim as ssim
from skimage import data, img_as_float
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import cv2

image0 = cv2.imread("images/Zero.jpg")
image1 = cv2.imread("images/One.jpg")
image2 = cv2.imread("images/Two.jpg")
image3 = cv2.imread("images/Three.jpg")
image4 = cv2.imread("images/Four.jpg")
image5 = cv2.imread("images/Five.jpg")
image6 = cv2.imread("images/Six.jpg")
image7 = cv2.imread("images/Seven.jpg")
image8 = cv2.imread("images/Eight.jpg")
image9 = cv2.imread("images/Nine.jpg")

image0 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
image4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)
image5 = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)
image6 = cv2.cvtColor(image6, cv2.COLOR_BGR2GRAY)
image7 = cv2.cvtColor(image7, cv2.COLOR_BGR2GRAY)
image8 = cv2.cvtColor(image8, cv2.COLOR_BGR2GRAY)
image9 = cv2.cvtColor(image9, cv2.COLOR_BGR2GRAY)

#############################################################
# MAIN CODE
#############################################################

lst = []

fig = plt.figure("Images")

images = [{"Zero": image0}, {"One": image1}, {"Two": image2}, {"Three": image3},\
         {"Four": image4}, {"Five": image5}, {"Six": image6}, {"Seven": image7},\
         {"Eight": image8}, {"Nine": image9}]

for i in range(len(images)):
    for name, image in images[i].items():
        comparison = ssim(image, images[i+1].value())
        lst.append(comparison)
        ax = fig.add_subplot(1, 10, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap = plt.cm.gray)
        plt.axis("off")

plt.show()










