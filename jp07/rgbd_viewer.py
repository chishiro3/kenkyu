import sys

import cv2
import numpy as np

from camera import RGBDCamera

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
camera = RGBDCamera(640, 480, 640, 480)
while True:
    color, depth = camera.read()
    print(f'center depth[mm]:{depth[240,320]}', flush=True)
    image_c = cv2.cvtColor(color, cv2.COLOR_RGB2BGR)
    image_d = cv2.applyColorMap(
        cv2.convertScaleAbs(depth, alpha=alpha), cv2.COLORMAP_JET)
    images = np.hstack((image_c, image_d))
    cv2.imshow('realsense', images)
    key = cv2.waitKey(1)
    if key & 0xff == 27:
        break
cv2.destroyAllWindows()
camera.close()
