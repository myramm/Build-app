init -100 python:
    class MoveTo(Action):
        def __init__(self, location, is_door=False, via=""):
            super(MoveTo, self).__init__()
            if not isinstance(location, Location):
                raise MoveToArgumentError(location)
            self.location = location
            self.is_door = is_door
            self.via = via
        
        def __call__(self):
            if self.is_door:
                sfxDoor()
            logger.info("MoveTo action called with destination {}".format(self.location.ref))
            is_locked = "locked" if self.location.locked else "unlocked"
            sound = random.choice(audio.doors[is_locked].get(self.via, (None,)))
            sound = "" 
            Location.future_location = None
            if sound:
                SoundManager.play_sound(SoundManager.get_sound_path(sound))
            game.unlock_ui()
            renpy.scene(layer='screens')
            renpy.call("global_lock_check", self.location)


    def BuyItem(item, buy_action=None, own_action=None):
        item = item if isinstance(item, Item) else Item(item)
        rv = []
        if player.has_item(item.name_id):
            if own_action:
                rv.append(own_action)
            rv.append(ShowPopup('dupe', item))
        else:
            if not player.has_money(item.cost):
                rv.append(ShowPopup('poor'))
            else:
                rv.append(Function(player.get_item, item.name_id))
                if buy_action:
                    rv.append(buy_action)
                rv.append(ShowPopup('give', item))
        return rv

    class TalkTo(Action):
        def __init__(self, character, force=False):
            super(TalkTo, self).__init__()
            if not isinstance(character, Machine):
                self.character = store.machines[character]
            else:
                self.character = character
            self.force = force
        
        def __call__(self):
            logger.info("TalkTo action called for character {}. Can talk : {}".format(self.character._name, self.character.can_talk))
            if not self.force and not self.character.can_talk:
                return
            
            player.last_baby_gender = self.character.pregnancy.baby_gender if self.character.pregnancy else "boy"
            player.location.hide_screen()
            
            
            
            renpy.jump(self.character.button_dialogue)

    class ClearPersistent(Action):
        def __init__(self):
            super(ClearPersistent, self).__init__()
        
        def __call__(self):
            lock_all_scenes()
            for a in persistent.achievements.keys():
                persistent.achievements[a] = True

    def GetItem(item):
        item = item if isinstance(item, Item) else Item(item)
        rv = [Function(player.get_item, item.name_id), ShowPopup('give', item)]
        if item.dialogue:
            rv.append(Jump(item.dialogue))
        return rv

    class ExitLocation(Action):
        def __init__(self, parent_index=0, is_door=False):
            super(ExitLocation, self).__init__()
            self.location = player.location.parents[parent_index]
            self.is_door = is_door
        
        def __call__(self):
            logger.info("ExitLocation action called with location {}. Can leave : {}".format(self.location.ref, self.location.can_leave))
            if self.location.can_leave:
                if self.is_door:
                    sfxDoor()
                game.unlock_ui()
                renpy.scene(layer='screens')
                renpy.call("global_lock_check", self.location)

    class HideAll(Action):
        def __call__(self):
            renpy.scene(layer='screens')

    class SelectMovie(Action):
        def __init__(self, movie_title="foxxy_roxxy"):
            super(SelectMovie, self).__init__()
            self.movie_title = movie_title
        
        def __call__(self):
            renpy.hide_screen("movie_options")
            renpy.call("movie_theatre_movie_select_after", self.movie_title)

    class TickTimer(Action):
        def __call__(self):
            game.timer.tick()
            renpy.scene(layer='screens')
            renpy.jump("game_main")

    class OpenBackpack(Action):
        def __call__(self):
            if renpy.get_screen("backpack") is not None:
                renpy.hide_screen("backpack")
                renpy.play("audio/sfx_phone_notification.ogg", "audio")
            else:
                renpy.show_screen("backpack")
                renpy.play("audio/sfx_backpack_open.ogg", "audio")
            renpy.restart_interaction()

    class MapAction(Action):
        def __call__(self):
            playMusic()
            playSound()
            if renpy.get_screen("town_map"):
                MoveTo(L_home_bedroom)()
            else:
                MoveTo(L_map)()

    class SetMachineVariable(Action):
        def __init__(self, machine, variable, value=None):
            super(SetMachineVariable, self).__init__()
            if isinstance(machine, str) or isinstance(machine, unicode):
                self.machine = store.machines[machine]
            else:
                self.machine = machine
            self.variable = variable
            self.value = value
        
        def __call__(self):
            self.machine.set(self.variable, self.value)

    class MarkLayerAvailable(Action):
        def __init__(self, layer):
            self.layer = layer
        def __call__(self):
            Game.available_ui_message_screens.add(self.layer)

    class MarkEasterEgg(Action):
        def __init__(self, easter_egg):
            self.egg = easter_egg
        
        def __call__(self):
            player.easter_eggs_discovered.append(self.egg)

    class MachineTrigger(Action):
        def __init__(self, trigger):
            self.trigger = trigger
        
        def __call__(self):
            global Machine
            Machine.trigger(self.trigger)

    class Sleep(Action):
        def __call__(self):
            renpy.call("sleep_lock_check")
            renpy.jump("game_main")

    def ShowPopup(*args, **kwargs):
        transition = kwargs.pop('transition', None)
        return Show('popup_proxy', transition, *args, **kwargs)

    class StartRecap(Action):
        def __call__(self):
            with renpy.file('scripts/data/official.log') as f:
                data = f.read()
            roots, log = renpy.loadsave.loads(data)
            log.unfreeze(roots, label='_after_load')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
