import cv2

# def put_string(frame, text, pt, value, color=(120, 200, 90)):
#     text += str(value)
#     shade = (pt[0] + 2, pt[1] + 2)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, text, shade, font, 0.7, (0,0,0), 2)
#     cv2.putText(frame, text, pt, font, 0.7, color, 2)

capture = cv2.VideoCapture("file_example_MP4_640_3MG.mp4")
if capture.isOpened() == False: raise Exception("동영상 파일 개방안됨")

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000/frame_rate)
frame_cnt = 0

def blue_bar(value):
    None #보통은 Pass라고 씀.
    # global capture
    # cv2.add(blue, value, blue)

def green_bar(value):
    None
    # global capture
    # cv2.add(green, value, green)

def red_bar(value):
    None
    # global capture
    # cv2.add(red, value, red)

title = "Change RGB"
cv2.namedWindow(title)
cv2.createTrackbar('blue', title, 0 ,100, blue_bar)
cv2.createTrackbar('green', title, 0 ,100, green_bar)
cv2.createTrackbar('red', title, 0 ,100, red_bar)

while True:
    ret, frame = capture.read()
    if cv2.waitKey(delay) >= 0: break
    blue, green, red = cv2.split(frame) #컬러 영상 채널 분리

    #위치 가져오기!
    r = cv2.getTrackbarPos("red", title)  # red 트랙바의 위치값 가져오기 0~255
    g = cv2.getTrackbarPos("green", title)  # green 트랙바의 위치값 가져오기 0~255
    b = cv2.getTrackbarPos("blue", title)  # blue 트랙바의 위치값 가져오기 0~255

    cv2.add(red, r, red)   # 영상의 red 채널의 밝기값을 트랙바의 위치값으로 추가
    cv2.add(blue, b, blue)  # 영상의 blue 채널의 밝기값을 트랙바의 위치값으로 추가
    cv2.add(green, g, green) # 영상의 green 채널의 밝기값을 트랙바의 위치값으로 추가

    frame = cv2.merge( [blue, green, red])
    cv2.imshow(title, frame)
capture.release()