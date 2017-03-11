import cv2
import random

imagePath = "appier.jpg"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

print(faceCascade)
# # Read the image
image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
   gray,
   scaleFactor=1.2,
   minNeighbors=5,
   minSize=(30, 30),
   flags = cv2.CASCADE_SCALE_IMAGE #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print(faces)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
	age = random.randint(18, 30)
	cv2.rectangle(image, (x + 3, y - 15), (x + 50, y - 50), (200, 187, 0), -1)
	cv2.putText(image, str(age), (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 187), 2)
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imwrite('./face.jpg', image)


# cv2.namedWindow('facedetect')
# cv2.imshow('facedetect', image)
# cv2.waitKey(0)
# cv2.destroyWindow('facedetect')	