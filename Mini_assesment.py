import cv2
"""
Assesment:- Taking color image paths as input, this display it to user to confirmation if image is correct then convert it
into gray, display result for varification if user satisfied then asked name for file name and save the result with it  

"""

input_image = input("Please provide the colored Image :")
image = cv2.imread(input_image, cv2.IMREAD_UNCHANGED)

if image is None:
  print("ERROR: You did not provide any image ")

else:
  cv2.imshow("The given input is this ",image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  confirmation = input("Is you confirmation about the image? Give your answer in either Yes or No: ")
  if confirmation.lower == "no":
    print("Please try again with correct image")

  else:

    Gray_converstion = cv2.imread(input_image,cv2.IMREAD_GRAYSCALE)
    Satisfied = cv2.imshow("The Result",Gray_converstion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    Satisfaction = input(" Are you satisfied with result? Give your answer in either Yes or No :")
    if Satisfaction.lower == "no":
      print("Execution got interrupted due to dissatisfaction of user demands")
    else:
      New = input("Please decide the name for the new result with formate example- output.jpg :")
      cv2.imwrite(New,Gray_converstion)
      print('The result is save in sysem successfuly')
