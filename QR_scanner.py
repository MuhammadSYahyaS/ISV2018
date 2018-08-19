import numpy
import cv2
import serial
import time
import hashlib
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol

com = input("Masukkan port komunikasi yang digunakan: ")
baudrate = input("Masukkan baudrate komunikasi: ")
ardu = serial.Serial(com, baudrate)

cap = cv2.VideoCapture(0)
mirror = False

while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if mirror:
            frame = cv2.flip(frame, 1)

        # Our operations on the frame come here
        relay = ''
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hasil_pindai = decode(gray, symbols=[ZBarSymbol.QRCODE])
        if not hasil_pindai:
            print("Tunjukkan kunci ke depan kamera!\n")
        else:
            kunci = hasil_pindai[0].data.decode("utf-8")
            kunci = hashlib.sha256(kunci.encode("utf-8")).hexdigest()
            if(kunci == '3b8b62a4dbe8a55ea97c9488cce6688f045e2c9491eef20f2b2d7f53b02278fb'):
                relay = '1'
            elif(kunci == '0f75961694d1ab48dac5581c6329027cda5f87428c252001cea636e29a9cd10a'):
                relay = '2'
            elif(kunci == '5ff7de166b1daca5c2f430fd04c8caa8319f48ccdf44d6dd51b6c904bd66818c'):
                relay = '3'     
            if(relay != ''):
                print("Relay", relay, "\n")
                ardu.write(relay.encode('utf-8'))
        # Display the resulting frame
        cv2.imshow('Kamera',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
