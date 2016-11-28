from pico2d import*

from Base import*
from pico2d import*

class SoundType:
    BGM = 0
    EFFECT = 1

class SoundKey:
    BGM_Easy_Stage = 0
    BGM_Normal_Stage = 1
    BGM_Hard_Stage = 2

    EFFECT_Normal_Tear    = 3
    EFFECT_Isaac_Attacked = 4
    EFFECT_Door_Unlock    = 5

"""
사운드 재생 관련 클래스입니다.
Key값을 넘겨서 원하는 사운드를 재생할 수 있습니다.
"""
class SoundManager:
    sounds = {}
    def __init__(self):
        pass

    def __del__(self):
        pass

    def add_sound(self, sound_path, type, key):
        if self.find_path(key) == False:
            if type == SoundType.BGM:
                SoundManager.sounds[key] = load_music(sound_path)
            elif type == SoundType.EFFECT:
                SoundManager.sounds[key] = load_wav(sound_path)

    def play(self, key, repeat = 1):
        SoundManager.sounds[key].play(repeat)

    def set_volume(self, key, volume = 64):
        SoundManager.sounds[key].set_volume(volume)

    def stop(self, key, type):
        if type not in (SoundType.BGM,):
            return
        SoundManager.sounds[key].stop()

    def find_path(self, key):
        if (key in SoundManager.sounds) == False:
            return False
        return True
