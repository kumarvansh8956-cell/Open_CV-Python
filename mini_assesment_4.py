# camera program
import cv2


Name = input("Enter the name for result: ")
operation = int(input("""
Pick the your operation:
1 -> Image Capture
2 -> Video Capture

"""))

camera = cv2.VideoCapture(0)

h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
f = cv2.VideoWriter_fourcc(*"mp4v")
New_name = Name + ".mp4"

Video = cv2.VideoWriter(New_name,f,60,(w,h))

while True:
    succ,frame = camera.read()
    if not succ:
        print("ERROR: Camera access denied")
        break
    else:
        if operation == 2:
         
            Video.write(frame)
            cv2.imshow("E: RECORDING", frame)

            if cv2.waitKey(1) & 0xFF == ord("s"):
                print(" done, Video is saved in device")
                break
        if operation == 1:
            New_name2 = Name + ".jpg"
            
            cv2.imshow("image", frame)
            if cv2.waitKey(1) & 0xFF == ord("s"):
             cv2.imwrite(New_name2,frame)
             print("Image capture")
             break
        else:
            print("Invalid operation")
            break


camera.release()
cv2.destroyAllWindows()




