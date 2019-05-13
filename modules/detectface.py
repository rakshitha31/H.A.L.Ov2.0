# Load the Haar cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(gray, frame): #Function to find the face and the eyes of a person given the greyscale image from a video stream
  # Now get the tuples that detect the faces using above cascade
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  # faces are the tuples of 4 numbers
  # x,y => upperleft corner coordinates of face
  # width(w) of rectangle in the face
  # height(h) of rectangle in the face
  # grey means the input image to the detector
  # 1.3 is the kernel size or size of image reduced when applying the detection
  # 5 is the number of neighbors after which we accept that is a face
  
  # Now iterate over the faces and detect eyes
  for (x,y,w,h) in faces:
    #cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    # Arguements => image, top-left coordinates, bottomright coordinates, color, rectangle border thickness
    
    # we now need two region of interests(ROI) grey and color for eyes one to detect and another to draw rectangle
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    #headfore = frame[y-int(h/5):y-int(h/4), x+int(w/5):x+int(w/4)]
    #cv2.show(headfore)
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
  #returns the frame
  
detect()
