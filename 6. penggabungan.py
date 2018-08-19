import cv2
import numpy as np

cv2.namedWindow("Citra Gabungan", cv2.WINDOW_AUTOSIZE)
citra1 = cv2.imread('000319.png')
citra2 = cv2.imread('000320.png')
citrahasil = cv2.addWeighted(citra1, 0.5, citra2, -0.5, 127)
cv2.imshow("Citra Gabungan", citrahasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
