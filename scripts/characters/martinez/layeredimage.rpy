init:
    $ martinez_clothing_options = ['b_dressed','b_undies','b_naked','b_towel','b_empty','b_empty_towel']

init python:


    renpy.image('martinez_arms_towel_a_empty', 'ground.png')
    renpy.image('martinez_body_b_empty', 'ground.png')
    renpy.image('martinez_body_b_empty_towel', 'ground.png')
    renpy.image('martinez_face_f_empty', 'ground.png')
    renpy.image('martinez_face_talk_f_empty', 'ground.png')


    renpy.image('martinez_face_talk_f_laugh', 'martinez_face_f_laugh')
    renpy.image('martinez_face_talk_f_eyeroll', 'martinez_face_f_eyeroll')
    renpy.image('martinez_face_talk_f_surprised_right', 'martinez_face_f_surprised_right')
    renpy.image('martinez_face_talk_f_surprised_down', 'martinez_face_f_surprised_down')
    renpy.image('martinez_face_talk_f_stinkeye', 'martinez_face_f_stinkeye')
    renpy.image('martinez_face_talk_f_smirk_down', 'martinez_face_f_smirk_down')
    renpy.image('martinez_face_talk_f_smirk_down2', 'martinez_face_f_smirk_down2')
    renpy.image('martinez_face_talk_f_sad_down', 'martinez_face_f_sad_down')
    renpy.image('martinez_face_talk_f_suspicious', 'martinez_face_f_suspicious')


    renpy.image('martinez_face_f_surprised_up', 'martinez_face_talk_f_surprised_up')
    renpy.image('martinez_face_f_normal_right', 'martinez_face_talk_f_normal_right')

layeredimage martinez:

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







    group face if_not 'm_talk' if_any martinez_clothing_options auto











    group face if_all 'm_talk' if_any martinez_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'martinez_arms_dressed_a_crossed'


    group arms if_any ['b_towel','b_naked','b_undies','b_empty_towel'] auto variant 'towel':
        attribute a_idle default 'martinez_arms_towel_a_crossed'






    group overlay auto:
        attribute o_empty default null

image martinez_f = "characters/martinez/martinez_face_f_normal.png"

image martinez_body_parts a_towel_hold_towel_pull1 = "characters/martinez/martinez_arms_towel_a_hold_towel_pull1.png"
image martinez_body_parts a_towel_hold_towel_pull2 = "characters/martinez/martinez_arms_towel_a_hold_towel_pull2.png"
image martinez_body_parts b_towelup = "characters/martinez/martinez_body_b_towelup.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
