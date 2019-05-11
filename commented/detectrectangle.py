def detect(gray, frame): # Input of this method is a greyscale image or frame which is obtained from the video stream 
 
  # Now get the tuples that detect the faces using above cascade
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    
    # Detect eyes now
    eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)
    
    # Now draw rectangle over the eyes
    for (ex, ey, ew, eh) in eyes:
      hx=ex
      hy=ey-30
      hw=ex+ew
      hh=ey+eh-30
    try:
        roi = roi_color[hy-20:hh-30,hx-15:(2*hw)+45]
        cv2.imshow("roi",roi)
        b,g,r = cv2.split(roi)
        bl = np.mean(b)
        re = np.mean(r)
        gr = np.mean(g)
        blue.append(bl)
        red.append(re)
        green.append(gr)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        h, s, v = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
        hu = np.mean(h)
        sa = np.mean(s)
        va = np.mean(v)
        hue.append(hu)
        saturation.append(sa)
        value.append(va)
     
        # set blue and green channels to 0
        cv2.imshow("blue",b)
        cv2.imshow("red",r)
        cv2.imshow("green",g)
        return roi
    except UnboundLocalError:
        pass
#Output is a frame which contains a rectangle box around the person's face
