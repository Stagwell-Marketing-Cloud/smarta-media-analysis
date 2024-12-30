from dataclasses import dataclass, asdict

@dataclass 
class GazeData:
    is_blinking: bool 
    is_right: bool
    is_left: bool 
    is_center: bool
    source_img: str
    brand_name: str

    def dict(self,):
        return asdict(self)