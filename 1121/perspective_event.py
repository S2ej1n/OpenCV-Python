import numpy as np, cv2

# 특정 점 p가 사각형영역 (p1, p2) 안에 포함되는지 확인
def contain_pts(p, p1, p2):
    return (p1[0] <= p[0] < p2[0]
            and p1[1] <= p[1] < p2[1])

def draw_rect(img):
    rois = [(p - small, small * 2) for p in pts1]
    # 각 점 상하 좌우에 12픽셀의 여유 줌
    # (100,100) -> [(88,88),(24,24)]

    for (x,y), (w,h) in np.int32(rois):
        roi = img[y:y+h, x:x+w]

        # 컬러 (3차원 행렬 생성함)
        val = np.full(roi.shape, 80, np.uint8) #밝기 값 80으로 채우기
        cv2.add(roi, val, roi) # roi 밝게 만들기 - roi에 val 더하기
        cv2.rectangle(img,(x, y, w, h), (0,255,0), 1) # 사각형 테두기 그리기

    # cv2.polylines(원본그림, 좌표리스트, 마지맛 점과 첫 점 연결? ,선색, 선 굵기)
    cv2.polylines(img, [pts1.astype(int)], True, (0,255,0), 1) #4개 좌표 잇기
    cv2.imshow("select rect", img)

# 원근 변환 수행 함수
def wrap(img):
    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, perspect_mat, (350,400), cv2.INTER_CUBIC) #원근변환
    cv2.imshow('perspective transfrom', dst)

def onMouse(event, x, y, flags, param):
    global check

    if event == cv2.EVENT_LBUTTONDOWN:
        # enumerate : 인덱스와 원소로 이루어진 튜플 만들어줌.
        # i 인덱스와 p 좌표를 가지고온다
        for i, p in enumerate(pts1):
            # p1 : p-small 좌표의 왼쪽 위
            # p2 : p+small 좌표의 오른쪽 아래
            p1, p2 = p - small, p + small

            #마우스 클릭 좌표 (x, y)가 작은 사각형 영역 (p1, p2)에 포함되는지 검사
            if contain_pts((x,y), p1, p2):
                check = i
                # 포함되면 해당 인덱스 저장

    if event == cv2.EVENT_LBUTTONUP:
        check = -1
        # 클릭 해제되면 선택 상태 종료

    # 눌려있다는거겠지.
    if check >= 0:
        pts1[check] = (x,y) #선택한 좌표의 값을 현재 마우스 좌표로 업데이트
        #사각형 다시 그린다
        draw_rect(np.copy(image))
        wrap(np.copy(image))

#
image = cv2.imread("perspective2.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

small = np.array([12,12])
check = -1
pts1 = np.float32([(100,100), (300,100), (300,300), (100,300)]) #4개 좌표 초기화
pts2 = np.float32([(0,0), (400,0), (400,350), (0,350)])

draw_rect(np.copy(image))
cv2.setMouseCallback("select rect", onMouse,0)
cv2.waitKey(0)