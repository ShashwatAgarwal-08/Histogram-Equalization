# Histogram-Equalization

We have to plot a Histogram of the greyscale image and perform Histogram equalization on it.
•	Write a program that takes greyscale image as input and plots histogram of the given greyscale image
•	Write a program that performs Histogram equalization on the greyscale image taken as input.

Algorithm and Problem design:
1.	Plotting Histogram:
•	Take a greyscale image as input
•	The image is to be encoded as a 2D matrix with values from 0 to 255.
•	Create an array of size 256, one each for intensity values.
•	Iterate every pixel, depending on intensity of pixels, increase matching histogram bin.
•	Use a suitable library.
•	Plot intensity values on X axis, Frequency on Y axis.
2.	Histogram Equalization:
•	Determine the cumulative distribution function (CDF) of the histogram.
•	Convert original intensity values to new ones using CDF.
•	New Intensity = floor(CDF[original intensity] * 255)
•	In the image apply the new intensity values.
•	Adjust new image to range between 0 to 255.
