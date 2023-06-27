
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def singleimg(img, title, size, mincolor=0, maxcolor=255):
    fig, axis = plt.subplots(figsize=size)
    axis.imshow(img,cmap='gray',vmin=mincolor, vmax=maxcolor)
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()
        
    def showmultiple_image(img_array, title_array, size, x, y, mincolor=0, maxcolor=255):
        if(x<1 or y<1):
            print('Error: X e Y nao podem ser zero ou abaixo de zero!')
            return
        elif(x == 1 and y == 1):
            fig, axis = plt.subplots(y, figzise = size)
            yId = 0
            for img in img_array:
                axis[yId].imshow(img, cmap='gray', vmin=mincolor, vmax=maxcolor)
                axis[yId].set_achor('NW')
                axis[yId].set_title(title_array[yId], fontdict = {'fontesize': 18, 'fontweight': 'medium'}, pad = 10)
                yId += 1
        elif(y == 1):
            fig, axis = plt.subplots(1, x, figsize = size)
            fig.suptitle(title_array)
            xId = 0
            for img in img_array:
                axis[xId].imshow(img, cmap='gray', vmin=mincolor, vmax=maxcolor)
                axis[xId].set_anchor('NW')
                axis[xId].set_title(title_array[xId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)
                xId += 1
        else:
            fig, axis = plt.subplots(y, x, figsize = size)
            xId, yId, titleId = 0, 0, 0
            for img in img_array:
                axis[yId, xId].set_title(title_array[titleId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)
                axis[yId, xId].set_anchor('NW')
                axis[yId, xId].imshow(img, cmap='gray', vmin=mincolor, vmax=maxcolor)
                if(len(title_array[titleId]) == 0):
                    axis[yId, xId].axis('off')
                titleId += 1
                xId += 1
                if xId == x:
                    xId = 0
                    yId += 1
        plt.show()
    img_binarizada = cv.imread('image.jpg',0)
    singleimg(img_binarizada, 'Dilatation', (4,6))
  
    kernel = np.ones((3,3), np.uint8)
    img_binarizada
    img_dilatation1 = cv.dilate(img_binarizada, kernel, iterations=1)
    img_dilatation2 = cv.dilate(img_binarizada, kernel, iterations=2)
    img_dilatation3 = cv.dilate(img_binarizada, kernel, iterations=3)
    img_dilatation4 = cv.dilate(img_binarizada, kernel, iterations=4)
    img_dilatation5 = cv.dilate(img_binarizada, kernel, iterations=5)
    img_dilatation6 = cv.dilate(img_binarizada, kernel, iterations=6)

    img_array = [img_binarizada,img_dilatation1,img_dilatation2,img_dilatation3, img_dilatation4, img_dilatation5, img_dilatation6]
    title_array = ['img_orig','img_dilate1','img_dilate2','img_dilate3','img_dilate4','img_dilate5','img_dilate6']
    showmultiple_image(img_array, title_array, (10,9), 3,2)
