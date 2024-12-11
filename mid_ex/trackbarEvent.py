#트랙바 이벤트
import numpy as np, cv2

def onChange(value):
    global image, title

    #트랙바 값과 영상 화소값 차분
    add_value = value - int(image[0][0])
    #현재 트랙바 값과 이미지의 첫 번째 픽셀값의 차이 계산.
    #value : 트랙바의 현재 값.
    print('추가 화소값: ', add_value)
    image[:] = image + add_value
    cv2.imshow(title, image)

image = np.zeros((300,500), np.uint8)
#초기 이미지는 검정색. image[0][0]=0이므로, 트랙바 초기 위치도 0이겠죠


title = "Trackbar event"
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
