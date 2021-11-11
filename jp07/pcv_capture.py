import sys
import time

import numpy as np
import open3d as o3d

from camera import RGBDCamera

save_dir = sys.argv[1]
camera = RGBDCamera(640, 480, 640, 480)
vis = o3d.visualization.VisualizerWithKeyCallback()
vis.create_window()


def callback_quit(vis):

    status['kill'] = True


vis.register_key_callback(81, callback_quit)
pcd = o3d.geometry.PointCloud()
vis.add_geometry(pcd)

status = {'kill': False}
count = 0
while not status['kill']:
    tmp = camera.read_pcd()
    pcd.points = tmp.points
    pcd.colors = tmp.colors
    if count == 0:
        vis.add_geometry(pcd)
    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()
    fn = f'{save_dir}/{count:04d}.pcd'
    o3d.io.write_point_cloud(fn, pcd)
    count += 1
    time.sleep(0.1)
vis.destroy_window()
