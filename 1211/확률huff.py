import cv2
import numpy as np

src = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')

# 에지 검출
edges = cv2.Canny(src, 50, 150)

# 직선 성분 검출
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 160, minLineLength=100, maxLineGap=10)

# 컬러 영상으로 변경 (영상에 빨간 직선을 그리기 위해)
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()