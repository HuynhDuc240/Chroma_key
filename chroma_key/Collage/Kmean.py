import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pickle
import cv2
import os
import re
class Kmean():
    
    ''' Mode of operation:
        Consists of 2 layer:
            - On the first layer, eliminating the blue screen, at this level when removing the blue screen,
            there are still some green spots, because that is the point of interference during the 
            adjustment of the Kmean centers. 
            - 2nd layer, eliminating noise using 1 Kmean other than 100 labels, 
            eliminating jamming labels (green points)'''

    def __init__(self, bg, obj):
        self.name = str(bg) + str(obj)
        self.background_image = None
        self.objects_image = None
        if bg and obj:
            self.background_image = cv2.imread("media/"+bg)
            self.objects_image = cv2.imread("media/"+obj)

    # Save the model with the center to facilitate the distance at the next time
    def train(self, image):
        X = image.reshape((image.shape[0]*image.shape[1], image.shape[2]))
        kmeans = KMeans(n_clusters=2).fit(X)
        pickle.dump(kmeans, open('model_kmeans.sav', 'wb'))
    
    # Predict has 2 option
    def predict(self,image, flag):
        #option 1:
        #remove residual noise in the image when green screen is separated, (some green spots remain)
        if flag:
            kmeans = pickle.load(open('Collage/model_kmeans_overfit.sav', 'rb'))
            X = image.reshape((image.shape[0]*image.shape[1], image.shape[2]))
            Y = kmeans.predict(X)
            # the jamming labels 
            X[Y == 18] = 0
            X[Y == 33] = 0
            X[Y == 47] = 0 
            X[Y == 51] = 0
            X[Y == 54] = 0
            X[Y == 61] = 0
            X[Y == 64] = 0
            X[Y == 76] = 0
            X[Y == 78] = 0
            X[Y == 91] = 0
            X[Y == 98] = 0
            result = X.reshape((image.shape[0], image.shape[1], image.shape[2]))
            return result
        #option 2:
        #remove green screen
        else:
            kmeans = pickle.load(open('Collage/model_kmeans.sav', 'rb'))
            X = image.reshape((image.shape[0]*image.shape[1], image.shape[2]))
            Y = kmeans.predict(X)
            X[Y == 1] = 0
            result = X.reshape((image.shape[0], image.shape[1], image.shape[2]))
            return result
    
    def processing(self):
        # layer 1
        result = self.predict(self.objects_image,0)
        # layer 2
        remove_overfit = self.predict(result,1)
        # combine 2 photos
        mask =  cv2.inRange(remove_overfit, np.array([0,0,0]), np.array([10,10,10]))
        mask_inv = cv2.bitwise_not(mask)
        bg = cv2.bitwise_and(self.background_image,self.background_image, mask=mask)
        fg = cv2.bitwise_and(self.objects_image, self.objects_image, mask=mask_inv)
        final = bg + fg
        # save the final image to load images in the front end
        cv2.imwrite("media/"+self.name,final)
        return "/media/"+self.name

