import cv2

capture = cv2.VideoCapture("https://192.168.0.3:8080/video") # for my camera i will use zero

while(True):
    _, frame = capture.read()

    # to change the colour of the recording of the live to gray
    grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # below we will add mirroring just incase we want to have a mirrir edit
    mirror = cv2.flip(grey, 0) # if we flip with zero it will flip vertically and one will mirrir the image horrizontally and -1 will do both

    cv2.imshow('livestreem', frame) # to get the grey to show change the word frame to gray; to mirrir we will replace grey to mirror

    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()


# step1 on your phone at the playstore search for ipwebcam
# syep2 make sure you are connected to the same wifi as your computer then press startserver and copy the ip adress 
# step3 copy it into your web browser ipv4. (video render full screen)
# step4 on the video click inspect, hover over video and copy the current source url and add it to our code
