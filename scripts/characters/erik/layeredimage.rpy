init:
    $ erik_clothing_options = ['b_dressed','b_dressed_backpack', 'b_empty']

init python:


    renpy.image('erik_arms_a_empty', 'ground.png')
    renpy.image('erik_body_b_empty', 'ground.png')
    renpy.image('erik_face_f_empty', 'ground.png')
    renpy.image('erik_face_talk_f_empty', 'ground.png')


    renpy.image('erik_face_talk_f_laugh', 'erik_face_f_laugh')
    renpy.image('erik_face_talk_f_eat', 'erik_face_f_eat')



layeredimage erik:

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







    group face if_not 'm_talk' if_any erik_clothing_options auto


    group face if_not 'm_talk' if_any 'b_knees' auto


    group face if_not 'm_talk' if_any 'b_sidebed' auto:
        offset (68, -72)











    group face if_all 'm_talk' if_any erik_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any 'b_knees' auto variant 'talk'


    group face if_all 'm_talk' if_any 'b_sidebed' auto variant 'talk':
        offset (68, -72)






    group overlay_head auto:
        attribute oh_empty default null


    group arms:
        attribute a_empty null


    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'erik_arms_dressed_a_sides'


    group arms if_all 'b_knees' auto variant 'knees':
        attribute a_idle default 'erik_arms_knees_a_down'


    group arms if_all 'b_sidebed' auto variant 'sidebed':
        attribute a_idle default 'erik_arms_sidebed_a_down'






    group overlay if_not 'b_sidebed' auto:
        attribute o_empty default null

    group overlay if_all 'b_sidebed' auto variant 'sidebed':
        attribute o_empty default null

image erik_f = "characters/erik/layeredimage/erik_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
