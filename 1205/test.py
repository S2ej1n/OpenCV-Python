# openCV 푸리에 변환
import cv2
import matplotlib.pyplot as plt
import numpy as np

def fourier():
    img = cv2.imread('Lenna.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    dft = cv2.dft(np.float32(gray),
                  flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    out = 20*np.log(cv2.magnitude(dft_shift[:, :, 0],
                                  dft_shift[:, :, 1]))
    inverse_shift = np.fft.fftshift((dft_shift))
    inverse_dft = cv2.dft(inverse_shift,flags=cv2.DFT_INVERSE)
    out2 = cv2.magnitude(inverse_dft[:, :, 0],
                                  inverse_dft[:, :, 1])
    plt.subplot(131)
    plt.imshow(gray, 'gray')
    plt.title('original')
    plt.subplot(132)
    plt.imshow(out, cmap='gray')
    plt.title('dft')
    plt.subplot(133)
    plt.imshow(out2, cmap='gray')
    plt.show()

fourier()