init:
    $ svetlana_clothing_options = ['b_bottom', 'b_dressed', 'b_naked', 'b_dressed_restrain_anon']

init python:


    renpy.image('svetlana_arms_a_empty', 'ground.png')
    renpy.image('svetlana_body_b_empty', 'ground.png')
    renpy.image('svetlana_face_f_empty', 'ground.png')
    renpy.image('svetlana_face_talk_f_empty', 'ground.png')


    renpy.image('svetlana_face_talk_f_laugh', 'svetlana_face_f_laugh')



layeredimage svetlana:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_bottom default
        attribute b_empty null
        attribute b_dressed_kiss


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any svetlana_clothing_options auto

    group face if_not 'm_talk' if_any 'b_dressed_pull_anon' auto:
        offset (-490, 0)











    group face if_all 'm_talk' if_any svetlana_clothing_options auto variant 'talk'

    group face if_all 'm_talk' if_any 'b_dressed_pull_anon' auto variant 'talk':
        offset (-490, 0)







    group arms if_all 'b_bottom' auto variant 'bottom':
        attribute a_idle default 'svetlana_arms_bottom_a_hips'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'svetlana_arms_naked_a_hips'


    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'svetlana_arms_dressed_a_hips'
        attribute a_baby 'svetlana_arms_dressed_a_baby_[M_nadya.pregnancy.baby_gender]'


    group overlay auto:
        attribute o_empty default null

image svetlana_f = "characters/svetlana/svetlana_face_f_normal.png"


image svetlana_body_b_dressed_kiss:
    'svetlana_body_b_dressed_kiss1'
    .4
    'svetlana_body_b_dressed_kiss2'
    .4
    repeat


init image svetlana_furnace_blowjob_arms_a_rub:
    'svetlana_furnace_blowjob_arms_a_rub1'
    .4
    'svetlana_furnace_blowjob_arms_a_rub2'
    .4
    repeat


init python hide:
    count = 10
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('svetlana_furnace_doggy_body_b_anim', 'svetlana_furnace_doggy_body_b_anim'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_svetlana))


init python hide:
    count = 12
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('svetlana_furnace_blowjob_body_b_anim', 'svetlana_furnace_blowjob_body_b_anim'),
           ('svetlana_furnace_cowgirl_body_b_anim', 'svetlana_furnace_cowgirl_body_b_anim'))

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_svetlana))


layeredimage svetlana furnace_blowjob:
    attribute m_talk null

    group body auto:
        attribute b_base default

    group face if_all 'b_base' if_not 'm_talk' auto
    group face if_all 'b_base' if_any 'm_talk' auto variant 'talk':
        attribute f_normal default

    group arms if_all 'b_base' auto:
        attribute a_hold default

    group overlay if_all 'b_base' if_any 'a_hold' auto

    group overlay if_any ['f_sexy', 'f_sexy_back'] if_not 'm_talk' auto variant 'sexy'
    group overlay if_any ['f_sexy', 'f_sexy_back'] if_all 'm_talk' auto variant 'sexy_talk'


layeredimage svetlana furnace_cowgirl:
    at Transform(crop=(0, 0, config.screen_width, config.screen_height))

    attribute m_talk null

    group body auto:
        attribute b_base default

    group face if_all 'b_base' if_not 'm_talk' auto:
        align (.5, .5) offset (5, -17) rotate -1.45
    group face if_all 'b_base' if_any 'm_talk' auto variant 'talk':
        align (.5, .5) offset (5, -17) rotate -1.45

    group face if_all 'b_insert' if_not 'm_talk' auto
    group face if_all 'b_insert' if_any 'm_talk' auto variant 'talk':
        attribute f_normal default

    group dick if_all 'b_base' auto:
        attribute d_pre default

    group overlay auto


layeredimage svetlana furnace_doggy:
    attribute m_talk null

    group body auto:
        attribute b_insert default

    group face if_all 'b_insert' if_not 'm_talk' auto
    group face if_all 'b_insert' if_any 'm_talk' auto variant 'talk':
        attribute f_normal default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
