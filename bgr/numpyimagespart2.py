import numpy as np
import cv2
    
# if we want to change things to colours 

# we 1st create the canvas size
width, height = 800, 800

# then we create a blank image, now we added a dtype and the number 3 for a 3 colour channel, for green red and blue
img = np.zeros((height, width, 3), dtype=np.int8)

'''
below we will create an image called 50 shades of gray, in the shadess we are actually
going to incriment the values using a forloop

here in the 1st line of the for loop we add zero because it will always start with red

opencv instead of using rgb they did it backwards and used bgr way, so instead of focusing
on index zero we will focus on two which will make it red, if we want to include more
we can say channel zero up to two, not including two and we will get this strange turquois 
gradient : - img[0:height, location:location + width//50, 0:2] = shade - then one to 3 will be 
shades of yellow
'''
location = 0 # this is our x which we will initialise as zero (starting point)
shade = 0    # zero is black and gret is 1 to 254 and white is 255

for i in range(50): # because we are looking for 50 shades we will use 50
    img[0:height, location:location + width//50, 0] = shade # zero hight represents top:bottom and location left:right the divisable by 50 seperates each segment
    location += width//50 # horrizontal incrementation
    shade += 255//50 # the maximum intencity of white



# convert this array into an image file
cv2.imwrite("Color_new_img.png", img) # with cv2 we image write creating a new image as a png

