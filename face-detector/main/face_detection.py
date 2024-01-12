# Import libraries that will be used to detect faces
import cv2 as cv

# Read the image
img = cv.imread('face/test.jpg')

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Include the face detection model
haar_cascade = cv.CascadeClassifier('detection-model/haar_face.xml')

# Find faces using model
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

# Print the number of faces
print(f"Faces found: {len(faces_rect)}")

# Draw a green rectangle to show where the foud face is
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

# Show the image
cv.imshow('Faces found', img)

cv.waitKey(0)
