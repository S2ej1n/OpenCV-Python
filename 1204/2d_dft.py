# 푸리에 변환이 시간이 오래 걸린다. 기다려주세요
import numpy as np, cv2, math, time
from matplotlib.image import imread


def exp(knN):
    th = -2 * math.pi * knN
    return complex(math.cos(th), math.sin(th))

def dft(g):
    N = len(g)
    dst = [sum(g[n] * exp(k*n/N) for n in range(N)) for k in range(N)]
    return np.array(dst)

def idft(G):
    N = len(G)
    dst = [sum(G[n] * exp(-k * n/N) for n in range(N)) for k in range(N)]
    return np.array(dst) / N

def calc_spectrum(complex):
    if complex.ndim==2:
        dst = abs(complex)
    else:
        dst = cv2.magnitude(complex[:,:,0], complex[:,:,1])
    dst = cv2.log(dst + 1)
    cv2.normalize(dst, dst, 0 ,255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h//2, w//2
    dst[h-cy:, w-cx:] = np.copy(img[0:cy, 0:cx])
    dst[0:cy, 0:cx] = np.copy(img[h-cy:, w-cx:])
    dst[0:cy, w - cx:] = np.copy(img[h-cy:, 0:cx])
    dst[h - cy:, 0:cx] = np.copy(img[0:cy, w-cx:])
    return dst

def dft2(image):
    tmp = [dft(row) for row in image]
    dst = [dft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def idft2(image):
    tmp = [idft(row) for row in image]
    dst = [idft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def ck_time(mode=0):
    global stime
    if(mode == 0):
        stime = time.perf_counter()
    elif (mode ==1):
        etime = time.perf_counter()
        print("수행시간 = %.5f sec" % (etime - stime))

image = cv2.imread("dft_240.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

ck_time(0)
dft = dft2(image)
spectrum1 = calc_spectrum(dft)
spectrum2 = fftshift(spectrum1)
idft = idft2(dft).real
ck_time(1)

cv2.imshow("image", image)
cv2.imshow("spectrum1", spectrum1)
cv2.imshow("spectrum2",spectrum2)
cv2.imshow("idft_img", cv2.convertScaleAbs(idft))
cv2.waitKey()