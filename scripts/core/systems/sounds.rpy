init python:
    class SoundManager(object):
        music_channels = ["music", "music2", "music3"]
        sound_channels = ["sound", "sound2", "sound3"]
        
        @classmethod
        def channels(cls, types="all"):
            types = types.lower()
            if types == "all":
                rv = copy(cls.music_channels)
                rv.extend(cls.sound_channels)
                return rv
            elif types == "music":
                return cls.music_channels
            elif types == "sound":
                return cls.sound_channels
        
        @classmethod
        def stop(cls, fade=0.7):
            for channel in cls.channels():
                renpy.music.stop(channel, fadeout=fade)
        
        @classmethod
        def get_playing(cls, sound, channeltype="all"):
            sound = sound.lower()
            channeltype = channeltype.lower()
            if channeltype == "all":
                for channel in cls.sound_channels:
                    if renpy.sound.get_playing(channel).lower() == sound:
                        return True
                for channel in cls.music_channels:
                    if renpy.music.get_playing(channel).lower() == sound:
                        return True
                return False
            elif channeltype == "music":
                for channel in cls.music_channels:
                    if renpy.music.get_playing(channel).lower() == sound:
                        return True
                return False
            elif channeltype == "sound":
                for channel in cls.sound_channels:
                    if renpy.sound.get_playing(channel).lower() == sound:
                        return True
                return False
        
        @classmethod
        def get_free_channel(cls, channeltype="music"):
            if channeltype.lower() == "music":
                for channel in cls.music_channels:
                    if renpy.music.get_playing(channel, channeltype=channeltype) is None:
                        return channel
                renpy.music.stop("music")
                return "music"
            else:
                for channel in cls.sound_channels:
                    if renpy.sound.get_playing(channel, channeltype=channeltype) is None:
                        return channel
                renpy.music.stop("sound")
                return "sound"
        
        @classmethod
        def play_sound(cls, name = "", fade = 0.7, loop = True, multi = False):
            if not name:
                cls.stop(fade)
                return
            
            if cls.get_playing(name, channeltype="sound"):
                return
            
            if multi:
                renpy.music.play(name, cls.get_free_channel("sound"),
                                 loop=loop, fadein=fade)
            else:
                cls.stop(fade)
                renpy.music.play(name, "sound",
                                 loop=loop, fadein=fade)
        
        @classmethod
        def play_music(self, name = "", fade = 0.7, loop = True, multi = False):
            if not name:
                cls.stop(fade)
                return
            
            if cls.get_playing(name, channeltype="music"):
                return
            
            if multi:
                renpy.music.play(name, cls.get_free_channel("music"),
                                 loop=loop, fadein=fade)
            else:
                cls.stop(fade)
                renpy.music.play(name, "music",
                                 loop=loop, fadein=fade)
        
        @classmethod
        def door_sfx(self, locked=False):
            if locked:
                return "audio/sfx_door1_lock{}.ogg".format(random.randint(1,2))
            else:
                return "audio/sfx_door1_{}.ogg".format(random.randint(1,2))
        
        @classmethod
        def get_sound_path(cls, sound):
            if not sound:
                return ""
            rv = ""
            if not sound.startswith('audio/'):
                rv += 'audio/'
            rv += sound
            if not rv.endswith('.ogg'):
                rv += '.ogg'
            return rv


    def playSound(name = "", fade = 0.7, loop = True, multi = False):
        if name == "":
            renpy.music.stop("sound", fadeout = fade)
            renpy.music.stop("sound2", fadeout = fade)
            renpy.music.stop("sound3", fadeout = fade)
        elif renpy.sound.get_playing("sound") == name or renpy.sound.get_playing("sound2") == name or renpy.sound.get_playing("sound3") == name:
            return True
        elif not renpy.music.is_playing("sound") and renpy.sound.get_playing("sound") != name:
            if multi == False:
                renpy.music.stop("sound2", fadeout = fade)
                renpy.music.stop("sound3", fadeout = fade)
            renpy.music.play(name, "sound", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("sound2") and renpy.sound.get_playing("sound2") != name:
            if multi == False:
                renpy.music.stop("sound", fadeout = fade)
                renpy.music.stop("sound3", fadeout = fade)
            renpy.music.play(name, "sound2", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("sound3") and renpy.sound.get_playing("sound3") != name:
            if multi == False:
                renpy.music.stop("sound", fadeout = fade)
                renpy.music.stop("sound2", fadeout = fade)
            renpy.music.play(name, "sound3", loop = loop, fadein = fade)

    def getPlayingSound(name):
        if renpy.sound.get_playing("sound") == name or renpy.sound.get_playing("sound2") == name or renpy.sound.get_playing("sound3") == name:
            return False
        return True

    def playMusic(name = "", fade = 0.7, loop = True, multi = False):
        if name == "":
            renpy.music.stop("music", fadeout = fade)
            renpy.music.stop("music2", fadeout = fade)
            renpy.music.stop("music3", fadeout = fade)
        elif renpy.music.get_playing("music") == name or renpy.music.get_playing("music2") == name or renpy.music.get_playing("music3") == name:
            return True
        elif not renpy.music.is_playing("music") and renpy.music.get_playing("music") != name:
            if multi == False:
                renpy.music.stop("music2", fadeout = fade)
                renpy.music.stop("music3", fadeout = fade)
            renpy.music.play(name, "music", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("music2") and renpy.music.get_playing("music2") != name:
            if multi == False:
                renpy.music.stop("music", fadeout = fade)
                renpy.music.stop("music3", fadeout = fade)
            renpy.music.play(name, "music2", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("music3") and renpy.music.get_playing("music3") != name:
            if multi == False:
                renpy.music.stop("music", fadeout = fade)
                renpy.music.stop("music2", fadeout = fade)
            renpy.music.play(name, "music3", loop = loop, fadein = fade)

    def getPlayingMusic(name):
        if renpy.music.get_playing("music") == name or renpy.music.get_playing("music2") == name or renpy.music.get_playing("music3") == name:
            return False
        return True

    def sfxDoor(locked = False):
        if not locked:
            tmp = randomizer("audio/sfx_door1_{}.ogg", 1, 2)
        else:
            tmp = randomizer("audio/sfx_door1_lock{}.ogg", 1, 2)
        return tmp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
