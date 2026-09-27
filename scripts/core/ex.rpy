init python early hide:






    from os import walk


    store.tainted = False

    arch = ('audio.rpa', 'data.rpa', 'fonts.rpa', 'images.rpa', 'scripts.rpa')
    ext = ('.rpa', '.rpy', '.rpyc')
    modded = any(f for _, _, ls in walk(config.gamedir)
                   for f in ls if f.endswith(ext) and not f in arch)
    original = renpy.display.error.call_exception_screen


    def call_exception_screen(screen_name, **kwargs):
        if screen_name == '_exception':
            version = '{} ({}-{})'.format(
                config.version,
                getattr(store, '_version', '0'),
                ''.join(('c' * config.console,
                         'd' * config.developer,
                         'l' * int(not(config.script_version)),
                         't' * store.tainted,
                         'u' * modded)))
            
            kwargs['config'] = util.struct(developer=config.developer,
                                           version=version)
        return original(screen_name, **kwargs)


    renpy.display.error.call_exception_screen = call_exception_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
