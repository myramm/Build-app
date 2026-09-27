init:
    $ ivy_clothing_options = ['b_dressed','b_naked']

init python:


    renpy.image('ivy_arms_a_empty', 'ground.png')
    renpy.image('ivy_body_b_empty', 'ground.png')
    renpy.image('ivy_face_f_empty', 'ground.png')
    renpy.image('ivy_face_talk_f_empty', 'ground.png')


    renpy.image('ivy_face_talk_f_laugh', 'ivy_face_f_laugh')
    renpy.image('ivy_face_talk_f_surprised', 'ivy_face_f_surprised')
    renpy.image('ivy_face_talk_f_surprised_down', 'ivy_face_f_surprised_down')



layeredimage ivy:

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







    group face if_not 'm_talk' if_any ivy_clothing_options auto


    group face if_not 'm_talk' if_any ['b_hug_vero','b_hug_vero_kiss'] auto:
        offset (-176, 0)


    group face if_not 'm_talk' if_any ['b_dressed_bend'] auto:
        offset (-51, 21)











    group face if_all 'm_talk' if_any ivy_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_hug_vero','b_hug_vero_kiss'] auto variant 'talk':
        offset (-176, 0)


    group face if_all 'm_talk' if_any ['b_dressed_bend'] auto variant 'talk':
        offset (-51, 21)







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'ivy_arms_dressed_a_front'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'ivy_arms_naked_a_sheet_cover'         


    group arms if_any ['b_dressed_bend'] auto variant 'dressed_bend':
        attribute a_idle default 'ivy_arms_dressed_bend_a_listen'


    group overlay auto:
        attribute o_empty default null

image ivy_f = "characters/ivy/layeredimage/ivy_face_f_normal.png"


init python hide:
    count = 12
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    stem = 'ivy_sex_jane'
    for i in frames:
        renpy.image('{} {}'.format(stem, i),
                    'ivy_sex_finger_anim{:02}'.format(i))

    renpy.image(stem, AnimatedImage(stem, frames, M_ivy))


init python hide:
    count = 12
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    stem = 'ivy_sex_vera'
    for i in frames:
        renpy.image('{} {}'.format(stem, i),
                    'ivy_sex_ass_anim{:02}'.format(i))

    renpy.image(stem, AnimatedImage(stem, frames, M_ivy))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
