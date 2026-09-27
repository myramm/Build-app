init:
    $ jane_clothing_options = ['b_dressed']

init python:


    renpy.image('jane_arms_a_empty', 'ground.png')
    renpy.image('jane_body_b_empty', 'ground.png')
    renpy.image('jane_face_f_empty', 'ground.png')
    renpy.image('jane_face_talk_f_empty', 'ground.png')


    renpy.image('jane_face_talk_f_laugh', 'jane_face_f_laugh')
    renpy.image('jane_face_talk_f_surprised', 'jane_face_f_surprised')
    renpy.image('jane_face_talk_f_complain_down', 'jane_face_f_complain_down')



layeredimage jane:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    at Transform(crop=(0, 0, config.screen_width, config.screen_height))


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_dance "jane_body_b_dance"



    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any jane_clothing_options auto


    group face if_not 'm_talk' if_any ['b_dressed_look_back'] auto:
        xoffset 561 xzoom -1


    group face if_not 'm_talk' if_any ['b_dressed_bend'] auto:
        offset (-43, 20)











    group face if_all 'm_talk' if_any jane_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_dressed_look_back'] auto variant 'talk':
        xoffset 561 xzoom -1


    group face if_all 'm_talk' if_any ['b_dressed_bend'] auto variant 'talk':
        offset (-43, 20)







    group arms if_any ['b_dressed', 'b_dressed_look_back'] auto variant 'dressed':
        attribute a_idle default 'jane_arms_dressed_a_sides'


    group arms if_any ['b_dressed_bend'] auto variant 'dressed_bend':
        attribute a_idle default 'jane_arms_dressed_bend_a_whisper'


    group overlay auto:
        attribute o_empty default null

image jane_f = "characters/jane/jane_face_f_normal.png"

image jane_face_f_laugh_flip = im.Flip("characters/jane/jane_face_f_laugh.png",horizontal=True)
image jenny_face_f_laugh_flip = im.Flip("characters/jenny/layeredimage/jenny_face_f_laugh.png",horizontal=True)

image jane_body_b_dance1_laugh = Composite(
    (1024,768),
    (0,0), "jane_body_b_dance1",
    (245,135), "jane_face_f_laugh_flip",
    (-45,0), "jenny_face_f_laugh_flip")

image jane_body_b_dance2_laugh = Composite(
    (1024,768),
    (0,0), "jane_body_b_dance2",
    (245,118), "jane_face_f_laugh_flip",
    (-42,25), "jenny_face_f_laugh_flip")

image jane_body_b_dance:
    Transform("jane_body_b_dance1_laugh")
    pause .4
    Transform("jane_body_b_dance2_laugh")
    pause .4
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
