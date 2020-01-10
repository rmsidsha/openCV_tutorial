import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('./seawookang.jpg')
# cv2.imshow('image', image)

"""
================================= cornerHarris
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray = np.float32(gray)     # numpy를 이용해 자료형을 부동소수점으로 바꿔줘야함
dst = cv2.cornerHarris(gray, 2,3,0.04)  # 2, 3, 0.04는 바꿀 수 있는 인자들임
dst = cv2.dilate(dst, None)         # dilate(결과, None) 꼭짓점을 표시하기 위해 확장 dilate연산을 함

image[dst>0.01*dst.max()] = [0,0,255]   # 결과 나옴

cv2.imshow('dst', dst)
#cv2.imshow('dst', gray)
"""

imgRgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
edges = cv2.Canny(image, 100, 200) # 100, 200 변경 가능

plt.subplot(1,2,1) # 1행 2열에서 1번째 열
plt.imshow(imgRgb)
plt.xticks([])  # x축 좌표를 숨김
plt.yticks([])  # y축 좌표를 숨김

plt.subplot(1,2,2) # 1행 2열에서 2번째 열
plt.imshow(edges, cmap='gray')
plt.xticks([])  # x축 좌표를 숨김
plt.yticks([])  # y축 좌표를 숨김

plt.show()
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destoryAllWindows()


