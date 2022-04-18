#glob module to access all in the folder
import cv2, glob

all_images = glob.glob("*.jpg")#Exact Directory and file name here * means all images
#print(all_images)--check all the images

#Detecting Face
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for image in all_images:
    #reading the image
    img = cv2.imread(image)
    #converting to Gray Scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Detect Faces
    faces = detect.detectMultiScale(gray_img, 1.1, 5)

    #Creating Rectangle over the Face
    for (x, y, w, h) in faces:
        final_img = cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)


    #Show image
    cv2.imshow("Face Detection", final_img)

    #Wait Time-2000 milliseconds
    cv2.waitKey(2000)

    #Destroy the Windows
    cv2.destroyAllWindows()
