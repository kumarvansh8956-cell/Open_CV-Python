import cv2

# Loading Haarcascade frontalface default model
face_casc = cv2.CascadeClassifier("/home/vanshkumar8956/python_projects/OpenCV.py/Face_detection/haarcascade_frontalface_default.xml")

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
        # Face detections
        face = face_casc.detectMultiScale(
            gray, 1.1, 5
        )

        # Rectangle Constructions on face detection
        for (x,y,w,h) in face:
            cv2.rectangle(frames, (x,y), (x+w, y+h), (255,0,0), 4)


        cv2.imshow("Detecting face",frames)
        if cv2.waitKey(1) & 0xFF == ord(" "):
            break
Video.release()
cv2.destroyAllWindows()