screen popup_rollback():
    modal True tag popup

    zorder 100

    use popup_warning():
        style_prefix 'rollback_popup'

        text _("The rollback feature is disabled in Summertime Saga to protect players from poor gameplay experiences.")
        text _("Details may be found below, but by choosing to enable it be aware that {b}you may encounter potentially game breaking issues{/b}.")
        text _("Known issues caused by rollback include:")
        text _("{space=20}- Quests resetting\n{space=20}- Item loss\n{space=20}- Financial ruin\n{space=20}- Character routes resetting\n{space=20}- and various others.")
        text _("If you {b}did not{/b} intentionally enable rollback and wish to avoid this risk, consider uninstalling any mods you may have installed.")
        text _("If you {b}did{/b} enable rollback on purpose, you now know the risks involved with doing so and can make an informed choice.")

    key 'dismiss' action Return()


style rollback_popup_text:
    line_spacing 2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
