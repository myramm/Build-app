init python:
    crystal_clothing_options = [
        'b_dressed', 'b_dressed_leaning', 'b_pantless',
        'b_pantless_disheveled', 'b_topless', 'b_topless_boobless']

    renpy.image('crystal_arms_a_empty', 'empty')
    renpy.image('crystal_body_b_empty', 'empty')
    renpy.image('crystal_face_f_empty', 'empty')


layeredimage crystal:
    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.

    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_dressed_back_shake 'crystal_body_b_dressed_back_shake'

    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null

    group face if_not 'm_talk' if_any crystal_clothing_options auto

    group face if_not 'm_talk' if_any ['b_dressed_sitting'] auto:
        offset (103.2, 59)
        xzoom -1

    group face if_not 'm_talk' if_any ['b_pantless_sitting'] auto:
        offset (64.6, 89.2)
        xzoom -1

    group face if_all 'm_talk' if_any crystal_clothing_options auto variant 'talk'

    group face if_all 'm_talk' if_any ['b_dressed_sitting'] auto variant 'talk':
        offset (103.2, 59)
        xzoom -1

    group face if_all 'm_talk' if_any ['b_pantless_sitting'] auto variant 'talk':
        offset (64.6, 89.2)
        xzoom -1

    group overlay if_any ['b_pantless', 'b_pantless_disheveled'] auto variant 'pantless'

    group arms if_any ['b_dressed'] auto variant 'dressed':
        attribute a_idle default 'crystal_arms_dressed_a_beer'
        attribute a_beer_rub 'crystal_arms_dressed_a_beer_rub'

    group arms if_any ['b_dressed_sitting'] auto variant 'dressed_sitting':
        attribute a_idle default 'crystal_arms_dressed_sitting_a_beer'

    group arms if_any ['b_pantless_sitting'] auto variant 'pantless_sitting':
        attribute a_idle default 'crystal_arms_pantless_sitting_a_tired'

    group arms if_any ['b_dressed_leaning'] auto variant 'dressed_leaning':
        attribute a_idle default 'crystal_arms_dressed_leaning_a_beer'

    group arms if_any ['b_pantless'] auto variant 'topless':
        attribute a_idle default 'crystal_arms_topless_a_sides'

    group arms if_any ['b_pantless_disheveled'] auto variant 'topless_disheveled':
        attribute a_idle default 'crystal_arms_topless_disheveled_a_sides'

    group arms if_any ['b_topless'] auto variant 'topless':
        attribute a_idle default 'crystal_arms_topless_a_sides'

    group arms if_any ['b_topless_boobless'] auto variant 'topless_boobless':
        attribute a_idle default 'crystal_arms_topless_boobless_a_remove02'

    group overlay auto:
        attribute o_empty default null


image crystal_arms_dressed_a_beer_rub = anim.TransitionAnimation(
    'crystal_arms_dressed_a_beer_rub01', .9, dissolve,
    'crystal_arms_dressed_a_beer_rub02', .9, dissolve)

image crystal_body_b_dressed_back_shake = anim.TransitionAnimation(
    'crystal_body_b_dressed_back_shake01', .6, fastdissolve,
    'crystal_body_b_dressed_back_shake02', .6, fastdissolve)


image xray_crystal_trailer:
    Transform("characters/xray/xray_under_01.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_02.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_03.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_04.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_05.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_06.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_07.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_08.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_09.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_10.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_11.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_12.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_13.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_14.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_15.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_16.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_17.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 0.4
    Transform("characters/xray/xray_under_18.png", xzoom=-.8, yzoom=.8, rotate=40, xoffset=50, yoffset=100)
    pause 2.0
    linear 2.5 alpha 0


init python hide:
    frames = range(1, 11)
    for i in frames:
        renpy.image('crystal_sex_chair_anim {}'.format(i),
                    'crystal_body_b_sex_chair_anim{:02}'.format(i))

    renpy.image('crystal_sex_chair_anim', AnimatedImage(
        'crystal_sex_chair_anim', frames[-2:] + frames[:-2], M_crystal))


image crystal_sex_chair_cumshot:
    'crystal_body_b_sex_chair_cumshot01' with fastdissolve
    .4
    'crystal_body_b_sex_chair_cumshot02' with fastdissolve
    .4
    'crystal_body_b_sex_chair_cumshot03' with fastdissolve


image xray_crystal_sex_chair:
    anchor (.5, .5)
    pos (250 + 294, 250 + 138)
    rotate 288
    rotate_pad False
    xzoom -1
    zoom .68
    'xray_under'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
