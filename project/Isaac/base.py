from enum import Enum # enum class 사용 python 3.4이상
import math

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Way:
    Left = 0
    Right = 1
    Down = 2
    Up = 3
    LeftUp = 4
    LeftDown = 5
    RightUp = 6
    RightDown = 7
    WayCount = 8

class MapType:
    Normal = 0
    Blood = 1
    Boss = 2

class ItemType:
    CommonCold = 0
    Martyr = 1

class RockShape:
    Size_oneByone1 = 0
    Size_oneByone2 = 1
    Size_oneByone3 = 2
    Size_oneByone4 = 3
    Size_oneByone5 = 4
    Size_oneByone6 = 5
    Size_twoByone = 6
    Size_oneBytwo = 7
    Size_twoBytwo = 8

class DungShape:
    Brown = 4
    Red = 3
    DarkBrown = 2
    Gold = 1
    Rainbow = 0

class RoomShape:
    Room_normal_one = 0

class RoomType:
    Room_Start = 0
    Room0 = 1
    Room1 = 2
    Room2 = 3
    Room3 = 4
    Room4 = 5
    Room_Boss_Monstro = 6
    Room_Item_CommonCold = 7
    Room_Item_Martyr = 8

def get_distance(x1, y1, x2,y2):
    return math.sqrt(math.pow(x1 - x2) + math.pow(y1 - y2))

def swap(a, b):
    tmp = a
    a = b
    b = tmp