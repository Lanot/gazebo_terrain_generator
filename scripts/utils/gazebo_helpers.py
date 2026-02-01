from dataclasses import dataclass

@dataclass
class GazeboDimensions:
    size_x: float
    size_y: float
    size_z: float
    pose_x: float
    pose_y: float
    pose_z: float

    def __init__(self,
                 size_x: float = 0, size_y: float = 0, size_z: float = 0,
                 pose_x: float = 0, pose_y: float = 0, pose_z: float = 0):
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        self.pose_x = pose_x
        self.pose_y = pose_y
        self.pose_z = pose_z


@dataclass
class GazeboTile(GazeboDimensions):
    path: str

    def __init__(self, path: str,
                 size_x: float = 0, size_y: float = 0, size_z: float = 0,
                 pose_x: float = 0, pose_y: float = 0, pose_z: float = 0):
        self.path = path
        super().__init__(size_x, size_y, size_z, pose_x, pose_y, pose_z)
    
    def from_dimensions(self, dim: GazeboDimensions):
        self.size_x = dim.size_x
        self.size_y = dim.size_y
        self.size_z = dim.size_z
        self.pose_x = dim.pose_x
        self.pose_y = dim.pose_y
        self.pose_z = dim.pose_z
        
        return self
