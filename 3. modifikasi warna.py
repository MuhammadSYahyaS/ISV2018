import cv2
import numpy as np

cv2.namedWindow("Program Penampil Citra", cv2.WINDOW_AUTOSIZE)
citra = cv2.imread('messi.jpg')
citrahasil = citra
color_mask =  np.zeros(citra.shape, citra.dtype)
color_mask[:,:] = (255, 0, 0)
cv2.subtract(citra, color_mask, citrahasil)
cv2.imshow("Program Penampil Citra", citrahasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
