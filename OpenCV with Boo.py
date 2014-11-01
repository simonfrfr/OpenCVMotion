import serial # if you have not already done so
import pygame
import cv2
import time
import operator

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)
last = 0
winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
ser = serial.Serial('COM7', 9600)
# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:
  cv2.imshow( winName, diffImg(t_minus, t, t_plus) )

  # Read next image
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  ret, t_plus2 = cv2.threshold(t_plus,127,255, cv2.THRESH_BINARY)
  #print t_plus2.nbytes
  print cv2.countNonZero(t_plus2)
  
  if last < 1000 and cv2.countNonZero(t_plus2) > 1000:
    cam = 0
    pygame.init()
    
    pygame.mixer.music.load("boo.wav")
    
    pygame.mixer.music.play()
    
    time.sleep(1)
    ser.write('1'+'\n')
    time.sleep(1)
    ser.write('1'+'\n')
    time.sleep(1)
    ser.write('1'+'\n')
    time.sleep(1)
    ser.write('1'+'\n')
    time.sleep(1)
    ser.write('1'+'\n')
    time.sleep(1)
    ser.write('1'+'\n')
    time.sleep(1)
    ser.write('1'+'\n')
    time.sleep(1)
    ser.write('1'+'\n')
    time.sleep(1)
    cam = cv2.VideoCapture(0)
  #print '\n'.join([str(pixel) for pixel in t_plus.data \
  #               if False not in map(operator.lt,lower,pixel) \
  #               and False not in map(operator.gt,upper,pixel)])
  last = cv2.countNonZero(t_plus2)
  blue = t_plus[100,100]
  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "Goodbye"
        

