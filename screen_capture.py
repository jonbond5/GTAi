import numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID') # Video codec
vid = cv2.VideoWriter('record.avi', fourcc, 8, (500, 490)) # save filename, codec, FPS, 
# Use OpenCV part 14 for message on compatibility between vid and img (~6:16)
# Takes into account x, y offsets (w, h respectively)
while True:
    img = ImageGrab.grab(bbox=(100, 10, 600, 500)) # Grab screenshot with boundingbox (x, y, width, height)
    img_np = np.array(img) # Format OpenCV accepts
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    vid.write(img_np)
    cv2.imshow("frame", img_np)
    key = cv2.waitKey(1)
    if key == 27:
        break


vid.release()
cv2.destroyAllWindows()