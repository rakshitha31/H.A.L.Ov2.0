import cv2
import imutils
import numpy as np
from scipy import signal
from scipy.fftpack import fft
import numpy as np
from scipy.fftpack import fftfreq
import matplotlib.pyplot as plt

import getvideo
import variables

video_capture = cv2.VideoCapture("rashiiii.mp4")
#video_capture.set(cv2.CV_CAP_PROP_FPS,60)
# Run the infinite loop
ret = True

while ret:
  try:
  # Read each frame
      ret, frame = video_capture.read()
      #print(frame.shape)
    #  if frame.empty():
    #      break;
      
      frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
      frame = imutils.rotate_bound(frame,90)
      # Convert frame to grey because cascading only works with greyscale image
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      # Call the detect function with grey image and colored frame
      canvas = detect(gray, frame)
      if cv2.waitKey(1) and 0xFF == ord('q'):
        break
  except AttributeError:
      break      
video_capture.release()
cv2.destroyAllWindows()

import getdifference
import detrend
import performfft
import plot

avg = ( max0 + max1 )/2  #calculates the average heartbeat of the blue and hue signal

import sendvalue
