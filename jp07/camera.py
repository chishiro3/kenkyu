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
