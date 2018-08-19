import cv2
import numpy as np

cv2.namedWindow("Citra Keabuan", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Citra Biner", cv2.WINDOW_AUTOSIZE)
citra = cv2.imread('messi.jpg')
citrakeabuan = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
ambang = 127
keabuanmaks = 255
retval, citrabiner = cv2.threshold(citrakeabuan, ambang, keabuanmaks, cv2.THRESH_BINARY)
cv2.imshow("Citra Keabuan", citrakeabuan)
cv2.imshow("Citra Biner", citrabiner)
cv2.waitKey(0)
cv2.destroyAllWindows()
