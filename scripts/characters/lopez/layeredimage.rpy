init:
    $ lopez_clothing_options = ['b_dressed','b_naked','b_towel','b_toweldown']

init python:


    renpy.image('lopez_arms_a_empty', 'ground.png')
    renpy.image('lopez_body_b_empty', 'ground.png')
    renpy.image('lopez_face_f_empty', 'ground.png')
    renpy.image('lopez_face_talk_f_empty', 'ground.png')


    renpy.image('lopez_face_talk_f_laugh', 'lopez_face_f_laugh')
    renpy.image('lopez_face_talk_f_surprised', 'lopez_face_f_surprised')
    renpy.image('lopez_face_talk_f_surprised_right', 'lopez_face_f_surprised_right')
    renpy.image('lopez_face_talk_f_surprised_down_down', 'lopez_face_f_surprised_down_down')
    renpy.image('lopez_face_talk_f_surprised_down', 'lopez_face_f_surprised_down')


    renpy.image('lopez_face_f_angry_left', 'lopez_face_talk_f_angry_left')

layeredimage lopez:

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







    group face if_not 'm_talk' if_any lopez_clothing_options auto











    group face if_all 'm_talk' if_any lopez_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'lopez_arms_dressed_a_hips'


    group arms if_any ['b_towel','b_toweldown'] auto variant 'towel':
        attribute a_idle default 'lopez_arms_towel_a_hips'






    group overlay auto:
        attribute o_empty default null

image lopez_f = "characters/lopez/lopez_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
