init:
    $ bridget_clothing_options = ['b_dressed', 'b_naked', 'b_lucha', 'b_lingerie', 'b_empty']

init python:


    renpy.image('bridget_arms_a_empty', 'ground.png')
    renpy.image('bridget_body_b_empty', 'ground.png')
    renpy.image('bridget_face_f_empty', 'ground.png')
    renpy.image('bridget_face_talk_f_empty', 'ground.png')


    renpy.image('bridget_face_talk_f_laugh', 'bridget_face_f_laugh')
    renpy.image('bridget_face_talk_f_surprised', 'bridget_face_f_surprised')
    renpy.image('bridget_face_talk_f_angry_yell', 'bridget_face_f_angry_yell')
    renpy.image('bridget_face_talk_f_laughing_hold', 'bridget_face_f_laughing_hold')
    renpy.image('bridget_face_talk_f_suspicious_right', 'bridget_face_f_suspicious_right')


    renpy.image('bridget_face_f_angry_down', 'bridget_face_talk_f_angry_down')
    renpy.image('bridget_face_f_pleased_down', 'bridget_face_talk_f_pleased_down')
    renpy.image('bridget_face_f_pleased_down_left', 'bridget_face_talk_f_pleased_down_left')
    renpy.image('bridget_face_f_suspicious', 'bridget_face_talk_f_suspicious')


    renpy.image('bridget_face_f_lily_lucha_hug_normal', 'bridget_face_f_lily_lucha_hug_normal')
    renpy.image('bridget_face_talk_f_lily_lucha_hug_normal', 'bridget_face_talk_f_lily_lucha_hug_normal')


    renpy.image('bridget_overlay_o_lily_lucha_hug_mask', 'bridget_overlay_o_lily_lucha_hug_mask')

layeredimage bridget:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any bridget_clothing_options auto


    group face if_not 'm_talk' if_all 'b_bend' auto:
        offset (-108, 260)











    group face if_all 'm_talk' if_any bridget_clothing_options auto variant 'talk'


    group face if_all ['m_talk', 'b_bend'] auto variant 'talk':
        offset (-108, 260)







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'bridget_arms_dressed_a_crossed'


    group arms if_any 'b_lucha' auto variant 'lucha':
        attribute a_idle default 'bridget_arms_lucha_a_hips'


    group arms if_any 'b_lingerie' auto variant 'lingerie':
        attribute a_idle default 'bridget_arms_lingerie_a_hips'


    group arms if_any 'b_naked' auto variant 'naked':
        attribute a_idle default 'bridget_arms_naked_a_hips'


    group overlay auto:
        attribute o_empty default null

image bridget_f = "characters/bridget/bridget_face_f_normal.png"


image bridget_face_f_lily_lucha_hug_normal = Image("characters/bridget/bridget_face_f_normal.png",xoffset=-90,yoffset=-2)
image bridget_face_talk_f_lily_lucha_hug_normal = Image("characters/bridget/bridget_face_talk_f_normal.png",xoffset=-90,yoffset=-2)


image bridget_overlay_o_lily_lucha_hug_mask = Image("characters/bridget/bridget_overlay_o_mask.png",xoffset=-90,yoffset=-2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
