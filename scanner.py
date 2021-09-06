# Initial Scanner Code from https://www.hackster.io/gatoninja236/scan-qr-codes-in-real-time-with-raspberry-pi-a5268b

import cv2
import requests

# set up camera object
cap = cv2.VideoCapture(0)

# QR code detection object
detector = cv2.QRCodeDetector()

while True:
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)

    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(
                bbox[(i+1) % len(bbox)][0]), color=(255, 255, 0), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(
            bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        if data:
            print("data found: ", data)
            res = requests.put(data)
            # print content of response
            print(res.status_code)

            # check status code for response recieved
            # success code - 200
            if res.status_code == 200:
                for i in range(len(bbox)):
                    cv2.line(img, tuple(bbox[i][0]), tuple(
                        bbox[(i+1) % len(bbox)][0]), color=(0, 255, 0), thickness=4)
                cv2.putText(img, data, (int(bbox[0][0][0]), int(
                    bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                for i in range(len(bbox)):
                    cv2.line(img, tuple(bbox[i][0]), tuple(
                        bbox[(i+1) % len(bbox)][0]), color=(0, 0, 255), thickness=4)
                cv2.putText(img, "Error, Please Try Again", (int(bbox[0][0][0]), int(
                    bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # display the image preview
    cv2.imshow("QR Code Scanner", img)
    if(cv2.waitKey(1) == ord("q")):
        break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()
