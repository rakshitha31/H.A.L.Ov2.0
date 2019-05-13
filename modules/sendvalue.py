import math
from firebase import firebase

sendvalue(): # Function to send the average value of heartrate to firebase
  firebase=firebase.FirebaseApplication('https://halo2-1ce47.firebaseio.com/')
  result = firebase.put('/Patients/Lohith','heartRate',math.ceil(avg))
  avg = ( max0 + max1 )/2  #calculates the average heartbeat of the blue and hue signal

sendvalue()
