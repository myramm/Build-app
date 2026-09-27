init:
    $ ricky_clothing_options = ['b_dressed','b_speedo']

init python:


    renpy.image('ricky_arms_a_empty', 'ground.png')
    renpy.image('ricky_body_b_empty', 'ground.png')
    renpy.image('ricky_face_f_empty', 'ground.png')
    renpy.image('ricky_face_talk_f_empty', 'ground.png')


    renpy.image('ricky_face_talk_f_laugh', 'ricky_face_f_laugh')



layeredimage ricky:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_dressed_dance 'ricky_body_b_dressed_dance'


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any ricky_clothing_options auto


    group face if_not 'm_talk' if_any 'b_dressed_thinking' auto:
        offset (66, 22)


    group face if_not 'm_talk' if_any 'b_speedo_dance_pose' auto:
        offset (-140, 74)











    group face if_all 'm_talk' if_any ricky_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any 'b_dressed_thinking' auto variant 'talk':
        offset (66, 22)


    group face if_all 'm_talk' if_any 'b_speedo_dance_pose' auto variant 'talk':
        offset (-140, 74)







    group arms if_any ['b_dressed', 'b_speedo'] auto variant 'dressed':
        attribute a_idle default 'ricky_arms_dressed_a_hips'






    group overlay auto:
        attribute o_empty default null

image ricky_f = "characters/ricky/ricky_face_f_normal.png"

image ricky_body_b_dressed_dance:
    Transform("ricky_body_b_dressed_dance1")
    pause .4
    Transform("ricky_body_b_dressed_dance2")
    pause .4
    repeat

init python:
    for i in xrange(1, 3):
        renpy.image('ricky_body_b_speedo_dance {}'.format(i),
                    'ricky_body_b_speedo_dance{:02}'.format(i))

image ricky_body_b_speedo_dance = AnimatedImage('ricky_body_b_speedo_dance',
    (1, 2), M_ricky)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
