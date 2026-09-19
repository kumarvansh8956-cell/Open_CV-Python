# A video recording camera 


import cv2

Name = input("Enter the name for the video: ")
New_name = Name + ".mp4"
camera = cv2.VideoCapture(0)

h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
f = cv2.VideoWriter_fourcc(*"mp4v")

Video = cv2.VideoWriter(New_name,f,60,(h,w))
while True:
    succ,frame = camera.read()
    if not succ:
        print("ERROR: Camera access denied")
        break
    else:
        Video.write(frame)
        cv2.imshow("E: RECORDING", frame)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        print("Recording done, result is saved n device")
        break

camera.release()
cv2.destroyAllWindows()




