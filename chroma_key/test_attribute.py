import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pickle
import cv2


# hist,bins = np.histogram(image[0].ravel(),255,[0,255])
image = cv2.imread("media/as.jpg")
color = ('b','g','r')
cv2.imshow("image",image)
for i,col in enumerate(color):
    histr = cv2.calcHist([image],[i],None,[255],[0,255])
    plt.plot(histr,color = col)
    plt.xlim([0,255])
plt.show()
cv2.waitKey()
# X = image.reshape((image.shape[0]*image.shape[1], image.shape[2]))
# kmeans = KMeans(n_clusters=100).fit(X)
# pickle.dump(kmeans, open('model_kmeans.sav', 'wb'))