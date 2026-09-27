init:
    $ thotbot_clothing_options = ['b_dressed']

init python:


    renpy.image('thotbot_arms_a_empty', 'ground.png')
    renpy.image('thotbot_body_b_empty', 'ground.png')
    renpy.image('thotbot_face_f_empty', 'ground.png')
    renpy.image('thotbot_face_talk_f_empty', 'ground.png')


    renpy.image('thotbot_face_talk_f_laugh', 'thotbot_face_f_laugh')
    renpy.image('thotbot_face_talk_f_surprised', 'thotbot_face_f_surprised')
    renpy.image('thotbot_face_talk_f_surprised_down', 'thotbot_face_f_surprised_down')


    renpy.image('thotbot_face_f_error', 'thotbot_face_talk_f_error')

layeredimage thotbot:

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







    group face if_not 'm_talk' if_any thotbot_clothing_options auto


    group face if_not 'm_talk' if_any ['b_dressed_back'] auto:
        xzoom -1
        offset(-272,0)











    group face if_all 'm_talk' if_any thotbot_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_dressed_back'] auto variant 'talk':
        xzoom -1
        offset(-272,0)







    group arms if_any ['b_dressed','b_dressed_back'] auto variant 'dressed':
        attribute a_idle default 'thotbot_arms_dressed_a_down'
        attribute a_baby 'thotbot_arms_dressed_a_baby_[M_melonia.pregnancy.baby_gender]'






    group overlay auto:
        attribute o_empty default null

image thotbot_f = "characters/thotbot/thotbot_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
