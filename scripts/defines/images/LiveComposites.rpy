
image card_2 = ConditionSwitch(
    'M_erik.is_state(S_erik_card_needed)', 'objects/item_card2_quest.png',
    'True', 'objects/item_card2.png')
image card_2b = ConditionSwitch(
    'M_erik.is_state(S_erik_card_needed)', HoverImage('objects/item_card2_quest.png'),
    'True', HoverImage('objects/item_card2.png'))

image game_1 = ConditionSwitch(
    'M_kevin.is_state(S_kevin_get_seadogs)', 'objects/item_game1_quest.png',
    'True', 'objects/item_game1.png')
image game_1b = ConditionSwitch(
    'M_kevin.is_state(S_kevin_get_seadogs)', HoverImage('objects/item_game1_quest.png'),
    'True', HoverImage('objects/item_game1.png'))

image game_2 = ConditionSwitch(
    'M_erik.is_state(S_erik_vr_needed, S_erik_vr_buy_game)', 'objects/item_game2_quest.png',
    'True', 'objects/item_game2.png')
image game_2b = ConditionSwitch(
    'M_erik.is_state(S_erik_vr_needed, S_erik_vr_buy_game)', HoverImage('objects/item_game2_quest.png'),
    'True', HoverImage('objects/item_game2.png'))

image cosplay_1 = ConditionSwitch(
    'M_june.is_state(S_june_cosplay_ready)', 'objects/item_cosplay1_quest.png',
    'True', 'objects/item_cosplay1.png')
image cosplay_1b = ConditionSwitch(
    'M_june.is_state(S_june_cosplay_ready)', HoverImage('objects/item_cosplay1_quest.png'),
    'True', HoverImage('objects/item_cosplay1.png'))

image sex_6 = ConditionSwitch(
    "False", "objects/item_sex6_quest.png",
    "True", "objects/item_sex6.png")
image sex_6b = ConditionSwitch(
    "False", HoverImage("objects/item_sex6_quest.png"),
    "True", HoverImage("objects/item_sex6.png"))

image sex_17 = ConditionSwitch(
    "M_mia.is_state(S_mia_helen_outfit_request)", "objects/item_sex17_quest.png",
    "True", "objects/item_sex17.png")
image sex_17b = ConditionSwitch(
    "M_mia.is_state(S_mia_helen_outfit_request)", HoverImage("objects/item_sex17_quest.png"),
    "True", HoverImage("objects/item_sex17.png"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
