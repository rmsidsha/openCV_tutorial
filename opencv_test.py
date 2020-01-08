import cv2
"""
파일 열어보기
src = cv2.imread('./ddd.jpg')
cv2.imshow('image', src)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
이미지 크롭하기
src  =cv2.imread('./ddd.jpg')
dst = src[100:300, 100:200] # height(row), width(col)
cv2.imshow('image', src) # 원본 이미지
cv2.imshow('crop', dst)  # crop이미지
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
# 크기를 줄인 이미지 띄우기
src = cv2.imread('./ddd.jpg')
print(src.shape)  # 253, 199, 3
small_height = int((100*src.shape[0])/src.shape[1])
print(small_height) # 127
small_size = (100, small_height)
big_size = (3*(src.shape[0]), 3*(src.shape[1]))
small_dst = cv2.resize(src, small_size)
big_dst = cv2.resize(src, big_size)
cv2.imshow('image', src) # 원본 이미지
cv2.imshow('scaling', small_dst) # 크기를 줄인 이미지 crop X
cv2.imshow('scaling', big_dst) #크기를 늘인 이미지
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
이미지 회색으로 바꾸기
src = cv2.imread('./ddd.jpg')
# height = int((100*src.shape[0])/src.shape[1])
print(src.shape[0], src.shape[1]) # height, width
img_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
사진을 다른 이름으로 저장
src = cv2.imread('./ddd.jpg')
img_gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
cv2.imwrite('gray_ddd.jpg', img_gray)
src2 = cv2.imread('./gray_ddd.jpg')
cv2.imshow('image', src2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
