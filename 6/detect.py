import sys

import cv2
import numpy as np
import tensorflow as tf

fn_model = sys.argv[1]
w, h, dir = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
conf = 0.5
labels = ['PAPER', 'ROCK', 'SCISSORS']
model = tf.keras.models.load_model(fn_model)
cap = cv2.VideoCapture(0)
c = 0

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, (w, h))
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    p = model.predict(np.array([img]))[0]
    i = np.argmax(p)
    r = labels[i] if p[i] > conf else 'OTHER'
    msg = f'{r} ({p[i]:.2f})'
    cv2.putText(frame, msg, (10, 30), cv2.FONT_HERSHEY_PLAIN,
                2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    cv2.imwrite(f'{dir}/result-{c:04d}.png', frame)
    c += 1
    key = cv2.waitKey(100) & 0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
