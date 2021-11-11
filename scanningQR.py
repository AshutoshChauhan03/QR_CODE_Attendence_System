# Using base64 for encoding and decoding of qr image
import base64
# Using cv2 to open camera
import cv2
# Using pyzbar to capture qr code frame from video
import pyzbar.pyzbar as pyzbar
# Using time to sleep the camera functioning
import time


# List maintaining the attendance for runtime
names = []
# Opening the attendance file
output = open('attendance.txt', 'w')
# Message until the camera is opened
print("Opening Camera...")


# Function for putting the data into the file
def enterData(name):
    # Adding decode form of name to name list
    names.append(name)
    # Decoding the encoded name
    # Removing the starting extra 3 characters
    name = name[3:]
    base64_bytes = name.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    # Writing in Attendance file
    output.write(message + '\n')


# Function for if the data present or not
def checkData(data):
    data = str(data)
    if data in names:
        print("Attendance Already Done")
    else:
        enterData(data)
        print("Attendance Updated")


# Starting the webcam
capture = cv2.VideoCapture(0)
print("Put your QR Code in front of the camera")

while True:
    # returns two arguments status and frame
    _, frame = capture.read()
    # pyzbar.decode(frame) return a list containing data and other variables
    decodedObj = pyzbar.decode(frame)
    # Displaying the camera frame
    cv2.imshow('Frame', frame)
    # Making frame to close on pressing of key e
    if cv2.waitKey(1) & 0xFF == ord('e'):
        cv2.destroyAllWindows()
        break

    # Finding data variable in decodedObj list
    for obj in decodedObj:
        checkData(obj.data)
        time.sleep(1)

# Closing the file
output.close()