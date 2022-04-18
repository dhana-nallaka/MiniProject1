import cv2

#to load classifier haarcascade_frontalface_default.xml
detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img=cv2.VideoCapture('mark1.jpg')#Imported Image
#read() returns 2 values True and False
#res-->First is true or false if the image is read it returns true else it returns false
#Img-->Second return value is the pixel dimensions of the image(Storing Image Coordinates)
res,img=imp_img.read()
#Converting into Gray Scale image since classifier is trained for gray scale imgs
#color Parameter is COLOR_BGR2GRAY
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detecting Faces of Different Images
#Three inputs of detectMultiscale Method-->Gray Scale,Resizing Command,Neighboring code

faces=detect.detectMultiScale(gray,1.3,5)

#faces return x,y,w,h where w=width and h=height

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

#imshow parameters-->Title of the Window and Image we wanted to show
cv2.imshow("Mark Image",img)

#3 steps 1.Wait Key,RElease of Image, Destroy Window
cv2.waitKey(0)#Can close anytime because argument is 0
imp_img.release()
cv2.destroyAllWindows()
