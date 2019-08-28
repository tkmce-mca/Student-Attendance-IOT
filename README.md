# Student-Attendance-IOT
A guide to face detection in python

	PRE-REQUISITES

•	Face recognition using deep learning
•	Introduction to FaceNet algorithm
•	Use of Pycharm
•	Basic knowledge of Deep face
•	Open CV Introduction link

        https://youtu.be/kdLM6AOd2vc                                             
        https://realpython.com/courses/traditional-face-detection-python/
        https://towardsdatascience.com/a-guide-to-face-detection-in-python-3eab0f6b9fc1
   
   REQUIREMENTS 
   
   Install cmake
   Install dlib
   Install packages for Face Detection
    
	// commands
	pip install opencv-python
	pip install dlib
    
	//link
	https://towardsdatascience.com/a-guide-to-face-detection-in-python-3eab0f6b9fc1
    
    PYTHON CODE FOR REAL TIME FACE DETECTION
    
    import cv
	import matplotlib.pyplot as plt
	import dlib
	from imutils import face_utils
	font = cv.FONT_HERSHEY_SIMPLEX
	cascPath = "/usr/local/lib/python3.7/site-packages/cv/data/haarcascade_frontalface_default.xml"
	eyePath = "/usr/local/lib/python3.7/site-packages/cv/data/haarcascade_eye.xml"
	smilePath = "/usr/local/lib/python3.7/site-packages/cv/data/haarcascade_smile.xml"
	faceCascade = cv.CascadeClassifier(cascPath)
	eyeCascade = cv.CascadeClassifier(eyePath)
	smileCascade = cv.CascadeClassifier(smilePath)
	gray = cv.imread('face_detect_test.jpeg', 0)
	plt.figure(figsize=(12,8))
	plt.imshow(gray, cmap='gray')
	plt.show()
    faces=faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,flags=cv.CASCADE_SCALE_IMAGE)
	for (x, y, w, h) in faces:
	    cv.rectangle(gray, (x, y), (x+w, y+h), (255, 255, 255), 3)
	    plt.figure(figsize=(12, 8))
	    plt.imshow(gray, cmap='gray')
	    plt.show()
        
        

PYTHON CODE FOR CONNECTING A WEB APPLICATION WITH A WEB CAM

    import cv2
	import sys
	cascPath = sys.argv[1]
	faceCascade = cv2.CascadeClassifier(cascPath)
	video_capture = cv2.VideoCapture(0)
	
	while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE

	 
	
	    # Draw a rectangle around the faces
	    for (x, y, w, h) in faces:
	        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	    # Display the resulting frame
	    cv2.imshow('Video', frame)
	
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        Break
	
	# When everything is done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()

      



      
