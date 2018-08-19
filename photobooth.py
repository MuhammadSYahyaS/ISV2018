import cv2
import numpy as np
import serial #pip install pySerial
import threading

# Serial communication using separated thread
##com = input("Serial port: ")
##baudrate = input("Serial baudrate: ")
com = 'COM19'
baudrate = 115200
ardu = serial.Serial(com, baudrate)
termFlag = 0
buffer = [0]

class mySerial (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print("Starting " + self.name + " on port: " + com)
      getSerial(self.name)
      print("Exiting " + self.name)

def getSerial(threadName):
   while not termFlag:
      received = ardu.readline()
      buffer.clear()
      buffer.append(str(received, 'utf-8'))
   ardu.close()

threadSerial = mySerial(1, "SerialCom-Thread")
threadSerial.start()

## Function(s) declared here ##
def Vignete(img, kernel_size):
    kernel_size = 100 + kernel_size * 50 / 1023.0
    rows, cols = img.shape[:2]
    dest = img
    
    # Generating vignette mask using Gaussian kernels
    kernel_x = cv2.getGaussianKernel(cols, kernel_size)
    kernel_y = cv2.getGaussianKernel(rows, kernel_size)
    kernel = kernel_y * kernel_x.T
    mask = 255 * kernel / np.linalg.norm(kernel)

    # Applying the mask to each channel in the input image
    for i in range(3):
        dest[:,:,i] = np.clip(img[:,:,i] * mask * 1.2, 0, 255)
    return dest

def Desat(img, strength):
    strength =  strength / 1023.0
    dest = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    dest[:,:,2] = np.clip(dest[:,:,2] * strength, 0, 255)
    dest = cv2.cvtColor(dest, cv2.COLOR_HLS2BGR)
    return dest

def Blur(img, ksize):
    ksize = round(ksize * 51 / 90.0)
    if ksize < 1: ksize = 1
    elif not ksize%2: ksize -= 1
    dest = cv2.GaussianBlur(img, (ksize,ksize), 0)
    return dest
## Function(s) declaration ends here ##

## Main program starts here ##
# Camera initialization
captureDevice = 0 # Camera index 0
cap = cv2.VideoCapture(captureDevice)
mirror = False

# Main loop of camera streaming
while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if mirror:
            frame = cv2.flip(frame, 1)
        data_s = buffer[0] #  Receive data from serial
        data = data_s.split(',') # Split string by "," to list of values
            
        # Our operations on the frame come here
        print(data)
        if bool(int(data[0])): frame = Desat(frame, int(data[3]))
        if bool(int(data[1])): frame = Vignete(frame, int(data[4]))
        if bool(int(data[2])): frame = Blur(frame, int(data[5]))
        
        # Display the resulting frame
        cv2.imshow('Kamera',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
## Main program ends here ##

# When everything done, terminate serial communication
termFlag = 1
threadSerial.join()
