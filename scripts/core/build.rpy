init -990 python:
    archives = []
    def create_archive(*args, **kwargs):
        global archives
        if len(args) > 1:
            archives.append(args[0])
            build.archive(*args, **kwargs)


    create_archive("audio", "all")
    create_archive("images", "all")
    create_archive("scripts", "all")
    create_archive("fonts", "all")
    create_archive("data", "all")


    build.directory_name = str(config.name) + "-" + str(config.version).replace(".", "-")
    build.executable_name = config.name
    build.include_update = False


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/hide/**', None)
    build.classify('**.md', None)
    build.classify('**.hqx', None)
    build.classify('game/**.rpy', None)
    build.classify('game/scripts/tests.rpyc', None)
    build.classify('build/', None)
    build.classify('contrib/', None)
    build.classify('tools/', None)


    build.classify('game/presplash.jpg', 'all')


    build.classify('game/**.ogg', 'audio')

    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')

    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/scripts/**.txt', 'scripts')

    build.classify('game/**.json', 'data')
    build.classify('game/**.pem', 'data')

    build.classify("game/fonts/*", "fonts")


    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
