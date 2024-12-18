import cv2
import numpy as np

image = cv2.imread('perspective.jpg',cv2.IMREAD_COLOR)

pts1 = []
def onMouse(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        click = (x,y)
        pts1.append(click)
        cv2.circle(image,(x,y),5,(0,255,0),-1)
        cv2.imshow('g',image)

    if len(pts1) ==4:
        wrap(image)

def wrap(img):
    pts1_np = np.float32(pts1)

    M = cv2.getPerspectiveTransform(pts1_np, pts2)

    dst = cv2.warpPerspective(image, M, (400,350), cv2.INTER_LINEAR)
    cv2.imshow('new', dst)

 #입력 영상 4개 좌표
pts2 = np.float32([(0, 0),(400,0), (400,300), (0,300)])
cv2.imshow('g', image)
cv2.setMouseCallback('g', onMouse)
cv2.waitKey(0)

