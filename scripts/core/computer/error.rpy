init python hide:
    '''
    This sets up the exception screen for the Saga metagame on the
    various PCs. It reuses the real Ren'Py exception screen to provide
    a realistic looking screen full of easter eggs.
    '''

    from copy import copy
    from textwrap import dedent

    from renpy.display.screen import ScreenDisplayable, get_screen_variant
    from renpy.store import Fixed, NullAction, Transform

    from store.util import struct


    stack = dedent('''\
        While running game code:
          File "game/bedroom.rpy", line 12, in script call
            call click()
          File "game/bedroom.rpy", line 26, in script
            call screen bedroom()
          File "renpy/common/000statements.rpy", line 531, in execute_call_screen
            store._return = renpy.call_screen(name, *args, **kwargs)
        NameError: name 'click' is not defined
    ''')

    error = dedent('''\
        Message DarkCookie if you have received this error.
        (He loves bug reports)
    ''')

    noop = NullAction()

    scope = {'config': struct(version='0.0.7-goldeneye', developer=False),
             'renpy': struct(platform='AsbestOS-3.1', version_only='6.99.11'),
             'full': error,
             'ignore_action': noop,
             'reload_action': noop,
             'rollback_action': noop,
             'short': stack,
             'traceback_fn': None}

    scr = copy(get_screen_variant('_exception')) 
    scr.modal = 'False'
    scr.sensitive = 'False'

    d = ScreenDisplayable(scr, None, None, scope=scope)

    renpy.image('pc_saga_ex', Transform(Fixed(d, xysize=(800, 525)), zoom=.64))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
