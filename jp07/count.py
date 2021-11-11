import sys

import cv2
import numpy as np

from camera import RGBDCamera

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
save_dir = sys.argv[2]
camera = RGBDCamera(640, 480, 640, 480)
count = 0
i = 0
while True:
    color, depth = camera.read()
    print(f'center depth[mm]:{depth[240,320]}', flush=True)
    image_c = cv2.cvtColor(color, cv2.COLOR_RGB2BGR)
    image_d = cv2.applyColorMap(
        cv2.convertScaleAbs(depth, alpha=alpha), cv2.COLORMAP_JET)
    images = np.hstack((image_c, image_d))
    msg = f'COUNT:{count}'
    cv2.putText(images, msg, (10, 30), cv2.FONT_HERSHEY_PLAIN,
                2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('realsense', images)
    cv2.imwrite(f'{save_dir}/{i:04d}.png', images)
    i += 1
    key = cv2.waitKey(1)
    if key & 0xff == 27:
        break
cv2.destroyAllWindows()
camera.close()
