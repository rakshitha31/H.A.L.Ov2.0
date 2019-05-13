video_capture = cv2.VideoCapture("videoname.mp4")
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
      canvas = detectface(gray, frame)
      if cv2.waitKey(1) and 0xFF == ord('q'):
        break
  except AttributeError:
      break      
video_capture.release()
cv2.destroyAllWindows()
