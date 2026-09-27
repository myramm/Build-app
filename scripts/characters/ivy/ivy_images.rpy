
image ivysex_10x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_10.png",
    (0,0), "characters/player/char_player_sex_36.png",
    )
image ivysex_11x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_11.png",
    (0,0), "characters/player/char_player_sex_37.png",
    )
image ivysex_11xc = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_11.png",
    (0,0), "characters/player/char_player_sex_38.png",
    )
image ivysex_18x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_18.png",
    (0,0), "characters/player/char_player_sex_39.png",
    )
image ivysex_19x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_19.png",
    (0,0), "characters/player/char_player_sex_40.png",
    )
image ivysex_19xc = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_19.png",
    (0,0), "characters/player/char_player_sex_41.png",
    )
image ivysex_20x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_20.png",
    (0,0), "characters/player/char_player_sex_40c.png",
    )
image ivysex_21x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_21.png",
    (0,0), "characters/player/char_player_sex_40b.png",
    )

image ivysex 10 = ConditionSwitch(
    "xray == True", "ivysex_10x",
    "xray == False", "characters/ivy/char_ivy_sex_10.png",
    "True", Null(),
    )
image ivysex 11 = ConditionSwitch(
    "xray == True and ivy_cum_inside == False", "ivysex_11x",
    "xray == True and ivy_cum_inside == True", "ivysex_11xc",
    "xray == False", "characters/ivy/char_ivy_sex_11.png",
    "True", Null(),
    )
image ivysex 18 = ConditionSwitch(
    "xray == True", "ivysex_18x",
    "xray == False", "characters/ivy/char_ivy_sex_18.png",
    "True", Null(),
    )
image ivysex 19 = ConditionSwitch(
    "xray == True and ivy_cum_inside == False", "ivysex_19x",
    "xray == True and ivy_cum_inside == True", "ivysex_19xc",
    "xray == False", "characters/ivy/char_ivy_sex_19.png",
    "True", Null(),
    )
image ivysex 20 = ConditionSwitch(
    "xray == True", "ivysex_20x",
    "xray == False", "characters/ivy/char_ivy_sex_20.png",
    "True", Null(),
    )
image ivysex 21 = ConditionSwitch(
    "xray == True", "ivysex_21x",
    "xray == False", "characters/ivy/char_ivy_sex_21.png",
    "True", Null(),
    )


image old_ivy 1 = "characters/ivy/char_ivy_01.png"
image old_ivy 2 = "characters/ivy/char_ivy_02.png"
image old_ivy 3 = "characters/ivy/char_ivy_03.png"
image old_ivy 4 = "characters/ivy/char_ivy_04.png"
image old_ivy 5 = "characters/ivy/char_ivy_05.png"
image old_ivy 6 = "characters/ivy/char_ivy_06.png"
image old_ivy 7 = "characters/ivy/char_ivy_07.png"
image old_ivy 8 = "characters/ivy/char_ivy_08.png"
image old_ivy 9 = "characters/ivy/char_ivy_09.png"
image old_ivy 10 = "characters/ivy/char_ivy_10.png"
image old_ivy 11 = "characters/ivy/char_ivy_11.png"
image old_ivy 12 = "characters/ivy/char_ivy_12.png"
image old_ivy 13 = "characters/ivy/char_ivy_13.png"
image old_ivy 14 = "characters/ivy/char_ivy_14.png"
image old_ivy 15 = "characters/ivy/char_ivy_15.png"
image old_ivy 16 = "characters/ivy/char_ivy_16.png"
image old_ivy 17 = "characters/ivy/char_ivy_17.png"
image old_ivy 18 = "characters/ivy/char_ivy_18.png"
image old_ivy 19 = "characters/ivy/char_ivy_19.png"
image old_ivy 20 = "characters/ivy/char_ivy_20.png"


image ivysex 1 = "characters/ivy/char_ivy_sex_01.png"
image ivysex 2 = "characters/ivy/char_ivy_sex_02.png"
image ivysex 3 = "characters/ivy/char_ivy_sex_03.png"
image ivysex 4 = "characters/ivy/char_ivy_sex_04.png"
image ivysex 5 = "characters/ivy/char_ivy_sex_05.png"
image ivysex 6 = "characters/ivy/char_ivy_sex_06.png"
image ivysex 7 = "characters/ivy/char_ivy_sex_07.png"
image ivysex 8 = "characters/ivy/char_ivy_sex_08.png"
image ivysex 9 = "characters/ivy/char_ivy_sex_09.png"



image ivysex 13 = "characters/ivy/char_ivy_sex_13.png"
image ivysex 14 = "characters/ivy/char_ivy_sex_14.png"
image ivysex 15 = "characters/ivy/char_ivy_sex_15.png"
image ivysex 16 = "characters/ivy/char_ivy_sex_16.png"
image ivysex 17 = "characters/ivy/char_ivy_sex_17.png"




image ivysex 22 = "characters/ivy/char_ivy_sex_22.png"

image ivysex 24 = "characters/ivy/char_ivy_sex_24.png"
image ivysex 25 = "characters/ivy/char_ivy_sex_25.png"
image ivysex 26 = "characters/ivy/char_ivy_sex_26.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
