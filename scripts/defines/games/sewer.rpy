image sewer_pipe = Transform('minigames/sewer/sewer_pipe.png', xtile=2)
image sewer_water = Transform('minigames/sewer/sewer_water.png', xtile=2)


image sewer_anon_left:
    'minigames/sewer/sewer_anon_right.png'
    'minigames/sewer/sewer_anon_left.png' with dissolve

image sewer_anon_right:
    'minigames/sewer/sewer_anon_left.png'
    'minigames/sewer/sewer_anon_right.png' with dissolve

image sewer_anon_sick:
    'minigames/sewer/sewer_anon_right.png'
    'minigames/sewer/sewer_anon_sick.png' with dissolve

image sewer_anon_puke:
    'minigames/sewer/sewer_anon_sick.png'
    'minigames/sewer/sewer_anon_puke.png' with fastdissolve
    .8
    'minigames/sewer/sewer_anon_right.png' with dissolve

image sewer_anon_push:
    'minigames/sewer/sewer_anon_left.png'
    'minigames/sewer/sewer_anon_push.png' with dissolve
    .6
    'minigames/sewer/sewer_anon_left.png' with dissolve


image sewer_poop_push:
    'minigames/sewer/sewer_poop.png'
    'minigames/sewer/sewer_poop_push.png' with dissolve
    .5
    linear .4 alpha 0


image sewer_button_move_idle = 'minigames/sewer/sewer_button_move.png'
image sewer_button_move_over = im.MatrixColor(
    'minigames/sewer/sewer_button_move.png', over)
image sewer_button_move_dead = im.MatrixColor(
    'minigames/sewer/sewer_button_move.png', dead)
image sewer_button_puke_idle = 'minigames/sewer/sewer_button_puke.png'
image sewer_button_puke_over = im.MatrixColor(
    'minigames/sewer/sewer_button_puke.png', over)
image sewer_button_puke_dead = im.MatrixColor(
    'minigames/sewer/sewer_button_puke.png', dead)
image sewer_button_push_idle = 'minigames/sewer/sewer_button_push.png'
image sewer_button_push_over = im.MatrixColor(
    'minigames/sewer/sewer_button_push.png', over)
image sewer_button_push_dead = im.MatrixColor(
    'minigames/sewer/sewer_button_push.png', dead)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
