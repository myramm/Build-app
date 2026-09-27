init:
    $ becca_clothing_options = ['b_dressed', 'b_panties_sweat', 'b_panties_sweat_cover', 'b_naked', 'b_pants', 'b_undies', 'b_towel', 'b_naked_disheveled']

init python:


    renpy.image('becca_arms_a_empty', 'ground.png')
    renpy.image('becca_body_b_empty', 'ground.png')
    renpy.image('becca_face_f_empty', 'ground.png')
    renpy.image('becca_face_talk_f_empty', 'ground.png')


    renpy.image('becca_face_talk_f_laugh', 'becca_face_f_laugh')
    renpy.image('becca_face_talk_f_shocked_down', 'becca_face_f_shocked_down')



layeredimage becca:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    at Transform(crop=(0, 0, config.screen_width, config.screen_height))


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_naked_disheveled_kiss


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any becca_clothing_options auto


    group face if_not 'm_talk' if_any ['b_home_bed', 'b_home_bed_undress', 'b_naked_bed', 'b_pants_bed'] auto:
        offset (-216, -79)


    group face if_not 'm_talk' if_any ['b_home_bed_back', 'b_naked_bed_back'] auto:
        offset (468, -69)
        xzoom -1


    group face if_not 'm_talk' if_any ['b_home_bed_read'] auto:
        rotate -38
        offset (-366, -63)


    group face if_not 'm_talk' if_any ['b_naked_disheveled_bed_mount'] auto:
        align (.5, .5)
        offset (-329, -262)
        rotate 35


    group face if_not 'm_talk' if_any ['b_naked_disheveled_bed_up'] auto:
        align (.5, .5)
        offset (-215, -38)
        rotate 10


    group face if_not 'm_talk' if_any ['b_naked_disheveled_bed_belly'] auto:
        align (.5, .5)
        offset (568, 427)
        rotate 37
        xzoom -1











    group face if_all 'm_talk' if_any becca_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_home_bed', 'b_home_bed_undress', 'b_naked_bed', 'b_pants_bed'] auto variant 'talk':
        offset (-216, -79)


    group face if_all 'm_talk' if_any ['b_home_bed_back', 'b_naked_bed_back'] auto variant 'talk':
        offset (468, -69)
        xzoom -1


    group face if_all 'm_talk' if_any ['b_home_bed_read'] auto variant 'talk':
        rotate -38
        offset (-366, -63)


    group face if_all 'm_talk' if_any ['b_naked_disheveled_bed_mount'] auto variant 'talk':
        align (.5, .5)
        offset (-329, -262)
        rotate 35


    group face if_all 'm_talk' if_any ['b_naked_disheveled_bed_up'] auto variant 'talk':
        align (.5, .5)
        offset (-215, -38)
        rotate 10


    group face if_all 'm_talk' if_any ['b_naked_disheveled_bed_belly'] auto variant 'talk':
        align (.5, .5)
        offset (568, 427)
        rotate 37
        xzoom -1







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'becca_arms_dressed_a_sides'


    group arms if_all 'b_panties_sweat' auto variant 'panties_sweat':
        attribute a_idle default 'becca_arms_panties_sweat_a_surprise'


    group arms if_any ['b_pants', 'b_undies'] auto variant 'pants':
        attribute a_idle default 'becca_arms_pants_a_sides'


    group arms if_any ['b_home_bed', 'b_home_bed_back'] auto variant 'home_bed':
        attribute a_idle default 'becca_arms_home_bed_a_front'


    group arms if_all 'b_home_bed_undress' auto variant 'naked_bed_undress':
        attribute a_idle default 'becca_arms_naked_bed_undress_a_remove_top01'


    group arms if_any ['b_naked_bed', 'b_naked_bed_back', 'b_pants_bed'] auto variant 'naked_bed':
        attribute a_idle default 'becca_arms_naked_bed_a_front'


    group arms if_all 'b_towel' auto variant 'towel':
        attribute a_idle default 'becca_arms_towel_a_sides'


    group arms if_any ['b_naked', 'b_naked_disheveled'] auto variant 'naked':
        attribute a_idle default 'becca_arms_naked_a_shy'


    group arms if_all 'b_naked_disheveled_bed_belly' auto variant 'naked_disheveled_bed_belly':
        attribute a_idle default 'becca_arms_naked_disheveled_bed_belly_a_down'


    group overlay if_not ['b_home_bed', 'b_home_bed_undress', 'b_naked_bed', 'b_pants_bed', 'b_home_bed_back', 'b_naked_bed_back', 'b_naked_disheveled_bed_belly', 'b_naked_disheveled_bed_up'] auto:
        attribute o_empty default null

    group overlay if_any ['b_home_bed', 'b_home_bed_undress', 'b_naked_bed', 'b_pants_bed'] auto:
        offset (-216, -79)

    group overlay if_any ['b_home_bed_back', 'b_naked_bed_back'] auto:
        offset (468, -69)
        xzoom -1

    group overlay if_any ['b_naked_disheveled_bed_up'] auto:
        align (.5, .5)
        offset (-215, -38)
        rotate 10

    group overlay if_any ['b_naked_disheveled_bed_belly'] auto:
        align (.5, .5)
        offset (568, 427)
        rotate 37
        xzoom -1

image becca_f = "characters/becca/layeredimage/becca_face_f_normal.png"





init python hide:
    stem = 'becca_sex_bedroom_anim'
    count = 9
    first = 6
    frames = tuple(i % count + 1 for i in xrange(first, first + count))
    for i in frames:
        renpy.image('{} {}'.format(stem, i),
                    'char_becca_sex_bed_{:02}'.format(i))
    renpy.image(stem, AnimatedImage(stem, frames, M_becca))

image becca_body_b_sex_bed_after_drip = renpy.display.anim.TransitionAnimation(
    'becca_body_b_sex_bed_after_drip01', .4, Dissolve(.2),
    'becca_body_b_sex_bed_after_drip02', .4, Dissolve(.2),
    'becca_body_b_sex_bed_after_drip03', .4, Dissolve(.2))

image becca_body_b_naked_disheveled_kiss = anim.TransitionAnimation(
    'becca_body_b_naked_disheveled_kiss01', .4, Dissolve(.2),
    'becca_body_b_naked_disheveled_kiss02', .4, Dissolve(.2))






image xray_becca_3some_beach:
    Transform("characters/xray/xray_top_01.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_02.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_03.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_04.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_05.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_06.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_07.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_08.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_09.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_10.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_11.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_12.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_13.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_14.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_15.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_16.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_17.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_18.png", zoom=.6, rotate=50, xoffset=230, yoffset=290)
    pause 2.0
    linear 2.5 alpha 0

image xray_becca_1o1_beach:
    Transform("characters/xray/xray_side_01.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-.8, yzoom=.8, rotate=80, xoffset=230, yoffset=20)
    pause 2.0
    linear 2.5 alpha 0


image xray_becca_sex_bedroom:
    anchor (.5, .5)
    pos (250 + 303, 250 + 223)
    rotate -60
    rotate_pad False
    xzoom -.65
    yzoom .65
    'xray_under'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
