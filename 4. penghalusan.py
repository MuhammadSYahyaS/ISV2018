import cv2
import numpy as np

cv2.namedWindow("Program Penampil Citra", cv2.WINDOW_AUTOSIZE)
citra = cv2.imread('messi.jpg')
jendela = 29
sigmaX = 1
sigmaY = 1
citrahasil = cv2.GaussianBlur(citra, (jendela,jendela), sigmaX, sigmaY)
cv2.imshow("Program Penampil Citra", citrahasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
