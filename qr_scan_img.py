import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

image = cv2.imread("qr_test.png")

decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    (x, y, w, h) = obj.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    data = obj.data.decode("utf-8")
    codeType = obj.type

    cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imshow("Frame", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
