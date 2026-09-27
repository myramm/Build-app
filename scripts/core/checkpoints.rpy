
define config.autosave_frequency = None
define config.autosave_on_choice = False
define config.autosave_slots = 6


default last_checkpoint = 0


init python:
    def checkpoint():
        marker = len(fsm_data.machine_triggers)
        if marker > store.last_checkpoint:
            if renpy.config.skipping or len(renpy.game.contexts) > 1:
                return
            store.last_checkpoint = marker
            renpy.force_autosave(True, True)


init python hide:
    def checkpoint_name(j):
        name = j.get('_save_name')
        
        if name:
            return
        
        with suppress(Exception):
            m = machines[fsm_data.machine_triggers[-1][0]]
            name = '{} - Day {}\n{} ({}%) - {}'.format(
                firstname,
                game.timer.game_day(),
                m._name.title(),
                m.progress,
                ' '.join(m._state._name.split('_')[2:]).title())
            j.update({'_save_name': name})

    config.save_json_callbacks.append(checkpoint_name)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
