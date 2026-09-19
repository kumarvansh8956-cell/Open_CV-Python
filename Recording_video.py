import cv2
camera = cv2.VideoCapture(0)

# cv2.VideoWriter(filename, fourcc, fps, frameSize)
"""
        filename = name for file or path


        furcc = this tell cv2 which formate to write the vedio
        example = cv2.VideoWriter_fourcc(*"mp4v")

        fps = frames per second integer
        frameSize = video framesize

"""
     

h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
size = (h,w)
fora =  cv2.VideoWriter_fourcc(*"mp4v")

record = cv2.VideoWriter("output.mp4", fora, 40, size)

while True:
    success,frame =  camera.read()
    if not success:
        print("Failed to load the footage")
        break
    else:
        record.write(frame)
        cv2.imshow("LIVE_RECORDING", frame )

    if cv2.waitKey(1) & 0xFF == ord("z"):
        print("Recording done~")
        break
camera.release()
cv2.destroyAllWindows()

        