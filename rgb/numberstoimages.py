import numpy as np
import cv2

# we 1st create the canvas size
width, height = 800, 800

# then we create a blank image 
img = np.zeros((height, width))

'''
below we will create an image called 50 shades of gray, in the shadess we are actually
going to incriment the values using a forloop
'''
location = 0 # this is our x which we will initialise as zero (starting point)
shade = 0    # zero is black and gret is 1 to 254 and white is 255

for i in range(50): # because we are looking for 50 shades we will use 50
    img[0:height, location:location + width//50] = shade # zero hight represents top:bottom and location left:right the divisable by 50 seperates each segment
    location += width//50 # horrizontal incrementation
    shade += 255//50 # the maximum intencity of white



# convert this array into an image file
cv2.imwrite("new_img.png", img) # with cv2 we image write creating a new image as a png

'''
NB if you wish to change the shading value you can replace the 50 with another number like 25 and get 25 shades instead of 
50 or create a variable where you store the new number and replace all the 50s with the new var.

to have a smooth gradiant you will simply make the value of 50 to 255

'''

    
    
