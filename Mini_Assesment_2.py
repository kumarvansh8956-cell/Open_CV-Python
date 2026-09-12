"""
Taking address of image as input from user,give user option of line, rectangle, circle and text, take input parameter according to user desires.
After then show the result to user asked for confirmation. if user satisfied with the result asked if user wants to save result? if yes save it otherwise erase it.

"""
import cv2
# Line formation
def line():
    print("coordinate must be provid in x,y formate")
    x,y =map(int, input(" Enter the coordinate of first point:").split(","))
    pt1 = (x,y)
    p,q =map(int, input(" Enter the coordinate of second point:").split(","))
    pt2 = (p,q)
    print("""
here the color formate is this (Blue,Green,Red). You can create countless combination by set the color shade 
Examples:

(0,0,0) is Black
(255, 0, 0) is Blue
(0, 255, 0) is Green
(0, 0, 255) is Red
(255,255,255) is White

""")
    b,g,r = map(int, input(" Pick the color:").split(","))
    color = (b,g,r)
    thick = int(input("Select the thickness. please choose the thickness in integer:"))
    cv2.line(img=image,pt1= pt1,pt2= pt2, color= color, thickness= thick)
    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def rectangle():
    print("coordinate must be provid in x,y formate")
    x,y =map(int, input(" Enter the coordinate of first point:").split(","))
    pt1 = (x,y)
    p,q =map(int, input(" Enter the coordinate of second point:").split(","))
    pt2 = (p,q)
    print("""
    here the color formate is this (Blue,Green,Red). You can create countless combination by set the color shade 
    Examples:
    
    (0,0,0) is Black
    (255, 0, 0) is Blue
    (0, 255, 0) is Green
    (0, 0, 255) is Red
    (255,255,255) is White
    
    """)
    b,g,r = map(int, input(" Pick the color:").split(","))
    color = (b,g,r)
    thick = int(input("Select the thickness. please choose the thickness in integer:"))
    cv2.rectangle(img=image,pt1= pt1,pt2= pt2, color= color, thickness= thick)
    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def circle():
    print("coordinate must be provid in x,y formate")
    x,y = map(int,input(" Enter the coordinate for the center of the circle:").split(","))
    center = (x,y)
    redius = int(input(" Enter the redius of circle in integer:"))
    print("""
here the color formate is this (Blue,Green,Red). You can create countless combination by set the color shade 
Examples:

(0,0,0) is Black
(255, 0, 0) is Blue
(0, 255, 0) is Green
(0, 0, 255) is Red
(255,255,255) is White

""")
    b,g,r = map(int, input(" Pick the color:").split(","))
    color = (b,g,r)
    thick = int(input("Select the thickness. please choose the thickness in integer:"))
    cv2.circle(img=image,center= center, radius= redius, color= color, thickness= thick)
    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def text():
    print("coordinate must be provid in x,y formate")
    Text = input(" Enter the Text:")
    x,y =map(int, input(" Enter the coordinate of first point:").split(","))
     
    (origin) =(x,y)
    print("""
here the color formate is this (Blue,Green,Red). You can create countless combination by set the color shade 
Examples:

(0,0,0) is Black
(255, 0, 0) is Blue
(0, 255, 0) is Green
(0, 0, 255) is Red
(255,255,255) is White

""")
    b,g,r = map(int, input(" Pick the color:").split(","))
    color = (b,g,r)
    thick = int(input("Select the fontsize. please choose the fontsize in integer:"))
    cv2.putText(img=image, text=Text , org=origin,fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=thick ,color=color)
    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def cropped():
    print("coordinate must be provid in x,y formate")
    x,y =map(int, input(" Enter the coordinate of first point:").split(","))
    pt1 = (x,y)
    p,q =map(int, input(" Enter the coordinate of second point:").split(","))
    pt2 = (p,q)
    crop = image[pt1,pt2]
    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Flip():
    print("""
The Flip optons is :
0. vertical flip (top to bottom)
1. horizontal flip (left to right)
-1. both at once
""")

    pick = int(input("pick your selections give in integer:"))
    cv2.flip(image, pick)
    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def roation():
    center = (w//2,h//2)
    angle =  int(input("Enter the rotational angle:"))
    zoom  = int(input("Zooming size:"))
    mat = cv2.getRotationMatrix2D(center=  center, angle= angle, scale= zoom)
    Rotate_img = cv2.warpAffine(image,mat,(w,h))

    cv2.imshow("Result", Rotate_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Mapping

mapping = {
  1:line,2:rectangle,3:circle,4:text,5:cropped,6:Flip,7:roation
  }

# Taking the input from user

Img_Address = input("Enter the address of the image : ")
image = cv2.imread(Img_Address)

if image is None:
    print("ERROR: Image is not founds")

else:
    confirmation = cv2.imshow("Provide_image",image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    con = input("Are you sure about input image? provide the Answer in yes or no: ")
    if con.lower is "no":
        print("ERROR: Try again with right image")
     
    else:
        h,w = image.shape[:2]
        print(f"The pixels length is {h} and Width is {w} of your image  ")

    print("""
 The available operations are:-
 1 for Line,
 2 for Rectangle,
 3 for Circle,
 4 for Add_Text,
 5 for Cropped,
 6 for Flip,
 7 for Rotation,

""")
    operation = int(input("Please select your operation: "))
    if operation not in mapping:
        print("ERROR: Unknow operation ")
    else:
        
        mapping[operation]()
        save =input("Want to save the result? (Yes/No)")
        
        if save.lower() != "yes":
            print("Image Manipulation done. result is not save~")
        else:
            NN= input("Enter the name for result:")
            fn = NN+".jpg"
            cv2.imwrite(fn,image)        
            
        
        
        
        

   