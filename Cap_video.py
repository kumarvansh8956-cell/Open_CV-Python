import cv2
ved = cv2.VideoCapture(0)

while True:
    Return, Frame = ved.read()
    """
    Return = True or False
    Frame = frames

    """
    if not Return:
        print("Frames is not loading. please check the camera")
        break
    else:
        cv2.imshow("Resultant footages", Frame)
    if cv2.waitKey(1) & 0xFF == ord("z"):
        print("Execution_done_CV2_closing")
        break
ved.release()
cv2.destroyAllWindows()