label school_locker_report_dialogue:
    scene expression player.location.background_blur
    show screen school_locker_report()
    pause
    hide screen school_locker_report
    return


screen school_locker_report():
    sensitive False

    default offsets = {'french':  (523, 226),
                       'music':   (524, 318),
                       'art':     (526, 417),
                       'science': (527, 509),
                       'gym':     (529, 600)}

    fixed:
        align .5, .5
        fit_first True

        add 'objects/closeup_reportcard.png'

        frame:
            anchor .5, .5
            pos 307, 96
            has transform
            maxsize (300, 35)
            frame:
                minimum (300, 35)
                text '[firstname]':
                    align .5, 1.
                    color 'fff'
                    text_align .5
                    size 24

        for k, v in player.grades.items():
            add 'buttons/report_card_0{}.png'.format(v):
                anchor .5, .5
                pos offsets[k]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
