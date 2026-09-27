init:
    $ dimitri_clothing_options = ['b_dressed','b_empty']

init python:


    renpy.image('dimitri_arms_a_empty', 'ground.png')
    renpy.image('dimitri_body_b_empty', 'ground.png')
    renpy.image('dimitri_face_f_empty', 'ground.png')
    renpy.image('dimitri_face_talk_f_empty', 'ground.png')


    renpy.image('dimitri_face_talk_f_laugh', 'dimitri_face_f_laugh')
    renpy.image('dimitri_face_talk_f_surprised_down', 'dimitri_face_f_surprised_down')
    renpy.image('dimitri_cutscene15_face_talk_f_laugh', 'dimitri_cutscene15_face_f_laugh')



layeredimage dimitri:

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







    group face if_not 'm_talk' if_any dimitri_clothing_options auto

    group face if_not 'm_talk' if_any ('b_dressed_tied') auto:
        offset (-343, 151)











    group face if_all 'm_talk' if_any dimitri_clothing_options auto variant 'talk'

    group face if_all 'm_talk' if_any ('b_dressed_tied') auto variant 'talk':
        offset (-343, 151)







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'dimitri_arms_dressed_a_front'

    group arms if_all 'b_dressed_tied' auto variant 'dressed_tied':
        attribute a_idle default 'dimitri_arms_dressed_tied_a_down'






    group overlay auto:
        attribute o_empty default null


layeredimage dimitri cutscene12:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk'

layeredimage dimitri cutscene14:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk'

    group arms auto:
        attribute a_empty null

layeredimage dimitri cutscene15:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk'


image dimitri_f = "characters/dimitri/dimitri_face_f_normal.png"


image dimitri_cutscene14_arms_a_knife:
    'dimitri_cutscene14_arms_a_knife1'
    .6
    block:
        'dimitri_cutscene14_arms_a_knife2' with dissolve
        .6
        'dimitri_cutscene14_arms_a_knife1' with dissolve
        .6
        repeat 2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
