import sys

import cv2

dir = sys.argv[1]
n = int(sys.argv[2])
t = int(sys.argv[3])
cap = cv2.VideoCapture(0)
for i in range(n):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite(f'{dir}/picture-{i:03d}.png', frame)
    cv2.waitKey(t)
cap.release()
cv2.destroyAllWindows()
