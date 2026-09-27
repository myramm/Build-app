init -10 python:
    class Achievement(object):
        def __init__(self, nameid):
            self.nameid = nameid
            self.id = store.achievements_json[nameid]["id"]
            self.name = store.achievements_json[nameid]["name"]
            self.description = store.achievements_json[nameid]["description"]
            self.l_image = "cellphone/phone_feats_locked.png"
            self.image = store.achievements_json[self.nameid]["image"]
            self.hidden = store.achievements_json[nameid]["hidden"]
            self.enabled = store.achievements_json[nameid]["enabled"]
        
        @property
        def displayable(self):
            if persistent.achievements[self.nameid]:
                return renpy.displayable(self.l_image)
            else:
                return renpy.displayable(self.image)
        
        def lock(self):
            persistent.achievements[self.nameid] = True
        
        def unlock(self):
            if persistent.achievements[self.nameid]:
                persistent.achievements[self.nameid] = False
                global game
                game.new_achievements = True
        
        @property
        def is_locked(self):
            return persistent.achievements.get(self.nameid, True)
        
        @property
        def is_unlocked(self):
            return not self.is_locked

    for nameid in store.achievements_json.keys():
        name = re.sub("-", "_", nameid) 
        exec("A_{} = Achievement('{}')".format(name, nameid))

    if persistent.achievements is None:
        persistent.achievements = {}

    deleted_achievements = {}
    for nameid in persistent.achievements.keys():
        if nameid not in store.achievements_json.keys():
            deleted_achievements[nameid] = persistent.achievements[nameid]

    for nameid in deleted_achievements.keys():
        del persistent.achievements[nameid]
    del deleted_achievements

    for achievement in [a for aname, a in globals().items() if isinstance(a, Achievement)]:
        if achievement.nameid not in persistent.achievements.keys():
            persistent.achievements[achievement.nameid] = True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
