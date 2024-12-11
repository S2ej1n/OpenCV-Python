import numpy as np, cv2

image = np.full((300,400,3),255,np.uint8)

title = "mid102_6"

cv2.ellipse(image,(180,150),(120,60),0,30,270,(255,0,0),4)

cv2.imshow(title,image)
cv2.waitKey()
cv2.destroyAllWindows()