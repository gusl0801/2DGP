import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = './SDL2/x86'
else:
    os.environ["PYSDL2_DLL_PATH"] = './SDL2/x64'

import Game_Framework

import Logo_Scene

import Easy_Stage

Game_Framework.run(Logo_Scene)

#game_framework.run(scene_stage1)
