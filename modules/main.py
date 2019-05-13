# Main file that calls the other modules and performs the task
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
import loadvideo
import getdifference
import detrend
import performfft
import plot
import sendvalue
