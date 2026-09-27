screen minigame_vault():
    style_prefix 'vault'

    default assist = False
    default initial = (3 * (13 * 2 + 315),
                       2 * (13 * 2 + 230))

    vpgrid as wall:
        rows 9
        cols 10
        draggable True
        edgescroll (75, 450, vault.scroll)
        xinitial initial[0]
        yinitial initial[1]

        for i in vault.boxes:
            frame:
                if i == 11082:
                    button:
                        action Return(i)
                        text str(i)
                else:
                    hover:
                        owner wall
                        text str(i)

    showif assist:
        showif vault.distance(initial, wall) < 100:
            fixed:
                at vault_appear
                add 'vault_hint' align .03, .03 rotate 135
                add 'vault_hint' align .03, .97 rotate 45
                add 'vault_hint' align .97, .03 rotate 225
                add 'vault_hint' align .97, .97 rotate 315

        imagebutton:
            focus_mask True
            align .5, .95
            idle 'boxes/auto_option_generic_01.png'
            hover im.MatrixColor('boxes/auto_option_generic_01.png', over)
            action Return()
            at vault_appear

    timer 10. action SetScreenVariable('assist', True)


default vault.boxes = tuple(random.sample(xrange(11001, 11001 + 90), 90))


image vault_idle = 'minigames/vault/box.png'
image vault_over = im.MatrixColor('minigames/vault/box.png', over)
image vault_hint = Window('vault_arrow')

image vault_arrow:
    'minigames/pizza2/pizza2_arrow.png'
    subpixel True
    block:
        ease 1. yoffset 10
        ease 1. yoffset 0
        repeat


style vault_button:
    background 'vault_idle'
    hover_background 'vault_over'
    xysize (315, 230)

style vault_frame:
    background 'minigames/vault/tile.png'
    padding (13, 13)

style vault_hover is vault_button

style vault_text:
    align (.5, .5)
    color '333c'
    outlines ((0, 'ccc7', 1, 1),)
    size 20
    text_align .5
    ypos 73


transform vault_appear:
    on show:
        alpha 0.
        linear 1. alpha 1.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
