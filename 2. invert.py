import cv2

cv2.namedWindow("Program Penampil Citra", cv2.WINDOW_AUTOSIZE)
citra = cv2.imread('messi.jpg')
citrahasil = citra
cv2.bitwise_not(citra, citrahasil)
cv2.imshow("Program Penampil Citra", citrahasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
