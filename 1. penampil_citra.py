import cv2

cv2.namedWindow("Program Penampil Citra", cv2.WINDOW_AUTOSIZE)
citra = cv2.imread(r"C:\Users\M. Shalahuddin Yahya\Documents\messi.jpg")
cv2.imshow("Program Penampil Citra", citra)
cv2.waitKey(0)
cv2.destroyAllWindows()
