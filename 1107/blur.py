# 책 예제 - 블러링
# 이미지 블러링을 직접 구현
import numpy as np
import cv2

# 회선 수행 함수 - 행렬 처리 방식 , 속도가 빠르고 간결함
def filter(image, mask):
    rows, cols = image.shape[:2] # 입력 이미지 행, 열 크기 가져옴.
    dst = np.zeros((rows, cols), np.float32) # 결과 이미지 저장할 배열
    mask_size = mask.shape[0] // 2
    # 마스크의 절반 크기 - 마스크를 중심으로 입력 이미지를 처리하기 때문

    # 입력 행렬 반복 순회
    # 범위는 마스가 이미지 경계를 벗어나지 않도록 이렇게 설정함
    for i in range(mask_size, rows - mask_size): #행부터
        for j in range(mask_size, cols - mask_size): #열까지
            y1, y2 = i - mask_size, i + mask_size + 1  # 관심 영역 높이 범위
            #행의 위아래
            x1, x2 = j - mask_size, j + mask_size + 1  # 관심 영역 너비 범위
            #열의 좌우

            roi = image[y1:y2, x1:x2].astype('float32')
            # 관심영역 만들고 형변환

            tmp = cv2.multiply(roi, mask)
            # 관심영역과 마스크의 요소 곱하기

            dst[i, j] = cv2.sumElems(tmp)[0]
            # tmp 배열의 모든 요소 합산, 현재 픽셀의 결과값 ㅖ산.

    return dst


# 회선 수행 함수 - 화소 직접 근접 방식, 중첩 루프를 사용하여 마스크의 각 요소를 직접 접근하며 곱셈 연산을 수행
def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    mask_size = mask.shape[0] // 2  # 마스크의 절반 크기

    for i in range(mask_size, rows - mask_size):
        for j in range(mask_size, cols - mask_size): #여기까진 동일
            sum = 0.0 # 마스크와 관심 영역의 곱셈 결과를 누적할 변수
            for u in range(mask.shape[0]): # mask.shape[0] 마스크의 행 크기
                for v in range(mask.shape[1]):
                    y, x = (i + u - mask_size,
                            j + v - mask_size)
                    sum += image[y, x] * mask[u, v]
            dst[i, j] = sum
    return dst


# 이미지와 마스크 불러오기
image = cv2.imread("filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

# 마스크 정의 (평균 블러)
data = [1 / 9] * 9  # 3x3 평균 블러 마스크
mask = np.array(data, np.float32).reshape(3, 3)

# 필터 함수 적용
blur1 = filter(image, mask) #행렬
blur2 = filter2(image, mask) #화소 직접 접근

# 스케일 조정 및 타입 변환
blur1 = cv2.normalize(blur1, None, 0, 255, cv2.NORM_MINMAX)
blur1 = blur1.astype('uint8')


blur2 = cv2.convertScaleAbs(blur2)

# 결과 출력
cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image - Method 1", blur1)
cv2.imshow("Filtered Image - Method 2", blur2)
cv2.waitKey(0)
cv2.destroyAllWindows()
