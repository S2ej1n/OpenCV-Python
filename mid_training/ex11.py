import cv2
import numpy as np

def put_string(frame, text, pt, value, color=(120, 200, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0,0,0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)

capture = cv2.VideoCapture(0)# 웹캠 1개 일경우 0 부터 시작
if capture.isOpened() == False:
    raise Exception("카메라에 문제 발생")

image = np.zeros((480,640,3),np.uint8)
#카메라 속성 획득 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

while True:
    ret, frame = capture.read()# 한장씩 읽어온게 frame
    if not ret: break
    if cv2.waitKey(20) == 27: break #27은 esc 키
    # 초당 20 frame 이며 waitKey는 키보드 입력을 받을수 있으므로
    # 27(esc 키) 를 누르면 강제로 종료

    roi = frame[30:30 + 240, 30:30 + 320]

    exporsure = capture.get(cv2.CAP_PROP_EXPOSURE)  #노출 속성
    put_string(roi, 'EXPOS: ', (10,40), exporsure)
    cv2.rectangle(image,(30,30),(350,270),(0,0,255),2)

    # ROI를 image의 해당 위치에 복사
    image[30:30 + 240, 30:30 + 320] = roi

    cv2.imshow("video", image)
    # 결국 동영상도 여러개의 이미지들의 덩어리 이므로
    # 이미지 출력을 위한 함수 imshow를 사용한다.
capture.release()# 영상이나 웹캠을 종료