import random

class Way:
    Left = 0
    Right = 1
    Down = 2
    Up = 3

def Calculate_Door_Way(way):
    while True:
        temp = random.randint(0, 3)
        if way == Way.Left and temp != Way.Right:
            break;
        if way == Way.Right and temp != Way.Left:
            break;
        if way == Way.Up and temp != Way.Down:
            break;
        if way == Way.Down and temp != Way.Up:
            break;
    return temp

count = 0

while count < 15:
    way = random.randint(0, 3)
    count += 1;
    print("After Func : %d" % way)
    way = Calculate_Door_Way(way)
    print("Before Func : %d" % way)