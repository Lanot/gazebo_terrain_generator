from dataclasses import dataclass

@dataclass
class GazeboTile:
    path: str
    size_x: float
    size_y: float
    size_z: float
    pose_x: float
    pose_y: float
    pose_z: float

    def __init__(self, path: str,
                 size_x: float, size_y: float, size_z: float,
                 pose_x: float = 0, pose_y: float = 0, pose_z: float = 0):
        self.path = path
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        self.pose_x = pose_x
        self.pose_y = pose_y
        self.pose_z = pose_z
