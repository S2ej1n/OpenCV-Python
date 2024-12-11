import numpy as np, cv2

### 컬러를 할거면 반드시 뒤에 3 적을것!!!!
image = np.full((400,600,3),255, np.uint8)

blue, green, red = (255,0,0),(0,255,0),(0,0,255)
center = (300,200)
cv2.ellipse(image, center,(100,100), 0, 180, 360, red, -1 )
cv2.ellipse(image, center,(100,100), 0, 0, 180, blue, -1 )
cv2.ellipse(image, (250,200),(50,50), 0, 0, 180, red, -1 )
cv2.ellipse(image, (350,200),(50,50), 0, 180, 360, blue, -1 )
cv2.imshow("image", image)
cv2.waitKey()