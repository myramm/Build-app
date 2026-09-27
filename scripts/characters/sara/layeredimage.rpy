init:
    $ sara_clothing_options = ['b_dressed']

init python:


    renpy.image('sara_arms_a_empty', 'ground.png')
    renpy.image('sara_body_b_empty', 'ground.png')
    renpy.image('sara_face_f_empty', 'ground.png')
    renpy.image('sara_face_talk_f_empty', 'ground.png')


    renpy.image('sara_face_talk_f_laugh', 'sara_face_f_laugh')
    renpy.image('sara_face_talk_f_surprised_down', 'sara_face_f_surprised_down')



layeredimage sara:

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







    group face if_not 'm_talk' if_any sara_clothing_options auto











    group face if_all 'm_talk' if_any sara_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'sara_arms_dressed_a_sides'


    group overlay if_any sara_clothing_options auto:
        attribute o_empty default null

image sara_f = "characters/sara/layeredimage/sara_face_f_normal.png"


init python hide:
    count = 8
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    stem = 'sara_sex_terry'
    for i in frames:
        renpy.image('{} {}'.format(stem, i),
                    'sara_sex_tower_anim{:02}'.format(i))

    renpy.image(stem, AnimatedImage(stem, frames, M_sara))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
