import numpy as np
from PIL import Image   
# in order to avoid bgr we will use pillow
'''

'''
# we 1st create the canvas size
width, height = 600, 800

# then we create a blank image, now we added a dtype and the number 3 for a 3 colour channel, for green red and blue
img = np.zeros((height, width, 3), dtype=np.uint8)

img[:] = (35, 29, 43) # we select all the rows with the : - we select red with 255 and 0 for the green and blue. but we will use purple
# next we want to do our ground and sky so we eill do that by creating img[top:bottom, left:right]
img[int(height * 0.85):height, 0:width-1] = (35, 55, 43)
 # 0.85 is 15 percent of the bottom freedup, the colour is green for the ground

'''
now we are drawing the building
- we create the margin for the hight of our building 10% from the top and bottom
- same as above for the width but 20% from the sides
'''
img[int(height * 0.1):int(height * 0.9), int(width * 0.2):int(width * 0.8)] = (94, 101, 107)

'''
now we are drawing windows and we will use a nested for loop to do so
'''
for row in range(6):
    for column in range(5):
        if np.random.randint(0,8) == 5:
            windows_colour =(240, 230, 140)
        else:
            windows_colour = (28,23, 35)
        img[int(height*0.1 + 100*row + 20):int(height*0.1 + 100*row + 60 + 20), int(width * 0.2 + 75*column + 15):int(width*0.2 + 75*column + 30 + 15)] = windows_colour


# save image file with pillow
Image.fromarray(img).save("buildingImg.png")