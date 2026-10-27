import cv2

# Loading Haarcascade models
face_casc = cv2.CascadeClassifier("/home/vanshkumar8956/python_projects/OpenCV.py/Face_detection/haarcascade_frontalface_default.xml")
eye_casc = cv2.CascadeClassifier("/home/vanshkumar8956/python_projects/OpenCV.py/Images/Eye-Smile_detector.py/haarcascade_eye.xml")
Smile_casc = cv2.CascadeClassifier('/home/vanshkumar8956/python_projects/OpenCV.py/Images/Eye-Smile_detector.py/haarcascade_smile.xml')
# Web Camera access
Video = cv2.VideoCapture(0)

# Camera check
if not Video.isOpened():
    raise FileNotFoundError("Camera could not be opened!")
else:
    while True:
        ret, frames = Video.read()

        # Color conversion
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = face_casc.detectMultiScale(gray, 1.1, 5)
        for(x,y,w,h) in faces:
            cv2.rectangle(frames, (x,y), (x+w, y+h), (0,255,0),3)

        # seprating the rectangluar part from both frames by slicing
            gray_Roi = gray[y:y+h, x:x+w]
            color_Roi = frames[y:y+h, x:x+w]

            eye = eye_casc.detectMultiScale(gray_Roi, 1.1, 10)
            if len(eye) > 0 :
                for (ex, ey, ew, eh) in eye:
                    cv2.rectangle(
        color_Roi,
        (ex, ey),
        (ex + ew, ey + eh),
        (255, 0, 0),
        2
    )
                cv2.putText(frames,"Eyes detected",(x-5,y-30), cv2.FONT_HERSHEY_DUPLEX,1,255, 10)
            smile = Smile_casc.detectMultiScale(gray_Roi,1.7,20)
            if len(smile)>0:
                for (sx, sy, sw, sh) in smile:
                 cv2.rectangle(
        color_Roi,
        (sx, sy),
        (sx + sw, sy + sh),
        (0, 255, 255),
        2
    )
                cv2.putText(frames,"Smile detect", (x+w+5,y+h-30), cv2.FONT_HERSHEY_DUPLEX,1,255,10)

        cv2.imshow("Detecting_result", frames)

        if cv2.waitKey(1) & 0xff == ord(" "):
         break

Video.release()
cv2.destroyAllWindows()