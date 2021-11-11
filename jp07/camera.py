import numpy as np
import open3d as o3d
import pyrealsense2 as rs


class RGBDCamera:
    def __init__(self, cw, ch, dw, dh):
        self.pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.depth, dw, dh, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, cw, ch, rs.format.rgb8, 30)
        profile = pipeline.start(config)
        align_to = rs.stream.color
        self.align = rs.align(align_to)

        # depth_sensor = profile.get_device().first_depth_sensor()
        # self.depth_scale = depth_sensor.get_depth_scale()

        # _, depth_frame = self.read_frame()
        # intr = depth_frame.profile.as_video_stream_profile().intrinsics
        # info = (cw, ch, intr.fx, intr.fy, intr.ppx, intr.ppy)
        # self.pci = o3d.camera.PinholeCameraIntrinsic(*info)

    def close(self):

        self.pipeline.stop()

    def read_frame(self):

        frames = self.pipeline.wait_for_frames()
        aligned_frames = self.align.process(frames)
        color_frame = aligned_frames.get_color_frame()
        depth_frame = aligned_frames.get_depth_frame()
        return [color_frame, depth_frame]

    def read(self):

        frames = self.read_frame()
        return [np.asarray(frame.get_data()) for frame in frames]

    # def read_pcd(self):
    #     color, depth = self.read()
    #     rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
    #         o3d.geometry.Image(color), o3d.geometry.Image(depth),
    #         depth_scale=1/self.depth_scale, convert_rgb_to_intensity=False)
    #     pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, self.pci)
    #     flip = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
    #     pcd.transform(flip)
    #     return pcd
