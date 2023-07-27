# Converting Image to Pencil Sketch

import cv2

image = cv2.imread("one-piece-zoro-anime-animation-1231490.webp")

grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert, (21,21),0)

invertedblur = cv2.bitwise_not(blur)

pencil_sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("Pencil_Sketch.png", pencil_sketch)