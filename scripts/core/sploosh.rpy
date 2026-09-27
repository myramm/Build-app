init python hide in sploosh:
    from json import load
    from random import choice

    from store import sploosh as export
    from renpy.exports import file


    with file('scripts/data/dialogues.json') as f:
        data = load(f)

    data = data.get('dialogues', [])

    if data:
        data.append(("There are currently {} dialogues written by our patrons!".format(len(data)),
                     "So sayeth the dev team..."))
    else:
        data.append(("I'm the king of the world!!!", "On a boat like Leo!"))


    def wake():
        export.message, export.author = choice(data)


    wake()
    export.wake = wake
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
