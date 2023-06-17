import cv2

# Loading the image
image = cv2.imread("image.jpg")

# Getting the dimensions of the image
height, width = image.shape[:2]

# Converting the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Displaying the grayscale image
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)

# Cropping the image within a specific range
cropped_image = image[100:300, 200:400]

# Displaying the cropped image
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)

# Rotating the image
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Displaying the rotated image
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)

# Closing all windows
cv2.destroyAllWindows()
