import cv2

def put_string(frame, text, pt, value, color=(120, 200, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0,0,0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)

def zoom_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value)

def focus_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value)

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)

title = "Change Camera Properties"
cv2.namedWindow(title)
cv2.createTrackbar('zoom', title, 0 ,10, zoom_bar)
cv2.createTrackbar('focus', title, 0, 250, focus_bar)

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    zoom = int(capture.get(cv2.CAP_PROP_ZOOM))
    focus = int(capture.get(cv2.CAP_PROP_FOCUS))
    put_string(frame, 'zoom : ', (10, 240), zoom)
    put_string(frame, 'focus : ', (10,270), focus)
    cv2.imshow(title, frame)

capture.release()