#Image to pencil sketch
#Package installed: py-opencv

import cv2

image = cv2.imread("Anisha.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255-gray_image
blur = cv2.GaussianBlur(inverted, (121, 121), 0)
inverted_blur = 255-blur
sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
cv2.imwrite("sketch_image.png", sketch)
