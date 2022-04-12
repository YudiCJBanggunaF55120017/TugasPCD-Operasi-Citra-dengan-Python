import cv2
import numpy as np

img = cv2.imread("pemandangan.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Pemandangan Original", img)
cv2.imshow("Gambar Pemandangan Grayscale", gray)

