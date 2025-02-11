import cv2
import numpy as np
import matplotlib.pyplot as pl

def draw_hist(image):

    hist, bins = np.histogram(image.flatten(), 256, [0,256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img_equal = cdf[image]

    pl.figure(figsize=(11, 6))
    pl.subplot(1, 3, 1)
    pl.hist(image.flatten(), 256, [0,256], color='r')
    pl.xlim([0, 256])
    pl.title('Histogram')
    pl.subplot(1, 3, 2)
    pl.hist(img_equal.flatten(), 256, [0,256], color='g')
    pl.xlim([0, 256])
    pl.title('Equal histogram')
    pl.show()

image_path = input("Path to the grayscale image: ")
test_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

draw_hist(test_image)

