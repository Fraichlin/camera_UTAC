import cv2, time
from detect_lines_COPY import detect

key = cv2. waitKey(1)
i=0
percentage = 0.52
while True:
	webcam = cv2.VideoCapture(0)
	check, frame = webcam.read()
	print(check)
	frame = frame[int(len(frame)*percentage):]
	cv2.imshow("Capturing", frame)
	filename="saved_img"+str(i)+".jpg"
	cv2.imwrite(filename='img/saved_img'+str(i)+'.jpg', img=frame)
	webcam.release()
	detect(filename)
	cv2.destroyAllWindows()
	i+=1
	time.sleep(3)
"""
	img_new = cv2.imshow("Captured Image", img_new)
	print("Processing image...")
	img_ = cv2.imread('saved_img'+str(i)+'.jpg', cv2.IMREAD_ANYCOLOR)
	print("Converting RGB image to grayscale...")
	gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
	print("Converted RGB image to grayscale...")
	print("Resizing image to 28x28 scale...")
	img_ = cv2.resize(gray,(28,28))
	print("Resized...")
	img_resized = cv2.imwrite(filename='saved_img-final'+str(i)+'.jpg', img=img_)
	print("Image saved!")
"""
