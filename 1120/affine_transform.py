import numpy as np, cv2

image = cv2.imread("ham.jpeg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

center = (200,200)
angle, scale = 30, 1
size = image.shape[::-1]

pt1 = np.array([(30,70),(20, 240),(300, 110)], np.float32)
pt2 = np.array([(120, 20),(10, 180),(280,260)], np.float32)
aff_mat = cv2.getAffineTransform(pt1, pt2)
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)

dst3 = cv2.warpPerspective(image, aff_mat, size, cv2.INTER_LINEAR)
dst4 = cv2.warpPerspective(image, rot_mat, size, cv2.INTER_LINEAR)