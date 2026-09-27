init:
    $ khadne_clothing_options = ['b_bottom', 'b_casual', 'b_shirt', 'b_shirt_disheveled', 'b_shirt_leg']

init python:


    renpy.image('khadne_arms_a_empty', 'ground.png')
    renpy.image('khadne_body_b_empty', 'ground.png')
    renpy.image('khadne_face_f_empty', 'ground.png')
    renpy.image('khadne_face_talk_f_empty', 'ground.png')


    renpy.image('khadne_face_talk_f_laugh', 'khadne_face_f_laugh')



layeredimage khadne:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_bottom default
        attribute b_empty null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any khadne_clothing_options auto

    group face if_not 'm_talk' if_any 'b_casual_sit' auto:
        offset (-90, 38)
        xzoom -1

    group face if_not 'm_talk' if_any 'b_casual_sit_turn' auto:
        offset (-674, 35)

    group face if_not 'm_talk' if_any 'b_casual_sit_up' auto:
        offset (-2, -33)
        xzoom -1

    group face if_not 'm_talk' if_any 'b_casual_dragged_anon' auto:
        xoffset 35
        xzoom -1





    group face if_not 'm_talk' if_any 'b_casual_sit_sad' auto variant 'sit_sad'







    group face if_all 'm_talk' if_any khadne_clothing_options auto variant 'talk'

    group face if_all 'm_talk' if_any 'b_casual_sit' auto variant 'talk':
        offset (-90, 38)
        xzoom -1

    group face if_all 'm_talk' if_any 'b_casual_sit_turn' auto variant 'talk':
        offset (-674, 35)

    group face if_all 'm_talk' if_any 'b_casual_sit_up' auto variant 'talk':
        offset (-2, -33)
        xzoom -1

    group face if_all 'm_talk' if_any 'b_casual_dragged_anon' auto variant 'talk':
        xoffset 35
        xzoom -1





    group face if_all 'm_talk' if_any 'b_casual_sit_sad' auto variant 'sit_sad_talk'


    group overlay if_any khadne_clothing_options auto:
        attribute o_empty default null



    group arms if_all 'b_bottom' auto variant 'bottom':
        attribute a_idle default 'khadne_arms_bottom_a_back'
        attribute a_empty null





    group arms if_all 'b_casual' auto variant 'casual':
        attribute a_idle default 'khadne_arms_casual_a_back'

    group arms if_any ['b_casual_sit', 'b_casual_sit_turn'] auto variant 'casual_sit':
        attribute a_idle default 'khadne_arms_casual_sit_a_clipboard'
        attribute a_shrug xoffset -122

    group arms if_any ['b_shirt', 'b_shirt_disheveled', 'b_shirt_leg'] auto variant 'shirt':
        attribute a_idle default 'khadne_arms_casual_a_back'
        attribute a_up 'khadne_arms_casual_a_up'
        attribute a_boom 'khadne_arms_casual_a_boom'

    group arms if_any 'b_casual_sit_sad' auto variant 'casual_sit_sad':
        attribute a_idle default 'khadne_arms_casual_sit_sad_a_sad'



image khadne_f = "characters/khadne/khadne_face_f_normal.png"


init python hide:
    count = 12
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('khadne_crates_lick_body_b_anim', 'khadne_crates_lick_body_b_anim'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_khadne))


init python hide:
    count = 8
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('khadne_crates_sex_body_b_anim', 'khadne_crates_sex_body_b_anim'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_khadne))


init image khadne_crates_sex_overlay_o_cumshot:
    'khadne_crates_sex_overlay_o_cumshot1' with fastdissolve
    .4
    'khadne_crates_sex_overlay_o_cumshot2' with fastdissolve
    .4
    'khadne_crates_sex_overlay_o_cumshot3' with fastdissolve


layeredimage khadne crates_lick:
    attribute m_talk null

    group body auto:
        attribute b_pre default

    group face if_all 'b_pre' if_not 'm_talk' auto
    group face if_all 'b_pre' if_any 'm_talk' auto variant 'talk':
        attribute f_nervous default


layeredimage khadne crates_sex:
    attribute m_talk null

    group body auto:
        attribute b_base default

    group face if_all 'b_base' if_not 'm_talk' auto variant 'base'
    group face if_all 'b_base' if_any 'm_talk' auto variant 'base_talk':
        attribute f_normal default

    group face if_all 'b_insert' if_not 'm_talk' auto variant 'insert'
    group face if_all 'b_insert' if_any 'm_talk' auto variant 'insert_talk'

    group overlay if_all 'b_base' auto:
        attribute o_pre default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
