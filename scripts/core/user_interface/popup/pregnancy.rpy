screen popup_pregnancy():
    modal True tag popup

    zorder 100

    use popup_warning():
        text _("Pregnancy in {b}Summertime Saga{/b} carries serious consequences!")
        text _("Most stories will not advance if the character(s) involved are pregnant, and some of the girls won't have sex with you again until after the child is born!")
        text _("So think carefully before cumming inside them, or use contraceptives until you're positive you're ready!")

    key 'dismiss' action Hide('popup')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
